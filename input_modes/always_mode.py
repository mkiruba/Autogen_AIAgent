import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-3.5-turbo"
llm_config = {
    "model": model,
    "api_key": os.getenv("OPENAI_API_KEY"),
}

agent_with_animal = ConversableAgent(
    name = "agent_with_animal",
    system_message="You are thinking of an animal. You have the animal 'elephant' in your mind , and I will try to guess it. If I guess incorrectly, give me a hint.",
    llm_config = llm_config,
    is_termination_msg=lambda msg: "elephant" in msg["content"],
    human_input_mode="NEVER")


human_proxy = ConversableAgent(
    name = "human_proxy",
    llm_config = False,
    human_input_mode="ALWAYS")

response = human_proxy.initiate_chat(
    agent_with_animal, 
    message="I am thinking of an animal. Guess which one!")
print(response)