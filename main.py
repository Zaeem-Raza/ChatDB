import os
import sqlite3
import service
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from User import User
from langchain.agents import create_react_agent,AgentExecutor
from langchain import hub
from pydantic import BaseModel, Field
from langchain.agents import create_openai_functions_agent
load_dotenv()
llm = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo")

prompt = hub.pull("hwchase17/openai-functions-agent")

class CreateUserInput(BaseModel):
    name: str = Field(..., description="The user's full name")
    age: int = Field(..., description="The user's age")

@tool(args_schema=CreateUserInput)
def create_user(name: str, age: int) -> str:
    """
    Create a new user with the given name and age.
    """
    user = User(name=name, age=age)
    return service.insert_user(user)


@tool
def get_all_users() -> str:
    """
    Retrieve all users from the database.
    """
    users = service.get_all_users()
    if not users:
        return "No users found in the database."
    return "\n".join([f"{user.name}, age {user.age}" for user in users])
agent = create_openai_functions_agent(
    llm=llm,
    tools=[create_user, get_all_users],
    prompt=prompt
)

agent_executor = AgentExecutor(agent=agent, tools=[create_user, get_all_users], verbose=True)

while True:
    user_input = input("You: ")
    if user_input.lower()=='q':
        break
    else:
        result = agent_executor.invoke({
            "input": user_input
        })
        print(result['output'])
        if 'error' in result:
            print(f"Error: {result['error']}")