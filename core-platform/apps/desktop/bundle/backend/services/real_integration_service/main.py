from pathlib import Path
import json
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated")
CONFIG_PATH = BASE_DIR / "config" / "app.json"
RUNTIME_TARGETS = BASE_DIR / "config" / "runtime" / "realization_targets.json"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_config():
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}

def load_targets():
    if RUNTIME_TARGETS.exists():
        return json.loads(RUNTIME_TARGETS.read_text(encoding="utf-8"))
    return {}

def write_payload(kind: str, payload: dict):
    out_dir = GEN_DIR / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{kind}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/targets")
def targets():
    return {"ok": True, "targets": load_targets()}

@app.post("/rag")
def rag(payload: dict):
    cfg = load_config()
    targets = load_targets()
    backend = cfg.get("rag_backend", "RAG-Anything-placeholder")
    result = {
        "ok": True,
        "kind": "rag",
        "backend": backend,
        "mode": "shell",
        "target": targets.get("rag", {}),
        "query": payload.get("prompt", ""),
        "note": "RAG shell is active; connect ingestion/index/query next"
    }
    result["output_path"] = write_payload("rag", result)
    return result

@app.post("/vision")
def vision(payload: dict):
    cfg = load_config()
    targets = load_targets()
    result = {
        "ok": True,
        "kind": "vision",
        "backend": cfg.get("vision_backend_primary", "Qwen3-VL-placeholder"),
        "fallbacks": [
            cfg.get("vision_backend_secondary", "Qwen2.5-VL-placeholder"),
            cfg.get("vision_backend_alt_1", "LLaVA-OneVision-1.5-placeholder"),
            cfg.get("vision_backend_alt_2", "LLaVA-NeXT-placeholder")
        ],
        "mode": "shell",
        "target": targets.get("vision", {}),
        "query": payload.get("prompt", ""),
        "note": "Vision shell is active; connect image inference next"
    }
    result["output_path"] = write_payload("vision", result)
    return result

@app.post("/finance")
def finance(payload: dict):
    cfg = load_config()
    targets = load_targets()
    result = {
        "ok": True,
        "kind": "finance",
        "backend": cfg.get("finance_research_backend", "Qlib-placeholder"),
        "mode": "shell",
        "target": targets.get("finance", {}),
        "query": payload.get("prompt", ""),
        "note": "Finance shell is active; connect qlib research pipeline next"
    }
    result["output_path"] = write_payload("finance", result)
    return result

@app.post("/tts")
def tts(payload: dict):
    cfg = load_config()
    targets = load_targets()
    result = {
        "ok": True,
        "kind": "tts",
        "backend": cfg.get("tts_backend", "VoxCPM-placeholder"),
        "mode": "shell",
        "target": targets.get("tts", {}),
        "text": payload.get("prompt", ""),
        "note": "TTS shell is active; connect VoxCPM inference next"
    }
    result["output_path"] = write_payload("audio", result)
    return result
