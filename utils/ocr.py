import cv2
import pytesseract
import os
from config.settings import IMAGE_SAVE_PATH

# Set Tesseract OCR path if needed (for Windows)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_frame(frame):
    """Extracts text from a given image frame using Tesseract OCR."""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray).strip()
    return text

def save_image(frame, text):
    """Saves the captured image with a filename based on extracted text."""
    if not os.path.exists(IMAGE_SAVE_PATH):
        os.makedirs(IMAGE_SAVE_PATH)
    image_path = os.path.join(IMAGE_SAVE_PATH, f"{text}.jpg")
    cv2.imwrite(image_path, frame)
    return image_path