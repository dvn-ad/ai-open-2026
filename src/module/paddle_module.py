from pathlib import Path
import torch
import logging

logger = logging.getLogger(__name__)

try:
    from paddleocr import PaddleOCRVL
except ImportError:
    PaddleOCRVL = None


def run_paddleocr(source):
    # output_dir = Path("./output")
    # output_dir.mkdir(parents=True, exist_ok=True)

    # NVIDIA GPU
    # pipeline = PaddleOCRVL()
    # Kunlunxin XPU
    # pipeline = PaddleOCRVL(device="xpu")
    # Hygon DCU
    # pipeline = PaddleOCRVL(device="dcu")
    # MetaX GPU
    # pipeline = PaddleOCRVL(device="metax_gpu")
    # Apple Silicon
    # pipeline = PaddleOCRVL(device="cpu")
    # Huawei Ascend NPU 
    # Huawei Ascend NPU please refer to Chapter 3 for inference using PaddlePaddle + vLLM

    # pipeline = PaddleOCRVL(use_doc_orientation_classify=True) # Use use_doc_orientation_classify to enable/disable document orientation classification model
    # pipeline = PaddleOCRVL(use_doc_unwarping=True) # Use use_doc_unwarping to enable/disable document unwarping module
    # pipeline = PaddleOCRVL(use_layout_detection=False) # Use use_layout_detection to enable/disable layout analysis module

    if PaddleOCRVL is not None:
        try:
            pipeline = PaddleOCRVL(
                device="gpu" if torch.cuda.is_available() else "cpu",
                use_doc_orientation_classify=True,
                use_doc_unwarping=True,
                use_layout_detection=False
            )

            output = pipeline.predict(source)
            for res in output:
                res.save_to_json(save_path='output/paddle.json')
            return output
        except Exception as e:
            logger.warning(f"PaddleOCRVL creation or prediction failed: {e}. Falling back to RapidOCR.")
            # Let the code fall through to the else (RapidOCR) block
    
    if True:  # Run the RapidOCR fallback if PaddleOCRVL was None or failed
        # Fallback to RapidOCR
        from rapidocr import RapidOCR, EngineType
        import json
        import os

        # Use CPU/Torch engine
        engine = RapidOCR(params={
            'Det.engine_type': EngineType.TORCH,
            'Cls.engine_type': EngineType.TORCH,
            'Rec.engine_type': EngineType.TORCH
        })

        result = engine(source)
        
        # Handle different RapidOCR version return types
        if isinstance(result, tuple) or isinstance(result, list):
            res_data = result[0]
        else:
            res_data = result

        boxes, txts, scores = None, None, None
        if hasattr(res_data, 'boxes'):
            boxes = res_data.boxes
            txts = res_data.txts
            scores = res_data.scores
        elif isinstance(res_data, dict):
            boxes = res_data.get('boxes')
            txts = res_data.get('txts')
            scores = res_data.get('scores')

        ocr_results = []
        if boxes is not None and txts is not None:
            # Check if scores is available, otherwise default to 1.0
            scores_list = scores if scores is not None else [1.0] * len(txts)
            for box, text, score in zip(boxes, txts, scores_list):
                # box can be [ [x1, y1], [x2, y2], [x3, y3], [x4, y4] ]
                try:
                    xs = [pt[0] for pt in box]
                    ys = [pt[1] for pt in box]
                    xmin = min(xs)
                    ymin = min(ys)
                    xmax = max(xs)
                    ymax = max(ys)
                    ocr_results.append({
                        "text": str(text),
                        "box": [float(xmin), float(ymin), float(xmax), float(ymax)],
                        "confidence": float(score)
                    })
                except Exception:
                    # Fallback for alternative box formats
                    ocr_results.append({
                        "text": str(text),
                        "box": [0.0, 0.0, 0.0, 0.0],
                        "confidence": float(score)
                    })

        os.makedirs('output', exist_ok=True)
        with open('output/paddle.json', 'w') as f:
            json.dump(ocr_results, f, indent=2)
        return ocr_results