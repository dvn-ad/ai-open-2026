import cv2
import PIL
from PIL import Image
print("OpenCV version:", cv2.__version__)
print("PIL version:", PIL.__version__)

try:
    from paddleocr import PaddleOCRVL
    print("PaddleOCRVL imported successfully!")
except Exception as e:
    print("Failed to import PaddleOCRVL:", e)

try:
    from docling.document_converter import DocumentConverter
    print("Docling imported successfully!")
except Exception as e:
    print("Failed to import Docling:", e)
