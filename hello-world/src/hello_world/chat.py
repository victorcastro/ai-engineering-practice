import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

conversations: dict[str, list[dict]] = {}

def get_or_create_conversation(conversation_id: str) -> list[dict]:
    if conversation_id not in conversations:
        conversations[conversation_id] = []
    return conversations[conversation_id]

def send_message(conversation_id: str, message: str) -> str:
    history = get_or_create_conversation(conversation_id)
    history.append({"role": "user", "content": message})

    response = client.messages.create(model="claude-sonnet-4-5", max_tokens=1024, messages=history)

    assistant_message = response.content[0].text
    history.append({"role": "assistant", "content": assistant_message})

    return assistant_message