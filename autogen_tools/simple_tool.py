import os
from typing import Annotated
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "temperature": 0.0,
    "api_key": os.getenv("OPENAI_API_KEY"),
}

# Define simple calculator functions
def add_numbers(
    a: Annotated[int, "First number"],
    b: Annotated[int, "Second number"]
    ) -> str:
    return f"The sum of {a} and {b} is {a + b}."

def multiply_numbers(
    a: Annotated[int, "First number"],
    b: Annotated[int, "Second number"]
    ) -> str:
    return f"The product of {a} and {b} is {a * b}."

assistant = ConversableAgent(
    name = "CalculatorAssistant",
    system_message="You are a helpful AI calculator. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config)


user_proxy = ConversableAgent(
    name = "User",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: msg.get("content") 
    and "TERMINATE" in msg["content"],
    )

assistant.register_for_llm(name="add_numbers", description="Add two numbers")(add_numbers)
assistant.register_for_llm(name="multiply_numbers", description="Multiply two numbers")(multiply_numbers)

user_proxy.register_for_execution(name="add_numbers", description="Add two numbers")(add_numbers)
user_proxy.register_for_execution(name="multiply_numbers", description="Multiply two numbers")(multiply_numbers)

response = user_proxy.initiate_chat(assistant, message="What is the sum of 7 and 5?")
print(response)