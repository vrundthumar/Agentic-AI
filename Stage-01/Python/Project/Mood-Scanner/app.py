import streamlit as st
import cv2
import numpy as np
import pandas as pd
from datetime import datetime
from utils.emotion import detect_emotion

st.set_page_config(
    page_title="Mood Scanner AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 AI Mood Scanner")
st.write("Detect human emotion using facial expressions")

option = st.radio(
    "Choose Input Method",
    ["Upload Image", "Use Webcam"]
)

def save_mood(mood):
    data = {
        "Time": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        "Mood": [mood]
    }
    df = pd.DataFrame(data)

    try:
        old = pd.read_csv("data/mood_log.csv")
        df = pd.concat([old, df], ignore_index=True)
    except:
        pass

    df.to_csv("data/mood_log.csv", index=False)

# IMAGE UPLOAD
if option == "Upload Image":
    uploaded = st.file_uploader("Upload a face image", type=["jpg", "png", "jpeg"])

    if uploaded:
        image = np.array(bytearray(uploaded.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        st.image(image, channels="BGR", caption="Uploaded Image")

        if st.button("Scan Mood"):
            mood = detect_emotion(image)
            st.success(f"Detected Mood: **{mood.upper()}**")
            save_mood(mood)

# WEBCAM
if option == "Use Webcam":
    picture = st.camera_input("Take a photo")

    if picture:
        image = np.array(bytearray(picture.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        st.image(image, channels="BGR")

        mood = detect_emotion(image)
        st.success(f"Detected Mood: **{mood.upper()}**")
        save_mood(mood)
