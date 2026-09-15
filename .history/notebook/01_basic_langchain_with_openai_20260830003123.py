from dotenv import load_dotenv
import os
load_dotenv()

keys = os.getenv("MISTRAL_API_KEY")
print(keys)

# from langchain_openai import ChatOpenAI
# llm = ChatOpenAI(model = "gpt-5-mini-2025-08-07")

from langchain_mistralai import ChatMistralAI
llm = ChatMistralAI(model="mistral-small-latest")

res = llm.invoke("Who is PM of India ?")

print(res.cpntent)