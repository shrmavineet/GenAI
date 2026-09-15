'''
    Requirements for Make a ChatBot
    LLM Model
    TOOL for Google Search
    Agent
'''

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

from langchain_community.utilities import GoogleSerperAPIWrapper
search = GoogleSerperAPIWrapper