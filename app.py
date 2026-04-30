import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.title("Crack Detection - Final Year Project")

@st.cache_resource
def load_model():
    model = YOLO("best.pt")
    return model

model = load_model()

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    with st.spinner("Detecting..."):
        results = model(image)

    result_img = results[0].plot()
    st.image(result_img, caption="Detection Result")