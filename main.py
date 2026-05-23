from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)
@app.get("/")
def read_root():
    return {"message": "it works!"}
class Message(BaseModel):
    text: str
@app.post("/chat")
def chat(message: Message):
    return {"reply": f"你刚刚说了: {message.text}"}
