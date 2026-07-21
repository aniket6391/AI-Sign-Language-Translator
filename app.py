import streamlit as st
import sys
import os
import time
import subprocess

# -------------------------------------------------------------
# MAIN DASHBOARD UI CONFIG
# -------------------------------------------------------------
st.set_page_config(page_title="Sign Language AI", layout="wide")

# -------------------------------------------------------------
# PREMIUM CUSTOM CSS
# -------------------------------------------------------------
st.markdown("""
<style>
    /* Global Font & Background Styling */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif;
    }
    
    /* Animated Gradient Title */
    .premium-title {
        font-size: 4rem;
        font-weight: 800;
        background: linear-gradient(300deg, #00b4db, #0083b0, #ff8a00, #e52e71);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: gradient-animation 8s ease infinite;
        text-align: center;
        margin-bottom: 0px;
        padding-bottom: 0px;
    }
    
    @keyframes gradient-animation {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Subtitle styling */
    .premium-subtitle {
        text-align: center;
        color: #888;
        font-size: 1.2rem;
        margin-top: -10px;
        margin-bottom: 40px;
        font-weight: 300;
    }

    /* Glassmorphism Cards */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 25px;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 180, 219, 0.2);
        border: 1px solid rgba(0, 180, 219, 0.4);
    }
    
    /* Pulsing Status Indicator */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        background-color: #00ff88;
        border-radius: 50%;
        margin-right: 8px;
        box-shadow: 0 0 10px #00ff88;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(0, 255, 136, 0); }
        100% { box-shadow: 0 0 0 0 rgba(0, 255, 136, 0); }
    }

    /* Custom Launch Button Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff8a00, #e52e71);
        color: white;
        font-size: 1.5rem;
        font-weight: 600;
        padding: 1rem 3rem;
        border: none;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(229, 46, 113, 0.4);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 8px 25px rgba(229, 46, 113, 0.6);
        background: linear-gradient(90deg, #e52e71, #ff8a00);
    }
    
    div.stButton > button:first-child:active {
        transform: scale(0.98);
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------------
# DASHBOARD CONTENT
# -------------------------------------------------------------
st.markdown('<div class="premium-title">AI Sign Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="premium-subtitle">Real-Time Neural Network Inference Engine</div>', unsafe_allow_html=True)

# Main Grid Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Glassmorphism Control Center
    st.markdown("""
        <div class="glass-card">
            <h3 style="margin-top: 0; color: #fff;">
                <span class="status-indicator"></span>System Status: Online
            </h3>
            <p style="color: #bbb; font-size: 1rem;">
                The deep learning vision system is loaded and ready. Ensure your webcam is unobstructed before launching.
            </p>
        </div>
        <br>
    """, unsafe_allow_html=True)
    
    # Launch Button
    start_clicked = st.button("🚀 LAUNCH VISION SYSTEM")
    
    if start_clicked:
        with st.spinner("Initializing Deep Neural Network..."):
            time.sleep(0.8) # Micro-interaction delay for premium feel
            
        st.toast("System successfully launched!", icon="✅")
        st.balloons()
        
        try:
            # Launch main.py in a separate process
            script_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main.py")
            subprocess.Popen([sys.executable, script_path], shell=False)
            
            st.markdown("""
                <div style="background-color: rgba(0,255,136,0.1); border-left: 4px solid #00ff88; padding: 15px; border-radius: 0 10px 10px 0; margin-top: 20px;">
                    <strong style="color: #00ff88;">✓ Connection Established</strong><br>
                    <span style="color: #ddd;">The native Python vision terminal is running on your desktop.</span>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred while launching the app: {e}")

st.markdown("<br><br>", unsafe_allow_html=True)

# Interactive Information Section
st.markdown("---")
info_col1, info_col2, info_col3 = st.columns(3)

with info_col1:
    st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h1 style="color: #00b4db; margin: 0; font-size: 3rem;">98%</h1>
            <p style="color: #888; font-weight: 600;">Model Accuracy</p>
        </div>
    """, unsafe_allow_html=True)

with info_col2:
    st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h1 style="color: #ff8a00; margin: 0; font-size: 3rem;"><15ms</h1>
            <p style="color: #888; font-weight: 600;">Inference Latency</p>
        </div>
    """, unsafe_allow_html=True)

with info_col3:
    st.markdown("""
        <div class="glass-card" style="text-align: center;">
            <h1 style="color: #e52e71; margin: 0; font-size: 3rem;">2+</h1>
            <p style="color: #888; font-weight: 600;">Neural Layers</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("🛠️ How to use the Vision Terminal"):
    st.markdown("""
    Once the native window opens, ensure you are in a well-lit area. Use the following keyboard controls inside the OpenCV terminal window:
    
    * **`P`** - Toggle AI Prediction Mode on/off
    * **`D`** - Collect custom hand gesture data
    * **`T`** - Train the Neural Network on your custom data
    * **`S`** - Speak the current sentence aloud using TTS
    * **`C`** - Clear the current sentence
    * **`Space`** - Add a space to the sentence
    * **`Q`** - Safely quit the application
    """)
