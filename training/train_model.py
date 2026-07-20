import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from training.preprocess import preprocess_offline

def build_model(input_shape=(128, 128, 3), num_classes=2):
    """
    Builds and compiles the Convolutional Neural Network (CNN) architecture.
    Architecture:
    Input -> Conv2D(ReLU) -> MaxPool -> Conv2D(ReLU) -> MaxPool -> Flatten -> Dense -> Dropout -> Dense(Softmax)
    """
    model = Sequential()
    
    # Convolutional Block 1
    # 32 filters, 3x3 kernel size. Extracts low-level features (edges, curves)
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2))) # Reduces spatial dimensions
    
    # Convolutional Block 2
    # 64 filters. Extracts higher-level features (shapes, patterns)
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    
    # Flattening Layer
    # Converts the 2D feature maps into a 1D vector for the Dense layers
    model.add(Flatten())
    
    # Fully Connected (Dense) Layer
    model.add(Dense(128, activation='relu'))
    
    # Dropout Layer
    # Randomly drops 50% of neurons to prevent overfitting to the training data
    model.add(Dropout(0.5))
    
    # Output Layer
    # Softmax activation provides a probability distribution across all classes
    model.add(Dense(num_classes, activation='softmax'))
    
    # Compile the model
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
                  
    return model

def train_cnn_model(dataset_dir="dataset/train", processed_dir="dataset/processed", epochs=15, batch_size=32):
    """
    Loads data, builds the model, trains it, and saves the trained model and labels.
    """
    print("Running offline preprocessing...")
    # This will skip images that are already processed
    classes = preprocess_offline(dataset_dir, processed_dir, img_size=(128, 128))
    
    if not classes:
        raise ValueError("No dataset found. Please collect data first.")
        
    num_classes = len(classes)
    
    print("Initializing Data Generators...")
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2 # 20% validation
    )
    
    train_generator = datagen.flow_from_directory(
        processed_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )
    
    val_generator = datagen.flow_from_directory(
        processed_dir,
        target_size=(128, 128),
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )
    
    # Extract the class labels in the exact order the generator assigned them
    class_labels = list(train_generator.class_indices.keys())
    
    print(f"Building model for {num_classes} classes...")
    model = build_model(input_shape=(128, 128, 3), num_classes=num_classes)
    
    print("Training model...")
    history = model.fit(
        train_generator,
        validation_data=val_generator,
        epochs=epochs
    )
    
    # Ensure models directory exists
    os.makedirs("models", exist_ok=True)
    
    # Save the trained Keras model
    model_path = os.path.join("models", "cnn_model.keras")
    model.save(model_path)
    print(f"Model saved to {model_path}")
    
    # Save the class labels so they map correctly to prediction outputs
    labels_path = os.path.join("models", "labels.txt")
    with open(labels_path, "w") as f:
        f.write("\n".join(class_labels))
    print(f"Labels saved to {labels_path}")
        
    return history, class_labels
