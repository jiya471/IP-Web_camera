import cv2

class IPCamera:
    def _init_(self, url):
        """Initialize the IP Camera with the given stream URL."""
        self.url = url
        self.cap = cv2.VideoCapture(self.url)

        if not self.cap.isOpened():
            print(f"❌ Error: Could not open stream at {self.url}")
            exit()

    def start_stream(self):
        """Start the live video stream."""
        print(f"📡 Connecting to: {self.url}")

        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("❌ Error: Failed to capture image.")
                break

            # Display the video feed
            cv2.imshow("IP Camera Stream", frame)

            # Press 'q' to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
        print("📴 Stream closed.")