from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import requests
import sys
import os
from pathlib import Path

# Runtime config loader (portable path resolution)
def _find_core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        if (parent / "data").exists() and (parent / "services").exists():
            return parent
    return Path.cwd().resolve()

def _load_runtime_config() -> dict:
    import json
    path = _find_core_platform_dir() / "data" / "runtime_config" / "runtime_config.json"
    if not path.exists():
        return {"services": {}}
    return json.loads(path.read_text(encoding="utf-8"))

def _get_ollama_base_url() -> str:
    config = _load_runtime_config()
    svc = config.get("services", {}).get("ollama", {})
    return svc.get("base_url", "http://127.0.0.1:11434")

OLLAMA_URL = _get_ollama_base_url() + "/api/generate"

PROFILE_MODEL_MAP = {
    "standard": "qwen2.5:7b",
    "light": "qwen2.5:1.5b",
    "code": "qwen2.5-coder:7b",
    "reasoning": "deepseek-r1:7b",
    "english": "llama3.1:8b",
    "small": "llama3.2:3b",
    "embed": "nomic-embed-text",
    "embed_multi": "bge-m3",
}

DEFAULT_MODEL = "qwen2.5:7b"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateReq(BaseModel):
    model: Optional[str] = None
    prompt: str
    profile: Optional[str] = None

@app.get("/health")
def health():
    return {"ok": True}

def _resolve_model(req: GenerateReq) -> str:
    """Resolve model: explicit model > profile mapping > default."""
    if req.model:
        return req.model
    if req.profile:
        return PROFILE_MODEL_MAP.get(req.profile, DEFAULT_MODEL)
    return DEFAULT_MODEL


def _get_available_models() -> set:
    """Query Ollama for available models."""
    try:
        r = requests.get(_get_ollama_base_url() + "/api/tags", timeout=3)
        r.raise_for_status()
        return {m["name"] for m in r.json().get("models", [])}
    except Exception:
        return set()


@app.post("/generate")
def generate(req: GenerateReq):
    model = _resolve_model(req)
    # If requested model not available, fallback to DEFAULT_MODEL
    available = _get_available_models()
    if available and model not in available:
        # Try to find a matching model (e.g., "qwen2.5:7b" matches "qwen2.5")
        model_base = model.split(":")[0]
        matched = [m for m in available if m.split(":")[0] == model_base]
        if matched:
            model = matched[0]
        else:
            model = DEFAULT_MODEL
    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": req.prompt,
                "stream": False
            },
            timeout=600
        )
        r.raise_for_status()
        data = r.json()
        return {"response": data.get("response", ""), "model_used": model}
    except Exception as e:
        # Final fallback: try DEFAULT_MODEL if we weren't already using it
        if model != DEFAULT_MODEL:
            try:
                r = requests.post(
                    OLLAMA_URL,
                    json={
                        "model": DEFAULT_MODEL,
                        "prompt": req.prompt,
                        "stream": False
                    },
                    timeout=600
                )
                r.raise_for_status()
                data = r.json()
                return {"response": data.get("response", ""), "model_used": DEFAULT_MODEL, "fallback": True}
            except Exception:
                pass
        return {"ok": False, "error": str(e), "model_attempted": model}
