import uuid
from fastapi import FastAPI
from hello_world.models import ChatRequest, ChatResponse
from hello_world.chat import send_message

app = FastAPI(title="Hello AI Engineer", description="A simple chat application using FastAPI and Anthropic's API.")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Welcome to the Hello AI Engineer API"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    conversation_id = request.conversation_id or str(uuid.uuid4())
    assistant_text = send_message(conversation_id, request.message)
    return ChatResponse(message=assistant_text, conversation_id=conversation_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello_world.main:app", host="127.0.0.1", port=8000, reload=True)