import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import time
import json
import logging
import argparse
import sys
import uuid
import shutil
from pathlib import Path
import pypdfium2 as pdfium

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

from module.docling_module import run_docling
from module.paddle_module import run_paddleocr
from module.layoutlm_module import run_layoutlm
from module.table_transformer_module import run_table_transformer
from module.ollama_module import run_ollama
from validation.schema import (
    ExtractedDocuments,
    CommercialInvoice,
    PackingList,
    BillOfLading,
    PIBDocument,
    FormEDocument
)
from validation.confidence_engine import ConfidenceEngine


def populate_confidence_scores(doc_obj, ocr_results):
    if not doc_obj:
        return
    
    # Calculate average OCR confidence for the entire page
    page_ocr_scores = [t.get("confidence", 1.0) * 100 for t in ocr_results if "confidence" in t]
    avg_page_confidence = sum(page_ocr_scores) / len(page_ocr_scores) if page_ocr_scores else 95.0
    
    scores = {}
    
    for field in doc_obj.model_fields.keys():
        if field in ["document_type", "items", "confidence_scores"]:
            continue
        val = getattr(doc_obj, field, None)
        if val is None or val == "":
            continue
            
        # Search for this value in OCR results
        val_str = str(val).upper().strip()
        matched_scores = []
        for token in ocr_results:
            token_text = str(token.get("text", "")).upper().strip()
            if val_str in token_text or token_text in val_str:
                matched_scores.append(token.get("confidence", 1.0) * 100)
                
        if matched_scores:
            scores[field] = round(sum(matched_scores) / len(matched_scores), 2)
        else:
            # Fallback to average page confidence
            scores[field] = round(min(99.0, max(50.0, avg_page_confidence)), 2)
            
    doc_obj.confidence_scores = scores


