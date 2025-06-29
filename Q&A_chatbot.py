from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro model and get response

model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

## Funtion that stores the responses as well

def get_gemini_response(question):
    '''
    This function returns the response of the question asked
    '''
    response=chat.send_message(question,stream=True)
    return response

# #### Another way of sending the response 

# def get_gemini_response(question):
#     '''
#     This function returns the response of the question asked
#     '''
#     response=model.generate_content(question)
#     return response.text               


### Initializing our streamlit app

st.set_page_config(page_title="Q&A Chatbot")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input=st.text_input("Input:",key="input")
submit=st.button("Ask the question")

### Way of sending the response ( without chat history )

# if submit:
#     response=get_gemini_response(input)
#     st.subheader("The Response is")
#     st.write(response)


### Another way of getting the response ( with chat history )
if submit and input:
    response=get_gemini_response(input)
    
    # --- > Now add user query and response in the history
    st.session_state['chat_history'].append("You",input)
    for chunk in response:    # As stream is true that's why this for loop. 
        st.write(chunk.text)
        st.session_state['chat_history'].append("Bot",chunk.text)
        
st.subheader("The Chat history is ")


for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")