from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()


import httpx

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com/v1",
    http_client=httpx.Client(
        proxy=None,
        trust_env=False
    )
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    text: str

@app.post("/chat")
def chat(message: Message):

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {
                "role":"user",
                "content":message.text
            }
        ]
    )

    reply = response.choices[0].message.content

    return {
        "reply": reply
    }
