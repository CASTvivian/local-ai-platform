"""FastAPI main application for code review gate service."""

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

from services.code_review_gate_service.app.models import (
    ReviewResult,
    ReviewRequest,
    SuggestTestsRequest,
)
from services.code_review_gate_service.app.storage import (
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.code_review_gate_service.app.service import (
    review_diff,
    suggest_tests,
    get_review_summary,
    get_recent_events,
    get_health_info,
)
from services.code_review_gate_service.app.rules import get_default_rules


app = FastAPI(title="Code Review Gate Service", version="0.3.1-enterprise")

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
    from services.code_review_gate_service.app.storage import append_error
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


@app.post("/review_diff")
def review_diff_endpoint(req: ReviewRequest):
    """Review code diff for security issues."""
    try:
        result = review_diff(req)
        return ok(result.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("review_diff", e))


@app.post("/suggest_tests")
def suggest_tests_endpoint(req: SuggestTestsRequest):
    """Suggest tests for code."""
    try:
        suggestions = suggest_tests(req)
        return ok({"suggestions": [s.model_dump() for s in suggestions], "count": len(suggestions)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("suggest_tests", e))


@app.get("/summary")
def summary_endpoint():
    """Get review summary statistics."""
    try:
        summary = get_review_summary()
        return ok(summary.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("summary", e))


@app.get("/recent")
def recent_events_endpoint(limit: int = 50):
    """Get recent events."""
    try:
        events = get_recent_events(limit)
        return ok({"events": events, "count": len(events)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("recent_events", e))


@app.get("/rules")
def get_rules_endpoint():
    """Get default security rules."""
    return ok({"rules": get_default_rules()})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=18124)
