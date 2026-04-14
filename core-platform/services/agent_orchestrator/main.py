from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

GATEWAY_URL = "http://127.0.0.1:18080/generate"
PLUGIN_URL = "http://127.0.0.1:18082/run"
EVAL_URL = "http://127.0.0.1:18083/task-runs"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AskReq(BaseModel):
    task_type: str
    prompt: str

def route_plugin(task_type: str, prompt: str):
    text = prompt.lower()

    if task_type == "image":
        return "image_gen_plugin"
    if task_type == "video":
        return "video_gen_plugin"

    if any(k in text for k in ["plugin", "tool", "echo"]):
        return "echo_tool"

    return None

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
        plugin_name = route_plugin(req.task_type, req.prompt)
        if plugin_name:
            route = "plugin"
            plugin_resp = requests.post(
                PLUGIN_URL,
                json={
                    "plugin_name": plugin_name,
                    "payload": {
                        "prompt": req.prompt,
                        "task_type": req.task_type,
                        "source": "agent_orchestrator"
                    }
                },
                timeout=120
            )
            plugin_resp.raise_for_status()
            plugin_data = plugin_resp.json()
            response_text = str(plugin_data.get("result", {}))
        else:
            model_resp = requests.post(
                GATEWAY_URL,
                json={"model": model, "prompt": req.prompt},
                timeout=600
            )
            model_resp.raise_for_status()
            model_data = model_resp.json()
            response_text = model_data.get("response", "")
    except Exception as e:
        response_text = f"ERROR: {str(e)}"

    try:
        requests.post(
            EVAL_URL,
            json={
                "task_type": req.task_type,
                "prompt": req.prompt,
                "model_used": f"{route}:{model}",
                "response_text": response_text
            },
            timeout=30
        )
    except Exception:
        pass

    return {
        "task_type": req.task_type,
        "route_used": route,
        "model_used": model,
        "response": response_text
    }
