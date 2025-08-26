import google.generativeai as genai
import streamlit as st
import PyPDF2
API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def file_upload(file) :
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
def ask_gemini(file_text):
    prompt = f"""
    summarize the text and create question and answer session{file_text}
    """
    response = model.generate_content(prompt)

    if response.text:
        return response.text
    else:
        return "⚠️ Gemini returned no answer."
