from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
from knowledge_base import KNOWLEDGE_BASE
from response_generator import IntentClassifier, ResponseGenerator

app = FastAPI(title="XYZON Chatbot API")

# Enable CORS for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    history: List[dict] # List of {"role": "user/bot", "content": "..."}

class ChatResponse(BaseModel):
    response: str
    intent: str

classifier = IntentClassifier()
generator = ResponseGenerator(KNOWLEDGE_BASE)

@app.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    intent = classifier.classify(request.message)
    response = generator.generate_response(intent, request.message, request.history[-3:]) # Use last 3 for context
    
    # Log user query and detected intent (Bonus feature)
    print(f"Query: {request.message} | Intent: {intent}")
    
    return ChatResponse(response=response, intent=intent)

@app.get("/welcome")
async def welcome_endpoint():
    return {"message": KNOWLEDGE_BASE["welcome"]["message"]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
