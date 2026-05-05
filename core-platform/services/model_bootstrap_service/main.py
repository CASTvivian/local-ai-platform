from __future__ import annotations
import os
import platform
import shutil
import subprocess
import time
from typing import Any, Dict, List
from fastapi import FastAPI
from pydantic import BaseModel

APP_VERSION = "0.1.0-d7-c4-bootstrap"
DEFAULT_TIMEOUT = int(os.environ.get("MAOMIAI_BOOTSTRAP_TIMEOUT", "1800"))

app = FastAPI(title="MAOMIAI Model Bootstrap Service", version=APP_VERSION)

class BootstrapStartRequest(BaseModel):
    profile: str = "standard"
    models: List[str] = []

def run_cmd(cmd: List[str], timeout: int = 30) -> Dict[str, Any]:
    try:
        p = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
            shell=False,
        )
        return {
            "ok": p.returncode == 0,
            "returncode": p.returncode,
            "stdout": p.stdout,
            "stderr": p.stderr,
            "cmd": cmd,
        }
    except Exception as e:
        return {
            "ok": False,
            "error": str(e),
            "cmd": cmd,
        }

def find_ollama() -> str | None:
    found = shutil.which("ollama")
    if found:
        return found

    candidates = []
    if platform.system().lower() == "windows":
        local = os.environ.get("LOCALAPPDATA")
        program_files = os.environ.get("ProgramFiles")
        if local:
            candidates.append(os.path.join(local, "Programs", "Ollama", "ollama.exe"))
        if program_files:
            candidates.append(os.path.join(program_files, "Ollama", "ollama.exe"))
    else:
        candidates.extend([
            "/usr/local/bin/ollama",
            "/opt/homebrew/bin/ollama",
        ])

    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None

def profile_to_models(profile: str, requested: List[str]) -> List[str]:
    # UI 不显示具体模型名；这里是本地实现映射。
    # 后续可以改为读取 manifests/model_registry。
    if requested:
        # 允许前端传抽象能力名。
        mapped = []
        for item in requested:
            if item == "standard-chat":
                mapped.append(os.environ.get("MAOMIAI_STANDARD_MODEL", "qwen2.5:7b"))
            elif item == "code-capability":
                mapped.append(os.environ.get("MAOMIAI_CODE_MODEL", "qwen2.5-coder:7b"))
            else:
                mapped.append(item)
        return mapped

    if profile == "code":
        return [os.environ.get("MAOMIAI_CODE_MODEL", "qwen2.5-coder:7b")]
    return [os.environ.get("MAOMIAI_STANDARD_MODEL", "qwen2.5:7b")]

@app.get("/health")
def health():
    return {
        "ok": True,
        "service": "model_bootstrap_service",
        "version": APP_VERSION,
    }

@app.get("/bootstrap/status")
def bootstrap_status():
    ollama = find_ollama()
    status: Dict[str, Any] = {
        "ok": True,
        "service": "model_bootstrap_service",
        "version": APP_VERSION,
        "platform": platform.platform(),
        "ollama_found": bool(ollama),
        "ollama_path": ollama,
        "models": [],
        "message": "",
    }

    if not ollama:
        status["ok"] = False
        status["message"] = "未检测到本地推理后端。请先安装并启动 Ollama。"
        status["next_steps"] = [
            "安装 Ollama Windows 版本。",
            "安装完成后重新打开 MAOMIAI。",
            "回到本地 AI 准备页重新检查。",
        ]
        return status

    version = run_cmd([ollama, "--version"], timeout=15)
    listed = run_cmd([ollama, "list"], timeout=30)
    status["ollama_version"] = version
    status["ollama_list"] = listed

    if listed.get("ok"):
        lines = [x.strip() for x in listed.get("stdout", "").splitlines() if x.strip()]
        status["models"] = lines
        status["message"] = "本地推理后端可用。"
    else:
        status["ok"] = False
        status["message"] = "已检测到本地推理后端，但无法读取模型列表。请确认服务已启动。"

    return status

@app.post("/bootstrap/start")
def bootstrap_start(req: BootstrapStartRequest):
    ollama = find_ollama()
    if not ollama:
        return {
            "ok": False,
            "message": "未检测到本地推理后端，无法下载模型。",
            "next_steps": [
                "请先安装 Ollama Windows 版本。",
                "安装并启动后，再点击准备本地 AI。",
            ],
        }

    models = profile_to_models(req.profile, req.models)
    results = []

    for model in models:
        started = time.time()
        res = run_cmd([ollama, "pull", model], timeout=DEFAULT_TIMEOUT)
        res["model"] = model
        res["elapsed_sec"] = round(time.time() - started, 2)
        results.append(res)

    ok = all(r.get("ok") for r in results)
    return {
        "ok": ok,
        "profile": req.profile,
        "models": models,
        "results": results,
        "message": "本地 AI 能力准备完成。" if ok else "部分模型准备失败，请查看详情。",
    }
