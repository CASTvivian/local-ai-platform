from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateReq(BaseModel):
    model: str
    prompt: str

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/generate")
def generate(req: GenerateReq):
    r = requests.post(
        OLLAMA_URL,
        json={
            "model": req.model,
            "prompt": req.prompt,
            "stream": False
        },
        timeout=600
    )
    r.raise_for_status()
    data = r.json()
    return {"response": data.get("response", "")}
