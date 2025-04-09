import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI, Request
from decision_tree import evaluate_compliance
from chatbot.openai_chat import ask_chatgpt

app = FastAPI()

@app.post("/analyze")
async def analyze(request: Request):
    data = await request.json()
    from json import loads
    responses = loads(data.get("policy"))
    return evaluate_compliance(responses)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("question")
    return {"answer": ask_chatgpt(user_input)}
