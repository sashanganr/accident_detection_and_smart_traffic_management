import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile
import os

st.title("🚗 Accident Detection with YOLOv8")

# Load YOLOv8 model
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi", "mov"])

if uploaded_file:
    st.video(uploaded_file)  # Show original

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_input:
        temp_input.write(uploaded_file.read())
        input_path = temp_input.name

    output_path = "output.mp4"
    cap = cv2.VideoCapture(input_path)

    width  = int(cap.get(3))
    height = int(cap.get(4))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    st.write("🔍 Processing video...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model.predict(frame, conf=0.4)
        annotated_frame = results[0].plot()
        out.write(annotated_frame)

    cap.release()
    out.release()

    st.success("✅ Video Processed!")
    st.video(output_path)  # Show processed video

    with open(output_path, "rb") as f:
        btn = st.download_button(
            label="📥 Download Processed Video",
            data=f,
            file_name="accident_output.mp4",
            mime="video/mp4"
        )
