from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

form stream
st.title("🤖 AskBuddy - AI QnA Bot")