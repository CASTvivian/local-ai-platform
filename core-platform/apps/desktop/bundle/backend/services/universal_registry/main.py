from pathlib import Path
import csv

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
REG_PATH = BASE_DIR / "manifests" / "capability_registry" / "repos_master_registry.csv"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_rows():
    if not REG_PATH.exists():
        return []
    rows = []
    with REG_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/repos")
def list_repos():
    rows = load_rows()
    return {"items": rows}

@app.get("/repos/grouped")
def grouped_repos():
    rows = load_rows()
    grouped = {
        "runtime": [],
        "plugin_placeholder": [],
        "lab": [],
        "blocked": []
    }
    for row in rows:
        lvl = row.get("integration_level", "lab")
        grouped.setdefault(lvl, []).append(row)
    return grouped

@app.get("/repos/{name}")
def get_repo(name: str):
    rows = load_rows()
    for row in rows:
        if row["name"] == name:
            return row
    raise HTTPException(status_code=404, detail="repo not found")
