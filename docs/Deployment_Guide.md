# Deployment Guide

## 1. Local Deployment (Windows/Mac/Linux)
The easiest way to deploy this application is locally.
1. Ensure Python 3.9+ is installed.
2. Open a terminal in the project directory.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run app.py`
5. The dashboard will automatically open in your default web browser at `http://localhost:8501`.

## 2. Cloud Deployment (Streamlit Community Cloud)
You can host this dashboard for free on Streamlit Cloud, however, **accessing the client's webcam over the internet requires WebRTC**, which is slightly different from the local `cv2.VideoCapture(0)` approach.

To deploy exactly as-is for a portfolio presentation:
1. Push the entire codebase to a public GitHub repository.
2. Note: Do **not** push the `venv/` folder. Ensure `.gitignore` is active.
3. Go to [share.streamlit.io](https://share.streamlit.io/).
4. Click "New App".
5. Select your repository, branch (`main`), and main file path (`app.py`).
6. Click Deploy.
*(Note: OpenCV `VideoCapture(0)` on a cloud server will look for a webcam plugged into the server rack, not the user's laptop. For real cloud webcam access, you would need to integrate the `streamlit-webrtc` library in the future).*
