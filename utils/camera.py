import cv2

class Camera:
    """
    A utility class to manage the webcam connection using OpenCV.
    Keeps the camera logic separate from the UI layer.
    """
    def __init__(self, src=0):
        self.src = src
        self.cap = None

    def start(self):
        """Initializes the webcam capture."""
        if self.cap is None or not self.cap.isOpened():
            self.cap = cv2.VideoCapture(self.src)

    def stop(self):
        """Releases the webcam resources."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    def get_frame(self):
        """
        Reads a frame from the webcam.
        Returns the frame converted to RGB format (which Streamlit expects).
        Returns None if frame cannot be read.
        """
        if self.cap is not None and self.cap.isOpened():
            success, frame = self.cap.read()
            if success:
                # OpenCV captures in BGR, we convert to RGB for Streamlit and MediaPipe
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Flip the frame horizontally for a mirror effect
                frame = cv2.flip(frame, 1)
                return frame
        return None
