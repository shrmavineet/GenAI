from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

from langchain_community.utilities import GoogleSearc
llm = ChatGroq(model="openai/gpt-oss-20b")

