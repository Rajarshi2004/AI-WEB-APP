import streamlit as st
from package.summarizer import *
from package.gemini import *   
from package.code_ass import *
from package.file_uploader import *
from package.pptmaker import *
import os
os.environ["STREAMLIT_DISABLE_WATCHDOG_WARNINGS"] = "true"
os.environ["WATCHDOG_DISABLE_FILE_WATCHING"] = "true"


st.title("🔥 AI on the Rocks 🔥")
st.subheader("Chill Vibes, Powerful AI 🚀")


mode = st.sidebar.selectbox(
    "Choose Mode", 
    ["Chatbot", "Summarizer", "Code Assistant", "File Assistant", "PPT GENERATOR"]
)
st.sidebar.markdown("---")
st.sidebar.markdown("## ℹ️ About this app:")
st.sidebar.markdown("""
This **AI Web App** brings multiple tools together:  
- 🤖 Gemini Chatbot  
- 📝 Text Summarizer  
- 💻 Code Assistant  
- 📂 File Q&A (PDF)  
- 📊 PPT Generator  

> Built with **Streamlit** and powered by **Gemini LLM**  

👨‍💻 Made by **Rajarshi Paul**  
[🔗 LinkedIn](https://www.linkedin.com/in/rajarshi-paul-a0710628b/)
""")
st.subheader("Mode selected:")
if mode == "Summarizer":
    st.header("Text Summarizer")
    st.write("Provide the text sample that you wish to organize 👇")
    transcript = st.text_area("Paste the text here:")
    if st.button("GENERATE"):
        ou = summarize_text(transcript)
        st.write(ou)

elif mode == "Chatbot":
    st.header("Chatbot")
    output = gem_chat()
    st.write(output)

elif mode == "Code Assistant":
    st.header("CODE ASSISTANT")
    st.write("This tool helps you debug and correct code 🛠️")
    c = st.text_area("Enter your piece of code")
    if st.button("ENTER"):
        o = code_assistant(c)
        st.write(o)

elif mode == "File Assistant":
    st.header("FILE Q&A")
    st.write("This tool helps you to summarize the contents of the file and create a QnA session")
    uploaded_file = st.file_uploader("Upload a file (PDF only)", type=["pdf"])
    if uploaded_file:
        tex = file_upload(uploaded_file)
        out = ask_gemini(tex)
        st.write(out)

elif mode == "PPT GENERATOR":
    st.write("⚡ Generate downloadable PPTX files with just a few prompts!")
    call()
