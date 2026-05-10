"""FastAPI main application for design system service."""

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

from services.design_system_service.app.models import (
    DesignSystem,
    ParsedDesignMd,
    RegisterDesignSystemRequest,
    ParseDesignMdRequest,
    RegisterBrandProfileRequest,
    AddDesignTokenRequest,
    RegisterComponentSpecRequest,
    SuggestUiConstraintsRequest,
    ComponentType,
)
from services.design_system_service.app.storage import (
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.design_system_service.app.service import (
    register_design_system,
    parse_design_md,
    list_design_systems,
    get_design_system,
    register_brand_profile,
    add_design_token,
    register_component_spec,
    export_design_system,
    suggest_ui_constraints,
    get_recent_events,
    get_health_info,
)


app = FastAPI(title="Design System Service", version="0.3.1-enterprise")

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
    from services.design_system_service.app.storage import append_error
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
def list_design_systems_endpoint():
    """List all design systems."""
    try:
        items = list_design_systems()
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list", e))


@app.post("/register")
def register_design_system_endpoint(req: RegisterDesignSystemRequest):
    """Register a new design system."""
    try:
        record = register_design_system(req)
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("register_design_system", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_design_system", e))


@app.get("/design/{design_system_id}")
def get_design_system_endpoint(design_system_id: str):
    """Get design system by ID."""
    try:
        record = get_design_system(design_system_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "design_system_not_found", "design_system_id": design_system_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("get_design_system", e))


@app.post("/parse_design_md")
def parse_design_md_endpoint(req: ParseDesignMdRequest):
    """Parse DESIGN.md content."""
    try:
        parsed = parse_design_md(req)
        return ok(parsed.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("parse_design_md", e))


@app.get("/export/{design_system_id}")
def export_design_system_endpoint(design_system_id: str):
    """Export design system as tokens and components."""
    try:
        data = export_design_system(design_system_id)
        if not data:
            return JSONResponse(status_code=404, content={"ok": False, "error": "design_system_not_found", "design_system_id": design_system_id})
        return ok(data)
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("export_design_system", e))


@app.post("/suggest_ui")
def suggest_ui_constraints_endpoint(req: SuggestUiConstraintsRequest):
    """Suggest UI constraints."""
    try:
        suggestions = suggest_ui_constraints(req)
        return ok(suggestions)
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("suggest_ui", e))


@app.post("/brand/register")
def register_brand_profile_endpoint(req: RegisterBrandProfileRequest):
    """Register brand profile."""
    try:
        profile = register_brand_profile(req)
        return ok(profile.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("register_brand_profile", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_brand_profile", e))


@app.post("/token/add")
def add_design_token_endpoint(req: AddDesignTokenRequest):
    """Add design token."""
    try:
        token = add_design_token(req)
        return ok(token.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("add_design_token", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("add_design_token", e))


@app.post("/component/register")
def register_component_spec_endpoint(req: RegisterComponentSpecRequest):
    """Register component specification."""
    try:
        spec = register_component_spec(req)
        return ok(spec.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("register_component_spec", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_component_spec", e))


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
    uvicorn.run(app, host="0.0.0.0", port=18127)
