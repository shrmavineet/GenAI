from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores import InMemoryVectorStore
from langchain.tools import tool
from langchain.agents import create_agent

#load the documents
loader = PyPDFLoader("../data/Vineet.pdf")
loaded_data = loader.load()

##Split the data into chunks

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
splitted_data = spli