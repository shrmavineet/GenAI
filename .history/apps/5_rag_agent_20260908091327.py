from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.tools import tool
from langchain.agents import create_agent
import streamlit as st

from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import InMemorySaver

#data in st session
if "document_upload" not in st.session_state:
    st.session_state.document_upload = False

if "agent" not in st.session_state:
    st.session_state.agent = None

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

#### Upload UI

if not st.session_state.document_uploaded:
    uploaded = st.file_uploader(label="Select PDF Files", type=["pdf"],accept_multiple_files=True)

if uploaded:
    with st.spinner("Processing..."):
        path = "./doc_files/"
        for file in uploaded:
            with open(path+file.name, "wb") as t:
                t.write(file.getvalue())
            process_document(path)
            st

while True:
    query = input("User: ")
    if query.lower() == "bye":
        break
    response = agent.invoke({"messages":[{"role": "user","content":query}]},
                            {"configurable": {"thread_id":1}}
                            )
    result = response["messages"][-1].content

    print("AI: ", result)