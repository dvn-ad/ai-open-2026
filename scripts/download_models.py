import os
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def download_models():
    """
    Pre-downloads and caches HuggingFace model checkpoints for:
    - LayoutLMv3 Base
    - TableTransformer Structure Recognition
    This allows offline run capability during the live demo.
    """
    logger.info("Initializing offline model cache-warming...")
    
    # 1. LayoutLMv3
    layoutlm_model = "microsoft/layoutlmv3-base"
    logger.info(f"Downloading {layoutlm_model} tokenizer, processor, and weights...")
    try:
        from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
        # This will download and save to default ~/.cache/huggingface/hub/
        processor = LayoutLMv3Processor.from_pretrained(layoutlm_model, apply_ocr=False)
        model = LayoutLMv3ForTokenClassification.from_pretrained(layoutlm_model, num_labels=6)
        logger.info(f"Successfully cached {layoutlm_model} model and processor.")
    except Exception as e:
        logger.error(f"Failed to cache {layoutlm_model}: {e}")
        
    # 2. TableTransformer
    table_model = "microsoft/table-transformer-structure-recognition"
    logger.info(f"Downloading {table_model} image processor and weights...")
    try:
        from transformers import AutoImageProcessor, TableTransformerForObjectDetection
        # This will download and save to default ~/.cache/huggingface/hub/
        image_processor = AutoImageProcessor.from_pretrained(table_model)
        model = TableTransformerForObjectDetection.from_pretrained(table_model)
        logger.info(f"Successfully cached {table_model} model and processor.")
    except Exception as e:
        logger.error(f"Failed to cache {table_model}: {e}")

    logger.info("Model download & cache warming execution finished.")

if __name__ == "__main__":
    download_models()
