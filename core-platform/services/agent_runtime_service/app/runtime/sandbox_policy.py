from __future__ import annotations
import json
import os
from pathlib import Path
from typing import Any, Dict

POLICY_FILE = Path("core-platform/data/sandbox_policy/sandbox_policy.json")

def load_sandbox_policy() -> Dict[str, Any]:
    if POLICY_FILE.exists():
        return json.loads(POLICY_FILE.read_text(encoding="utf-8"))
    return {
        "default_profile": "local_restricted",
        "profiles": {
            "local_restricted": {
                "allowed_binaries": ["python", "python3", "node", "bash", "sh"],
                "blocked_binaries": [],
                "timeout_seconds": 20,
                "max_stdout_bytes": 200000,
                "max_stderr_bytes": 200000,
                "env_allowlist": ["PATH", "PYTHONPATH", "NODE_PATH", "HOME", "TMPDIR"],
                "env_overrides": {"MAOMIAI_SANDBOX": "1"},
            }
        },
    }

def get_sandbox_profile(profile: str | None = None) -> Dict[str, Any]:
    policy = load_sandbox_policy()
    name = profile or policy.get("default_profile") or "local_restricted"
    profiles = policy.get("profiles") or {}
    item = profiles.get(name)
    if not item:
        item = profiles.get(policy.get("default_profile")) or {}
    return {
        "name": name,
        **item,
    }

def build_sandbox_env(profile: Dict[str, Any]) -> Dict[str, str]:
    allowlist = set(profile.get("env_allowlist") or [])
    env = {}
    for key in allowlist:
        if key in os.environ:
            env[key] = os.environ[key]
    for key, value in (profile.get("env_overrides") or {}).items():
        env[str(key)] = str(value)
    return env

def validate_command(binary: str, profile: Dict[str, Any]) -> Dict[str, Any]:
    allowed = set(profile.get("allowed_binaries") or [])
    blocked = set(profile.get("blocked_binaries") or [])

    if binary in blocked:
        return {
            "ok": False,
            "reason": f"binary blocked by sandbox policy: {binary}",
        }
    if allowed and binary not in allowed:
        return {
            "ok": False,
            "reason": f"binary not allowed by sandbox policy: {binary}",
        }
    return {
        "ok": True,
        "reason": "allowed",
    }