from dotenv import load_dotenv
load_dotenv()

## db, llm, tools, create_agent, system_prompt

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
import streamlit as st

db = SQLDatabase.from_uri("sqlite:///my_task.db")
db.run("""
    CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT CHECK (status IN ('pending', 'progress', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

print("Created Successfully")

llm = ChatGroq(model="openai/gpt-oss-20b")

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools= toolkit.get_tools()

system_prompt = """
You are a task management assistant that interacts with a SQL database containing a 'tasks' table.

TASK RULES:
1. Limit SELECT queries to 10 results max with ORDER BY created_at DESC
2. After CREATE/UPDATE/DELETE, confirm with SELECT query
3. If the user requests a list of tasks, present the output in a structured table formate to ensure.

CRUD OPERATIONS:
CREATE: INSERT INTO task(title, description, status)
READ: SELECT * FROM task WHERE ... LIMIT 10
UPDATE: UPDATE tasks SET status=? WHERE id=? OR title=?
DELETE: DELETE FROM task WHERE id=? OR title=?

Table schema: id,title, description, status(pending/progress/completed), created_at.
"""

@st.cache_resource
def get_agent():
    agent = create_agent(
        model = llm,
        tools = tools,
        checkpointer=InMemorySaver(),
        system_prompt=system_prompt
    )
    return agent

st.subheader("TaskBot - Manages your todos")

prompt = st.chat_input("Ask me to manage your task")
while True:
    query = input("User: ")

    response = agent.invoke(
        {"messages":[{"role":"user","content":query}]},
        {"configurable":{"thread_id": 1}}
    )

    result = response["messages"][-1].content
    print("AI: ", result)