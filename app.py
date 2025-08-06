import streamlit as st
import pytesseract
from PIL import Image
from dental_ai import backend_api

st.set_page_config(page_title="Dental AI Anamnesis Tool", layout="wide")
st.title("🦷 Dental AI Anamnesis Processor")

# API key input
api_key = st.text_input("OpenAI API Key (leave empty to use default)", type="password")

st.subheader("Anamnesis Input")

# Keep anamnesis text in session so it updates automatically
if "anamnesis_text" not in st.session_state:
    st.session_state.anamnesis_text = ""

# Define clear function
def clear_text():
    st.session_state.anamnesis_text = ""

# High-resolution camera capture / file upload
st.write("📷 Capture or upload a photo of the anamnesis:")
uploaded_img = st.file_uploader(
    "Take a photo or choose from gallery",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=False
)

if uploaded_img:
    # OCR extraction
    image = Image.open(uploaded_img)
    extracted_text = pytesseract.image_to_string(image, lang="eng+heb")
    st.success("Text extracted from image:")
    st.write(extracted_text)

    # Auto-fill the text area with extracted text
    st.session_state.anamnesis_text = extracted_text.strip()

# Manual text entry (linked to session state)
st.text_area("Enter anamnesis text", height=300, key="anamnesis_text")

# Buttons
col1, col2 = st.columns([1, 1])
with col1:
    st.button("Clear Text", on_click=clear_text)
with col2:
    if st.button("Process"):
        if not st.session_state.anamnesis_text.strip():
            st.error("Please enter or capture anamnesis text first.")
        else:
            st.info("Processing...")
            backend = backend_api.APIBackend(api_key=api_key if api_key else None)
            output = backend.process(st.session_state.anamnesis_text)
            st.subheader("Processed Output")
            st.text_area("Output", output, height=400)
