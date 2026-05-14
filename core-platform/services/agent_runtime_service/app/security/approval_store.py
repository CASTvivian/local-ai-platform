"""JSON-file approval store for Agent Runtime."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import List, Optional

from .approval_models import ApprovalDecision, ApprovalRecord


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
APPROVAL_ROOT = CORE_PLATFORM_ROOT / "data" / "approval_store"
APPROVAL_ROOT.mkdir(parents=True, exist_ok=True)


def approval_file(approval_id: str) -> Path:
    return APPROVAL_ROOT / f"{approval_id}.json"


def save_approval(record: ApprovalRecord) -> None:
    approval_file(record.approval_id).write_text(record.model_dump_json(indent=2), encoding="utf-8")


def load_approval(approval_id: str) -> Optional[ApprovalRecord]:
    path = approval_file(approval_id)
    if not path.exists():
        return None
    return ApprovalRecord.model_validate_json(path.read_text(encoding="utf-8"))


def list_approvals() -> List[ApprovalRecord]:
    out: List[ApprovalRecord] = []
    for path in sorted(APPROVAL_ROOT.glob("*.json")):
        try:
            out.append(ApprovalRecord.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception:
            continue
    return out


def resolve_approval(decision: ApprovalDecision) -> Optional[ApprovalRecord]:
    record = load_approval(decision.approval_id)
    if not record:
        return None
    record.approved = decision.approved
    record.reviewer = decision.reviewer
    record.reason = decision.reason
    record.resolved_at = datetime.utcnow().isoformat()
    save_approval(record)
    return record
