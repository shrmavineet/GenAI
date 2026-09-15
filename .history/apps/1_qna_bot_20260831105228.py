from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit

llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.title("🤖 AskBuddy - AI QnA Bot")
st.mar