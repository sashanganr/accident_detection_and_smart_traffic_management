# 🚗 Accident Detection with YOLOv8m

This project demonstrates a YOLOv8m-based accident detection model deployed using Streamlit.

## 🔍 Overview

- 📦 Model: YOLOv8m (`best.pt`)
- 🧠 Framework: [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- 💻 UI: Streamlit
- ☁️ Deployment: Hugging Face Spaces

## 📂 How to Use

1. Upload an accident video file (`.mp4`, `.avi`, etc.).
2. The app runs the YOLOv8m model on the video.
3. Download or view the output with accident regions detected.

## 🚀 Running Locally

```bash
git clone https://github.com/your-username/accident-detector-yolo.git
cd accident-detector-yolo
pip install -r requirements.txt
streamlit run app.py
```

## 🧾 File Structure

```
.
├── app.py             # Streamlit UI
├── best.pt            # Trained YOLOv8m model
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🛠 Requirements

- Python 3.8+
- Streamlit
- Ultralytics

## 🤗 Deployment

You can deploy this on [Hugging Face Spaces](https://huggingface.co/spaces) by uploading the files and selecting Streamlit as the SDK.

---

© 2025 YourName. All rights reserved.