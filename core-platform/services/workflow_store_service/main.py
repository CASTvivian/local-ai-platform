"""FastAPI main application for workflow store service."""

import sys
import os
from pathlib import Path

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ValidationError

from services.workflow_store_service.app.models import (
    RegisterWorkflowRequest,
    ImportWorkflowRequest,
    DryRunRequest,
    WorkflowDefinition,
    ValidationResult,
)
from services.workflow_store_service.app.storage import (
    load_store,
    make_workflow_id,
    append_error,
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.workflow_store_service.app.service import (
    register_workflow,
    import_workflow,
    list_workflows,
    get_workflow,
    export_workflow,
    dry_run,
    validate_definition,
    get_recent_events,
)


app = FastAPI(title="Workflow Store Service", version="0.3.1-enterprise")


def ok(data=None, **extra):
    """Return success response."""
    return {"ok": True, **(data or {}), **extra}


def fail(where: str, err: Exception):
    """Return error response."""
    append_error(where, str(err), {"type": type(err).__name__})
    return {"ok": False, "where": where, "error": str(err), "type": type(err).__name__}


@app.get("/health")
def health():
    """Health check endpoint."""
    store = load_store()
    return {
        "ok": True,
        "service": "workflow_store_service",
        "version": "0.3.1-enterprise",
        "store_version": store.store_version,
        "count": len(store.items),
    }


@app.get("/debug/storage")
def debug_storage():
    """Debug storage paths."""
    return {
        "ok": True,
        "base_dir": str(BASE_DIR),
        "data_dir": str(DATA_DIR),
        "store_path": str(STORE_PATH),
        "store_exists": STORE_PATH.exists(),
        "store_size": STORE_PATH.stat().st_size if STORE_PATH.exists() else 0,
    }


@app.get("/list")
def list_workflows_endpoint():
    """List all workflows."""
    try:
        items = list_workflows()
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list_workflows", e))


@app.post("/register")
def register_workflow_endpoint(req: RegisterWorkflowRequest):
    """Register a new workflow."""
    try:
        record = register_workflow(req)
        return ok(record.model_dump())
    except ValueError as e:
        # Validation error
        return JSONResponse(status_code=400, content=fail("register_workflow", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_workflow", e))


@app.post("/import")
def import_workflow_endpoint(req: ImportWorkflowRequest):
    """Import workflow from JSON."""
    try:
        record = import_workflow(req)
        return ok(record.model_dump())
    except ValidationError as e:
        return JSONResponse(status_code=400, content=fail("import_workflow", e))
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("import_workflow", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("import_workflow", e))


@app.get("/get/{workflow_id}")
def get_workflow_endpoint(workflow_id: str):
    """Get workflow details by ID."""
    try:
        record = get_workflow(workflow_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "workflow not found"})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("get_workflow", e))


@app.get("/export/{workflow_id}")
def export_workflow_endpoint(workflow_id: str):
    """Export workflow as JSON."""
    try:
        data = export_workflow(workflow_id)
        if not data:
            return JSONResponse(status_code=404, content={"ok": False, "error": "workflow not found"})
        return ok(data)
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("export_workflow", e))


@app.post("/validate")
def validate_workflow_endpoint(defn: WorkflowDefinition):
    """Validate workflow definition."""
    try:
        result = validate_definition(defn)
        return ok(result.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("validate_workflow", e))


@app.post("/dry_run")
def dry_run_endpoint(req: DryRunRequest):
    """Generate dry run execution plan."""
    try:
        result = dry_run(req.workflow_id, req.input_context)
        if not result:
            return JSONResponse(status_code=404, content={"ok": False, "error": "workflow not found"})
        return ok(result)
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("dry_run", e))


@app.get("/recent")
def recent_events_endpoint(limit: int = 50):
    """Get recent events."""
    try:
        events = get_recent_events(limit)
        return ok({"events": events, "count": len(events)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("recent_events", e))
