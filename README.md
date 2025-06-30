# Gemini-Powered Chatbots Suite 🤖

Welcome to a multi-functional suite of AI-powered chatbots built using Google's **Gemini 2.5 Pro** and **Gemini 2.5 Pro Vision** models. This project showcases various real-world use cases such as:
- ATS resume evaluation
- PDF document question answering
- Image interpretation
- YouTube transcript summarization
- Nutritional analysis from food images
- General Q&A using chat history

All bots are built with **Streamlit** for easy UI access, and powered by **Google Generative AI APIs**, **LangChain**, and **FAISS**.

---

## 📁 Project Structure

```
├── main.py                         # Launchpad interface for selecting chatbots
├── requirements.txt               # Project dependencies
├── .env                           # Stores API key (keep secret)
├── Pages/
│   ├── ATS_bot.py                 # Resume matcher against job descriptions
│   ├── Image_chatbot.py          # Interprets images using Gemini Vision
│   ├── Nutritionist_Bot.py       # Estimates calories from food images
│   ├── PDF_Chatbot.py            # QA over PDF documents with semantic search
│   ├── Q&A_chatbot.py            # Conversational chatbot with chat history
│   └── Youtube_summarizer_bot.py # Summarizes YouTube videos using transcripts
└── env/                           # Python virtual environment (ignored)
```

---

## 🤖 Chatbots Included

### 1. 🧑‍💼 ATS Resume Analyzer
- Upload your resume PDF
- Paste a job description
- Get match score, missing keywords, and profile summary

### 2. 🖼️ Image Chatbot
- Upload an image and optional prompt
- Get visual analysis and descriptive feedback using Gemini Vision

### 3. 🥗 Nutritionist Bot
- Upload a food image
- Get calorie estimation per item

### 4. 📄 PDF Chatbot
- Upload multiple PDFs
- Chunk content → Generate embeddings → Ask questions
- Get contextual answers using FAISS & Gemini

### 5. 💬 Q&A Chatbot
- Ask general questions
- Maintains session chat history with streamed responses

### 6. 📺 YouTube Summarizer
- Input YouTube video URL
- Extracts transcript and generates 250-word bullet summary

---

## 🧠 Technologies Used

- **Google Generative AI API (Gemini 2.5 Pro / Vision)**
- **LangChain** for prompts, chaining, and embeddings
- **FAISS** for vector storage and semantic search
- **Streamlit** for UI development
- **PyPDF2**, **PIL**, **pdf2image** for file/image handling
- **dotenv** for secure API key management

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

### 5. Launch the Suite
```bash
streamlit run main.py
```

---

## 📌 Notes

- Ensure your **Google API key** has access to the **Gemini 1.5/2.5 API**.
- Ensure all files inside `Pages/` remain unchanged or referenced relatively.
- For PDF QA, FAISS vector store is saved locally under `faiss-index/`.
- Some bots use image-to-text or token-heavy models, so monitor quotas.

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 🙌 Acknowledgements

Huge thanks to:
- **Google Generative AI** for Gemini APIs
- **LangChain & FAISS** for backend NLP support
- **Streamlit** for rapid frontend development
- The open-source community for enabling creative tools

---

🎯 Feel free to fork, extend, or deploy these tools for your use case!
