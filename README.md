# Gemini-Powered Chatbots Suite 🤖

Welcome to a collection of AI-driven chatbot applications built using Google's **Gemini Pro** and **Gemini Pro Vision** models. This repository showcases various use cases such as image-based understanding, document question-answering (QA), and conversational chat interfaces — all powered by the **Google Generative AI API**.

## 📁 Project Structure

```
├── Image_chatbot.py        # Interacts with images and responds to user queries using Gemini Vision
├── pdf_Chatbot.py          # Extracts and processes PDF documents, enables semantic search QA
├── Q&A_chatbot.py          # Simple LLM-based QA interface using chat history
├── requirements.txt        # Python dependencies
├── .env                    # Environment file storing your Gemini API key
└── env/                    # Virtual environment (excluded from Git)
```

## 🚀 Chatbots Included

### 1. 🖼️ Image Chatbot (Gemini Pro Vision)

* Upload an image and optionally provide a prompt.
* Get detailed descriptions, insights, or analysis using Gemini's vision model.

### 2. 📄 PDF Chatbot (Gemini Pro + FAISS)

* Upload multiple PDFs.
* Extract text → Chunk into embeddings → Store with FAISS.
* Ask contextual questions and get precise answers with Gemini.

### 3. 💬 Q\&A Chatbot (Gemini Pro)

* Engage in general text-based conversations.
* Maintains chat history using session state.
* Streams answers in real-time.

---

## 🧠 Technologies Used

* **Google Generative AI API (Gemini Pro, Gemini Pro Vision)**
* **LangChain** for vector search & prompting
* **FAISS** for vector store & similarity search
* **Streamlit** for front-end UI
* **PyPDF2**, **PIL** for file and image handling
* **dotenv** for environment variable management

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/gemini-chatbot-suite.git
cd gemini-chatbot-suite
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your `.env` file

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 5. Run an app

```bash
streamlit run Image_chatbot.py
# or
streamlit run pdf_Chatbot.py
# or
streamlit run Q&A_chatbot.py
```

---

## 📌 Notes

* Ensure your **Google API key** has access to the **Gemini API**.
* For PDF QA, FAISS index is stored locally (`faiss-index/`).
* Use `stream=True` for better response streaming with chat.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

Thanks to Google Generative AI, LangChain, and the open-source community for enabling rapid prototyping of AI-powered applications.

---

Feel free to fork, extend, and build on top of this suite 🚀
