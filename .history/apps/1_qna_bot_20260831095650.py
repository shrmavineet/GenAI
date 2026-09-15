from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")
que = "Who is PM of India ?"

while True:
    query = input()
result = llm.invoke(que)
print(result.content)