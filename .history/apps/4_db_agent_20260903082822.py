from dotenv import load_dotenv
load_dotenv()

## db, llm, tools, create_agent, system_prompt

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit

db = SQLDatabase.from_uri("sqlite:///my_task.db")
db.run("""
    CREATE TABLE IF NOT EXIST
""")

print("Created Successfully")