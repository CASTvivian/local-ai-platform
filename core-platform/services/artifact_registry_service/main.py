"""FastAPI main application for artifact registry service."""

import sys
from pathlib import Path

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from services.artifact_registry_service.app.models import (
    ArtifactRecord,
    RegisterExecutionResultRequest,
    UpdateLifecycleRequest,
    Lifecycle,
)
from services.artifact_registry_service.app.storage import (
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.artifact_registry_service.app.service import (
    register_execution_result,
    list_artifacts,
    get_artifact,
    get_artifact_file_status,
    get_download_info,
    update_artifact_lifecycle,
    disable_artifact,
    get_recent_events,
    get_health_info,
)


app = FastAPI(title="Artifact Registry Service", version="0.3.1-enterprise")

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
    from services.artifact_registry_service.app.storage import append_error
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
def list_items(enabled: bool | None = None, lifecycle: str | None = None):
    """List all artifacts with optional filtering."""
    try:
        # Convert lifecycle string to enum if provided
        lc = None
        if lifecycle:
            try:
                lc = Lifecycle(lifecycle)
            except ValueError:
                return JSONResponse(status_code=400, content=fail("list", ValueError(f"invalid lifecycle: {lifecycle}")))

        items = list_artifacts(enabled, lc)
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list", e))


@app.post("/register_execution_result")
def register_execution_result_endpoint(req: RegisterExecutionResultRequest):
    """Register a new execution result artifact."""
    try:
        record = register_execution_result(req)
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("register_execution_result", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_execution_result", e))


@app.get("/artifact/{artifact_id}")
def get_artifact_endpoint(artifact_id: str):
    """Get artifact details by ID."""
    try:
        record = get_artifact(artifact_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "artifact_not_found", "artifact_id": artifact_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("get_artifact", e))


@app.get("/artifact/{artifact_id}/file_status")
def get_file_status_endpoint(artifact_id: str):
    """Get file status for an artifact."""
    try:
        status = get_artifact_file_status(artifact_id)
        if not status:
            return JSONResponse(status_code=404, content={"ok": False, "error": "artifact_not_found", "artifact_id": artifact_id})
        return ok(status.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("file_status", e))


@app.get("/download/{artifact_id}")
def download_endpoint(artifact_id: str):
    """Get download information for an artifact."""
    try:
        info = get_download_info(artifact_id)
        if not info:
            return JSONResponse(status_code=404, content={"ok": False, "error": "artifact_not_found", "artifact_id": artifact_id})
        return ok(info.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("download", e))


@app.post("/artifact/{artifact_id}/lifecycle")
def update_lifecycle_endpoint(artifact_id: str, req: UpdateLifecycleRequest):
    """Update artifact lifecycle."""
    try:
        record = update_artifact_lifecycle(artifact_id, req)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "artifact_not_found", "artifact_id": artifact_id})
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("update_lifecycle", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("update_lifecycle", e))


@app.post("/disable/{artifact_id}")
def disable_endpoint(artifact_id: str):
    """Disable an artifact by ID."""
    try:
        record = disable_artifact(artifact_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "artifact_not_found", "artifact_id": artifact_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("disable", e))


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
    uvicorn.run(app, host="0.0.0.0", port=18123)
