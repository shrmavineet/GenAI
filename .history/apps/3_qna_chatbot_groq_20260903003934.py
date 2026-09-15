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
llm = ChatGroq(model="openai/gpt-oss-20b", str)

from langchain_community.utilities import GoogleSerperAPIWrapper
search = GoogleSerperAPIWrapper()

from langchain.agents import create_agent

from langgraph.checkpoint.memory import MemorySaver

import streamlit as st

if "memory" not in st.session_state:
    st.session_state.memory = MemorySaver()
    st.session_state.history = []



agent = create_agent(
    model = llm,
    tools = [search.run],
    checkpointer=st.session_state.memory,
    system_prompt="You are the best ai agent and you can search anything on google"
)


#### Building Web Interface
st.subheader("Quick Answer - Answer at the speed of thought")

query = st.chat_input("Ask Anything ?")


for message in st.session_state.history:
    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)

if query:
    st.session_state.history.append({"role":"user", "content":query})
    st.chat_message("user").markdown(query)

    response = agent.invoke(
        {"messages":[{"role":"user", "content":query}]},
        {"configurable": {"thread_id": 1 }}
    )

    answer = response["messages"][-1].content
    st.session_state.history.append({"role":"ai", "content": answer})
    st.chat_message("ai").markdown(answer)
