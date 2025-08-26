# gemini.py
import streamlit as st
import google.generativeai as genai

API_KEY = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

def gem_chat():
    

    
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    user_input = st.text_input("You:", placeholder="Type your message...")

    latest_reply = None

    if st.button("Send"):
        if user_input.strip():
           
            st.session_state["messages"].append({"role": "user", "parts": [user_input]})

           
            response = model.generate_content(st.session_state["messages"])
            latest_reply = response.text or "⚠️ No response generated."

            
            st.session_state["messages"].append({"role": "model", "parts": [latest_reply]})
            
        else:
            st.warning("⚠️ Please enter a message before sending.")

    
    for msg in st.session_state["messages"]:
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['parts'][0]}")
        else:
            st.markdown(f"**Gemini:** {msg['parts'][0]}")

    return latest_reply  # send last reply back to main.py
