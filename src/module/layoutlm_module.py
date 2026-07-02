import os
import re
import logging
import torch
import numpy as np
from PIL import Image

# Configure logging
logger = logging.getLogger(__name__)

# Classes mapping
LABEL_NAMES = ['HEADER', 'FIELD_NAME', 'FIELD_VALUE', 'LINE_ITEM', 'TOTAL', 'OTHER']

class LayoutLMModule:
    def __init__(self, model_name="microsoft/layoutlmv3-base"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = None
        self.model = None
        self.is_loaded = False

    def load_model(self):
        """Lazy load LayoutLMv3 model to optimize startup time and handle errors gracefully."""
        if self.is_loaded:
            return True
        try:
            from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
            logger.info(f"Loading LayoutLMv3 model '{self.model_name}' on {self.device}...")
            self.processor = LayoutLMv3Processor.from_pretrained(self.model_name, apply_ocr=False)
            self.model = LayoutLMv3ForTokenClassification.from_pretrained(
                self.model_name, 
                num_labels=len(LABEL_NAMES)
            ).to(self.device)
            self.model.eval()
            self.is_loaded = True
            logger.info("LayoutLMv3 model loaded successfully.")
            return True
        except Exception as e:
            logger.warning(f"Failed to load LayoutLMv3 model: {e}. Graceful fallback will be used.")
            self.processor = None
            self.model = None
            self.is_loaded = False
            return False

    def _normalize_box(self, box, width, height):
        """Normalize bbox coordinates to [0, 1000]."""
        # Ensure box is in [xmin, ymin, xmax, ymax]
        if len(box) == 4:
            xmin, ymin, xmax, ymax = box
        elif len(box) == 8: # Polygon points [x1, y1, x2, y2, x3, y3, x4, y4]
            x_coords = box[0::2]
            y_coords = box[1::2]
            xmin = min(x_coords)
            ymin = min(y_coords)
            xmax = max(x_coords)
            ymax = max(y_coords)
        else:
            return [0, 0, 0, 0]

        normalized = [
            int(1000 * (xmin / width)),
            int(1000 * (ymin / height)),
            int(1000 * (xmax / width)),
            int(1000 * (ymax / height))
        ]
        
        # Clip to [0, 1000]
        return [
            max(0, min(1000, normalized[0])),
            max(0, min(1000, normalized[1])),
            max(0, min(1000, normalized[2])),
            max(0, min(1000, normalized[3]))
        ]

    def _apply_heuristics(self, word, box, raw_label=None):
        """Apply domain-specific heuristics using regex and spatial position (coordinates in 0-1000)."""
        text = word.upper().strip()
        
        # 1. HEADER: Near top of page or containing typical header terms
        if box[3] < 180 or any(kw in text for kw in ["INVOICE", "FAKTUR", "PACKING", "BILL", "LADING", "DELIVERY", "PEMERINTAH", "DIREKTORAT", "KANTOR"]):
            return "HEADER"
        
        # 2. TOTAL: Matches standard invoice total terms
        if any(kw in text for kw in ["TOTAL", "SUBTOTAL", "GRAND", "SAY", "TERBILANG", "AMOUNT"]):
            return "TOTAL"
            
        # 3. FIELD_NAME: Field descriptor words
        if any(kw in text for kw in ["NO", "NUMBER", "DATE", "IMPORTER", "SHIPPER", "CONSIGNEE", "TAX", "NPWP", "CURRENCY", "VALUTA", "WEIGHT", "GROSS", "NET"]):
            # Exclude numbers themselves
            if not re.match(r"^\d+$", text):
                return "FIELD_NAME"
            
        # 4. FIELD_VALUE: Common formats for identifiers/numbers/dates/codes
        if (re.match(r"^\d{2,4}[-/.]\d{2}[-/.]\d{2,4}$", text) or  # Date format
            re.match(r"^[A-Z]{3}$", text) or                      # Currency (USD, IDR)
            re.match(r"^[A-Z0-9]{5,20}$", text) or                # Document numbers
            re.match(r"^\d{2}\.\d{3}\.\d{3}\.\d-\d{3}\.\d{3}$", text)): # Tax ID / NPWP format
            return "FIELD_VALUE"
            
        # 5. LINE_ITEM: Common steel/customs keywords, or structured numeric rows in the middle
        if (any(kw in text for kw in ["COIL", "STEEL", "BESI", "BAJA", "KG", "PCS", "METER", "BOX", "DRUM", "PLATE", "SHEET"]) or
            (box[1] > 250 and box[3] < 800 and re.match(r"^\d+(?:\.\d+)?$", text))): # numerical values in table area
            return "LINE_ITEM"

        # Default to raw prediction if exists, else OTHER
        if raw_label in LABEL_NAMES:
            return raw_label
        return "OTHER"

    def run_layoutlm(self, image_path, ocr_results):
        """
        Runs LayoutLMv3 token classification.
        ocr_results format: List of Dict containing 'text' and 'box' [xmin, ymin, xmax, ymax]
        """
        # Ensure model is loaded (or fallback)
        has_model = self.load_model()
        
        # Open image to get dimensions
        try:
            image = Image.open(image_path).convert("RGB")
            width, height = image.size
        except Exception as e:
            logger.error(f"Failed to open image {image_path}: {e}")
            return []

        words = []
        normalized_boxes = []
        original_boxes = []
        
        for idx, item in enumerate(ocr_results):
            word = item.get("text", "")
            box = item.get("box", [0, 0, 0, 0])
            
            words.append(word)
            original_boxes.append(box)
            normalized_boxes.append(self._normalize_box(box, width, height))

        predictions = []
        raw_labels = [None] * len(words)

        # Run forward pass if the model is loaded
        if has_model and words:
            try:
                # Wrap lists in batches
                encoding = self.processor(
                    image, 
                    words, 
                    boxes=normalized_boxes, 
                    return_tensors="pt"
                )
                
                # Move tensors to device
                for k, v in encoding.items():
                    encoding[k] = v.to(self.device)
                
                with torch.no_grad():
                    outputs = self.model(**encoding)
                
                logits = outputs.logits.squeeze(0).cpu().numpy()
                word_ids = encoding.word_ids(0)
                
                # Group sub-token logits by original word_id
                word_predictions = {}
                for idx, word_id in enumerate(word_ids):
                    if word_id is not None:
                        if word_id not in word_predictions:
                            word_predictions[word_id] = []
                        word_predictions[word_id].append(logits[idx])
                
                for word_id, logit_list in word_predictions.items():
                    if word_id < len(words):
                        avg_logit = np.mean(logit_list, axis=0)
                        label_id = np.argmax(avg_logit)
                        raw_labels[word_id] = LABEL_NAMES[label_id]
            except Exception as e:
                logger.warning(f"Error during LayoutLMv3 inference: {e}. Falling back to heuristics.")

        # Post-process with heuristics
        for idx, word in enumerate(words):
            raw_lbl = raw_labels[idx]
            norm_box = normalized_boxes[idx]
            final_label = self._apply_heuristics(word, norm_box, raw_lbl)
            
            predictions.append({
                "text": word,
                "box": original_boxes[idx],
                "normalized_box": norm_box,
                "semantic_role": final_label
            })
            
        return predictions

def run_layoutlm(image_path, ocr_results):
    module = LayoutLMModule()
    return module.run_layoutlm(image_path, ocr_results)
