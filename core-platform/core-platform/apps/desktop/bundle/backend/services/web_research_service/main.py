from pathlib import Path
import json
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def write_payload(kind: str, payload: dict):
    out_dir = GEN_DIR / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{kind}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/stock_research")
def stock_research(payload: dict):
    result = {
        "ok": True,
        "kind": "stock_research",
        "mode": "shell",
        "query": payload.get("prompt", ""),
        "note": "stock research shell ready; connect realtime stock/news provider next"
    }
    result["output_path"] = write_payload("stock_research", result)
    return result

@app.post("/web_research")
def web_research(payload: dict):
    result = {
        "ok": True,
        "kind": "web_research",
        "mode": "shell",
        "query": payload.get("prompt", ""),
        "note": "web research shell ready; connect live search/news provider next"
    }
    result["output_path"] = write_payload("web_research", result)
    return result
