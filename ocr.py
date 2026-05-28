from docling.document_converter import DocumentConverter

from pathlib import Path
from paddleocr import PaddleOCRVL

source = "./2.jpg"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"


output_dir = Path("./output")
output_dir.mkdir(parents=True, exist_ok=True)

# NVIDIA GPU
# pipeline = PaddleOCRVL()
# Kunlunxin XPU
# pipeline = PaddleOCRVL(device="xpu")
# Hygon DCU
# pipeline = PaddleOCRVL(device="dcu")
# MetaX GPU
# pipeline = PaddleOCRVL(device="metax_gpu")
# Apple Silicon
pipeline = PaddleOCRVL(device="cpu")
# Huawei Ascend NPU 
# Huawei Ascend NPU please refer to Chapter 3 for inference using PaddlePaddle + vLLM

pipeline = PaddleOCRVL(use_doc_orientation_classify=True) # Use use_doc_orientation_classify to enable/disable document orientation classification model
pipeline = PaddleOCRVL(use_doc_unwarping=True) # Use use_doc_unwarping to enable/disable document unwarping module
pipeline = PaddleOCRVL(use_layout_detection=False) # Use use_layout_detection to enable/disable layout analysis module

output = pipeline.predict(source)
for res in output:
    res.print() ## Print the structured prediction output
    # res.save_to_json(save_path=output_dir) ## Save the current image's structured result in JSON format
    res.save_to_markdown(save_path=output_dir) ## Save the current image's result in Markdown format
    # res.save_to_word(save_path="output") ## Save the current image's result in Word format