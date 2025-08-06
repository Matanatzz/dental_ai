import streamlit as st
import pytesseract
from PIL import Image
from dental_ai import backend_api, backend_local

st.set_page_config(page_title="Dental AI Anamnesis Tool", layout="wide")
st.title("🦷 Dental AI Anamnesis Processor")

backend_choice = st.radio("Choose backend", ("OpenAI API", "Local LLaMA model"))

api_key = None
if backend_choice == "OpenAI API":
    api_key = st.text_input("OpenAI API Key (leave empty to use default)", type="password")

model_path = None
if backend_choice == "Local LLaMA model":
    model_path = st.text_input("Path to local LLaMA model", value="models/llama-2-7b.Q4_K_M.gguf")

st.subheader("Anamnesis Input")

# Keep anamnesis text in session so it updates automatically
if "anamnesis_text" not in st.session_state:
    st.session_state.anamnesis_text = ""

# Define clear function
def clear_text():
    st.session_state.anamnesis_text = ""

# Camera capture
st.write("📷 Or capture from camera:")
img = st.camera_input("Take a photo of the anamnesis")

if img is not None:
    # OCR extraction
    image = Image.open(img)
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
            if backend_choice == "OpenAI API":
                backend = backend_api.APIBackend(api_key=api_key if api_key else None)
            else:
                backend = backend_local.LocalBackend(model_path)

            output = backend.process(st.session_state.anamnesis_text)
            st.subheader("Processed Output")
            st.text_area("Output", output, height=400)
