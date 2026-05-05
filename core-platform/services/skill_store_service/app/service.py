"""Business logic layer for skill store service."""

from datetime import datetime
from typing import List, Optional, Dict, Any

from .models import (
    SkillRecord,
    StoreFile,
    ParseSkillMdRequest,
    InstallSkillMdRequest,
    UpdateSkillRequest,
    EnableSkillRequest,
    SkillSource,
    SignatureStatus,
    SkillStatus,
    AgentBinding,
    ParsedSkillMd,
    SkillInstallResponse,
    SkillEnableResponse,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_skill_id,
    BASE_DIR,
)
from .parser import parse_skill_md_text, validate_skill_md_text
from .validation import (
    validate_skill_record,
    validate_skill_name,
    validate_version,
    validate_agent_bindings,
)


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def parse_skill_md(req: ParseSkillMdRequest) -> ParsedSkillMd:
    """Parse SKILL.md content into structured data."""
    parsed = parse_skill_md_text(req.text)
    return ParsedSkillMd(**parsed)


def install_skill_md(req: InstallSkillMdRequest) -> SkillRecord:
    """Install a skill from SKILL.md content."""
    # Parse the markdown
    parsed = parse_skill_md_text(req.text)

    # Validate parsed data
    name_errors = validate_skill_name(parsed["name"])
    version_errors = validate_version(parsed["version"])
    
    if name_errors:
        raise ValueError(f"Invalid skill name: {', '.join(name_errors)}")
    if version_errors:
        raise ValueError(f"Invalid version: {', '.join(version_errors)}")

    # Validate agent bindings
    if req.agent_bindings:
        binding_errors = validate_agent_bindings(req.agent_bindings)
        if binding_errors:
            raise ValueError(f"Invalid agent bindings: {', '.join(binding_errors)}")

    # Generate skill ID
    skill_id = make_skill_id(parsed["name"])
    ts = now_ts()

    # Create skill record
    record = SkillRecord(
        id=skill_id,
        name=parsed["name"],
        description=parsed["description"],
        source=req.source,
        version=parsed["version"],
        enabled=True,
        status=SkillStatus.active,
        signature_status=SignatureStatus.unsigned,
        agents=parsed.get("agents", []),
        tags=parsed.get("tags", []),
        agent_bindings=req.agent_bindings or [],
        payload={
            **parsed,
            "raw": req.text,
            "signature": req.signature or "",
            "install_mode": "skill_md_text",
        },
        created_at=ts,
        updated_at=ts,
    )

    # Validate complete record
    record_errors = validate_skill_record(record)
    if record_errors:
        raise ValueError(f"Record validation errors: {', '.join(record_errors)}")

    # Check for duplicates (same name + version)
    store = load_store()
    for existing in store.items:
        if existing.name == record.name and existing.version == record.version:
            raise ValueError(f"Skill {record.name} v{record.version} already exists")

    # Store record
    store.items.append(record)
    save_store(store)
    append_event("install_skill_md", {"id": skill_id, "name": parsed["name"], "version": parsed["version"]})

    return record


def list_skills(enabled: Optional[bool] = None, status: Optional[SkillStatus] = None) -> List[SkillRecord]:
    """List skills with optional filtering."""
    store = load_store()
    items = store.items

    # Filter by enabled status
    if enabled is not None:
        items = [x for x in items if x.enabled == enabled]

    # Filter by status
    if status is not None:
        items = [x for x in items if x.status == status]

    return items


def get_skill(skill_id: str) -> Optional[SkillRecord]:
    """Get skill by ID."""
    store = load_store()
    for record in store.items:
        if record.id == skill_id:
            return record
    return None


def enable_skill(skill_id: str, req: Optional[EnableSkillRequest] = None) -> Optional[SkillRecord]:
    """Enable a skill."""
    store = load_store()

    for record in store.items:
        if record.id == skill_id:
            record.enabled = True
            record.status = SkillStatus.active
            record.updated_at = now_ts()

            # Update agent bindings if provided
            if req and req.agent_bindings:
                binding_errors = validate_agent_bindings(req.agent_bindings)
                if binding_errors:
                    raise ValueError(f"Invalid agent bindings: {', '.join(binding_errors)}")
                record.agent_bindings = req.agent_bindings

            save_store(store)
            append_event("enable_skill", {"id": skill_id, "name": record.name})
            return record

    return None


def disable_skill(skill_id: str) -> Optional[SkillRecord]:
    """Disable a skill."""
    store = load_store()

    for record in store.items:
        if record.id == skill_id:
            record.enabled = False
            record.status = SkillStatus.disabled
            record.updated_at = now_ts()
            save_store(store)
            append_event("disable_skill", {"id": skill_id, "name": record.name})
            return record

    return None


def update_skill(skill_id: str, req: UpdateSkillRequest) -> Optional[SkillRecord]:
    """Update skill metadata."""
    store = load_store()

    for record in store.items:
        if record.id == skill_id:
            if req.description is not None:
                record.description = req.description
            if req.tags is not None:
                record.tags = req.tags
            if req.status is not None:
                record.status = req.status

            # Update enabled flag based on status
            if req.status == SkillStatus.disabled:
                record.enabled = False
            elif req.status == SkillStatus.active:
                record.enabled = True

            record.updated_at = now_ts()
            save_store(store)
            append_event("update_skill", {"id": skill_id, "name": record.name})
            return record

    return None


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)


def get_health_info() -> Dict[str, Any]:
    """Get health information."""
    store = load_store()
    return {
        "service": "skill_store_service",
        "version": "0.3.1-enterprise",
        "kind": "skill_store",
        "description": "技能安装、禁用、签名、版本、来源和 per-agent skill control。",
        "store_version": store.store_version,
        "count": len(store.items),
    }
