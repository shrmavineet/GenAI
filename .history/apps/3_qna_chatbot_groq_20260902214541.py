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

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()
import streamlit as st

agent = create_agent(
    model = llm,
    tools = [search.run],
    checkpointer=memory,
    system_prompt="You are the best ai agent and you can search anything on google"
)


#### Building Web Interface
st.subheader("Quick Answer - ")

response = agent.invoke(
    {"messages":[{"role":"user", "content":"Who is the Pm of India ?"}]},
    {"configurable": {"thread_id": 1 }}
)
print(response["messages"][-1].content)
