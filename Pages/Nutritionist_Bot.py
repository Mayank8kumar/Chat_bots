############ LIM App : Large Image model ##########

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel("gemini-2.5-flash")
    response=model.generate_content([input_prompt,image[0]])
    return response.text


def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


### Initialization of the streamlit app 

st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
# input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)


submit=st.button("Tell me the total calories")

input_prompt="""
You are a certified nutritionist and food analysis expert. Given an input image containing one or more food items, your task is to:

1. Identify each food item present in the image accurately.
2. Estimate the calorie content of each item based on its visual quantity and type.
3. Calculate and display the total estimated calorie intake for the entire plate.

Please present the output in the following structured format:

- Food Item 1: XX calories  
- Food Item 2: XX calories  
- ...  
- Total Estimated Calories: XXX calories

Be concise, accurate, and professional in your response. If any items are unclear or ambiguous, mention them clearly as “Unidentified Item – Unable to estimate”.

"""

## If submit button is clicked

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.subheader("The Response is")
    st.write(response)
