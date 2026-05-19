import streamlit as st
from ultralytics import YOLO
from PIL import Image

# PAGE CONFIG
st.set_page_config(
    page_title="AI Crack Detection",
    page_icon="🛣️",
    layout="wide"
)

# CUSTOM CSS
st.markdown("""
<style>

.stApp {
    background-color: #0E1117;
}

h1 {
    color: #00BFA6;
    text-align: center;
    font-size: 50px;
}

h3 {
    color: white;
}

.stFileUploader {
    border: 2px dashed #00BFA6;
    padding: 20px;
    border-radius: 15px;
    background-color: #262730;
}

.stButton>button {
    background-color: #00BFA6;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #262730;
    color: white;
    text-align: center;
    font-size: 24px;
}

</style>
""", unsafe_allow_html=True)

# TITLE
st.title("🛣️ AI-Based Road Crack Detection System")

st.markdown("""
<div class="result-box">
Final Year Project using YOLOv8 and Streamlit
</div>
""", unsafe_allow_html=True)

st.write("")

# SIDEBAR
st.sidebar.title("Project Information")
st.sidebar.info("""
This AI model detects:
- Cracks
- Potholes
- Road Damage

Developed using:
- YOLOv8
- Streamlit
- Python
""")

# LOAD MODEL
@st.cache_resource
def load_model():
    model = YOLO("best.pt")
    return model

model = load_model()

# FILE UPLOADER
uploaded_file = st.file_uploader(
    "Upload Road Image",
    type=["jpg", "png", "jpeg"]
)

# PROCESS IMAGE
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with st.spinner("Analyzing pavement condition..."):

        results = model(image)

        result_img = results[0].plot()

    with col2:
        st.subheader("Detection Result")
        st.image(result_img, use_container_width=True)

    st.success("Detection Completed Successfully")
