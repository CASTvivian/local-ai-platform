from pathlib import Path
import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "sqlite" / "platform.db"
GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def conn():
    return sqlite3.connect(DB_PATH)

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/summary")
def summary():
    c = conn()
    cur = c.cursor()

    task_runs = 0
    evaluations = 0
    agent_tasks = 0
    agent_steps = 0

    try:
        task_runs = cur.execute("SELECT COUNT(*) FROM task_runs").fetchone()[0]
    except Exception:
        pass

    try:
        evaluations = cur.execute("SELECT COUNT(*) FROM evaluations").fetchone()[0]
    except Exception:
        pass

    try:
        agent_tasks = cur.execute("SELECT COUNT(*) FROM agent_tasks").fetchone()[0]
    except Exception:
        pass

    try:
        agent_steps = cur.execute("SELECT COUNT(*) FROM agent_steps").fetchone()[0]
    except Exception:
        pass

    c.close()

    generated = {}
    for name in ["rag", "vision", "finance", "audio"]:
        d = GEN_DIR / name
        generated[name] = len(list(d.glob("*.json"))) if d.exists() else 0

    return {
        "ok": True,
        "summary": {
            "task_runs": task_runs,
            "evaluations": evaluations,
            "agent_tasks": agent_tasks,
            "agent_steps": agent_steps,
            "generated": generated
        }
    }

@app.get("/insights")
def insights():
    c = conn()
    cur = c.cursor()

    latest_runs = []
    latest_evals = []
    latest_steps = []

    try:
        rows = cur.execute(
            "SELECT id, task_type, model_used, response_text, created_at FROM task_runs ORDER BY id DESC LIMIT 10"
        ).fetchall()
        latest_runs = [
            {
                "id": r[0],
                "task_type": r[1],
                "model_used": r[2],
                "response_text": (r[3] or "")[:500],
                "created_at": r[4],
            } for r in rows
        ]
    except Exception:
        pass

    try:
        rows = cur.execute(
            "SELECT id, task_run_id, score, feedback_text, created_at FROM evaluations ORDER BY id DESC LIMIT 10"
        ).fetchall()
        latest_evals = [
            {
                "id": r[0],
                "task_run_id": r[1],
                "score": r[2],
                "feedback_text": (r[3] or "")[:300],
                "created_at": r[4],
            } for r in rows
        ]
    except Exception:
        pass

    try:
        rows = cur.execute(
            "SELECT id, task_id, step_type, content, status, created_at FROM agent_steps ORDER BY id DESC LIMIT 10"
        ).fetchall()
        latest_steps = [
            {
                "id": r[0],
                "task_id": r[1],
                "step_type": r[2],
                "content": (r[3] or "")[:500],
                "status": r[4],
                "created_at": r[5],
            } for r in rows
        ]
    except Exception:
        pass

    c.close()

    return {
        "ok": True,
        "insights": {
            "latest_task_runs": latest_runs,
            "latest_evaluations": latest_evals,
            "latest_agent_steps": latest_steps
        }
    }

@app.get("/recommendations")
def recommendations():
    return {
        "ok": True,
        "recommendations": [
            "优先把 rag_real 从 shell 升级到真实文件 ingest + retrieval。",
            "优先把 vision_real 接到真实图像理解模型。",
            "优先把 finance_real 接到 qlib 研究链路。",
            "优先把 tts_real 接到 VoxCPM 推理。"
        ]
    }
