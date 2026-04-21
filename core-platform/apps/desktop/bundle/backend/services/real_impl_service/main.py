from __future__ import annotations
from pathlib import Path
from datetime import datetime
import json
import subprocess
import tempfile
import base64
import shutil

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated")
RAG_DIR = BASE_DIR / "data" / "rag"
ASK_URL = "http://127.0.0.1:18081/ask"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_TAGS_URL = "http://127.0.0.1:11434/api/tags"
VOXCPM_DIR = Path("/Users/mofamaomi/Documents/本地ai/references/VoxCPM")

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

VOICE_PRESETS = {
    "default_cn": {"voice": "Tingting"},
    "soft_cn": {"voice": "Tingting"},
    "male_cn": {"voice": "Daniel"},
    "narration_en": {"voice": "Samantha"}
}

def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def write_json(kind: str, payload: dict):
    out_dir = GEN_DIR / kind
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / f"{kind}_{ts()}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)

def ask_model(task_type: str, prompt: str, timeout: int = 1200):
    import requests
    r = requests.post(ASK_URL, json={"task_type": task_type, "prompt": prompt}, timeout=timeout)
    r.raise_for_status()
    return r.json()

def read_text_file(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in [".txt", ".md", ".py", ".js", ".ts", ".json", ".csv", ".yaml", ".yml", ".html"]:
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return ""
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
            reader = PdfReader(str(path))
            parts = []
            for page in reader.pages[:30]:
                try:
                    parts.append(page.extract_text() or "")
                except Exception:
                    pass
            return "\n".join(parts)
        except Exception:
            return ""
    return ""

def build_rag_index(workspace: Path):
    RAG_DIR.mkdir(parents=True, exist_ok=True)
    docs = []
    count = 0
    for p in workspace.rglob("*"):
        if p.is_file() and p.suffix.lower() in [".txt", ".md", ".py", ".js", ".ts", ".json", ".csv", ".yaml", ".yml", ".html", ".pdf"]:
            content = read_text_file(p)
            if content.strip():
                docs.append({"path": str(p), "content": content[:30000]})
                count += 1
    idx = RAG_DIR / "index.json"
    idx.write_text(json.dumps(docs, ensure_ascii=False, indent=2), encoding="utf-8")
    return idx, count

def rag_search(query: str, topk: int = 5):
    idx = RAG_DIR / "index.json"
    if not idx.exists():
        return []
    docs = json.loads(idx.read_text(encoding="utf-8"))
    q_terms = [x.strip().lower() for x in query.split() if x.strip()]
    scored = []
    for d in docs:
        text = d["content"].lower()
        score = sum(text.count(t) for t in q_terms) if q_terms else 0
        scored.append((score, d))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored[:topk] if x[0] > 0] or [x[1] for x in scored[:topk]]

def pick_best_vision_model(models: list[str], preferred: str | None = None) -> tuple[str | None, list[str]]:
    ranked = []
    for m in models:
        name = m.lower()
        score = 0
        if preferred and preferred.lower() == name:
            score = 1000
        elif "qwen2.5-vl" in name or "qwen2.5vl" in name:
            score = 100
        elif "qwen3-vl" in name or "qwen3vl" in name:
            score = 95
        elif "llava" in name and "vision" in name:
            score = 90
        elif "llava" in name:
            score = 85
        elif "vision" in name or "vl" in name:
            score = 70
        if score > 0:
            ranked.append((score, m))
    ranked.sort(key=lambda x: x[0], reverse=True)
    return (ranked[0][1] if ranked else None), [x[1] for x in ranked]


def vox_runtime_exists():
    return VOXCPM_DIR.exists()

def command_exists(name: str):
    return shutil.which(name) is not None

def detect_voxcpm_entry():
    """
    尝试探测 VoxCPM 可运行入口。
    这里只做最小可用探测：
    - infer.py
    - webui.py
    - app.py
    - cli.py
    """
    if not VOXCPM_DIR.exists():
        return None

    candidates = [
        VOXCPM_DIR / "infer.py",
        VOXCPM_DIR / "webui.py",
        VOXCPM_DIR / "app.py",
        VOXCPM_DIR / "cli.py",
    ]
    for c in candidates:
        if c.exists():
            return c
    return None

