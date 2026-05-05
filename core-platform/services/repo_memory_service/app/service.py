"""Business logic layer for repo memory service."""

from datetime import datetime
from typing import List, Optional, Dict, Any

from .models import (
    RepoRecord,
    FixRecord,
    ContextSnapshot,
    KnowledgeEntry,
    StoreFile,
    RegisterRepoRequest,
    RecordFixRequest,
    SnapshotContextRequest,
    AddKnowledgeRequest,
    SearchKnowledgeRequest,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_repo_id,
    make_fix_id,
    make_snapshot_id,
    make_knowledge_id,
    BASE_DIR,
)
from .validation import (
    validate_repo_name,
    validate_repo_path,
    validate_fix_record,
    validate_context_snapshot,
    validate_knowledge_entry,
)


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def register_repo(req: RegisterRepoRequest) -> RepoRecord:
    """Register a new repository."""
    # Validate name
    name_errors = validate_repo_name(req.name)
    if name_errors:
        raise ValueError(f"Invalid repo name: {', '.join(name_errors)}")

    # Validate path
    path_errors = validate_repo_path(req.path)
    if path_errors:
        raise ValueError(f"Invalid repo path: {', '.join(path_errors)}")

    # Generate repo ID
    repo_id = make_repo_id(req.name)
    ts = now_ts()

    # Create repo record
    record = RepoRecord(
        id=repo_id,
        name=req.name,
        path=req.path,
        description=req.description,
        tags=req.tags,
        services=req.services,
        created_at=ts,
        updated_at=ts,
    )

    # Check for duplicates
    store = load_store()
    for existing in store.repos:
        if existing.name == record.name:
            raise ValueError(f"Repo {record.name} already exists")

    # Store record
    store.repos.append(record)
    save_store(store)
    append_event("register_repo", {"id": repo_id, "name": req.name})

    return record


def get_repo(repo_id: str) -> Optional[RepoRecord]:
    """Get repository by ID."""
    store = load_store()
    for record in store.repos:
        if record.id == repo_id:
            return record
    return None


def list_repos() -> List[RepoRecord]:
    """List all repositories."""
    store = load_store()
    return store.repos


def record_fix(req: RecordFixRequest) -> FixRecord:
    """Record a fix history."""
    fix_id = make_fix_id()
    ts = now_ts()

    # Create fix record
    record = FixRecord(
        id=fix_id,
        repo_id=req.repo_id,
        title=req.title,
        problem=req.problem,
        solution=req.solution,
        files_changed=req.files_changed,
        commands_run=req.commands_run,
        tests_run=req.tests_run,
        result=req.result,
        commit_hash=req.commit_hash,
        created_at=ts,
    )

    # Validate
    errors = validate_fix_record(record)
    if errors:
        raise ValueError(f"Invalid fix record: {', '.join(errors)}")

    # Store record
    store = load_store()
    store.fixes.append(record)
    save_store(store)
    append_event("record_fix", {"id": fix_id, "repo_id": req.repo_id, "title": req.title})

    return record


def list_fixes(repo_id: Optional[str] = None) -> List[FixRecord]:
    """List fix history, optionally filtered by repo."""
    store = load_store()
    fixes = store.fixes

    if repo_id:
        fixes = [f for f in fixes if f.repo_id == repo_id]

    return fixes


def snapshot_context(req: SnapshotContextRequest) -> ContextSnapshot:
    """Create context snapshot."""
    snapshot_id = make_snapshot_id()
    ts = now_ts()

    # Create snapshot
    snapshot = ContextSnapshot(
        id=snapshot_id,
        repo_id=req.repo_id,
        title=req.title,
        summary=req.summary,
        files=req.files,
        services=req.services,
        tokens_estimate=req.tokens_estimate,
        created_at=ts,
    )

    # Validate
    errors = validate_context_snapshot(snapshot)
    if errors:
        raise ValueError(f"Invalid context snapshot: {', '.join(errors)}")

    # Store snapshot
    store = load_store()
    store.snapshots.append(snapshot)
    save_store(store)
    append_event("snapshot_context", {"id": snapshot_id, "repo_id": req.repo_id, "title": req.title})

    return snapshot


def compress_context(repo_id: str) -> Dict[str, Any]:
    """Generate compressed context summary."""
    store = load_store()

    # Get repo info
    repo = next((r for r in store.repos if r.id == repo_id), None)
    if not repo:
        raise ValueError(f"Repo not found: {repo_id}")

    # Get related snapshots
    snapshots = [s for s in store.snapshots if s.repo_id == repo_id]

    # Get related fixes
    fixes = [f for f in store.fixes if f.repo_id == repo_id]

    # Get related knowledge
    knowledge = [k for k in store.knowledge if k.repo_id == repo_id]

    # Compress summary
    total_tokens = sum(s.tokens_estimate for s in snapshots)
    avg_tokens = total_tokens / len(snapshots) if snapshots else 0

    return {
        "repo_id": repo_id,
        "repo_name": repo.name,
        "description": repo.description,
        "tags": repo.tags,
        "services": repo.services,
        "snapshots_count": len(snapshots),
        "fixes_count": len(fixes),
        "knowledge_count": len(knowledge),
        "total_tokens_estimate": total_tokens,
        "average_tokens_estimate": avg_tokens,
        "compressed_summary": f"Repo {repo.name} with {len(snapshots)} snapshots, {len(fixes)} fixes, and {len(knowledge)} knowledge entries. Avg {int(avg_tokens)} tokens per snapshot.",
    }


def add_knowledge(req: AddKnowledgeRequest) -> KnowledgeEntry:
    """Add knowledge entry."""
    knowledge_id = make_knowledge_id()
    ts = now_ts()

    # Create knowledge entry
    entry = KnowledgeEntry(
        id=knowledge_id,
        repo_id=req.repo_id,
        category=req.category,
        title=req.title,
        content=req.content,
        tags=req.tags,
        source=req.source,
        created_at=ts,
    )

    # Validate
    errors = validate_knowledge_entry(entry)
    if errors:
        raise ValueError(f"Invalid knowledge entry: {', '.join(errors)}")

    # Store entry
    store = load_store()
    store.knowledge.append(entry)
    save_store(store)
    append_event("add_knowledge", {"id": knowledge_id, "repo_id": req.repo_id, "title": req.title})

    return entry


def search_knowledge(req: SearchKnowledgeRequest) -> List[KnowledgeEntry]:
    """Search knowledge base."""
    store = load_store()
    knowledge = store.knowledge

    # Filter by repo
    if req.repo_id:
        knowledge = [k for k in knowledge if k.repo_id == req.repo_id]

    # Filter by category
    if req.category:
        knowledge = [k for k in knowledge if k.category == req.category]

    # Search by query
    query_lower = req.query.lower()
    results = []
    for entry in knowledge:
        # Search in title, content, and tags
        if (
            query_lower in entry.title.lower()
            or query_lower in entry.content.lower()
            or any(query_lower in tag.lower() for tag in entry.tags)
        ):
            results.append(entry)

    # Limit results
    return results[: req.limit]


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)


def get_health_info() -> Dict[str, Any]:
    """Get health information."""
    store = load_store()
    return {
        "service": "repo_memory_service",
        "version": "0.3.1-enterprise",
        "kind": "repo_memory",
        "description": "repo map、历史修复、上下文压缩、项目记忆。",
        "store_version": store.store_version,
        "repos_count": len(store.repos),
        "fixes_count": len(store.fixes),
        "snapshots_count": len(store.snapshots),
        "knowledge_count": len(store.knowledge),
    }
