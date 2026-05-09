from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os

app = FastAPI()

import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Cloud AI Server Running"}

@app.post("/chat")
def chat(msg: Message):

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful and concise AI assistant also avoid repetitions and text answers smart easy to understand also which is short."},
                {"role": "user", "content": msg.text}
            ]
        }
    )

    result = response.json()
    return {
        "response": result["choices"][0]["message"]["content"]
    }
