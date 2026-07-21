import streamlit as st
import sys
import os
import time

# Ensure the current directory is in the path so we can import main
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    from main import main as run_opencv_app
except ImportError:
    st.error("Error: Could not import main.py. Make sure it exists in the same folder as app.py.")
    st.stop()

# -------------------------------------------------------------
# MAIN DASHBOARD UI
# -------------------------------------------------------------
st.set_page_config(page_title="Sign Language AI", layout="centered", page_icon="🤟")

st.title("🤟 AI Sign Language Translator")
st.markdown("---")

st.info(
    "**Local Vision System Ready.**\n\n"
    "Click **START** to open the native camera window."
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    start_clicked = st.button("🚀 Start Camera", use_container_width=True, type="primary")

st.markdown("---")

# -------------------------------------------------------------
# APPLICATION LAUNCH LOGIC
# -------------------------------------------------------------
if start_clicked:
    with st.spinner("Initializing Neural Network and Camera..."):
        time.sleep(1) # Small delay for UX
        
    st.success("✅ Application Running! Check your taskbar for the new Python window.")
    
    # This completely blocks Streamlit while the OpenCV app is open,
    # which is exactly what we want. It prevents Streamlit from doing weird things.
    try:
        run_opencv_app()
        st.info("ℹ️ Camera window closed. Click Start to run again.")
    except Exception as e:
        st.error(f"An error occurred while running the app: {e}")
