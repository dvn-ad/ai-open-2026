from docling.document_converter import DocumentConverter
import json
import os
from PIL import Image

def run_docling(source, export_format="markdown", temp_pdf_path="./output/temp_preprocessed.pdf"):
    """
    Run Docling OCR and Layout Parser on the source document.
    
    Args:
        source: Can be a file path (str) to a PDF/image, or a list of PIL Images (preprocessed pages).
        export_format: "markdown" or "json"
        temp_pdf_path: Path to save the intermediate preprocessed PDF if a list of PIL images is provided.
    
    Returns:
        str: Clean Markdown or JSON string representation of the document.
    """
    converter = DocumentConverter()
    
    # If the source is a list of PIL Images, we compile them into a single clean PDF first
    if isinstance(source, list) and len(source) > 0 and isinstance(source[0], Image.Image):
        print(f"Compiling {len(source)} preprocessed page images into a single PDF for Docling parsing...")
        os.makedirs(os.path.dirname(temp_pdf_path), exist_ok=True)
        # Save as a multi-page PDF
        source[0].save(
            temp_pdf_path, 
            save_all=True, 
            append_images=source[1:], 
            resolution=300.0, 
            quality=95
        )
        actual_source = temp_pdf_path
    else:
        actual_source = source
        
    print(f"Running Docling converter on: {actual_source}")
    result = converter.convert(actual_source)
    
    # Export based on requested format
    if export_format.lower() == "json":
        return json.dumps(result.document.export_to_dict(), indent=2)
    else:
        # Default is Markdown, which preserves tables and headings beautifully for LLM consumption
        return result.document.export_to_markdown()
