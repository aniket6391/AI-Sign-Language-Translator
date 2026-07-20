import cv2
import numpy as np

class Preprocessor:
    """
    Handles image transformations required before feeding frames into the CNN.
    """
    def __init__(self, target_size=(128, 128), padding=20):
        self.target_size = target_size
        self.padding = padding

    def get_bounding_box(self, frame, hand_landmarks):
        """
        Calculates a bounding box around the detected hand landmarks.
        """
        h, w, c = frame.shape
        x_min, y_min = w, h
        x_max, y_max = 0, 0

        # Find the min and max coordinates among all 21 landmarks
        for lm in hand_landmarks.landmark:
            x, y = int(lm.x * w), int(lm.y * h)
            if x < x_min: x_min = x
            if y < y_min: y_min = y
            if x > x_max: x_max = x
            if y > y_max: y_max = y

        # Apply padding around the hand to ensure no parts are cut off
        x_min = max(0, x_min - self.padding)
        y_min = max(0, y_min - self.padding)
        x_max = min(w, x_max + self.padding)
        y_max = min(h, y_max + self.padding)

        return x_min, y_min, x_max, y_max

    def crop_and_resize(self, frame, hand_landmarks):
        """
        Crops the frame based on the hand bounding box and resizes it to the target size.
        Returns the processed image array.
        """
        x_min, y_min, x_max, y_max = self.get_bounding_box(frame, hand_landmarks)
        
        # Crop the image using array slicing
        cropped_img = frame[y_min:y_max, x_min:x_max]
        
        # Guard against invalid crops (e.g. hand off-screen)
        if cropped_img.size == 0:
            return None
            
        # Resize the cropped image to standard size (e.g., 128x128)
        resized_img = cv2.resize(cropped_img, self.target_size)
        return resized_img
