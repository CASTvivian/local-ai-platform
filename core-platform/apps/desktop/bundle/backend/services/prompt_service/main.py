from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
WORKFLOW_DIR = BASE_DIR / "prompts" / "workflows"
GUIDELINE_DIR = BASE_DIR / "prompts" / "guidelines"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def read_text(path: Path) -> str:
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"not found: {path.name}")
    return path.read_text(encoding="utf-8")

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/workflows")
def list_workflows():
    items = []
    for p in sorted(WORKFLOW_DIR.glob("*.md")):
        items.append({"name": p.stem, "path": str(p)})
    return {"items": items}

@app.get("/workflows/{name}")
def get_workflow(name: str):
    p = WORKFLOW_DIR / f"{name}.md"
    return {"name": name, "content": read_text(p)}

@app.get("/guidelines")
def list_guidelines():
    items = []
    for p in sorted(GUIDELINE_DIR.glob("*.md")):
        items.append({"name": p.stem, "path": str(p)})
    return {"items": items}

@app.get("/guidelines/{name}")
def get_guideline(name: str):
    p = GUIDELINE_DIR / f"{name}.md"
    return {"name": name, "content": read_text(p)}