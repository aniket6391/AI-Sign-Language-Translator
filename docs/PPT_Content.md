# Presentation Outline (PPT Content)

**Slide 1: Title Slide**
- Project Title: AI Sign Language Translator
- Subtitle: Real-Time Gesture Recognition using Deep Learning
- Submitted By: [Your Name]
- Degree: Master of Computer Applications (MCA)

**Slide 2: Problem Statement**
- Communication gap between hearing/speech-impaired individuals and the general public.
- Lack of accessible, real-time translation tools.

**Slide 3: Objectives**
- Develop an AI application to recognize hand gestures in real-time.
- Convert recognized signs into readable text and voice output.
- Build a user-friendly dashboard for dataset collection and model training.

**Slide 4: Technology Stack**
- Language: Python
- Frontend: Streamlit
- Computer Vision: OpenCV, MediaPipe
- Machine Learning: TensorFlow, Keras, Scikit-learn
- Text-to-Speech: pyttsx3

**Slide 5: System Architecture**
- Diagram Flow: Webcam -> OpenCV -> MediaPipe Landmarks -> Crop/Resize -> CNN Model -> Prediction -> Streamlit UI / Audio.

**Slide 6: MediaPipe Hand Tracking**
- Explaining how MediaPipe extracts 21 3D landmarks.
- Why it's better than raw pixel background subtraction.

**Slide 7: CNN Model Architecture**
- 2 Convolutional Layers (Feature Extraction).
- MaxPooling (Dimensionality Reduction).
- Dense Layers & Dropout (Classification & Overfitting prevention).

**Slide 8: Dashboard & Features**
- Showcase the Streamlit UI.
- Explain the built-in Dataset Collector and 1-click Training.

**Slide 9: Results & Evaluation**
- Display the Accuracy, Precision, and Confusion Matrix.
- Mention Real-time FPS achieved.

**Slide 10: Future Enhancements & Conclusion**
- Future: LSTM for video sequences, Mobile App deployment.
- Conclusion: Successfully built a scalable AI translator.
