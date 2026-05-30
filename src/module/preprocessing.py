import cv2
import numpy as np
import pypdfium2 as pdfium
from PIL import Image
import os

def pdf_to_images(pdf_path, dpi=300):
    """
    Render PDF pages into high-resolution PIL images using pypdfium2.
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
    doc = pdfium.PdfDocument(pdf_path)
    images = []
    scale = dpi / 72.0  # pypdfium2 uses 72 points per inch as default
    
    for i in range(len(doc)):
        page = doc[i]
        bitmap = page.render(scale=scale)
        pil_img = bitmap.to_pil()
        images.append(pil_img)
    return images

def pil_to_cv2(pil_img):
    """
    Convert a PIL Image to an OpenCV BGR image.
    """
    cv_img = np.array(pil_img)
    if len(cv_img.shape) == 3:
        if cv_img.shape[2] == 4:
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGBA2BGR)
        else:
            cv_img = cv2.cvtColor(cv_img, cv2.COLOR_RGB2BGR)
    return cv_img

def cv2_to_pil(cv_img):
    """
    Convert an OpenCV BGR image to a PIL Image.
    """
    if len(cv_img.shape) == 3:
        return Image.fromarray(cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB))
    return Image.fromarray(cv_img)

def get_skew_angle(cv_img):
    """
    Detect the skew angle of a document page using contours of text blocks.
    """
    # Convert to grayscale
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) if len(cv_img.shape) == 3 else cv_img
    
    # Invert and binarize using Otsu thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Dilate text blocks horizontally to merge words/lines into solid bars
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=5)
    
    # Find contours
    contours, _ = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    angles = []
    
    for contour in contours:
        if cv2.contourArea(contour) < 150:
            continue
            
        rect = cv2.minAreaRect(contour)
        angle = rect[2]
        
        # minAreaRect returns angles depending on implementation version.
        # Standardize angle to a relative skew offset in range [-45, 45]
        if angle < -45:
            angle = 90 + angle
        elif angle > 45:
            angle = angle - 90
            
        # Ignore outliers (anything skewed by more than 15 degrees is likely non-text or noise)
        if abs(angle) < 15:
            angles.append(angle)
            
    if not angles:
        return 0.0
        
    return float(np.median(angles))

def rotate_image(cv_img, angle):
    """
    Rotate an image around its center by a specific angle (in degrees).
     Fills background margins with solid white.
    """
    if abs(angle) < 0.05:
        return cv_img
        
    (h, w) = cv_img.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    
    border_val = (255, 255, 255) if len(cv_img.shape) == 3 else 255
    rotated = cv2.warpAffine(
        cv_img, M, (w, h), 
        flags=cv2.INTER_CUBIC, 
        borderMode=cv2.BORDER_CONSTANT, 
        borderValue=border_val
    )
    return rotated

def deskew_image(cv_img):
    """
    Automatically deskew the image.
    Returns: (deskewed_image, detected_angle)
    """
    angle = get_skew_angle(cv_img)
    if abs(angle) < 0.1:
        return cv_img, 0.0
    return rotate_image(cv_img, angle), angle

def correct_orientation_via_projection(cv_img):
    """
    Checks if a document is rotated by 90/270 degrees (landscape vs. portrait)
    by analyzing the variance of horizontal vs vertical projection profiles.
    Returns: (corrected_image, rotation_applied_degrees)
    """
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) if len(cv_img.shape) == 3 else cv_img
    
    # Standard thresholding
    _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    # Calculate projection profiles
    # Sum pixels along horizontal rows (axis=1) and vertical columns (axis=0)
    proj_horiz = np.sum(thresh, axis=1)
    proj_vert = np.sum(thresh, axis=0)
    
    # High variance in horizontal projection implies horizontal lines of text (standard portrait)
    # High variance in vertical projection implies vertical orientation (rotated 90 or 270)
    var_horiz = np.var(proj_horiz)
    var_vert = np.var(proj_vert)
    
    # If vertical variance is significantly higher, it is likely rotated 90 or 270 degrees
    if var_vert > var_horiz * 1.5:
        # We need to determine if we rotate 90 degrees clockwise or counterclockwise.
        # We can look at the half-page projection profiles or simply check OCR direction.
        # Since standard scans are landscape-flipped, let's rotate 90 degrees and re-verify.
        img_rot90 = cv2.rotate(cv_img, cv2.ROTATE_90_CLOCKWISE)
        return img_rot90, 90
        
    return cv_img, 0

def correct_orientation_paddleocr(cv_img):
    """
    Optionally corrects page orientation using PaddleOCR's angle classifier.
    """
    try:
        from paddleocr import PaddleOCR
        # Initialize a lightweight PaddleOCR for angle classification
        ocr = PaddleOCR(use_angle_cls=True, lang='en', show_log=False)
        # We perform detection with classification, but no recognition (det=True, rec=False, cls=True)
        results = ocr.ocr(cv_img, det=True, rec=False, cls=True)
        
        if not results or not results[0]:
            return cv_img, 0
            
        # Parse the angle classifications
        angles = []
        for res in results[0]:
            # res structure: [box, (angle_label, confidence)]
            if len(res) > 1 and isinstance(res[1], tuple):
                angle_label, conf = res[1]
                if conf > 0.7:
                    angles.append(int(angle_label))
                    
        if not angles:
            return cv_img, 0
            
        # Find dominant angle (0, 90, 180, 270)
        dominant_angle = max(set(angles), key=angles.count)
        
        if dominant_angle == 90:
            return cv2.rotate(cv_img, cv2.ROTATE_90_CLOCKWISE), 90
        elif dominant_angle == 180:
            return cv2.rotate(cv_img, cv2.ROTATE_180), 180
        elif dominant_angle == 270:
            return cv2.rotate(cv_img, cv2.ROTATE_90_COUNTERCLOCKWISE), 270
            
        return cv_img, 0
    except Exception as e:
        print(f"Warning: PaddleOCR orientation check failed ({e}). Falling back to projection check.")
        return correct_orientation_via_projection(cv_img)

def enhance_binarize_image(cv_img):
    """
    Applies binarization and contrast enhancement for optimal OCR results.
    """
    gray = cv2.cvtColor(cv_img, cv2.COLOR_BGR2GRAY) if len(cv_img.shape) == 3 else cv_img
    
    # Adaptive thresholding to remove shadows and dark patches
    enhanced = cv2.adaptiveThreshold(
        gray, 255, 
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
        cv2.THRESH_BINARY, 15, 8
    )
    
    # Convert single channel back to 3 channel for compatibility with Docling/OCR models
    return cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)

def preprocess_page(pil_img, use_paddle_orient=True):
    """
    Main page-level preprocessing orchestrator.
    Takes a PIL Image and returns a preprocessed PIL Image.
    """
    cv_img = pil_to_cv2(pil_img)
    
    # 1. Orientation Correction (90/180/270 deg)
    if use_paddle_orient:
        cv_img, rot_angle = correct_orientation_paddleocr(cv_img)
        if rot_angle != 0:
            print(f"Page orientation corrected by {rot_angle} degrees.")
    else:
        cv_img, rot_angle = correct_orientation_via_projection(cv_img)
        if rot_angle != 0:
            print(f"Page landscape-to-portrait corrected by {rot_angle} degrees.")
            
    # 2. Deskewing (fine tilt correction)
    cv_img, skew_angle = deskew_image(cv_img)
    if abs(skew_angle) > 0.1:
        print(f"Page deskewed by {skew_angle:.2f} degrees.")
        
    # 3. Return preprocessed PIL Image
    return cv2_to_pil(cv_img)
