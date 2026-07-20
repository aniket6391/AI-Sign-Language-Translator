# AI Sign Language Translator

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-FF6F00.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.9.0-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.11-blue.svg)

An AI-powered Sign Language Translator that recognizes hand gestures in real-time using a laptop webcam and converts them into readable text and speech. Developed as an MCA Final Year Project.

## 🚀 Features
- **Real-Time Recognition:** Processes live webcam feeds with minimal latency.
- **MediaPipe Integration:** Extracts 21 3D hand landmarks to isolate the hand from background noise.
- **Deep Learning (CNN):** Custom Convolutional Neural Network built with TensorFlow/Keras for high-accuracy classification.
- **Text-to-Speech (TTS):** Automatically speaks the predicted sign using `pyttsx3` when confidence is high.
- **Dataset Collection Tool:** Built-in UI to easily capture and expand the dataset for new signs.
- **Native OpenCV Window:** A sleek, extremely fast desktop terminal experience.

## 📁 Project Structure
The project is modularly divided into `prediction`, `training`, and `utils` modules. Please see `docs/GitHub_Structure.md` for a detailed breakdown.

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/AI_Sign_Language_Translator.git
   cd AI_Sign_Language_Translator
   ```

2. **Create a Virtual Environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

## 📖 How to Use
1. **Start the App:** Run `python main.py`. A camera window will open.
2. **Collect Data:** Press `c`. Enter the class name in the terminal. The app will automatically collect data from the camera.
3. **Train Model:** Press `t`. The CNN will train on your collected images. Check terminal for progress.
4. **Predict:** Press `p`. Show your signs to the webcam. The predicted text will appear directly on the camera screen and be spoken aloud.
5. **Quit:** Press `q` to exit.

## 📄 Documentation
Check the `docs/` folder for the Project Report, Presentation slides, Viva Questions, and more.
