from config.settings import CAMERA_URL, RTSP_URL, USE_RTSP
from modules.camera import IPCamera

if __name__ == "__main__":
    # Choose the correct URL based on settings
    stream_url = RTSP_URL if USE_RTSP else CAMERA_URL

    # Initialize and start the camera stream
    ip_camera = IPCamera(stream_url)
    ip_camera.start_stream()