from dotenv import load_dotenv
load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# function to load Gemini Pro model and get reponses
model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text


# initialize our streamlit app
st.set_page_config(page_title="Farhan Q&A Bot")

st.title("Farhan GPT 🤖")
st.subheader("AI Assistant 🥷")


# initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# when submit is clicked
if prompt := st.chat_input("Your question"):  # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_gemini_response(prompt)
    st.session_state.messages.append({"role": "bot", "content": response})
    st.write(response)
