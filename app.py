import sys
import os
import time
import uuid
import json
import shutil
import httpx
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

# Add src/ to python path so imports match main.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from main import is_scanned_pdf
from module.preprocessing import pdf_to_images, preprocess_page
from module.docling_module import run_docling
from module.ollama_module import run_ollama
from module.openai_module import run_openai

app = FastAPI(
    title="CEISA Customs OCR & Restructuring API",
    description="API to preprocess, OCR, and restructure customs documents into CEISA PIB structured JSON",
    version="1.0.0"
)

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount outputs for serving preprocessed images
app.mount("/output", StaticFiles(directory="output"), name="output")

DEMO_FILES = {
    "demo_pdf": "dataset/ilide.info-draft-pib-pr_24011a9eb9424f0410a915e7e917a653.pdf",
    "demo_img1": "dataset/1.png",
    "demo_img2": "dataset/2.jpg",
    "demo_img3": "dataset/3.jpg",
    "demo_img4": "dataset/4.png"
}

@app.get("/api/models")
async def get_models():
    """
    Get available Ollama and OpenAI models.
    """
    ollama_models = []
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:11434/api/tags", timeout=2.0)
            if response.status_code == 200:
                data = response.json()
                ollama_models = [m["name"] for m in data.get("models", [])]
    except Exception as e:
        print(f"Ollama not running or unreachable: {e}")
        
    # If Ollama is not running, provide standard placeholders
    if not ollama_models:
        ollama_models = ["gemma3:270m", "gemma3:1b", "gemma3:4b"]
        
    return {
        "ollama": ollama_models,
        "openai": ["gpt-4o-mini", "gpt-4o", "o1-mini"]
    }

@app.get("/api/demos")
async def get_demos():
    """
    Get list of available demo files with metadata.
    """
    demos = []
    for key, path in DEMO_FILES.items():
        if os.path.exists(path):
            size = os.path.getsize(path)
            ext = os.path.splitext(path)[1].lower()
            demos.append({
                "id": key,
                "name": os.path.basename(path),
                "type": "PDF" if ext == ".pdf" else "Image",
                "size_kb": round(size / 1024, 2)
            })
    return demos

