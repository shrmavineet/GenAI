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

if st.session_state.memory:
    
memory = MemorySaver()
import streamlit as st

agent = create_agent(
    model = llm,
    tools = [search.run],
    checkpointer=memory,
    system_prompt="You are the best ai agent and you can search anything on google"
)


#### Building Web Interface
st.subheader("Quick Answer - Answer at the speed of thought")

query = st.chat_input("Ask Anything ?")


if query:
    st.chat_message("user").markdown(query)

    response = agent.invoke(
        {"messages":[{"role":"user", "content":query}]},
        {"configurable": {"thread_id": 1 }}
    )

    answer = response["messages"][-1].content
    st.chat_message("ai").markdown(answer)
