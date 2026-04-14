from fastapi import FastAPI
from pydantic import BaseModel
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

app = FastAPI()


class GenerateReq(BaseModel):
    model: str
    prompt: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/generate")
def generate(req: GenerateReq):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": req.model,
            "prompt": req.prompt,
            "stream": False,
        },
        timeout=600,
    )
    response.raise_for_status()
    payload = response.json()
    return {"response": payload.get("response", "")}
