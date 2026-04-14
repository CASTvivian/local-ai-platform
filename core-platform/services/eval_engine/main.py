from pathlib import Path
import sqlite3

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "sqlite" / "platform.db"

app = FastAPI()


class TaskRunReq(BaseModel):
    task_type: str
    prompt: str
    model_used: str
    response_text: str


class EvaluationReq(BaseModel):
    task_run_id: int
    score: float
    feedback_text: str = ""


def get_conn():
    if not DB_PATH.exists():
        raise RuntimeError(f"Database not found: {DB_PATH}")
    return sqlite3.connect(DB_PATH)


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/task-runs")
def create_task_run(req: TaskRunReq):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO task_runs (task_type, prompt, model_used, response_text) VALUES (?, ?, ?, ?)",
        (req.task_type, req.prompt, req.model_used, req.response_text),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return {"ok": True, "task_run_id": row_id}


@app.get("/task-runs")
def list_task_runs():
    conn = get_conn()
    cur = conn.cursor()
    rows = cur.execute(
        "SELECT id, task_type, prompt, model_used, created_at FROM task_runs ORDER BY id DESC LIMIT 50"
    ).fetchall()
    conn.close()
    return {
        "items": [
            {
                "id": row[0],
                "task_type": row[1],
                "prompt": row[2],
                "model_used": row[3],
                "created_at": row[4],
            }
            for row in rows
        ]
    }


@app.post("/evaluations")
def create_evaluation(req: EvaluationReq):
    conn = get_conn()
    cur = conn.cursor()

    exists = cur.execute("SELECT id FROM task_runs WHERE id = ?", (req.task_run_id,)).fetchone()
    if not exists:
        conn.close()
        raise HTTPException(status_code=404, detail=f"task_run_id not found: {req.task_run_id}")

    cur.execute(
        "INSERT INTO evaluations (task_run_id, score, feedback_text) VALUES (?, ?, ?)",
        (req.task_run_id, req.score, req.feedback_text),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return {"ok": True, "evaluation_id": row_id}


@app.get("/evaluations")
def list_evaluations():
    conn = get_conn()
    cur = conn.cursor()
    rows = cur.execute(
        """
        SELECT e.id, e.task_run_id, e.score, e.feedback_text, e.created_at
        FROM evaluations e
        ORDER BY e.id DESC
        LIMIT 50
        """
    ).fetchall()
    conn.close()
    return {
        "items": [
            {
                "id": row[0],
                "task_run_id": row[1],
                "score": row[2],
                "feedback_text": row[3],
                "created_at": row[4],
            }
            for row in rows
        ]
    }
