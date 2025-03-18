
import cv2
import pytesseract
import os
import time
from utils.video_search import search_youtube_video


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


API_KEY = "8fd3d69fbdmsh91400bc8e41583ap1fbfcajsnaaf910b35543"  


IMAGE_SAVE_PATH = "captured_frames"
os.makedirs(IMAGE_SAVE_PATH, exist_ok=True)



def extract_text_from_frame(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    text = pytesseract.image_to_string(gray).strip()
    return text

def save_frame(frame, count):
    image_path = os.path.join(IMAGE_SAVE_PATH, f"frame_{count}.jpg")
    cv2.imwrite(image_path, frame)

def start_camera():
    
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
       print("Error: Unable to access camera.")
       return
    else:
       print("Camera successfully opened!")
  #  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
  #  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    
    frame_count = 0
    detected_text = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Camera", frame)
        save_frame(frame, frame_count) 

        text = extract_text_from_frame(frame)
        print(f"Detected Text: {text}")

        if text: 
            detected_text = text
            print(f"Text detected: {detected_text}")
            break

        frame_count += 1
        time.sleep(1) 

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if detected_text:
        search_youtube_video(detected_text, API_KEY)

    generate_video(frame_count)

def generate_video(frame_count):
    """Creates a video from saved frames."""
    video_name = "captured_video.avi"
    
    first_frame_path = os.path.join(IMAGE_SAVE_PATH, "frame_0.jpg")
    if not os.path.exists(first_frame_path):
        print("Error: No frames captured. Video cannot be created.")
        return

    frame = cv2.imread(first_frame_path)
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'XVID'), 10, (width, height))

    for i in range(frame_count):
        frame_path = os.path.join(IMAGE_SAVE_PATH, f"frame_{i}.jpg")
        if os.path.exists(frame_path):
            video.write(cv2.imread(frame_path))

    video.release()
    print(f"Video saved as {video_name}")

if __name__ == "__main__":
    start_camera()