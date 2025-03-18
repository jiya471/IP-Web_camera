"""
import cv2
class IPCamera:
    def _init_(self, stream_url):
       
        self.cap = cv2.VideoCapture(self.url)  

        if not self.cap.isOpened():
            print(f"Error: Could not open stream at {self.url}")
            exit()

def start_stream(self):
    print(f"Connecting to: {self.url}")

    while True:
        ret, frame = self.cap.read()
        if not ret:
            print("Error: Failed to capture image.")
            break

        cv2.imshow("IP Camera Stream", frame)

        # Read a key press (with a short delay so OpenCV can refresh the window)
        key = cv2.waitKey(1) & 0xFF

        # If the user presses 'c', capture and save the current frame
        if key == ord('c'):
            cv2.imwrite("captured_frame.jpg", frame)
            print("Captured and saved as 'captured_frame.jpg'")

        # Press 'q' to quit the stream
        if key == ord('q'):
            print("Stream closed.")
            break

 
    self.cap.release()
    cv2.destroyAllWindows()

    """



import webbrowser

def search_youtube_video(query):
   
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    print(f"Opening YouTube search: {search_url}")
    webbrowser.open(search_url)
import cv2

class IPCamera:
    def _init_(self, stream_url):
        self.url = stream_url
        self.cap = cv2.VideoCapture(self.url)

        if not self.cap.isOpened():
            print(f"Error: Could not open stream at {self.url}")
            exit()

    def start_stream(self):
        print(f"Connecting to: {self.url}")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break

            cv2.imshow("IP Camera Stream", frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('c'):
                cv2.imwrite("captured_frame.jpg", frame)
                print("Captured and saved as 'captured_frame.jpg'.")

            if key == ord('q'):
                print("Stream closed.")
                break

        self.cap.release()
        cv2.destroyAllWindows()