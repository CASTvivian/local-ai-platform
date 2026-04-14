import requests
from fastapi import FastAPI
from pydantic import BaseModel

GATEWAY_URL = "http://127.0.0.1:18080/generate"
PLUGIN_URL = "http://127.0.0.1:18082/run"
EVAL_URL = "http://127.0.0.1:18083/task-runs"

app = FastAPI()


class AskReq(BaseModel):
    task_type: str
    prompt: str


def should_use_plugin(prompt: str) -> bool:
    text = prompt.lower()
    keywords = ["plugin", "tool", "echo"]
    return any(keyword in text for keyword in keywords)


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/ask")
def ask(req: AskReq):
    model = "qwen2.5:7b"
    route = "model"

    if req.task_type in ["code", "coding", "dev"]:
        model = "qwen2.5-coder:7b"

    response_text = ""

    try:
        if should_use_plugin(req.prompt):
            route = "plugin"
            plugin_resp = requests.post(
                PLUGIN_URL,
                json={
                    "plugin_name": "echo_tool",
                    "payload": {
                        "message": req.prompt,
                        "task_type": req.task_type,
                        "source": "agent_orchestrator",
                    },
                },
                timeout=60,
            )
            plugin_resp.raise_for_status()
            plugin_data = plugin_resp.json()
            response_text = str(plugin_data.get("result", {}))
        else:
            model_resp = requests.post(
                GATEWAY_URL,
                json={"model": model, "prompt": req.prompt},
                timeout=600,
            )
            model_resp.raise_for_status()
            model_data = model_resp.json()
            response_text = model_data.get("response", "")
    except Exception as exc:
        response_text = f"ERROR: {exc}"

    try:
        requests.post(
            EVAL_URL,
            json={
                "task_type": req.task_type,
                "prompt": req.prompt,
                "model_used": f"{route}:{model}",
                "response_text": response_text,
            },
            timeout=30,
        )
    except Exception:
        pass

    return {
        "task_type": req.task_type,
        "route_used": route,
        "model_used": model,
        "response": response_text,
    }
