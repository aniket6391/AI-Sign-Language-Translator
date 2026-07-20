# GitHub Repository Structure

```text
AI_Sign_Language_Translator/
│
├── app.py                      # Main Streamlit dashboard application
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview and setup instructions
├── .gitignore                  # Git ignore file
│
├── assets/                     # UI assets
│   ├── css/                    # Custom styling (style.css)
│   ├── images/
│   └── icons/
│
├── dataset/                    # Stored image data (Auto-generated)
│   └── train/                  # Contains subfolders for each sign class
│
├── models/                     # Saved trained models and label mappings
│   ├── cnn_model.keras         # The trained Neural Network
│   └── labels.txt              # Class names corresponding to model outputs
│
├── training/                   # Model training pipeline
│   ├── collect_dataset.py      # Logic for capturing webcam images
│   ├── preprocess.py           # Data normalization and train/test splitting
│   ├── train_model.py          # CNN architecture and Keras fit loop
│   └── evaluate_model.py       # Scikit-learn metrics (Accuracy, Confusion Matrix)
│
├── prediction/                 # Real-time inference logic
│   └── predictor.py            # Wrapper to load model and run model.predict()
│
├── utils/                      # Helper functions
│   ├── camera.py               # cv2.VideoCapture management
│   ├── mediapipe_utils.py      # MediaPipe initialization and drawing logic
│   ├── preprocessing.py        # Real-time frame cropping and resizing
│   └── speech.py               # pyttsx3 threading logic
│
└── docs/                       # Project Documentation
    ├── Project_Report.md
    ├── PPT_Content.md
    ├── Viva_Questions.md
    ├── Interview_Questions.md
    ├── Deployment_Guide.md
    └── User_Manual.md
```
