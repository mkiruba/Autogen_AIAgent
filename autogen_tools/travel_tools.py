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

def get_flight_status(
    flight_number: Annotated[str, "Flight number"]
    ) -> str:
    dummy_data = {
        "AA123": "On time",
        "DL456":"Delayed",
        "UA789":"Cancelled"
    }
    return f"The current status of flight {flight_number} is {dummy_data.get(flight_number, 'not found')}."

def get_hotel_info(
    location: Annotated[str, "Location"]
    ) -> str:
    dummy_data = {
        "New York": "Top hotel in New York: The Plaza - 5 stars",
        "Los Angeles":"Top hotel in Los Angelese: The Beverly Hills Hotel - 5 stars",
        "Chicago":"Top hotel in Chicago: The Langham - 5 stars",
        "UA789":"Cancelled"
    }
    return dummy_data.get(location, f"No hotels found in {location}.")

def get_travel_advice(
    location: Annotated[str, "Location"]
    ) -> str:
    dummy_data = {
        "New York": "Travel advice for New York: Visit Central Park and Times Square.",
        "Los Angeles":"Travel advice for Los Angeles: Visit Hollywood and Santa Monica.",
        "Chicago":"Travel advice for Chicago: Visit Millennium Park and Navy Pier.",
        "UA789":"Cancelled"
    }
    return dummy_data.get(location, f"No travel advice available for {location}.")

assistant = ConversableAgent(
    name = "TravelAssistant",
    system_message="You are a helpful AI travel. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config)


assistant = ConversableAgent(
    name = "TravelAssistant",
    system_message="You are a helpful AI travel. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config
    )

user_proxy = ConversableAgent(
    name = "User",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: msg.get("content") 
    is not None and "TERMINATE" in msg["content"],
    )

assistant.register_for_llm(name="get_flight_status", description="Get the current status of a flight based on the location")(get_flight_status)
assistant.register_for_llm(name="get_hotel_info", description="Get information about hotels in a specific location")(get_hotel_info)
assistant.register_for_llm(name="get_travel_advice", description="Get itravel advice for a specific location")(get_travel_advice)

user_proxy.register_for_execution(name="get_flight_status")(get_flight_status)
user_proxy.register_for_execution(name="get_hotel_info")(get_hotel_info)
user_proxy.register_for_execution(name="get_travel_advice")(get_travel_advice)

response = user_proxy.initiate_chat(assistant, message="What is the current status of flight AA123? Also include travel advice for New York.")