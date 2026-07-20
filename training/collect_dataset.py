import os
import cv2

class DatasetCollector:
    """
    Utility class to manage the collection and saving of dataset images.
    Organizes images into class-specific folders inside dataset/train/
    """
    def __init__(self, base_dir="dataset/train"):
        self.base_dir = base_dir
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

    def create_class_dir(self, class_name):
        """Creates a directory for a new sign language class if it doesn't exist."""
        class_name = class_name.upper().strip()
        class_path = os.path.join(self.base_dir, class_name)
        if not os.path.exists(class_path):
            os.makedirs(class_path)
        return class_path

    def get_existing_count(self, class_name):
        """Returns the number of images currently saved for a given class."""
        class_name = class_name.upper().strip()
        class_path = os.path.join(self.base_dir, class_name)
        if not os.path.exists(class_path):
            return 0
        return len(os.listdir(class_path))

    def save_image(self, frame, class_name, count):
        """
        Saves an RGB frame to the dataset directory as a JPEG.
        Converts RGB back to BGR for cv2.imwrite.
        """
        class_name = class_name.upper().strip()
        class_path = self.create_class_dir(class_name)
        file_path = os.path.join(class_path, f"{class_name}_{count}.jpg")
        
        # Streamlit provides the frame in RGB, OpenCV imwrite expects BGR
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.imwrite(file_path, frame_bgr)
        return file_path
    
    def get_dataset_info(self):
        """Returns total classes and total images currently in the dataset."""
        if not os.path.exists(self.base_dir):
            return 0, 0
        classes = os.listdir(self.base_dir)
        total_images = sum([len(os.listdir(os.path.join(self.base_dir, c))) for c in classes])
        return len(classes), total_images
