from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.tools import tool
from langchain.agents import create_agent

from langchain_groq import ChatGroq

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
def retrieve_