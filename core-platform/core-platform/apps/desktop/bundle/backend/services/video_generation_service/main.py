from __future__ import annotations
from pathlib import Path
import subprocess
import json
from datetime import datetime

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
SCRIPT_PATH = BASE_DIR / "scripts" / "run_cogvideo.py"
GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated/videos")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def write_json(payload: dict):
    out = GEN_DIR / f"video_job_{ts()}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

@app.get("/health")
def health():
    return {
        "ok": True,
        "script_exists": SCRIPT_PATH.exists(),
        "script_path": str(SCRIPT_PATH)
    }

@app.post("/video/generate")
def generate(payload: dict):
    prompt = payload.get("prompt", "").strip()
    if not prompt:
        return {"ok": False, "error": "prompt is required"}

    extra = {
        "num_frames": payload.get("num_frames"),
        "num_inference_steps": payload.get("num_inference_steps"),
        "guidance_scale": payload.get("guidance_scale"),
        "fps": payload.get("fps")
    }

    cmd = ["python3", str(SCRIPT_PATH), prompt]

    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=3600
    )

    result = {
        "ok": proc.returncode == 0,
        "kind": "video_generate",
        "prompt": prompt,
        "params": extra,
        "cmd": cmd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-8000:],
        "stderr": proc.stderr[-8000:]
    }
    result["output_path"] = write_json(result)
    return result
