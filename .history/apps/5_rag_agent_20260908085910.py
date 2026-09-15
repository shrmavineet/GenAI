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
if "document"

#load the documents
loader = PyPDFLoader("../data/Vineet.pdf")
loaded_data = loader.load()

##Split the data into chunks

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
splitted_data = splitter.split_documents(loaded_data)

##embeddings and Vector DB

embedding = MistralAIEmbeddings(model="mistral-embed-2312")

vector_data = InMemoryVectorStore.from_documents(
    documents=splitted_data,
    embedding=embedding
)

## create a agent - tool | llm | system_prompt

llm = ChatGroq(model="openai/gpt-oss-20b")

@tool
def retrieve_context(query:str):
    """
        Retrieve document relevant to a query from the knowledge base
    """
    context = ""

    for doc in vector_data.similarity_search(query=query,k=4):
        context = context + doc.page_content +"\n"
    return context

system_prompt = """You are a helpful assistant that answers questions using retrieved context. 
        My knowledge base consists of the details from the uploaded document. 
        ALWAYS use the `retrieve_context` tool for questions requiring external knowledge."""

memory =InMemorySaver()

agent = create_agent(
    model=llm,
    tools=[retrieve_context],
    system_prompt=system_prompt,
    checkpointer=memory
)

while True:
    query = input("User: ")
    if query.lower() == "bye":
        break
    response = agent.invoke({"messages":[{"role": "user","content":query}]},
                            {"configurable": {"thread_id":1}}
                            )
    result = response["messages"][-1].content

    print("AI: ", result)