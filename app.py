from dotenv import load_dotenv
load_dotenv()  ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load Gemini Pro model and get reponses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title="Farhan Q&A Bot")

st.header("Farhan GPT")

input=st.text_input("Prompt: ",key="Write prompt")
submit=st.button("Generate")

## Whwn submit is clicked

if submit:
   response=get_gemini_response(input) 
   #st.subheader("Here is the Output Read below")
   st.write(response)


