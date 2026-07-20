import os
import numpy as np
import tensorflow as tf

class Predictor:
    """
    Utility class to load the trained CNN model and make real-time predictions.
    """
    def __init__(self, model_path="models/cnn_model.keras", labels_path="models/labels.txt"):
        self.model = None
        self.classes = []
        
        # Load Model
        if os.path.exists(model_path):
            self.model = tf.keras.models.load_model(model_path)
            
        # Load Labels
        if os.path.exists(labels_path):
            with open(labels_path, "r") as f:
                self.classes = f.read().strip().split("\n")

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
