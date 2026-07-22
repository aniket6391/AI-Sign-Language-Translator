import os
import sys
import numpy as np
import tensorflow as tf

class Predictor:
    """
    Utility class to load the trained CNN model and make real-time predictions.
    """
    def __init__(self):
        self.model = None
        self.classes = []

        # Get correct path
        if getattr(sys, "frozen", False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        model_path = os.path.join(base_path, "models", "cnn_model.keras")
        labels_path = os.path.join(base_path, "models", "labels.txt")

        print("Model Path:", model_path)
        print("Labels Path:", labels_path)

        # Load Model
        if os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
            print("✅ Model Loaded")
        else:
            print("❌ Model Not Found")

        # Load Labels
        if os.path.exists(labels_path):
            with open(labels_path, "r") as f:
                self.classes = f.read().strip().split("\n")
            print("✅ Labels Loaded")
        else:
            print("❌ Labels Not Found")

    def is_ready(self):
        """Checks if both model and labels are successfully loaded."""
        return self.model is not None and len(self.classes) > 0

    def predict(self, processed_img):
        """
        Takes a processed image (cropped, resized, normalized) and predicts the sign.
        Returns:
            predicted_label (str): The name of the predicted sign.
            confidence (float): The probability of the prediction (0.0 to 1.0).
        """
        if not self.is_ready() or processed_img is None:
            return None, 0.0
            
        # Keras models expect inputs in batches. 
        # Our single image has shape (128, 128, 3), we expand it to (1, 128, 128, 3)
        img_batch = np.expand_dims(processed_img, axis=0)
        
        # Perform inference
        predictions = self.model.predict(img_batch, verbose=0)
        
        # Get the index of the highest probability
        class_index = np.argmax(predictions[0])
        confidence = float(predictions[0][class_index])
        
        predicted_label = self.classes[class_index]
        return predicted_label, confidence
