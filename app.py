import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Crack Detection System",
    page_icon="🏗️",
    layout="centered"
)

# ---------------- Load Model (cached) ----------------
@st.cache_resource
def load_model():
    return YOLO("best.pt")

model = load_model()

# ---------------- UI Styling ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F5F7FA;
}

/* Title */
h1 {
    color: #1F4E79;
    text-align: center;
    font-size: 42px;
    font-weight: 700;
}

/* Upload Box */
.stFileUploader {
    border: 2px dashed #1F77B4;
    padding: 20px;
    border-radius: 12px;
    background-color: white;
}

/* Button */
.stButton>button {
    background-color: #1F77B4;
    color: white;
    border-radius: 8px;
    height: 3em;
    width: 100%;
    font-size: 16px;
    border: none;
}

/* Result Box */
.result-box {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    text-align: center;
    font-size: 20px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #DCE6F2;
}
</style>
""", unsafe_allow_html=True)

# ---------------- App Title ----------------
st.title("Crack Detection System 🏗️")

st.write("Upload an image of a structure and detect cracks using AI.")

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# ---------------- Prediction ----------------
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Convert image for model
    img_array = np.array(image)

    # Run prediction
    results = model.predict(img_array)

    # Display result
    st.markdown("### Result")

    # Simple output logic (you can improve based on your model)
    if len(results[0].boxes) > 0:
        st.success("Crack Detected ⚠️")
    else:
        st.success("No Crack Detected ✅")
