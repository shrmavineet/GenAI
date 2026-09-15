from dotenv import load_dotenv
import os
load_dotenv()

keys = os.getenv("OPENAI_API_KEY")
print(keys)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model = "gpt-5-mini-2025-08-07")
print(llm)

llm