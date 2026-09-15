from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Groq !")

if "message" not in st.session_state:
    st.session_state.message = []

query =st.chat_input("Ask anything 😒?")

if query:
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.chat_message("ai").markdown(res.container)