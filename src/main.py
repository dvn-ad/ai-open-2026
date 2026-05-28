from paddle_module import run_paddle_ocr
from docling_module import run_docling
import os

def main():
    source = "./images/3.jpg"
    
    # 1. Jalankan Docling
    print("--- Running Docling ---")
    md_output = run_docling(source)
    print(md_output)
    
    # 2. Jalankan PaddleOCR
    print("\n--- Running PaddleOCR ---")
    run_paddle_ocr(source)

if __name__ == "__main__":
    main()