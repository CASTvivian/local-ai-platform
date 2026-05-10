"""FastAPI main application for skill store service."""

import sys
from pathlib import Path
from typing import Optional

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from services.skill_store_service.app.models import (
    SkillRecord,
    ParseSkillMdRequest,
    InstallSkillMdRequest,
    UpdateSkillRequest,
    EnableSkillRequest,
    SkillStatus,
)
from services.skill_store_service.app.storage import (
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.skill_store_service.app.service import (
    parse_skill_md,
    install_skill_md,
    list_skills,
    get_skill,
    enable_skill,
    disable_skill,
    update_skill,
    get_recent_events,
    get_health_info,
)


app = FastAPI(title="Skill Store Service", version="0.3.1-enterprise")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def ok(data=None, **extra):
    """Return success response."""
    return {"ok": True, **(data or {}), **extra}


def fail(where: str, err: Exception):
    """Return error response."""
    from services.skill_store_service.app.storage import append_error
    append_error(where, str(err), {"type": type(err).__name__})
    return {"ok": False, "where": where, "error": str(err), "type": type(err).__name__}


@app.get("/health")
def health():
    """Health check endpoint."""
    info = get_health_info()
    return ok(info)


@app.get("/debug/storage")
def debug_storage():
    """Debug storage paths."""
    return ok({
        "base_dir": str(BASE_DIR),
        "data_dir": str(DATA_DIR),
        "store_path": str(STORE_PATH),
        "store_exists": STORE_PATH.exists(),
        "store_size": STORE_PATH.stat().st_size if STORE_PATH.exists() else 0,
    })


@app.get("/list")
def list_items(enabled: bool | None = None, status: str | None = None):
    """List all skills with optional filtering."""
    try:
        # Convert status string to enum if provided
        st = None
        if status:
            try:
                st = SkillStatus(status)
            except ValueError:
                return JSONResponse(status_code=400, content=fail("list", ValueError(f"invalid status: {status}")))

        items = list_skills(enabled, st)
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list", e))


@app.post("/parse_skill_md")
def parse_skill_md_endpoint(req: ParseSkillMdRequest):
    """Parse SKILL.md content."""
    try:
        parsed = parse_skill_md(req)
        return ok(parsed.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("parse_skill_md", e))


@app.post("/install_skill_md")
def install_skill_md_endpoint(req: InstallSkillMdRequest):
    """Install a skill from SKILL.md content."""
    try:
        record = install_skill_md(req)
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("install_skill_md", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("install_skill_md", e))


@app.get("/skill/{skill_id}")
def get_skill_endpoint(skill_id: str):
    """Get skill details by ID."""
    try:
        record = get_skill(skill_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "skill_not_found", "skill_id": skill_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("get_skill", e))


@app.post("/enable/{skill_id}")
def enable_skill_endpoint(skill_id: str, req: Optional[EnableSkillRequest] = None):
    """Enable a skill."""
    try:
        record = enable_skill(skill_id, req)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "skill_not_found", "skill_id": skill_id})
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("enable_skill", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("enable_skill", e))


@app.post("/disable/{skill_id}")
def disable_skill_endpoint(skill_id: str):
    """Disable a skill."""
    try:
        record = disable_skill(skill_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "skill_not_found", "skill_id": skill_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("disable_skill", e))


@app.post("/skill/{skill_id}/update")
def update_skill_endpoint(skill_id: str, req: UpdateSkillRequest):
    """Update skill metadata."""
    try:
        record = update_skill(skill_id, req)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "skill_not_found", "skill_id": skill_id})
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("update_skill", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("update_skill", e))


@app.get("/recent")
def recent_events_endpoint(limit: int = 50):
    """Get recent events."""
    try:
        events = get_recent_events(limit)
        return ok({"events": events, "count": len(events)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("recent_events", e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18121)
