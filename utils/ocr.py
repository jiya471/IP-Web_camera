"""
import cv2
import pytesseract
import os
from config.settings import IMAGE_SAVE_PATH


# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_frame(frame):

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray).strip()
    return text

def save_image(frame, text):
 
    if not os.path.exists(IMAGE_SAVE_PATH):
        os.makedirs(IMAGE_SAVE_PATH)
    image_path = os.path.join(IMAGE_SAVE_PATH, f"{text}.jpg")
    cv2.imwrite(image_path, frame)
    return image_path


"""

import cv2
import pytesseract
import os
from config.settings import IMAGE_SAVE_PATH

# Set correct path for Tesseract OCR (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def extract_text_from_frame(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    text = pytesseract.image_to_string(gray).strip()
    return text

def save_image(frame, text):
    if not os.path.exists(IMAGE_SAVE_PATH):
        os.makedirs(IMAGE_SAVE_PATH)

    image_path = os.path.join(IMAGE_SAVE_PATH, f"{text}.jpg")
    cv2.imwrite(image_path, frame)
    return image_path