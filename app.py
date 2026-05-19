st.markdown("""
<style>

.stApp {
    background-color: #F5F7FA;
}

/* Main Title */
h1 {
    color: #1F4E79;
    text-align: center;
    font-size: 48px;
    font-weight: bold;
}

/* Subheadings */
h3 {
    color: #1E1E1E;
}

/* Upload Box */
.stFileUploader {
    border: 2px dashed #1F77B4;
    padding: 20px;
    border-radius: 15px;
    background-color: white;
}

/* Buttons */
.stButton>button {
    background-color: #1F77B4;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    border: none;
}

/* Result Box */
.result-box {
    padding: 20px;
    border-radius: 15px;
    background-color: white;
    color: #1E1E1E;
    text-align: center;
    font-size: 22px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #DCE6F2;
}

</style>
""", unsafe_allow_html=True)
