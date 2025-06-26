from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import sqlite3
from User import User
# load the env

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            name TEXT,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

init_db()
load_dotenv()
llm=ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2)

