from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

model = ChatGroq(model="openai/gpt-oss-20b")

from langchain_community.utilities import GoogleSerperAPIWrapper

search = GoogleSerperAPIWrapper()

from langgraph.checkpoint.memory import MemorySaver
memory = MemorySaver()

from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[search.run],
    system_prompt="You are agent which search anything on google"
)



while True:
    query = input("User: ")
    if query.lower == ["exit","bye"]:
        print("Exiting...")
        break

    response = agent.invoke({"messages":[{"role":"user","content": query}]})
    print("AI: ",response["messages"][-1].content)
