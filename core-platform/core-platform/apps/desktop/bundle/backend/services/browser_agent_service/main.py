from __future__ import annotations
from pathlib import Path
from datetime import datetime
import json
import shutil
import subprocess

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated")
BROWSER_USE_DIR = Path("/Users/mofamaomi/Documents/本地ai/references/browser-use")
STAGEHAND_DIR = Path("/Users/mofamaomi/Documents/本地ai/references/stagehand")
SKYVERN_DIR = Path("/Users/mofamaomi/Documents/本地ai/references/skyvern")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STANDARD_ACTIONS = ["navigate", "extract", "form_flow"]

def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def write_json(kind: str, payload: dict):
    out_dir = GEN_DIR / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{kind}_{ts()}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

def cmd_exists(name: str) -> bool:
    return shutil.which(name) is not None

def run_cmd(cmd: list[str], cwd: str | None = None, timeout: int = 60):
    proc = subprocess.run(
        cmd,
        cwd=cwd,
        timeout=timeout,
        capture_output=True,
        text=True
    )
    return {
        "cmd": cmd,
        "cwd": cwd,
        "returncode": proc.returncode,
        "stdout": proc.stdout[-5000:],
        "stderr": proc.stderr[-5000:]
    }

def probe_python_modules(mods: list[str]):
    results = {}
    for m in mods:
        try:
            __import__(m)
            results[m] = True
        except Exception:
            results[m] = False
    return results

def provider_runtime(provider: str, prompt: str, start_url: str, action: str, form_data: dict | None = None):
    if action not in STANDARD_ACTIONS:
        return {
            "ok": False,
            "provider": provider,
            "error": f"unsupported action: {action}",
            "supported_actions": STANDARD_ACTIONS
        }

    if provider == "browser_use":
        repo = BROWSER_USE_DIR
        checks = {
            "repo_exists": repo.exists(),
            "python_exists": cmd_exists("python3"),
            "module_probe": probe_python_modules(["dotenv", "pydantic_settings", "requests"])
        }
        cmds = [
            ["python3", "-m", "browser_use"],
            ["python3", "main.py"],
            ["python3", "--version"]
        ]
    elif provider == "stagehand":
        repo = STAGEHAND_DIR
        checks = {
            "repo_exists": repo.exists(),
            "node_exists": cmd_exists("node"),
            "npm_exists": cmd_exists("npm")
        }
        cmds = [
            ["npm", "run"],
            ["node", "--version"]
        ]
    elif provider == "skyvern":
        repo = SKYVERN_DIR
        checks = {
            "repo_exists": repo.exists(),
            "python_exists": cmd_exists("python3"),
            "module_probe": probe_python_modules(["structlog", "pydantic_settings", "requests"])
        }
        cmds = [
            ["python3", "-m", "skyvern"],
            ["python3", "--version"]
        ]
    else:
        return {"ok": False, "provider": provider, "error": f"unknown provider: {provider}"}

    if not checks.get("repo_exists"):
        return {"ok": False, "provider": provider, "action": action, "error": "repo not found"}

    attempts = []
    for cmd in cmds:
        try:
            attempts.append(run_cmd(cmd, cwd=str(repo), timeout=25))
        except Exception as e:
            attempts.append({"cmd": cmd, "cwd": str(repo), "error": str(e)})

    return {
        "ok": True,
        "provider": provider,
        "action": action,
        "prompt": prompt,
        "start_url": start_url,
        "form_data": form_data or {},
        "checks": checks,
        "attempts": attempts,
        "mode": "runtime_bridge",
        "note": "Browser Agent Batch 5 standard action executed"
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/providers")
def providers():
    return {
        "ok": True,
        "providers": [
            {
                "name": "browser_use",
                "repo": str(BROWSER_USE_DIR),
                "exists": BROWSER_USE_DIR.exists(),
                "python_exists": cmd_exists("python3"),
                "priority": 1,
                "actions": ["navigate"]
            },
            {
                "name": "stagehand",
                "repo": str(STAGEHAND_DIR),
                "exists": STAGEHAND_DIR.exists(),
                "node_exists": cmd_exists("node"),
                "npm_exists": cmd_exists("npm"),
                "priority": 2,
                "actions": ["extract"]
            },
            {
                "name": "skyvern",
                "repo": str(SKYVERN_DIR),
                "exists": SKYVERN_DIR.exists(),
                "python_exists": cmd_exists("python3"),
                "priority": 3,
                "actions": ["form_flow"]
            }
        ],
        "standard_actions": STANDARD_ACTIONS
    }

@app.post("/run")
def run(payload: dict):
    provider = payload.get("provider", "browser_use")
    prompt = payload.get("prompt", "")
    start_url = payload.get("start_url", "")
    action = payload.get("action", "navigate")
    form_data = payload.get("form_data", {})

    result = provider_runtime(provider, prompt, start_url, action, form_data=form_data)
    result["kind"] = "browser_agent_runtime"
    result["output_path"] = write_json("browser", result)
    return result
