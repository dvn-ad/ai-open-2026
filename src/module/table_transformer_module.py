import os
import logging
import torch
import numpy as np
from PIL import Image

# Configure logging
logger = logging.getLogger(__name__)

class TableTransformerModule:
    def __init__(self, model_name="microsoft/table-transformer-structure-recognition"):
        self.model_name = model_name
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.image_processor = None
        self.model = None
        self.is_loaded = False

    def load_model(self):
        """Lazy load TableTransformer model to optimize startup time and handle errors gracefully."""
        if self.is_loaded:
            return True
        try:
            from transformers import AutoImageProcessor, TableTransformerForObjectDetection
            logger.info(f"Loading TableTransformer model '{self.model_name}' on {self.device}...")
            self.image_processor = AutoImageProcessor.from_pretrained(self.model_name)
            self.model = TableTransformerForObjectDetection.from_pretrained(self.model_name).to(self.device)
            self.model.eval()
            self.is_loaded = True
            logger.info("TableTransformer model loaded successfully.")
            return True
        except Exception as e:
            logger.warning(f"Failed to load TableTransformer model: {e}. Graceful fallback will be used.")
            self.image_processor = None
            self.model = None
            self.is_loaded = False
            return False

    def _get_midpoint(self, box):
        """Get midpoint of a bbox [xmin, ymin, xmax, ymax]."""
        return (box[0] + box[2]) / 2.0, (box[1] + box[3]) / 2.0

    def _box_overlap(self, box_a, box_b):
        """Check if two boxes overlap."""
        return not (box_a[2] < box_b[0] or box_a[0] > box_b[2] or box_a[3] < box_b[1] or box_a[1] > box_b[3])

    def _heuristics_table_extraction(self, ocr_results):
        """
        Fallback heuristic table extractor if the TableTransformer model is unavailable.
        Groups OCR tokens in the table region by similar y-coordinates to construct rows.
        """
        logger.info("Running heuristic table extraction fallback...")
        if not ocr_results:
            return []

        # Find potential table area: middle to lower section of the page
        # Sort items by vertical position
        sorted_ocr = sorted(ocr_results, key=lambda x: (x["box"][1], x["box"][0]))
        
        # Group tokens into lines based on vertical overlap / distance
        lines = []
        current_line = []
        last_y_mid = -1
        
        for item in sorted_ocr:
            box = item["box"]
            y_mid = (box[1] + box[3]) / 2
            
            # If distance is small enough, it's the same row/line (threshold roughly 15-20 pixels)
            if last_y_mid == -1:
                current_line.append(item)
                last_y_mid = y_mid
            elif abs(y_mid - last_y_mid) < 15:
                current_line.append(item)
            else:
                lines.append(current_line)
                current_line = [item]
                last_y_mid = y_mid
        if current_line:
            lines.append(current_line)

        # Filter lines that look like line-item tables (e.g. they have multiple columns / numeric cells)
        table_rows = []
        for line in lines:
            # Sort words inside the line from left to right
            sorted_line = sorted(line, key=lambda x: x["box"][0])
            
            # Filter headers or short lines
            if len(sorted_line) >= 2:
                # Group adjacent words that are very close to form table cell text
                cells = []
                current_cell = []
                last_x_max = -1
                for item in sorted_line:
                    box = item["box"]
                    if last_x_max == -1:
                        current_cell.append(item["text"])
                        last_x_max = box[2]
                    elif box[0] - last_x_max < 25: # small gap means same cell
                        current_cell.append(item["text"])
                        last_x_max = max(last_x_max, box[2])
                    else:
                        cells.append(" ".join(current_cell))
                        current_cell = [item["text"]]
                        last_x_max = box[2]
                if current_cell:
                    cells.append(" ".join(current_cell))
                
                # If cells contain numbers and descriptions, it's highly likely to be a table row
                table_rows.append(cells)

        if table_rows:
            return [{
                "box": [0, 0, 1000, 1000],
                "rows": table_rows
            }]
        return []

    def run_table_transformer(self, image_path, ocr_results):
        """
        Runs TableTransformer structure recognition and returns extracted tabular rows.
        ocr_results format: List of Dict containing 'text' and 'box' [xmin, ymin, xmax, ymax]
        """
        has_model = self.load_model()
        
        if not has_model:
            return self._heuristics_table_extraction(ocr_results)

        try:
            image = Image.open(image_path).convert("RGB")
            width, height = image.size
        except Exception as e:
            logger.error(f"Failed to open image {image_path}: {e}")
            return self._heuristics_table_extraction(ocr_results)

        try:
            inputs = self.image_processor(images=image, return_tensors="pt")
            for k, v in inputs.items():
                inputs[k] = v.to(self.device)
                
            with torch.no_grad():
                outputs = self.model(**inputs)
                
            target_sizes = [image.size[::-1]]
            results = self.image_processor.post_process_object_detection(
                outputs, 
                threshold=0.6, 
                target_sizes=target_sizes
            )[0]
            
            boxes = results["boxes"].cpu().numpy()
            labels = results["labels"].cpu().numpy()
            scores = results["scores"].cpu().numpy()
            
            # Extract tables, columns, rows
            # Label index mappings:
            # 0: table, 1: table column, 2: table row
            table_boxes = []
            col_boxes = []
            row_boxes = []
            
            for box, label, score in zip(boxes, labels, scores):
                box_list = [float(x) for x in box]
                if label == 0:
                    table_boxes.append(box_list)
                elif label == 1:
                    col_boxes.append(box_list)
                elif label == 2:
                    row_boxes.append(box_list)

            # Fallback if no rows or columns detected by TableTransformer
            if not row_boxes or not col_boxes:
                logger.warning("TableTransformer detected no columns/rows. Falling back to heuristics.")
                return self._heuristics_table_extraction(ocr_results)

            # Sort rows top-to-bottom and columns left-to-right
            row_boxes = sorted(row_boxes, key=lambda b: b[1])
            col_boxes = sorted(col_boxes, key=lambda b: b[0])
            
            tables_output = []
            
            # If no tables boxes are detected, treat the entire page or detected row region as one table
            if not table_boxes:
                table_boxes = [[
                    min(b[0] for b in col_boxes),
                    min(b[1] for b in row_boxes),
                    max(b[2] for b in col_boxes),
                    max(b[3] for b in row_boxes)
                ]]
                
            for t_box in table_boxes:
                # Find rows and columns belonging to this table
                t_rows = [r for r in row_boxes if self._box_overlap(t_box, r)]
                t_cols = [c for c in col_boxes if self._box_overlap(t_box, c)]
                
                extracted_rows = []
                
                for r_box in t_rows:
                    row_cells = []
                    for c_box in t_cols:
                        # Define cell bounds
                        cell_xmin = c_box[0]
                        cell_ymin = r_box[1]
                        cell_xmax = c_box[2]
                        cell_ymax = r_box[3]
                        
                        # Find OCR tokens inside this cell using midpoint check
                        cell_tokens = []
                        for item in ocr_results:
                            box = item["box"]
                            mx, my = self._get_midpoint(box)
                            if cell_xmin <= mx <= cell_xmax and cell_ymin <= my <= cell_ymax:
                                cell_tokens.append(item)
                                
                        # Sort tokens left-to-right and join text
                        cell_tokens = sorted(cell_tokens, key=lambda x: x["box"][0])
                        cell_text = " ".join(t["text"] for t in cell_tokens)
                        row_cells.append(cell_text)
                    
                    # Only add rows that contain non-empty cells
                    if any(cell.strip() for cell in row_cells):
                        extracted_rows.append(row_cells)
                
                if extracted_rows:
                    tables_output.append({
                        "box": t_box,
                        "rows": extracted_rows
                    })
                    
            return tables_output
            
        except Exception as e:
            logger.warning(f"Error in TableTransformer processing: {e}. Falling back to heuristics.")
            return self._heuristics_table_extraction(ocr_results)

def run_table_transformer(image_path, ocr_results):
    module = TableTransformerModule()
    return module.run_table_transformer(image_path, ocr_results)
