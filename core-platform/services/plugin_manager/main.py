import importlib
import json
from pathlib import Path
from typing import Any, Dict

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parents[2]
REGISTRY_PATH = BASE_DIR / "manifests" / "plugins" / "registry.json"

app = FastAPI()

PLUGIN_CACHE = {}


class PluginRunReq(BaseModel):
    plugin_name: str
    payload: Dict[str, Any]


def load_registry():
    if not REGISTRY_PATH.exists():
        return {"plugins": []}
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


def load_plugin(entrypoint: str):
    if entrypoint in PLUGIN_CACHE:
        return PLUGIN_CACHE[entrypoint]
    module_path, class_name = entrypoint.split(":")
    module = importlib.import_module(module_path)
    cls = getattr(module, class_name)
    instance = cls()
    PLUGIN_CACHE[entrypoint] = instance
    return instance


@app.get("/health")
def health():
    return {"ok": True}


@app.get("/plugins")
def list_plugins():
    return load_registry()


@app.post("/run")
def run_plugin(req: PluginRunReq):
    registry = load_registry()
    plugins = registry.get("plugins", [])
    target = next(
        (p for p in plugins if p["name"] == req.plugin_name and p.get("enabled", False)),
        None,
    )
    if not target:
        raise HTTPException(status_code=404, detail=f"Plugin not found or disabled: {req.plugin_name}")

    plugin = load_plugin(target["entrypoint"])
    result = plugin.run(req.payload)
    return {
        "ok": True,
        "plugin": req.plugin_name,
        "result": result,
    }
