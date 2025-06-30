from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro Vision model.

model=genai.GenerativeModel("gemini-2.5-flash")
# chat=model.start_chat(history=[])


def get_gemini_response(input,image):
    '''
    This function returns the response 
    '''
    if input !='':
        response=model.generate_content(input,image)
    else:
        response=model.generate_content(image)

    return response.text


## Initialize out streamlit app

st.set_page_config(page_title="Gemini Image Creation")

st.header("Gemini Application")
input=st.text_input("Input Prompt:",key="input")

uploaded_file=st.file_uploader("Choose an image...",type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Tell me about the image")


# If submit is clicked 
if submit:
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)