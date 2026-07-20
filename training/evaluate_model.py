import os
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from training.preprocess import load_and_preprocess_data

def evaluate_cnn_model(dataset_dir="dataset/train", model_path="models/cnn_model.keras"):
    """
    Evaluates the trained CNN model using standard ML classification metrics.
    Suitable for demonstrating academic rigor in an MCA project.
    """
    if not os.path.exists(model_path):
        print("Error: Model file not found. Please train the model first.")
        return
        
    print("Loading data for evaluation...")
    # We call our preprocessor. It uses a fixed random_state=42, so the 20% validation split 
    # returned here is exactly the same unseen data the model was validated against during training.
    _, X_val, _, y_val, classes = load_and_preprocess_data(dataset_dir)
    
    if X_val is None or len(X_val) == 0:
        print("Error: No validation data available.")
        return
        
    print(f"Loading trained model from {model_path}...")
    model = tf.keras.models.load_model(model_path)
    
    print("Running predictions on validation set...")
    # y_val is one-hot encoded (e.g., [0, 1, 0]), convert it back to 1D class indices (e.g., 1)
    y_true = np.argmax(y_val, axis=1)
    
    # Predict probabilities for the entire validation set
    y_pred_probs = model.predict(X_val)
    # Convert prediction probabilities to 1D class indices
    y_pred = np.argmax(y_pred_probs, axis=1)
    
    # Calculate standard Machine Learning Metrics using scikit-learn
    accuracy = accuracy_score(y_true, y_pred)
    conf_matrix = confusion_matrix(y_true, y_pred)
    
    # classification_report automatically calculates Precision, Recall, and F1-Score for every class
    class_report = classification_report(y_true, y_pred, target_names=classes)
    
    # Print the detailed report
    print("\n" + "="*50)
    print("MODEL EVALUATION METRICS")
    print("="*50)
    print(f"Overall Accuracy : {accuracy*100:.2f}%\n")
    
    print("Classification Report (Precision, Recall, F1-Score):")
    print(class_report)
    
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("="*50)
    
if __name__ == "__main__":
    # If this script is run directly, execute the evaluation function
    evaluate_cnn_model()
