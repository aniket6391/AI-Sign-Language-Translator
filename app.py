import streamlit as st
import cv2
import av
import numpy as np

from streamlit_webrtc import (
    webrtc_streamer,
    VideoProcessorBase,
    WebRtcMode,
)

from prediction.predictor import Predictor
from utils.mediapipe_utils import HandDetector
from utils.preprocessing import Preprocessor


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="AI Sign Language Translator",
    page_icon="🤟",
    layout="wide",
)

# ==========================================================
# TITLE
# ==========================================================

st.title("🤟 AI Sign Language Translator")

st.markdown(
    """
    Real-Time Sign Language Recognition using **MediaPipe + TensorFlow + CNN**
    """
)

st.markdown("---")


# ==========================================================
# LOAD MODEL
# ==========================================================

@st.cache_resource
def load_predictor():
    return Predictor()


predictor = load_predictor()

print("Model Ready:", predictor.is_ready())


# ==========================================================
# LOAD MEDIAPIPE
# ==========================================================

detector = HandDetector(max_num_hands=1)

preprocessor = Preprocessor()


# ==========================================================
# SESSION STATE
# ==========================================================

if "sentence" not in st.session_state:
    st.session_state.sentence = ""

if "prediction" not in st.session_state:
    st.session_state.prediction = ""

if "confidence" not in st.session_state:
    st.session_state.confidence = 0.0
    # ==========================================================
# VIDEO PROCESSOR
# ==========================================================

class SignProcessor(VideoProcessorBase):

    def __init__(self):
        self.current_label = "-"
        self.current_confidence = 0.0

    def recv(self, frame):

        try:
            # Browser frame -> OpenCV image
            image = frame.to_ndarray(format="bgr24")

            # Mirror image
            image = cv2.flip(image, 1)

            # Convert BGR -> RGB
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Detect hand
            processed_image, results = detector.process_frame(rgb)

            print("Frame received")

            # Convert RGB -> BGR for display
            display_image = cv2.cvtColor(
                processed_image,
                cv2.COLOR_RGB2BGR
            )

            # Reset prediction
            self.current_label = "-"
            self.current_confidence = 0.0

            # If hand detected
            if results.multi_hand_landmarks:

                print("Hand detected")

                hand_landmarks = results.multi_hand_landmarks[0]

                # Crop hand
                cropped_hand = preprocessor.crop_and_resize(
                    rgb,
                    hand_landmarks
                )

                if cropped_hand is not None:

                    print("Crop successful")

                    cropped_hand = cropped_hand.astype(np.float32)
                    cropped_hand /= 255.0

                    if predictor.is_ready():

                        print("Model loaded")

                        label, confidence = predictor.predict(
                            cropped_hand
                        )

                        print(
                            "Prediction:",
                            label,
                            confidence
                        )

                        self.current_label = label
                        self.current_confidence = confidence

                        # Draw prediction
                        cv2.putText(
                            display_image,
                            f"Letter : {label}",
                            (20, 40),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 255, 0),
                            2
                        )

                        cv2.putText(
                            display_image,
                            f"Confidence : {confidence*100:.2f}%",
                            (20, 80),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (255, 255, 0),
                            2
                        )

            return av.VideoFrame.from_ndarray(
                display_image,
                format="bgr24"
            )

        except Exception as e:

            print("ERROR:", e)

            return av.VideoFrame.from_ndarray(
                image,
                format="bgr24"
            )
        # ==========================================================
# START WEBCAM
# ==========================================================

st.markdown("---")
st.subheader("📷 Live Camera")

ctx = webrtc_streamer(
    key="sign-language-camera",
    mode=WebRtcMode.SENDRECV,
    video_processor_factory=SignProcessor,
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
    async_processing=True,
)

st.markdown("---")


# ==========================================================
# DASHBOARD
# ==========================================================

col1, col2 = st.columns([3, 1])

with col2:

    st.subheader("📊 Prediction")

    if ctx.video_processor is not None:

        st.metric(
            "Current Letter",
            ctx.video_processor.current_label
        )

        st.metric(
            "Confidence",
            f"{ctx.video_processor.current_confidence*100:.2f}%"
        )

    else:

        st.metric("Current Letter", "-")
        st.metric("Confidence", "0.00%")


with col1:

    st.subheader("📝 Sentence")

    sentence_box = st.empty()

    sentence_box.text_area(
        "Detected Text",
        value=st.session_state.sentence,
        height=150,
        disabled=True
    )