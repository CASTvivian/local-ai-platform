from pathlib import Path
import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
DISTILLED_REG_PATH = BASE_DIR / "docs" / "distilled" / "registry.json"
DOCS_DIR = BASE_DIR / "docs" / "distilled"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_registry():
    if not DISTILLED_REG_PATH.exists():
        return {"items": []}
    return json.loads(DISTILLED_REG_PATH.read_text(encoding="utf-8"))

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/distilled")
def list_distilled():
    return load_registry()

@app.get("/distilled/{name}")
def get_distilled(name: str):
    reg = load_registry()
    for item in reg.get("items", []):
        item_name = item.get("name") or item.get("id")
        if item_name == name:
            docs = []
            for rel in item.get("outputs", []):
                p = BASE_DIR / rel
                if p.exists():
                    docs.append({
                        "path": rel,
                        "content": p.read_text(encoding="utf-8")
                    })
            return {
                "item": item,
                "docs": docs
            }
    raise HTTPException(status_code=404, detail="distilled item not found")

@app.post("/distilled/{name}/mark/{status}")
def mark_status(name: str, status: str):
    reg = load_registry()
    updated = False
    for item in reg.get("items", []):
        item_name = item.get("name") or item.get("id")
        if item_name == name:
            item["status"] = status
            updated = True
    if not updated:
        raise HTTPException(status_code=404, detail="distilled item not found")
    DISTILLED_REG_PATH.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    return {"ok": True, "status": status, "name": name}
