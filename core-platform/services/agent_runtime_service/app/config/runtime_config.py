from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any


def find_core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        if (parent / "data").exists() and (parent / "services").exists():
            return parent
    return Path.cwd().resolve()


def runtime_config_path() -> Path:
    return find_core_platform_dir() / "data" / "runtime_config" / "runtime_config.json"


def load_runtime_config() -> dict[str, Any]:
    path = runtime_config_path()
    if not path.exists():
        return {
            "version": "missing",
            "host": "127.0.0.1",
            "services": {},
            "model_profiles": {},
            "defaults": {},
            "error": f"runtime_config.json not found: {path}"
        }
    return json.loads(path.read_text(encoding="utf-8"))


def get_service_config(name: str) -> dict[str, Any]:
    config = load_runtime_config()
    services = config.get("services", {})
    service = services.get(name, {})
    if not isinstance(service, dict):
        return {}
    return service


def get_service_base_url(name: str) -> str | None:
    service = get_service_config(name)
    value = service.get("base_url")
    return str(value) if value else None


def get_service_health_url(name: str) -> str | None:
    service = get_service_config(name)
    base = service.get("base_url")
    path = service.get("health_path", "/health")
    if not base:
        return None
    return str(base).rstrip("/") + "/" + str(path).lstrip("/")


def get_model_profile(profile: str | None = None) -> dict[str, Any]:
    config = load_runtime_config()
    defaults = config.get("defaults", {})
    profile_name = profile or defaults.get("profile") or "light"
    profiles = config.get("model_profiles", {})
    item = profiles.get(profile_name)
    if isinstance(item, dict):
        result = dict(item)
        result["id"] = profile_name
        return result
    return {
        "id": profile_name,
        "provider": "unknown",
        "model": None,
        "error": f"model profile not found: {profile_name}"
    }


def list_model_profiles() -> dict[str, Any]:
    config = load_runtime_config()
    profiles = config.get("model_profiles", {})
    return profiles if isinstance(profiles, dict) else {}


def runtime_defaults() -> dict[str, Any]:
    config = load_runtime_config()
    defaults = config.get("defaults", {})
    return defaults if isinstance(defaults, dict) else {}
