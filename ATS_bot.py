import streamlit as st
import os
import io
import base64
import pdf2image
import PyPDF2
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#             FIRST METHOD TO CREATE THE BOT
'''
This method converts the pdf to image and then model uses that image provides the desired response. 
'''

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-2.5-flash')
    response=model.generate_content([input,pdf_content[0],prompt])
    return response.text



def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the PDF to image
        images=pdf2image.convert_from_bytes(uploaded_file.read())

        first_page=images[0]

        # Convert to bytes and take that in form of JPG
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")
    

### Streamlit APP creation 

st.set_page_config(page_title="ATS Resume analyzer")
st.header("Application Tracting System")
input_text=st.text_area("Job Description:",key="input")
uploaded_file=st.file_uploader("Upload you resume(PDF)..",type=["pdf"])

if uploaded_file is not None:
    st.write("PDF file successfully uploaded")

submit1=st.button("Tell me about the Resume")
# submit2=st.button("How can i Improve my skills")
submit3=st.button("What are the things which are missing")
submit4=st.button("Percentage Matched")

input_prompt1 = """
 You are an experienced HR with tech experience in the field of any one job role from Data Science or Full stack or web development or Big Data engineering or Devops or Data analyst, your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt3 = """
You are a technical hiring expert and career strategist with strong experience in evaluating profiles for roles like Data Scientist, Full Stack Developer, Web Developer, Big Data Engineer, DevOps Engineer, and Data Analyst.

Your task is to deeply analyze the candidate’s resume against the given job description and list out all the key elements that are missing in the resume which are required by the role.

This includes missing skills, tools, technologies, certifications, experience levels, project exposure, or domain knowledge. Provide a structured output highlighting:
1. Missing Technical Skills or Tools
2. Missing Soft Skills or Domain Experience
3. Missing Certifications or Educational Background
4. Suggestions to improve or tailor the resume for better alignment with the role
"""

input_prompt4 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of Data Science, Full stack, web development, Big Data engineering, Devops, Data analyst and deep ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit3:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")

elif submit4:
    if uploaded_file is not None:
        pdf_content=input_pdf_setup(uploaded_file)
        response=get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")



####################################################################################################################################################################
####################################################################################################################################################################
####################################################################################################################################################################

#                   ANOTHER WAY OF CREATING THE BOT 
'''
This method converts the pdf to text and then using that text model provides the response 
'''

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)