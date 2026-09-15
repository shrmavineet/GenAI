from dotenv import load_dotenv
load_dotenv()
import streamlit as st

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain ")