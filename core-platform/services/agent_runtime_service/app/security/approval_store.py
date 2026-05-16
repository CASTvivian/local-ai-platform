from __future__ import annotations
import json
import os
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Literal

ApprovalStatus = Literal["pending", "approved", "rejected", "expired", "cancelled"]
RiskLevel = Literal["low", "medium", "high", "critical"]


@dataclass
class ApprovalRequest:
    id: str
    action: str
    risk: RiskLevel
    reason: str
    payload: dict[str, Any]
    status: ApprovalStatus = "pending"
    requester: str | None = None
    reviewer: str | None = None
    decision_reason: str | None = None
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")

    def model_dump(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "action": self.action,
            "risk": self.risk,
            "reason": self.reason,
            "payload": self.payload,
            "status": self.status,
            "requester": self.requester,
            "reviewer": self.reviewer,
            "decision_reason": self.decision_reason,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }


def _core_platform_dir() -> Path:
    env = os.environ.get("MAOMIAI_CORE_PLATFORM_DIR")
    if env:
        return Path(env).expanduser().resolve()
    current = Path(__file__).resolve()
    for parent in [current, *current.parents]:
        if (parent / "data").exists() and (parent / "services").exists():
            return parent
    return Path.cwd().resolve()


def _approval_dir() -> Path:
    path = _core_platform_dir() / "data" / "approvals"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _audit_dir() -> Path:
    path = _core_platform_dir() / "data" / "approval_audit"
    path.mkdir(parents=True, exist_ok=True)
    return path


def _now() -> str:
    return datetime.utcnow().isoformat() + "Z"


def _safe_id(value: str) -> str:
    return "".join(ch for ch in value if ch.isalnum() or ch in {"-", "_"})


def _path(approval_id: str) -> Path:
    return _approval_dir() / f"{_safe_id(approval_id)}.json"


def _write_audit(event: dict[str, Any]) -> str:
    stamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S%fZ")
    out = _audit_dir() / f"approval_{stamp}.json"
    out.write_text(
        json.dumps(
            {
                "created_at": _now(),
                **event,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    return str(out)


def save_approval(req: ApprovalRequest) -> None:
    _path(req.id).write_text(json.dumps(req.model_dump(), ensure_ascii=False, indent=2), encoding="utf-8")


def load_approval(approval_id: str) -> ApprovalRequest:
    data = json.loads(_path(approval_id).read_text(encoding="utf-8"))
    return ApprovalRequest(
        id=data["id"],
        action=data["action"],
        risk=data["risk"],
        reason=data["reason"],
        payload=data.get("payload") or {},
        status=data.get("status", "pending"),
        requester=data.get("requester"),
        reviewer=data.get("reviewer"),
        decision_reason=data.get("decision_reason"),
        created_at=data.get("created_at", _now()),
        updated_at=data.get("updated_at", _now()),
    )


def create_approval_request(
    action: str,
    risk: RiskLevel,
    reason: str,
    payload: dict[str, Any],
    requester: str | None = None,
) -> ApprovalRequest:
    req = ApprovalRequest(
        id="approval_" + uuid.uuid4().hex,
        action=action,
        risk=risk,
        reason=reason,
        payload=payload,
        requester=requester,
    )
    save_approval(req)
    _write_audit({
        "event": "approval_requested",
        "approval": req.model_dump(),
    })
    return req


def decide_approval(
    approval_id: str,
    approved: bool,
    reviewer: str | None = None,
    decision_reason: str | None = None,
) -> ApprovalRequest:
    req = load_approval(approval_id)
    if req.status != "pending":
        raise ValueError(f"approval is not pending: {req.status}")
    req.status = "approved" if approved else "rejected"
    req.reviewer = reviewer
    req.decision_reason = decision_reason
    req.updated_at = _now()
    save_approval(req)
    _write_audit({
        "event": "approval_decided",
        "approved": approved,
        "approval": req.model_dump(),
    })
    return req


def cancel_approval(approval_id: str, reason: str | None = None) -> ApprovalRequest:
    req = load_approval(approval_id)
    if req.status != "pending":
        raise ValueError(f"approval is not pending: {req.status}")
    req.status = "cancelled"
    req.decision_reason = reason
    req.updated_at = _now()
    save_approval(req)
    _write_audit({
        "event": "approval_cancelled",
        "approval": req.model_dump(),
    })
    return req


def list_approvals(status: ApprovalStatus | None = None, limit: int = 50) -> list[dict[str, Any]]:
    rows = []
    files = sorted(_approval_dir().glob("approval_*.json"), key=lambda p: p.stat().st_mtime, reverse=True)
    for path in files[:limit * 3]:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if status and data.get("status") != status:
            continue
        rows.append({
            "id": data.get("id"),
            "action": data.get("action"),
            "risk": data.get("risk"),
            "reason": data.get("reason"),
            "status": data.get("status"),
            "requester": data.get("requester"),
            "reviewer": data.get("reviewer"),
            "updated_at": data.get("updated_at"),
        })
        if len(rows) >= limit:
            break
    return rows


def requires_approval(action: str, risk: RiskLevel, payload: dict[str, Any] | None = None) -> bool:
    if risk in {"high", "critical"}:
        return True
    dangerous_actions = {
        "shell.exec",
        "filesystem.write",
        "filesystem.delete",
        "network.post",
        "credential.access",
        "external.browser.action",
    }
    if action in dangerous_actions:
        return True
    return False


def ensure_approved_or_request(
    action: str,
    risk: RiskLevel,
    reason: str,
    payload: dict[str, Any],
    requester: str | None = None,
    approval_id: str | None = None,
) -> dict[str, Any]:
    """Return allow/blocked/pending decision for an action."""
    if approval_id:
        req = load_approval(approval_id)
        if req.status == "approved":
            return {
                "ok": True,
                "status": "approved",
                "approval": req.model_dump(),
            }
        return {
            "ok": False,
            "status": req.status,
            "approval": req.model_dump(),
            "error": "approval_not_approved",
        }
    if not requires_approval(action, risk, payload):
        return {
            "ok": True,
            "status": "not_required",
            "approval": None,
        }
    req = create_approval_request(
        action=action,
        risk=risk,
        reason=reason,
        payload=payload,
        requester=requester,
    )
    return {
        "ok": False,
        "status": "pending_approval",
        "approval": req.model_dump(),
        "error": "approval_required",
    }
