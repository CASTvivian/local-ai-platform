import subprocess
import uuid
import json
import shlex
from pathlib import Path
from .sandbox_policy import get_sandbox_profile, build_sandbox_env, validate_command

RUNTIME_ROOT = Path("core-platform/data/sandbox_runtime")
RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)

def _clip(value: str | None, limit: int) -> str:
    data = value or ""
    encoded = data.encode("utf-8", errors="replace")
    if len(encoded) <= limit:
        return data
    return encoded[:limit].decode("utf-8", errors="replace") + "\n... truncated by sandbox policy"

def execute_sandboxed(command: str, profile_name: str | None = None):
    sandbox_id = str(uuid.uuid4())
    workdir = RUNTIME_ROOT / sandbox_id
    workdir.mkdir(parents=True, exist_ok=True)

    try:
        cmd = shlex.split(command.strip())
    except Exception as e:
        return {
            "ok": False,
            "sandbox_id": sandbox_id,
            "message": f"command parse failed: {e}",
        }

    if not cmd:
        return {
            "ok": False,
            "sandbox_id": sandbox_id,
            "message": "empty command",
        }

    profile = get_sandbox_profile(profile_name)
    binary = cmd[0]
    policy_result = validate_command(binary, profile)

    if not policy_result.get("ok"):
        return {
            "ok": False,
            "sandbox_id": sandbox_id,
            "message": policy_result.get("reason"),
            "policy": {
                "profile": profile.get("name"),
                "filesystem": profile.get("filesystem"),
                "network": profile.get("network"),
            },
        }

    timeout = int(profile.get("timeout_seconds") or 20)
    max_stdout = int(profile.get("max_stdout_bytes") or 200000)
    max_stderr = int(profile.get("max_stderr_bytes") or 200000)
    env = build_sandbox_env(profile)

    policy_snapshot = {
        "profile": profile.get("name"),
        "timeout_seconds": timeout,
        "max_stdout_bytes": max_stdout,
        "max_stderr_bytes": max_stderr,
        "filesystem": profile.get("filesystem"),
        "network": profile.get("network"),
        "allowed_binaries": profile.get("allowed_binaries"),
    }

    (workdir / "policy.json").write_text(
        json.dumps(policy_snapshot, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    try:
        result = subprocess.run(
            cmd,
            cwd=str(workdir),
            capture_output=True,
            text=True,
            timeout=timeout,
            env=env,
        )
        stdout = _clip(result.stdout, max_stdout)
        stderr = _clip(result.stderr, max_stderr)

        (workdir / "stdout.txt").write_text(stdout, encoding="utf-8")
        (workdir / "stderr.txt").write_text(stderr, encoding="utf-8")

        return {
            "ok": True,
            "sandbox_id": sandbox_id,
            "returncode": result.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "policy": policy_snapshot,
        }
    except subprocess.TimeoutExpired as e:
        return {
            "ok": False,
            "sandbox_id": sandbox_id,
            "message": f"command timeout after {timeout}s",
            "stdout": _clip(e.stdout.decode("utf-8", errors="replace") if isinstance(e.stdout, bytes) else e.stdout, max_stdout),
            "stderr": _clip(e.stderr.decode("utf-8", errors="replace") if isinstance(e.stderr, bytes) else e.stderr, max_stderr),
            "policy": policy_snapshot,
        }
    except Exception as e:
        return {
            "ok": False,
            "sandbox_id": sandbox_id,
            "message": str(e),
            "policy": policy_snapshot,
        }