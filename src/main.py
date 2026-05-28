from module.paddle_module import run_paddleocr
from module.docling_module import run_docling
from module.ollama_module import run_ollama
import time


def main():
    source = "./images/3.jpg"
    

    # 1. Docling
    start_time = time.time()
    print("--- Running Docling ---")
    md_output = run_docling(source)
    print(md_output)
    with open("./output/docling.json","w") as f:
        f.write(md_output)
    end_time = time.time()
    print(f"Docling finished in: {end_time - start_time:.2f} seconds")

    # 2. PaddleOCR
    start_time = time.time()
    print("\n--- Running PaddleOCR ---")
    run_paddleocr(source)
    end_time = time.time()
    print(f"PaddleOCR finished in: {end_time - start_time:.2f} seconds")

    # 3. ollama
    start_time = time.time()
    print("\n--- Running ollama ---")
    ollamaOutput=run_ollama(source) or ""
    with open("./output/ollama.json","w") as f:
        f.write(ollamaOutput)
    end_time = time.time()
    print(f"ollama finished in: {end_time - start_time:.2f} seconds")

    
if __name__ == "__main__":
    main()