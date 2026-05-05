"""Business logic layer for artifact registry service."""

from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict, Any

from .models import (
    ArtifactRecord,
    StoreFile,
    RegisterExecutionResultRequest,
    UpdateLifecycleRequest,
    Lifecycle,
    ArtifactType,
    FileStatus,
    DownloadInfo,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_artifact_id,
    BASE_DIR,
)
from .validation import (
    validate_artifact_record,
    validate_register_request,
    validate_lifecycle_transition,
)


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def register_execution_result(req: RegisterExecutionResultRequest) -> ArtifactRecord:
    """Register a new execution result artifact."""
    # Validate request
    errors = validate_register_request(req)
    if errors:
        raise ValueError(f"Validation errors: {', '.join(errors)}")

    store = load_store()

    # Extract name from request
    name = req.name or req.title or req.payload.get("title") or "execution-result"
    run_id = req.run_id or req.trace_id or make_artifact_id(name)

    # Generate artifact ID
    artifact_id = make_artifact_id(name, run_id)
    ts = now_ts()

    # Create artifact record
    record = ArtifactRecord(
        id=artifact_id,
        name=name,
        source=req.source,
        version=req.version,
        enabled=True,
        type=req.type,
        path=req.path,
        lifecycle=req.lifecycle,
        trace_id=req.trace_id,
        run_id=run_id,
        payload=req.payload,
        created_at=ts,
        updated_at=ts,
    )

    # Validate record
    record_errors = validate_artifact_record(record)
    if record_errors:
        raise ValueError(f"Record validation errors: {', '.join(record_errors)}")

    # Store record
    store.items.append(record)
    save_store(store)
    append_event("register_execution_result", {"id": artifact_id, "name": name, "run_id": run_id})

    return record


def list_artifacts(enabled: Optional[bool] = None, lifecycle: Optional[Lifecycle] = None) -> List[ArtifactRecord]:
    """List artifacts with optional filtering."""
    store = load_store()
    items = store.items

    # Filter by enabled status
    if enabled is not None:
        items = [x for x in items if x.enabled == enabled]

    # Filter by lifecycle
    if lifecycle is not None:
        items = [x for x in items if x.lifecycle == lifecycle]

    return items


def get_artifact(artifact_id: str) -> Optional[ArtifactRecord]:
    """Get artifact by ID."""
    store = load_store()
    for record in store.items:
        if record.id == artifact_id:
            return record
    return None


def get_artifact_file_status(artifact_id: str) -> Optional[FileStatus]:
    """Get file status for an artifact."""
    record = get_artifact(artifact_id)
    if not record:
        return None

    path = record.path or record.payload.get("path", "")
    exists = False
    size = 0

    if path:
        try:
            p = Path(path)
            exists = p.exists() and p.is_file()
            size = p.stat().st_size if exists else 0
        except Exception:
            exists = False

    return FileStatus(
        path=path,
        exists=exists,
        size_bytes=size,
        download_ready=exists,
        note="P3.14-C3 reports file status. System open/download will be connected through Tauri command later.",
    )


def get_download_info(artifact_id: str) -> Optional[DownloadInfo]:
    """Get download information for an artifact."""
    record = get_artifact(artifact_id)
    if not record:
        return None

    path = record.path or record.payload.get("path", "")
    exists = False
    size = 0

    if path:
        try:
            p = Path(path)
            exists = p.exists() and p.is_file()
            size = p.stat().st_size if exists else 0
        except Exception:
            exists = False

    return DownloadInfo(
        item_id=artifact_id,
        path=path,
        exists=exists,
        size_bytes=size,
        download_ready=exists,
        message="P3.14-C3 placeholder: file status is ready; real open/download will be connected through Tauri command later.",
    )


def update_artifact_lifecycle(artifact_id: str, req: UpdateLifecycleRequest) -> Optional[ArtifactRecord]:
    """Update artifact lifecycle."""
    store = load_store()

    for record in store.items:
        if record.id == artifact_id:
            # Validate transition
            if not validate_lifecycle_transition(record.lifecycle, req.lifecycle):
                raise ValueError(
                    f"Invalid lifecycle transition: {record.lifecycle} -> {req.lifecycle}"
                )

            # Update lifecycle
            record.lifecycle = req.lifecycle
            record.updated_at = now_ts()

            # Update enabled status based on lifecycle
            if req.lifecycle == Lifecycle.deleted:
                record.enabled = False
            elif req.lifecycle in {Lifecycle.active, Lifecycle.draft}:
                record.enabled = True

            save_store(store)
            append_event(
                "update_lifecycle",
                {
                    "id": artifact_id,
                    "from": str(record.lifecycle),
                    "to": str(req.lifecycle),
                    "reason": req.reason,
                }
            )

            return record

    return None


def disable_artifact(artifact_id: str) -> Optional[ArtifactRecord]:
    """Disable an artifact by ID."""
    store = load_store()

    for record in store.items:
        if record.id == artifact_id:
            record.enabled = False
            record.updated_at = now_ts()
            save_store(store)
            append_event("disable_artifact", {"id": artifact_id})
            return record

    return None


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)


def get_health_info() -> Dict[str, Any]:
    """Get health information."""
    store = load_store()
    return {
        "service": "artifact_registry_service",
        "version": "0.3.1-enterprise",
        "kind": "artifact_registry",
        "description": "文件产物索引、下载、生命周期、类型和来源记录。",
        "store_version": store.store_version,
        "count": len(store.items),
    }
