import cv2
import mediapipe as mp

class HandDetector:
    """
    A utility class to handle MediaPipe Hands initialization and frame processing.
    """
    def __init__(self, static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5):
        # Initialize MediaPipe Hands solution
        self.mp_hands = mp.solutions.hands
        self.mp_draw = mp.solutions.drawing_utils
        
        # Configure the Hands object
        self.hands = self.mp_hands.Hands(
            static_image_mode=static_image_mode,
            max_num_hands=max_num_hands,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=min_tracking_confidence
        )

    def process_frame(self, frame):
        """
        Process an RGB frame to detect hands.
        Args:
            frame: A numpy array representing the image (in RGB format).
        Returns:
            frame: The image with landmarks drawn.
            results: The raw MediaPipe results object.
        """
        # Process the RGB image to detect hands
        results = self.hands.process(frame)
        
        # Draw landmarks if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw the 21 landmarks and the connections between them
                self.mp_draw.draw_landmarks(
                    frame, 
                    hand_landmarks, 
                    self.mp_hands.HAND_CONNECTIONS,
                    # Custom styling for landmarks (Dots)
                    self.mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=3),
                    # Custom styling for connections (Lines)
                    self.mp_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2)
                )
        return frame, results
