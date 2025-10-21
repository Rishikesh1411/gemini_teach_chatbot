import streamlit as st
import google.generativeai as genai

st.markdown("# Simple Chat Bot page ?")
st.sidebar.markdown("# Chat Bot page ?")

# Replace the google_api_key here
GOOGLE_API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
genai.configure(api_key=GOOGLE_API_KEY)

# Dynamically select a supported model
try:
    available_models = [m.name for m in genai.list_models()]
    geminiModel = None
    for m in available_models:
        if "gemini-2.5" in m and "flash" in m:
            geminiModel = genai.GenerativeModel(m)
            break
    if not geminiModel:
        for m in available_models:
            if "gemini" in m:
                geminiModel = genai.GenerativeModel(m)
                break
    if not geminiModel:
        st.error("No suitable Gemini model found. Check your API key or available models.")
        st.stop()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

chat = geminiModel.start_chat(history=[])

def get_gemini_response(query):
    instantResponse = chat.send_message(query, stream=True)
    return instantResponse

st.header("A simple Chat Bot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

inputText = st.text_input("Input: ", key="input")
submitButton = st.button("Get Instant answers")

if submitButton and inputText:
    try:
        output = get_gemini_response(inputText)
        st.session_state['chat_history'].append(("You", inputText))
        st.subheader("The Response is")
        for outputChunk in output:
            st.write(outputChunk.text)
            st.session_state['chat_history'].append(("Bot", outputChunk.text))
    except Exception as e:
        st.error(f"Error getting response: {e}")

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:

    st.write(f"{role}: {text}")
