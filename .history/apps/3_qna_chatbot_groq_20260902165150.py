'''
    Requirements for Make a ChatBot
    LLM Model
    TOOL for Google Search
    Agent
    Memory
    Streaming
    Web Interface
'''

from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
llm = ChatGroq(model="openai/gpt-oss-20b")

from langchain_community.utilities import GoogleSerperAPIWrapper
search = GoogleSerperAPIWrapper()

from langchain.agents import create_agent

agent = create_agent(
    model = llm,
    tool = [search.run],
    system_prompt="You are the best agent and you can search anything on google"
)