def try_voxcpm_tts(text: str, out_path: Path):
    """
    最小真接入策略：
    1. 探测仓目录与入口脚本
    2. 优先尝试常见 CLI 参数
    3. 若成功产出文件即视为 voxcpm 成功
    4. 否则回退 say
    """
    entry = detect_voxcpm_entry()
    if not entry:
        return {"ok": False, "reason": "voxcpm_entry_not_found"}

    attempts = []

    # 尝试几种常见参数风格
    candidates = [
        ["python3", str(entry), "--text", text, "--output", str(out_path)],
        ["python3", str(entry), "--prompt", text, "--output", str(out_path)],
        ["python3", str(entry), "--input", text, "--output", str(out_path)],
    ]

    for cmd in candidates:
        try:
            proc = subprocess.run(cmd, cwd=str(VOXCPM_DIR), capture_output=True, text=True, timeout=600)
            attempts.append({
                "cmd": cmd,
                "returncode": proc.returncode,
                "stdout": proc.stdout[-2000:],
                "stderr": proc.stderr[-2000:],
            })
            if proc.returncode == 0 and out_path.exists() and out_path.stat().st_size > 0:
                return {
                    "ok": True,
                    "backend": "voxcpm",
                    "entry": str(entry),
                    "attempts": attempts,
                }
        except Exception as e:
            attempts.append({"cmd": cmd, "error": str(e)})

    return {
        "ok": False,
        "reason": "voxcpm_attempts_failed",
        "entry": str(entry),
        "attempts": attempts,
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/vision/models")
def vision_models():
    import requests
    try:
        r = requests.get(OLLAMA_TAGS_URL, timeout=20)
        r.raise_for_status()
        data = r.json()
        models = [m.get("name", "") for m in data.get("models", [])]
        best, ranked = pick_best_vision_model(models)
        return {"ok": True, "models": models, "vision_candidates": ranked, "best_model": best}
    except Exception as e:
        return {"ok": False, "error": str(e), "models": [], "vision_candidates": [], "best_model": None}

@app.get("/tts/voices")
def tts_voices():
    proc = subprocess.run(["say", "-v", "?"], capture_output=True, text=True)
    voices = []
    if proc.returncode == 0:
        for line in proc.stdout.splitlines():
            if line.strip():
                voices.append(line.split()[0])

    entry = detect_voxcpm_entry()
    return {
        "ok": True,
        "voices": voices[:50],
        "presets": VOICE_PRESETS,
        "voxcpm_repo_exists": vox_runtime_exists(),
        "voxcpm_entry": str(entry) if entry else None,
        "tts_backends": {
            "voxcpm": bool(entry),
            "say_fallback": command_exists("say")
        }
    }

@app.post("/rag/index")
def rag_index(payload: dict):
    workspace = Path(payload.get("workspace") or "/Users/mofamaomi/Documents/本地ai").resolve()
    idx, count = build_rag_index(workspace)
    result = {"ok": True, "kind": "rag_index", "workspace": str(workspace), "index_path": str(idx), "doc_count": count}
    result["output_path"] = write_json("rag", result)
    return result

@app.post("/rag/query")
def rag_query(payload: dict):
    query = payload.get("prompt", "")
    topk = int(payload.get("topk", 5))
    hits = rag_search(query, topk=topk)
    context = "\n\n".join([f"[{i+1}] {h['path']}\n{h['content'][:4000]}" for i, h in enumerate(hits)])
    answer = ""
    if context.strip():
        try:
            data = ask_model("general", f"根据下面检索内容回答问题。\n\n问题：{query}\n\n检索内容：\n{context}", timeout=1200)
            answer = data.get("response", "")
        except Exception as e:
            answer = f"RAG answer fallback error: {e}"
    result = {"ok": True, "kind": "rag_query", "query": query, "topk": topk, "hits": [h["path"] for h in hits], "answer": answer}
    result["output_path"] = write_json("rag", result)
    return result

@app.post("/vision/analyze")
def vision_analyze(payload: dict):
    import requests
    from PIL import Image

    image_path = payload.get("image_path", "").strip()
    prompt = payload.get("prompt", "").strip() or "请分析这张图片。"
    preferred_model = payload.get("preferred_model", "").strip() or None
    img = Path(image_path)

    meta = {}
    if img.exists():
        try:
            im = Image.open(img)
            meta = {"path": str(img), "format": im.format, "size": im.size, "mode": im.mode}
        except Exception as e:
            meta = {"path": str(img), "error": str(e)}

    used_model = None
    ranked_models = []
    analysis = None
    fallback_summary = None
    status = "fallback"

    try:
        tags = requests.get(OLLAMA_TAGS_URL, timeout=15).json()
        models = [m.get("name", "") for m in tags.get("models", [])]
        used_model, ranked_models = pick_best_vision_model(models, preferred=preferred_model)

        if used_model and img.exists():
            raw = img.read_bytes()
            b64 = base64.b64encode(raw).decode("utf-8")
            req = {"model": used_model, "prompt": prompt, "images": [b64], "stream": False}
            r = requests.post(OLLAMA_URL, json=req, timeout=300)
            r.raise_for_status()
            analysis = r.json().get("response", "")
            if analysis:
                status = "model_success"
    except Exception as e:
        analysis = f"vision_runtime_error: {e}"

    if status != "model_success":
        try:
            fallback_summary = ask_model(
                "general",
                f"用户要分析一张图片。你只能基于这些元数据给出谨慎说明，不要编造图片细节。\n\n用户问题：{prompt}\n\n图片元数据：{json.dumps(meta, ensure_ascii=False)}",
                timeout=300
            ).get("response", "")
            status = "fallback_summary"
        except Exception as e:
            fallback_summary = f"vision_fallback_error: {e}"
            status = "fallback_error"

    result = {
        "ok": True,
        "kind": "vision_analyze",
        "status": status,
        "image_exists": img.exists(),
        "meta": meta,
        "prompt": prompt,
        "preferred_model": preferred_model,
        "used_model": used_model,
        "ranked_models": ranked_models,
        "analysis": analysis,
        "fallback_summary": fallback_summary,
        "note": "Vision Batch 4 closeout"
    }
    result["output_path"] = write_json("vision", result)
    return result

@app.post("/finance/research")
def finance_research(payload: dict):
    prompt = payload.get("prompt", "").strip()
    import akshare as ak

    notes = []
    data_preview = {}

    try:
        df = ak.stock_zh_index_spot_em()
        data_preview["index_spot_head"] = df.head(10).to_dict(orient="records")
        notes.append("已真实拉取A股指数行情快照")
    except Exception as e:
        notes.append(f"行情拉取失败: {e}")

    summary = ""
    try:
        data = ask_model("general", f"基于下面的市场数据预览，回答并分析：{prompt}\n\n数据：{json.dumps(data_preview, ensure_ascii=False)[:12000]}", timeout=1200)
        summary = data.get("response", "")
    except Exception as e:
        summary = f"模型总结失败: {e}"

    result = {"ok": True, "kind": "finance_research", "prompt": prompt, "notes": notes, "data_preview": data_preview, "summary": summary}
    result["output_path"] = write_json("finance", result)
    return result

@app.post("/finance/stock")
def finance_stock(payload: dict):
    code = payload.get("code", "").strip()
    import akshare as ak
    notes = []
    data_preview = {}

    try:
        df = ak.stock_individual_info_em(symbol=code)
        data_preview["stock_info"] = df.to_dict(orient="records")
        notes.append("已真实拉取个股信息")
    except Exception as e:
        notes.append(f"个股信息拉取失败: {e}")

    result = {"ok": True, "kind": "finance_stock", "code": code, "notes": notes, "data_preview": data_preview}
    result["output_path"] = write_json("finance", result)
    return result

@app.post("/tts/speak")
def tts_speak(payload: dict):
    text = payload.get("prompt", "").strip()
    preset = payload.get("preset", "").strip()
    requested_voice = payload.get("voice", "").strip()

    selected_voice = requested_voice
    if preset and preset in VOICE_PRESETS:
        selected_voice = VOICE_PRESETS[preset]["voice"]
    if not selected_voice:
        selected_voice = "Tingting"

    out_dir = GEN_DIR / "audio"
    out_dir.mkdir(parents=True, exist_ok=True)

    wav_path = out_dir / f"tts_{ts()}.wav"
    aiff_path = out_dir / f"tts_{ts()}.aiff"

    backend = None
    vox_result = None

    # 优先 VoxCPM
    if vox_runtime_exists():
        vox_result = try_voxcpm_tts(text, wav_path)
        if vox_result.get("ok"):
            backend = "voxcpm"
            result = {
                "ok": True,
                "kind": "tts_speak",
                "backend": backend,
                "vox_result": vox_result,
                "preset": preset,
                "voice": selected_voice,
                "text": text,
                "audio_path": str(wav_path),
                "returncode": 0,
                "stderr": ""
            }
            result["output_path"] = write_json("audio", result)
            return result

    # 回退 macOS say
    backend = "say_fallback"
    cmd = ["say", "-v", selected_voice, "-o", str(aiff_path), text]
    proc = subprocess.run(cmd, capture_output=True, text=True)

    result = {
        "ok": proc.returncode == 0,
        "kind": "tts_speak",
        "backend": backend,
        "vox_result": vox_result,
        "preset": preset,
        "voice": selected_voice,
        "text": text,
        "audio_path": str(aiff_path),
        "returncode": proc.returncode,
        "stderr": proc.stderr[-1000:]
    }
    result["output_path"] = write_json("audio", result)
    return result
