from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function for extracting text data from all pdfs. 
def get_pdf_texts(pdf_docs):
    '''
    Extracts all the text from the pdf from each page. 
    '''
    text=''
    for pdf in pdf_docs:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader:
            text+=page.extract_text()
    
    return text


## Function to create the chunks out of the text
def get_text_chunks(text):
    '''
    Function creates the chunks out of the texts
    '''
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,chunk_overlap=1000)
    chunks=text_splitter.split_text(text)
    return chunks


## Function creates the embeddings and stores them
def get_vector_store(text_chunks):
    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store=FAISS.from_texts(text_chunks,embeddings=embeddings)
    vector_store.save_local("faiss-index")


## Function holds the model and prompt
def get_conversational_chain():
    prompt_template = """
    You are a highly knowledgeable assistant. Use the provided context to answer the question with as much detail and accuracy as possible.

Instructions:
- Base your answer **strictly on the context** provided.
- If the answer is **not found** in the context, respond with: **"The answer is not available in the context."**
- Do **not infer, guess, or fabricate** information outside the given content.

---

Context:
\n{context}\n

Question:
\n{question}\n

Answer:
    """
    model=ChatGoogleGenerativeAI(model="gemini=pro",temprature=0.3)

    prompt=PromptTemplate(template=prompt_template, input_variables=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain

## Function which takes the input of the user
def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)   # loading vectors from the local
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])


def main():
    st.set_page_config("Chat with Multiple PDF")
    st.header("Chat with Multiple PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_texts(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()