def main():
    parser = argparse.ArgumentParser(
        description="AI-Powered Customs Declaration Automation Platform - CLI Ingestion"
    )
    parser.add_argument(
        "file_path",
        help="Path to the target document (PDF or Image file)"
    )
    parser.add_argument(
        "--output",
        default="output/validation_result.json",
        help="Path to save validation result JSON"
    )
    args = parser.parse_args()

    source = args.file_path

    if not os.path.exists(source):
        logger.error(f"Source file '{source}' not found.")
        sys.exit(1)

    # Ensure output directory exists
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    temp_dir = os.path.join(output_dir, "temp_pages")
    os.makedirs(temp_dir, exist_ok=True)

    # Determine pages to process
    pages_to_process = []
    suffix = Path(source).suffix.lower()

    if suffix == ".pdf":
        logger.info(f"Ingesting PDF: {source}. Rendering pages to images...")
        try:
            pdf = pdfium.PdfDocument(source)
            for idx in range(len(pdf)):
                page = pdf[idx]
                bitmap = page.render(scale=2)
                pil_img = bitmap.to_pil()
                page_path = os.path.join(temp_dir, f"page_{idx+1}_{uuid.uuid4().hex[:8]}.png")
                pil_img.save(page_path)
                
                # Extract native text if any
                textpage = page.get_textpage()
                native_text = textpage.get_text_bounded() or ""
                
                pages_to_process.append({
                    "image_path": page_path,
                    "native_text": native_text,
                    "page_number": idx + 1
                })
            logger.info(f"Rendered {len(pages_to_process)} pages from PDF.")
        except Exception as e:
            logger.error(f"Failed to process PDF file: {e}")
            sys.exit(1)
    elif suffix in [".png", ".jpg", ".jpeg"]:
        pages_to_process.append({
            "image_path": source,
            "native_text": "",
            "page_number": 1
        })
    else:
        logger.error(f"Unsupported file type: {suffix}. Supported types: PDF, PNG, JPG, JPEG.")
        sys.exit(1)

    combined_data = {
        "commercial_invoice": None,
        "packing_list": None,
        "bill_of_lading": None,
        "pib": None,
        "form_e": None,
        "import_permits": []
    }
    
    modules_used = ["docling", "paddleocr", "layoutlmv3", "tabletransformer", "ollama"]
    errors = []
    
    for page_info in pages_to_process:
        img_path = page_info["image_path"]
        native_text = page_info["native_text"]
        page_num = page_info["page_number"]
        
        logger.info(f"\nProcessing page {page_num}: {img_path}")
        
        # 1. PaddleOCR
        start_time = time.time()
        logger.info("=== Stage 1: Running PaddleOCR ===")
        try:
            ocr_results = run_paddleocr(img_path) or []
            logger.info(f"PaddleOCR finished for page {page_num}.")
        except Exception as e:
            logger.exception(f"PaddleOCR stage failed for page {page_num}")
            errors.append(f"PaddleOCR failed for page {page_num}: {str(e)}")
            continue
        print(f"PaddleOCR elapsed: {time.time() - start_time:.2f} seconds")
            
        # Classify document type using keywords in OCR and native text
        ocr_text = " ".join(t.get("text", "") for t in ocr_results)
        full_text = (native_text + " " + ocr_text).upper()
        
        doc_type = "other"
        if 'PEMBERITAHUAN IMPOR' in full_text or 'BC2.0' in full_text or 'BC 2.0' in full_text:
            doc_type = 'pib'
        elif 'FORM E' in full_text or 'FORM_E' in full_text:
            doc_type = 'form_e'
        elif 'COMMERCIAL INVOICE' in full_text:
            doc_type = 'commercial_invoice'
        elif 'PACKING LIST' in full_text:
            doc_type = 'packing_list'
        elif 'BILL OF LADING' in full_text or 'WAYBILL' in full_text or 'LADING' in full_text:
            doc_type = 'bill_of_lading'
            
        logger.info(f"Classified page {page_num} as: {doc_type.upper()}")
        
        if doc_type == "other":
            logger.info("Skipping page classified as 'other'.")
            continue
            
        # 2. Docling
        start_time = time.time()
        logger.info("=== Stage 2: Running Docling ===")
        try:
            run_docling(img_path)
            logger.info(f"Docling finished for page {page_num}.")
        except Exception as e:
            logger.warning(f"Docling failed for page {page_num}: {e}")
        print(f"Docling elapsed: {time.time() - start_time:.2f} seconds")
            
        # 3. LayoutLMv3
        start_time = time.time()
        logger.info("=== Stage 3: Running LayoutLMv3 ===")
        try:
            layout_results = run_layoutlm(img_path, ocr_results) or []
            logger.info(f"LayoutLMv3 finished for page {page_num}.")
        except Exception as e:
            logger.warning(f"LayoutLMv3 failed for page {page_num}: {e}")
            layout_results = []
        print(f"LayoutLMv3 elapsed: {time.time() - start_time:.2f} seconds")
            
        # 4. TableTransformer
        start_time = time.time()
        logger.info("=== Stage 4: Running TableTransformer ===")
        try:
            table_results = run_table_transformer(img_path, ocr_results) or []
            logger.info(f"TableTransformer finished for page {page_num}.")
        except Exception as e:
            logger.warning(f"TableTransformer failed for page {page_num}: {e}")
            table_results = []
        print(f"TableTransformer elapsed: {time.time() - start_time:.2f} seconds")
            
        # 5. Ollama
        start_time = time.time()
        logger.info("=== Stage 5: Running Ollama Structuring ===")
        try:
            ollama_output = run_ollama(img_path, layout_results, table_results) or ""
            if ollama_output.strip():
                # Clean up potential markdown formatting from LLM response
                cleaned_json = ollama_output.strip()
                if cleaned_json.startswith("```"):
                    cleaned_json = cleaned_json.split("\n", 1)[1]
                if cleaned_json.endswith("```"):
                    cleaned_json = cleaned_json.rsplit("\n", 1)[0]
                cleaned_json = cleaned_json.strip()
                if cleaned_json.startswith("json"):
                    cleaned_json = cleaned_json[4:].strip()
                    
                parsed_json = json.loads(cleaned_json)
                
                if isinstance(parsed_json, dict):
                    # Merge document objects
                    for key, model_cls in [
                        ("commercial_invoice", CommercialInvoice),
                        ("packing_list", PackingList),
                        ("bill_of_lading", BillOfLading),
                        ("pib", PIBDocument),
                        ("form_e", FormEDocument)
                    ]:
                        doc_data = parsed_json.get(key)
                        if doc_data and isinstance(doc_data, dict):
                            try:
                                # Clean up document_type to prevent validation errors if LLM outputs null
                                if "document_type" in doc_data and doc_data["document_type"] is None:
                                    del doc_data["document_type"]
                                    
                                # Clean up items list to prevent Pydantic validation errors on None values
                                if "items" in doc_data and isinstance(doc_data["items"], list):
                                    cleaned_items = []
                                    for item in doc_data["items"]:
                                        if isinstance(item, dict):
                                            desc = item.get("description") or item.get("uraian") or "Unknown"
                                            qty = item.get("quantity") or item.get("jumlah")
                                            try:
                                                qty = float(qty) if qty is not None else 0.0
                                            except Exception:
                                                qty = 0.0
                                            
                                            # Convert optional fields safely
                                            unit_pr = None
                                            if item.get("unit_price") is not None:
                                                try:
                                                    unit_pr = float(item["unit_price"])
                                                except Exception:
                                                    pass
                                                    
                                            tot_pr = None
                                            if item.get("total_price") is not None:
                                                try:
                                                    tot_pr = float(item["total_price"])
                                                except Exception:
                                                    pass

                                            cleaned_item = {
                                                "description": str(desc),
                                                "quantity": qty,
                                                "hs_code": str(item.get("hs_code")) if item.get("hs_code") is not None else None,
                                                "unit_price": unit_pr,
                                                "total_price": tot_pr
                                            }
                                            cleaned_items.append(cleaned_item)
                                    doc_data["items"] = cleaned_items
                                    
                                doc_obj = model_cls(**doc_data)
                                populate_confidence_scores(doc_obj, ocr_results)
                                combined_data[key] = doc_obj.model_dump()
                            except Exception as p_err:
                                logger.error(f"Failed parsing Pydantic object {key} on page {page_num}: {p_err}")
                                errors.append(f"Failed parsing Pydantic object {key} on page {page_num}: {str(p_err)}")
                                
                    # Merge permits (filter out null/None and empty values)
                    if parsed_json.get("import_permits") and isinstance(parsed_json["import_permits"], list):
                        cleaned_permits = [str(p) for p in parsed_json["import_permits"] if p is not None and str(p).strip() != ""]
                        combined_data["import_permits"].extend(cleaned_permits)
            logger.info(f"Ollama finished for page {page_num}.")
        except Exception as e:
            logger.error(f"Ollama/parsing failed for page {page_num}: {e}")
            errors.append(f"Ollama/parsing failed for page {page_num}: {str(e)}")
        print(f"Ollama elapsed: {time.time() - start_time:.2f} seconds")

    # Final cleanup of permits
    combined_data["import_permits"] = list(
        set(str(p) for p in combined_data["import_permits"] if p is not None and str(p).strip() != "")
    )
    
    # 6. Validation Intelligence Layer Integration
    logger.info("=== Stage 6: Running Validation Intelligence Layer ===")
    try:
        # Parse output into our Pydantic schema
        docs = ExtractedDocuments(**combined_data)
        
        # Verify that we extracted at least one document
        has_any_doc = any(
            getattr(docs, f) is not None for f in [
                "commercial_invoice", "packing_list", "bill_of_lading", "pib", "form_e"
            ]
        )
        if not has_any_doc:
            logger.warning("No valid documents (Invoice, Packing List, BL, PIB, Form E) were extracted from the input file.")

        # Run validation engine
        engine = ConfidenceEngine()
        result = engine.process_declaration(docs)
        
        # Print Validation Result JSON to stdout
        print("\nValidation Result JSON:")
        print(json.dumps(result, indent=2))
        
        # Write validation result to file
        output_file = args.output
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)
        logger.info(f"Pipeline complete. Validation results saved to {output_file}")
    except Exception as e:
        logger.error(f"Validation layer failed: {e}")
        sys.exit(1)
    finally:
        # Cleanup temporary rendered page images if input was a PDF
        if suffix == ".pdf":
            logger.info("Cleaning up temporary page images...")
            try:
                shutil.rmtree(temp_dir)
            except Exception as e:
                logger.warning(f"Failed to clean up temp directory {temp_dir}: {e}")


if __name__ == "__main__":
    main()