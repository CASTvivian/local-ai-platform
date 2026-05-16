#!/usr/bin/env python3
"""C26-R2-FUSION-POLICY: Fuse new skill references into existing builtin modules."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[2]
SKILLS = ROOT / "data" / "skill_brain" / "default_skills.json"
MODULES = ROOT / "data" / "skill_brain" / "our_builtin_skill_modules.json"
POLICY = ROOT / "data" / "skill_brain" / "fusion_policy.json"
OUT = ROOT / "data" / "skill_brain" / "skill_reference_fusion_result.json"
AUDIT = ROOT / "data" / "agent_core_audit" / "c26" / "skill_brain" / "skill_reference_fusion_result_audit.json"


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def text_for_skill(skill: dict) -> str:
    return " ".join([
        str(skill.get("id") or ""),
        str(skill.get("title") or ""),
        str(skill.get("source_path") or ""),
        str(skill.get("description") or ""),
        " ".join(skill.get("tags") or []),
    ]).lower()


def text_for_module(module: dict) -> str:
    return " ".join([
        str(module.get("id") or ""),
        str(module.get("title") or ""),
        " ".join(module.get("merged_capabilities") or []),
        " ".join(module.get("implementation_plan") or []),
    ]).lower()


def score_match(skill: dict, module: dict) -> float:
    skill_tags = set(skill.get("tags") or [])
    module_text = text_for_module(module)
    skill_text = text_for_skill(skill)
    score = 0.0
    for tag in skill_tags:
        if tag.lower() in module_text:
            score += 0.25
    for token in skill_text.split():
        if len(token) >= 4 and token in module_text:
            score += 0.03
    return round(min(score, 1.0), 4)


def main() -> None:
    skills_data = load_json(SKILLS, {"skills": []})
    modules_data = load_json(MODULES, {"modules": []})
    policy = load_json(POLICY, {})
    skills = skills_data.get("skills", [])
    modules = modules_data.get("modules", [])

    assignments = []
    candidates = []

    existing_refs = set()
    for module in modules:
        for ref in module.get("source_references", []):
            if ref.get("skill_id"):
                existing_refs.add(ref["skill_id"])

    for skill in skills:
        sid = skill.get("id")
        if not sid or sid in existing_refs:
            continue
        scored = [
            {
                "module_id": module.get("id"),
                "module_title": module.get("title"),
                "score": score_match(skill, module),
            }
            for module in modules
        ]
        scored.sort(key=lambda x: -x["score"])
        best = scored[0] if scored else {"score": 0}
        row = {
            "skill_id": sid,
            "title": skill.get("title"),
            "source_path": skill.get("source_path"),
            "tags": skill.get("tags", []),
            "best_match": best,
            "top_matches": scored[:5],
        }
        if best.get("score", 0) >= 0.25:
            assignments.append(row)
        else:
            candidates.append(row)

    result = {
        "version": "c26-r2-fusion-result",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "policy_version": policy.get("version"),
        "assignment_count": len(assignments),
        "new_module_candidate_count": len(candidates),
        "assignments": assignments,
        "new_module_candidates": candidates,
        "note": "This file is an audit/proposal. It does not auto-enable new runtime capabilities."
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(
        json.dumps({
            "checked_at": datetime.utcnow().isoformat() + "Z",
            "assignment_count": len(assignments),
            "new_module_candidate_count": len(candidates),
            "policy_version": policy.get("version"),
        }, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps({
        "assignment_count": len(assignments),
        "new_module_candidate_count": len(candidates),
        "policy_version": policy.get("version"),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