@app.post("/api/process")
async def process_document(
    file: UploadFile = File(None),
    demo_id: str = Form(None),
    llm_engine: str = Form("ollama"),
    model: str = Form("gemma3:270m"),
    use_paddle_orient: bool = Form(True),
    api_key: str = Form(None)
):
    overall_start_time = time.time()
    
    # 1. Validation and File Setup
    if not file and not demo_id:
        raise HTTPException(status_code=400, detail="Please upload a file or select a demo document.")
        
    run_id = str(uuid.uuid4())
    run_dir = f"output/runs/{run_id}"
    preprocessed_dir = f"{run_dir}/preprocessed"
    os.makedirs(preprocessed_dir, exist_ok=True)
    
    # Determine the source document path
    if file:
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in [".pdf", ".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
            raise HTTPException(status_code=400, detail=f"Unsupported file format: {file_ext}")
        source_doc = f"{run_dir}/input{file_ext}"
        with open(source_doc, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    else:
        if demo_id not in DEMO_FILES:
            raise HTTPException(status_code=400, detail=f"Invalid demo document ID: {demo_id}")
        demo_path = DEMO_FILES[demo_id]
        if not os.path.exists(demo_path):
            raise HTTPException(status_code=404, detail="Demo document not found on server.")
        file_ext = os.path.splitext(demo_path)[1].lower()
        source_doc = f"{run_dir}/input{file_ext}"
        shutil.copy(demo_path, source_doc)

    # 2. Ingestion & Preprocessing
    preprocess_start = time.time()
    preprocessed_pages = []
    preprocessed_image_urls = []
    is_scanned = True
    doc_type = "pdf" if file_ext == ".pdf" else "image"
    
    try:
        if file_ext == ".pdf":
            is_scanned = is_scanned_pdf(source_doc)
            if is_scanned:
                print(f"[Run {run_id}] Ingesting scanned PDF. Converting pages to high-res images...")
                raw_pages = pdf_to_images(source_doc, dpi=300)
                
                for idx, page in enumerate(raw_pages):
                    cleaned_page = preprocess_page(page, use_paddle_orient=use_paddle_orient)
                    audit_filename = f"page_{idx + 1}_cleaned.png"
                    audit_path = os.path.join(preprocessed_dir, audit_filename)
                    cleaned_page.save(audit_path)
                    preprocessed_pages.append(cleaned_page)
                    preprocessed_image_urls.append(f"/output/runs/{run_id}/preprocessed/{audit_filename}")
                ocr_source = preprocessed_pages
            else:
                print(f"[Run {run_id}] Digital PDF detected. Bypassing preprocessing.")
                ocr_source = source_doc
                
        elif file_ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
            raw_img = Image.open(source_doc)
            cleaned_img = preprocess_page(raw_img, use_paddle_orient=use_paddle_orient)
            audit_filename = "cleaned_image.png"
            audit_path = os.path.join(preprocessed_dir, audit_filename)
            cleaned_img.save(audit_path)
            preprocessed_pages.append(cleaned_img)
            preprocessed_image_urls.append(f"/output/runs/{run_id}/preprocessed/{audit_filename}")
            ocr_source = [cleaned_img]
            is_scanned = True
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Preprocessing error: {str(e)}")
        
    preprocess_end = time.time()
    preprocess_duration = preprocess_end - preprocess_start

    # 3. High-Fidelity OCR & Layout Parser (Docling)
    docling_start = time.time()
    temp_pdf_path = f"{run_dir}/temp_preprocessed.pdf"
    
    try:
        # We export to Markdown for LLM restructuring
        print(f"[Run {run_id}] Running Docling layout parsing (Markdown)...")
        docling_md = run_docling(ocr_source, export_format="markdown", temp_pdf_path=temp_pdf_path)
        
        # Save raw layout Markdown
        raw_md_path = f"{run_dir}/raw_layout.md"
        with open(raw_md_path, "w", encoding="utf-8") as f:
            f.write(docling_md)
            
        # Also save structured JSON format
        print(f"[Run {run_id}] Running Docling layout parsing (JSON)...")
        docling_json = run_docling(ocr_source, export_format="json", temp_pdf_path=temp_pdf_path)
        raw_json_path = f"{run_dir}/docling_layout.json"
        with open(raw_json_path, "w", encoding="utf-8") as f:
            f.write(docling_json)
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Docling conversion error: {str(e)}")
        
    docling_end = time.time()
    docling_duration = docling_end - docling_start

    # 4. Semantic Restructuring (LLM Mapping)
    llm_start = time.time()
    restructured_json_str = ""
    
    try:
        if llm_engine.lower() == "ollama":
            restructured_json_str = run_ollama(docling_md, model=model)
        elif llm_engine.lower() == "openai":
            restructured_json_str = run_openai(docling_md, model=model, api_key=api_key)
        else:
            raise ValueError(f"Unknown LLM engine: {llm_engine}")
            
        # Save restructured CEISA JSON
        final_output_path = f"{run_dir}/restructured_ceisa.json"
        with open(final_output_path, "w", encoding="utf-8") as f:
            f.write(restructured_json_str)
            
    except Exception as e:
        restructured_json_str = json.dumps({
            "error": "LLM restructuring failed",
            "details": str(e)
        }, indent=2)
        
    llm_end = time.time()
    llm_duration = llm_end - llm_start
    overall_duration = time.time() - overall_start_time
    
    # Try parsing the final restructured JSON string to send as object
    try:
        restructured_json = json.loads(restructured_json_str)
    except Exception:
        restructured_json = {"error": "Failed to parse LLM response as JSON", "raw": restructured_json_str}

    # Remove the temporary compiled PDF to save disk space
    if os.path.exists(temp_pdf_path):
        try:
            os.remove(temp_pdf_path)
        except Exception:
            pass

    return {
        "success": True,
        "run_id": run_id,
        "doc_type": doc_type,
        "is_scanned": is_scanned,
        "preprocessed_images": preprocessed_image_urls,
        "raw_markdown": docling_md,
        "restructured_json": restructured_json,
        "timing": {
            "preprocessing": round(preprocess_duration, 2),
            "docling": round(docling_duration, 2),
            "llm": round(llm_duration, 2),
            "total": round(overall_duration, 2)
        }
    }

# Fallback route to serve index.html
@app.get("/")
async def get_index():
    if os.path.exists("static/index.html"):
        with open("static/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(f.read())
    return HTMLResponse("""
    <html>
        <head>
            <title>CEISA Customs OCR Setup</title>
            <style>
                body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }
                .container { text-align: center; background: #1e293b; padding: 2rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
                h1 { color: #38bdf8; margin-bottom: 1rem; }
                p { color: #94a3b8; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>CEISA Customs OCR POC Server</h1>
                <p>The backend is running, but the frontend files have not been created yet.</p>
                <p>Please wait while the frontend assets are being generated...</p>
            </div>
        </body>
    </html>
    """)

# Serve all other static assets directly
app.mount("/", StaticFiles(directory="static"), name="static_root")
