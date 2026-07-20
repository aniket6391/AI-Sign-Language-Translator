import os
import cv2
from utils.mediapipe_utils import HandDetector
from utils.preprocessing import Preprocessor

def preprocess_offline(dataset_dir="dataset/train", processed_dir="dataset/processed", img_size=(128, 128)):
    """
    Scans the dataset directory, processes all raw images by extracting the hand,
    resizing, and saving them to the processed_dir. Skips already processed images.
    """
    if not os.path.exists(dataset_dir):
        print(f"Dataset directory '{dataset_dir}' not found.")
        return []
        
    os.makedirs(processed_dir, exist_ok=True)
    
    detector = HandDetector(static_image_mode=True, max_num_hands=1)
    preprocessor = Preprocessor(target_size=img_size)
    
    classes = sorted([d for d in os.listdir(dataset_dir) if os.path.isdir(os.path.join(dataset_dir, d))])
    
    if not classes:
        print("No class directories found in dataset.")
        return []

    print(f"Starting offline preprocessing. Processed images will be saved to '{processed_dir}'...")

    for class_name in classes:
        class_dir = os.path.join(dataset_dir, class_name)
        out_class_dir = os.path.join(processed_dir, class_name)
        os.makedirs(out_class_dir, exist_ok=True)
        
        images = os.listdir(class_dir)
        new_count = 0
        
        for img_name in images:
            out_img_path = os.path.join(out_class_dir, img_name)
            if os.path.exists(out_img_path):
                continue # Skip already processed
                
            img_path = os.path.join(class_dir, img_name)
            img = cv2.imread(img_path)
            if img is None:
                continue
                
            # If the image is already perfectly cropped and resized (128x128),
            # simply copy it over to bypass the MediaPipe extraction again.
            if img.shape[:2] == img_size:
                cv2.imwrite(out_img_path, img)
                new_count += 1
                continue
                
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            _, results = detector.process_frame(img_rgb)
            
            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                processed_img = preprocessor.crop_and_resize(img_rgb, hand_landmarks)
                
                if processed_img is not None:
                    # Convert back to BGR for saving
                    processed_img_bgr = cv2.cvtColor(processed_img, cv2.COLOR_RGB2BGR)
                    cv2.imwrite(out_img_path, processed_img_bgr)
                    new_count += 1

        if new_count > 0:
            print(f"Processed {new_count} new images for class '{class_name}'.")

    return classes
