import cv2

def start_camera():
    print("Attempting to start the camera...")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Failed to open camera!")
        return
    else:
        print("Camera started successfully!")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        cv2.imshow("Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    cap.release()
    cv2.destroyAllWindows()

start_camera()