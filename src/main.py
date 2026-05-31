from module.preprocessing import pdf_to_images, preprocess_page, pil_to_cv2, cv2_to_pil
from module.docling_module import run_docling
from module.ollama_module import run_ollama
from module.openai_module import run_openai
import time
import os
import pypdfium2 as pdfium
from PIL import Image

def is_scanned_pdf(pdf_path):
    """
    Detects if a PDF is scanned or digital by checking text density on the first few pages.
    """
    try:
        doc = pdfium.PdfDocument(pdf_path)
        total_chars = 0
        pages_to_check = min(len(doc), 3)
        for i in range(pages_to_check):
            page = doc[i]
            text_page = page.get_textpage()
            text = text_page.get_text_bounded()
            total_chars += len(text)
        
        # If very few characters are found, it's highly likely a scan
        is_scanned = total_chars < 150
        print(f"PDF Analysis: Detected {total_chars} characters in first {pages_to_check} page(s). "
              f"Document is classified as: {'SCANNED' if is_scanned else 'DIGITAL'}")
        return is_scanned
    except Exception as e:
        print(f"Warning: Could not analyze PDF text density ({e}). Assuming scanned.")
        return True

def main():
    # --- PIPELINE CONFIGURATION ---
    # Target document to process. Can be a PDF or an image.
    source_doc = "./dataset/ilide.info-draft-pib-pr_24011a9eb9424f0410a915e7e917a653.pdf"
    # source_doc = "./dataset/2.jpg"  # Uncomment to test with raw scanned image
    
    # Restructuring LLM Engine Choice: "ollama" or "openai"
    llm_engine = "ollama" 
    
    # LLM Model choices
    ollama_model = "gemma3:270m"  # Can also be "qwen2.5:14b", "llama3", etc. gemma3:4b gemma3:1b
    openai_model = "gpt-4o-mini"
    
    # --- PIPELINE START ---
    overall_start_time = time.time()
    print("==================================================================")
    print("      CEISA CUSTOMS OCR & RESTRICTURING PIPELINE POC              ")
    print("==================================================================")
    print(f"Source Document: {source_doc}")
    print(f"LLM Extraction Engine: {llm_engine.upper()}")
    print("------------------------------------------------------------------")

    # Ensure output folders exist
    output_dir = "./output"
    preprocessed_dir = "./output/preprocessed"
    os.makedirs(preprocessed_dir, exist_ok=True)
    
    # Step 1: Ingestion & Preprocessing (Deskew / Rotate)
    preprocess_start = time.time()
    file_ext = os.path.splitext(source_doc)[1].lower()
    
    preprocessed_pages = []
    
    if file_ext == ".pdf":
        if is_scanned_pdf(source_doc):
            print("\n[Step 1] Ingesting scanned PDF. Converting pages to high-res images...")
            raw_pages = pdf_to_images(source_doc, dpi=300)
            print(f"Successfully rendered {len(raw_pages)} pages. Starting preprocessing (Deskew & Rotate)...")
            
            for idx, page in enumerate(raw_pages):
                print(f"Processing page {idx + 1}/{len(raw_pages)}...")
                # We turn off PaddleOCR orientation checking if GPU is not present or if we want faster CPU execution,
                # but we keep it enabled as default.
                cleaned_page = preprocess_page(page, use_paddle_orient=True)
                
                # Save audit image
                audit_path = os.path.join(preprocessed_dir, f"page_{idx + 1}_cleaned.png")
                cleaned_page.save(audit_path)
                preprocessed_pages.append(cleaned_page)
                
            print(f"Preprocessing completed. Audit images saved to {preprocessed_dir}")
            ocr_source = preprocessed_pages
        else:
            print("\n[Step 1] Digital PDF detected. Bypassing image preprocessing to retain original fonts/layout.")
            ocr_source = source_doc
            
    elif file_ext in [".png", ".jpg", ".jpeg", ".tiff", ".bmp"]:
        print(f"\n[Step 1] Scanned Image detected: {source_doc}. Starting preprocessing (Deskew & Rotate)...")
        raw_img = Image.open(source_doc)
        cleaned_img = preprocess_page(raw_img, use_paddle_orient=True)
        
        # Save audit image
        audit_path = os.path.join(preprocessed_dir, "cleaned_image.png")
        cleaned_img.save(audit_path)
        print(f"Preprocessing completed. Audit image saved to {audit_path}")
        ocr_source = [cleaned_img]
        
    else:
        raise ValueError(f"Unsupported file format: {file_ext}")
        
    preprocess_end = time.time()
    print(f"--> Preprocessing finished in: {preprocess_end - preprocess_start:.2f} seconds")

    # Step 2: High-Fidelity OCR & Layout Parser (Docling)
    print("\n[Step 2] Launching Docling layout parsing and OCR...")
    docling_start = time.time()
    
    # We export to Markdown as it represents tables and structures perfectly for LLM consumption
    docling_md = run_docling(ocr_source, export_format="markdown")
    
    # Save raw layout Markdown for auditing
    raw_md_path = os.path.join(output_dir, "raw_layout.md")
    with open(raw_md_path, "w", encoding="utf-8") as f:
        f.write(docling_md)
        
    # Also save structured JSON format from Docling
    docling_json = run_docling(ocr_source, export_format="json")
    raw_json_path = os.path.join(output_dir, "docling_layout.json")
    with open(raw_json_path, "w", encoding="utf-8") as f:
        f.write(docling_json)
        
    docling_end = time.time()
    print(f"Raw layout text preview (First 300 chars):\n---\n{docling_md[:300]}...\n---")
    print(f"--> Docling finished in: {docling_end - docling_start:.2f} seconds")
    print(f"--> Raw structural layout saved to {raw_md_path} and {raw_json_path}")

    # Step 3: Semantic Restructuring (LLM Mapping)
    print(f"\n[Step 3] Sending structured raw layout to LLM ({llm_engine.upper()}) for CEISA restructuring...")
    llm_start = time.time()
    
    if llm_engine.lower() == "ollama":
        restructured_json = run_ollama(docling_md, model=ollama_model)
    elif llm_engine.lower() == "openai":
        restructured_json = run_openai(docling_md, model=openai_model)
    else:
        raise ValueError(f"Unknown LLM engine: {llm_engine}")
        
    # Save final restructured CEISA JSON
    final_output_path = os.path.join(output_dir, "restructured_ceisa.json")
    with open(final_output_path, "w", encoding="utf-8") as f:
        f.write(restructured_json)
        
    llm_end = time.time()
    print(f"--> LLM restructuring finished in: {llm_end - llm_start:.2f} seconds")
    print(f"--> Restructured CEISA JSON saved to {final_output_path}")

    # --- PIPELINE END ---
    overall_end_time = time.time()
    print("\n==================================================================")
    print("                      PIPELINE EXECUTION SUMMARY                  ")
    print("==================================================================")
    print(f"1. Preprocessing Time : {preprocess_end - preprocess_start:.2f}s")
    print(f"2. OCR / Docling Time : {docling_end - docling_start:.2f}s")
    print(f"3. LLM Parsing Time   : {llm_end - llm_start:.2f}s")
    print(f"Total Execution Time  : {overall_end_time - overall_start_time:.2f}s")
    print("------------------------------------------------------------------")
    print("Outputs Produced:")
    print(f"- Clean Preprocessed Pages : {preprocessed_dir}")
    print(f"- Raw Markdown Layout      : {raw_md_path}")
    print(f"- Raw Docling Layout JSON  : {raw_json_path}")
    print(f"- Structured CEISA JSON    : {final_output_path}")
    print("==================================================================")

if __name__ == "__main__":
    main()