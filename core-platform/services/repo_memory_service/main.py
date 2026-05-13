"""FastAPI main application for repo memory service."""

import sys
from pathlib import Path
from typing import Optional

# Add services directory to path
SERVICE_DIR = Path(__file__).parent
sys.path.insert(0, str(SERVICE_DIR.parent.parent))

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from services.repo_memory_service.app.models import (
    RepoRecord,
    FixRecord,
    ContextSnapshot,
    KnowledgeEntry,
    RegisterRepoRequest,
    RecordFixRequest,
    SnapshotContextRequest,
    AddKnowledgeRequest,
    SearchKnowledgeRequest,
)
from services.repo_memory_service.app.storage import (
    resolve_core_platform_dir,
    BASE_DIR,
    DATA_DIR,
    STORE_PATH,
)
from services.repo_memory_service.app.service import (
    register_repo,
    get_repo,
    list_repos,
    record_fix,
    list_fixes,
    snapshot_context,
    compress_context,
    add_knowledge,
    search_knowledge,
    get_brain_asset_catalog,
    seed_brain_assets,
    search_brain_assets,
    get_recent_events,
    get_health_info,
)


app = FastAPI(title="Repo Memory Service", version="0.3.1-enterprise")

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
    from services.repo_memory_service.app.storage import append_error
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


@app.get("/repo/list")
def list_repos_endpoint():
    """List all repositories."""
    try:
        items = list_repos()
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list_repos", e))


@app.get("/repo/{repo_id}")
def get_repo_endpoint(repo_id: str):
    """Get repository by ID."""
    try:
        record = get_repo(repo_id)
        if not record:
            return JSONResponse(status_code=404, content={"ok": False, "error": "repo_not_found", "repo_id": repo_id})
        return ok(record.model_dump())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("get_repo", e))


@app.post("/repo/register")
def register_repo_endpoint(req: RegisterRepoRequest):
    """Register a new repository."""
    try:
        record = register_repo(req)
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("register_repo", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("register_repo", e))


@app.get("/fix/list")
def list_fixes_endpoint(repo_id: Optional[str] = None):
    """List fix history, optionally filtered by repo."""
    try:
        items = list_fixes(repo_id)
        return ok({"items": [r.model_dump() for r in items], "count": len(items)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("list_fixes", e))


@app.post("/fix/record")
def record_fix_endpoint(req: RecordFixRequest):
    """Record a fix history."""
    try:
        record = record_fix(req)
        return ok(record.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("record_fix", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("record_fix", e))


@app.post("/context/snapshot")
def snapshot_context_endpoint(req: SnapshotContextRequest):
    """Create context snapshot."""
    try:
        snapshot = snapshot_context(req)
        return ok(snapshot.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("snapshot_context", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("snapshot_context", e))


@app.get("/context/compress/{repo_id}")
def compress_context_endpoint(repo_id: str):
    """Generate compressed context summary."""
    try:
        compressed = compress_context(repo_id)
        return ok(compressed)
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("compress_context", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("compress_context", e))


@app.post("/knowledge/add")
def add_knowledge_endpoint(req: AddKnowledgeRequest):
    """Add knowledge entry."""
    try:
        entry = add_knowledge(req)
        return ok(entry.model_dump())
    except ValueError as e:
        return JSONResponse(status_code=400, content=fail("add_knowledge", e))
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("add_knowledge", e))


@app.post("/knowledge/search")
def search_knowledge_endpoint(req: SearchKnowledgeRequest):
    """Search knowledge base."""
    try:
        results = search_knowledge(req)
        return ok({"items": [r.model_dump() for r in results], "count": len(results)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("search_knowledge", e))


@app.get("/brain/assets")
def brain_assets_endpoint():
    """Return the current brain asset catalog summary."""
    try:
        return ok(get_brain_asset_catalog())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("brain_assets", e))


@app.post("/brain/seed")
def seed_brain_assets_endpoint():
    """Seed summarized brain assets into repo memory."""
    try:
        return ok(seed_brain_assets())
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("seed_brain_assets", e))


@app.post("/brain/search")
def search_brain_assets_endpoint(req: SearchKnowledgeRequest):
    """Search brain asset knowledge entries."""
    try:
        results = search_brain_assets(req)
        return ok({"items": [r.model_dump() for r in results], "count": len(results)})
    except Exception as e:
        return JSONResponse(status_code=500, content=fail("search_brain_assets", e))


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
    uvicorn.run(app, host="0.0.0.0", port=18125)
