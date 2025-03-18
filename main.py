import cv2
from config.settings import CAMERA_URL
from utils.ocr import extract_text_from_frame, save_image
from utils.video_search import search_youtube_video

def main():
    print("Starting IP Camera Stream...")
    cap = cap = cv2.VideoCapture(0) 

    if not cap.isOpened():
        print("Error: Unable to access the camera stream.")
        return

    detected_texts = set()  # To avoid repeated detections

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break
        
        # Extract text from the frame
        text = extract_text_from_frame(frame)

        if text and text not in detected_texts:
            print(f"Detected Text: {text}")
            detected_texts.add(text)
            
            # Save the image
            save_image(frame, text)
            
            # Search YouTube and play video
            search_youtube_video(text)

        # Show the live feed
        cv2.imshow("Camera Feed", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()