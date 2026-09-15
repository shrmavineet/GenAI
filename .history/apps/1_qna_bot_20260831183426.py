from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st

llm = ChatGoogleGenerativeAI(model = "gemini-3.6-flash")

st.title("🤖 AskBuddy - AI QnA Bot")
st.markdown("My QnA Bot with LangChain and Google Gemini !")

if "messages" in st.session_state.messages:
    st.session_state.messages = []

for messages in st.session_state:
    role = messages["role"]
    content = messages["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anthing ?")
if query:
    st.session_state.messages.append({"role": "user", "content": "query"})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    st.session_state.messages.append({
        
    })
    st.chat_message("ai").markdown(res.content[0]["text"])