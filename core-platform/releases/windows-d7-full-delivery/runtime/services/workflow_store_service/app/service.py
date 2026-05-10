"""Business logic layer for workflow store service."""

from datetime import datetime
from typing import Dict, List, Any, Optional

from .models import (
    WorkflowRecord,
    RegisterWorkflowRequest,
    ImportWorkflowRequest,
    WorkflowDefinition,
    ValidationResult,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_workflow_id,
)
from .validation import validate_workflow


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def register_workflow(req: RegisterWorkflowRequest) -> WorkflowRecord:
    """Register a new workflow."""
    validation = validate_workflow(req)
    if not validation.ok:
        raise ValueError(validation.model_dump_json())

    store = load_store()
    wid = make_workflow_id(req.name, req.version)
    ts = now_ts()

    # Check for duplicates
    for existing in store.items:
        if existing.id == wid:
            # Update existing workflow
            existing.definition = WorkflowDefinition.model_validate(req.model_dump())
            existing.description = req.description
            existing.source = req.source
            existing.updated_at = ts
            save_store(store)
            append_event("update_workflow", {"id": wid, "name": req.name, "version": req.version})
            return existing

    # Create new workflow
    record = WorkflowRecord(
        id=wid,
        name=req.name,
        version=req.version,
        description=req.description,
        source=req.source,
        enabled=True,
        definition=WorkflowDefinition.model_validate(req.model_dump()),
        created_at=ts,
        updated_at=ts,
    )

    store.items.append(record)
    save_store(store)
    append_event("register_workflow", {"id": wid, "name": req.name, "version": req.version})
    return record


def import_workflow(req: ImportWorkflowRequest) -> WorkflowRecord:
    """Import workflow from JSON."""
    defn = WorkflowDefinition.model_validate(req.workflow_json)
    register_req = RegisterWorkflowRequest.model_validate(
        {
            **req.workflow_json,
            "nodes": defn.nodes,
            "edges": defn.edges,
            "runtime_requirements": defn.runtime_requirements,
        }
    )
    return register_workflow(register_req)


def list_workflows() -> List[WorkflowRecord]:
    """List all workflows."""
    store = load_store()
    return store.items


def get_workflow(workflow_id: str) -> Optional[WorkflowRecord]:
    """Get workflow by ID."""
    store = load_store()
    for record in store.items:
        if record.id == workflow_id:
            return record
    return None


def export_workflow(workflow_id: str) -> Optional[Dict[str, Any]]:
    """Export workflow as JSON."""
    record = get_workflow(workflow_id)
    if not record:
        return None

    return {
        "id": record.id,
        "name": record.name,
        "version": record.version,
        "description": record.description,
        "source": record.source,
        "enabled": record.enabled,
        "definition": record.definition.model_dump(),
        "created_at": record.created_at,
        "updated_at": record.updated_at,
    }


def dry_run(workflow_id: str, input_context: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Generate dry run execution plan."""
    record = get_workflow(workflow_id)
    if not record:
        return None

    defn = record.definition

    # Build execution plan
    steps = []

    # Find start node
    start_nodes = [n for n in defn.nodes if n.type == "start"]
    if not start_nodes:
        return None

    # Simple BFS to traverse graph
    visited = set()
    queue = [(start_nodes[0].id, None)]

    while queue:
        node_id, from_edge = queue.pop(0)
        if node_id in visited:
            continue
        visited.add(node_id)

        node = next((n for n in defn.nodes if n.id == node_id), None)
        if not node:
            continue

        steps.append({
            "step": len(steps),
            "node_id": node.id,
            "node_type": node.type,
            "node_name": node.name,
            "from_edge": from_edge,
            "config": node.config,
        })

        # Find outgoing edges
        for edge in defn.edges:
            if edge.source == node_id:
                queue.append((edge.target, edge.id))

    return {
        "workflow_id": workflow_id,
        "input_context": input_context,
        "steps": steps,
        "total_steps": len(steps),
    }


def validate_definition(defn: WorkflowDefinition) -> ValidationResult:
    """Validate workflow definition."""
    return validate_workflow(defn)


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)
