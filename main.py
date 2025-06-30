import streamlit as st

st.set_page_config(page_title="Gemini Chatbot Suite", page_icon="🤖")

st.title("🤖 Gemini Powered Chatbots Suite")
st.subheader("Select a bot to launch")
st.markdown("---")

bot_options = {
    "🧑‍💼 ATS Resume Analyzer": "Pages/ATS_bot.py",
    "🖼️ Image Chatbot": "Pages/Image_chatbot.py",
    "🥗 Nutritionist Bot": "Pages/Nutritionist_Bot.py",
    "📄 PDF Chatbot": "Pages/PDF_Chatbot.py",
    "💬 Q&A Chatbot": "Pages/Q&A_chatbot.py",
    "📺 YouTube Summarizer": "Pages/Youtube_summarizer_bot.py"
}

selected_bot = st.selectbox("Choose a Bot", list(bot_options.keys()))

if st.button("🚀 Launch Bot"):
    target_page = bot_options[selected_bot]
    st.switch_page(target_page)


# if option != "-- Select --":
#     st.markdown("---")
#     if st.button("🚀 Launch Selected Bot"):
#         if option == "🔍 ATS Resume Analyzer":
#             st.switch_page("ATS_bot.py")
#         elif option == "🖼️ Image Analysis Bot":
#             st.switch_page("Image_chatbot.py")
#         elif option == "🥗 Nutrition Estimator Bot":
#             st.switch_page("Nutritionist_Bot.py")
#         elif option == "📄 PDF QA Chatbot":
#             st.switch_page("PDF_Chatbot.py")
#         elif option == "💬 Q&A Chatbot":
#             st.switch_page("Q&A_chatbot.py")
#         elif option == "📺 YouTube Summarizer Bot":
#             st.switch_page("Youtube_summarizer_bot.py")