from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Google Gemini !")

query = st.chat_input("Ask anthing ?")
if query:
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    print(res.content[0]["text"])
    st.chat_message("ai").markdown(res.content[0].{text})