import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("Camera Test")

webrtc_streamer(
    key="camera",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration={
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    },
    media_stream_constraints={
        "video": True,
        "audio": False,
    },
)