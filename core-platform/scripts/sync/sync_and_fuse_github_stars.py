#!/usr/bin/env python3
"""C26-STAR-SYNC-FUSION: Sync latest GitHub starred repos, fuse into builtin modules."""
from __future__ import annotations
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path("core-platform")
RAW = ROOT / "data/github_stars/github_stars_latest.json"
PREV = ROOT / "data/github_stars/CASTvivian_starred_repos.json"
NEW = ROOT / "data/github_stars/github_stars_new_since_last_sync.json"
DEFAULT_SKILLS = ROOT / "data/skill_brain/default_skills.json"
SKILL_STATE = ROOT / "data/skill_brain/skill_state.json"
MODULES = ROOT / "data/skill_brain/our_builtin_skill_modules.json"
SOURCE_LOGIC = ROOT / "data/skill_brain/source_core_logic_map.json"
FUSION_RESULT = ROOT / "data/skill_brain/skill_reference_fusion_result.json"
AUDIT = ROOT / "data/agent_core_audit/c26/skill_brain/c26_star_sync_fusion_audit.json"
REPORT = ROOT / "docs/reports/C26_STAR_SYNC_FUSION.md"

MODULE_RULES = [
    ("builtin.browser_operator", 90, ["browser", "playwright", "selenium", "crawl", "crawler", "scrape", "web automation", "web agent"]),
    ("builtin.mcp_tool_hub", 85, ["mcp", "model context protocol", "tool server", "tools", "protocol"]),
    ("builtin.memory_rag_core", 80, ["rag", "memory", "vector", "embedding", "retrieval", "knowledge graph", "graph", "database"]),
    ("builtin.code_agent_core", 76, ["code agent", "coding agent", "developer", "ide", "copilot", "patch", "diff", "refactor", "source code", "code"]),
    ("builtin.workflow_orchestrator", 72, ["workflow", "langgraph", "automation", "orchestrator", "pipeline", "agent workflow"]),
    ("builtin.local_model_runtime", 70, ["ollama", "local llm", "inference", "qwen", "llama", "model runtime", "vllm"]),
    ("builtin.prompt_skill_engine", 66, ["prompt", "skill", "template", "instruction", "system prompt"]),
    ("builtin.security_sandbox", 64, ["security", "sandbox", "permission", "approval", "policy", "guardrail", "cyber"]),
    ("builtin.eval_benchmark", 60, ["eval", "benchmark", "score", "testing", "quality", "regression"]),
    ("builtin.ui_desktop_operator", 55, ["desktop", "tauri", "electron", "ui", "react", "vue", "frontend"]),
    ("builtin.artifact_report_engine", 50, ["report", "document", "artifact", "ppt", "slides", "pdf"]),
    ("builtin.agent_runtime_core", 45, ["agent", "agentic", "multi-agent", "runtime", "autonomous"]),
]


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def normalize_raw_star_payload(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return raw
    text = RAW.read_text(encoding="utf-8", errors="ignore").strip()
    if not text:
        return []
    try:
        return json.loads(text)
    except Exception:
        pass
    repos: list[dict[str, Any]] = []
    decoder = json.JSONDecoder()
    idx = 0
    while idx < len(text):
        while idx < len(text) and text[idx].isspace():
            idx += 1
        if idx >= len(text):
            break
        obj, end = decoder.raw_decode(text, idx)
        if isinstance(obj, list):
            repos.extend(obj)
        elif isinstance(obj, dict):
            repos.append(obj)
        idx = end
    return repos


def repo_full_name(repo: dict[str, Any]) -> str:
    return str(repo.get("full_name") or repo.get("repo_full_name") or repo.get("name_with_owner") or "").strip()


def repo_to_star_record(repo: dict[str, Any]) -> dict[str, Any]:
    owner = repo.get("owner") or {}
    full_name = repo_full_name(repo)
    return {
        "full_name": full_name,
        "name": repo.get("name"),
        "owner": owner.get("login") if isinstance(owner, dict) else None,
        "html_url": repo.get("html_url"),
        "description": repo.get("description") or "",
        "language": repo.get("language"),
        "topics": repo.get("topics") or [],
        "stargazers_count": repo.get("stargazers_count") or repo.get("stars") or 0,
        "forks_count": repo.get("forks_count") or 0,
        "pushed_at": repo.get("pushed_at"),
        "updated_at": repo.get("updated_at"),
        "created_at": repo.get("created_at"),
    }


def readme_excerpt(full_name: str, limit: int = 1800) -> str:
    if not full_name:
        return ""
    try:
        out = subprocess.check_output(
            ["gh", "api", f"/repos/{full_name}/readme", "--jq", ".content"],
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=12,
        ).strip()
        if not out:
            return ""
        import base64
        text = base64.b64decode(out).decode("utf-8", errors="ignore")
        text = re.sub(r"\s+", " ", text).strip()
        return text[:limit]
    except Exception:
        return ""


def text_for_repo(record: dict[str, Any]) -> str:
    return " ".join([
        str(record.get("full_name") or ""),
        str(record.get("description") or ""),
        " ".join(str(x) for x in record.get("topics") or []),
        str(record.get("language") or ""),
        str(record.get("readme_excerpt") or ""),
    ]).lower()


def classify_repo(record: dict[str, Any]) -> tuple[str, int, list[str]]:
    text = text_for_repo(record)
    hits: list[tuple[str, int, list[str]]] = []
    for module_id, base_score, kws in MODULE_RULES:
        matched = []
        for kw in kws:
            if kw.lower() in text:
                matched.append(kw)
        if matched:
            score = base_score + min(20, len(matched) * 4)
            hits.append((module_id, score, matched))
    if not hits:
        return "builtin.agent_runtime_core", 30, []
    hits.sort(key=lambda x: (-x[1], x[0]))
    return hits[0]


def skill_id_from_full_name(full_name: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9]+", "_", full_name.lower()).strip("_")
    return "skill_star_" + safe


def tags_for_module(module_id: str, record: dict[str, Any]) -> list[str]:
    base: dict[str, list[str]] = {
        "builtin.code_agent_core": ["code_agent", "agent_runtime"],
        "builtin.browser_operator": ["browser_agent", "agent_runtime"],
        "builtin.mcp_tool_hub": ["mcp_tool", "agent_runtime"],
        "builtin.memory_rag_core": ["memory", "agent_runtime"],
        "builtin.workflow_orchestrator": ["workflow", "agent_runtime"],
        "builtin.local_model_runtime": ["local_model", "agent_runtime"],
        "builtin.prompt_skill_engine": ["prompt_framework", "agent_runtime"],
        "builtin.security_sandbox": ["security", "agent_runtime"],
        "builtin.eval_benchmark": ["evaluation", "agent_runtime"],
        "builtin.ui_desktop_operator": ["ui_component", "agent_runtime"],
        "builtin.artifact_report_engine": ["artifact", "agent_runtime"],
        "builtin.agent_runtime_core": ["agent_runtime"],
    }
    base_tags = base.get(module_id, ["agent_runtime"])
    topics = [str(x).lower().replace("-", "_") for x in record.get("topics") or []]
    lang = str(record.get("language") or "").lower()
    if lang:
        topics.append(lang)
    out: list[str] = []
    for x in base_tags + topics:
        if x and x not in out:
            out.append(x)
    return out[:16]


def core_logic_for(module_id: str, record: dict[str, Any]) -> dict[str, list[str]]:
    title = record.get("full_name") or record.get("name") or ""
    common: dict[str, list[str]] = {
        "core_logic": [],
        "unique_capability": [],
        "rebuild_value": [],
        "what_must_not_be_lost": [],
    }
    mapping: dict[str, tuple[list[str], list[str], list[str], list[str]]] = {
        "builtin.code_agent_core": (
            ["workspace code understanding", "patch-oriented editing", "developer task execution"],
            ["code agent workflow pattern"],
            ["absorb into code_agent_core planning, patch and repair loop"],
            ["do not lose code modification and developer workflow logic"],
        ),
        "builtin.browser_operator": (
            ["browser/web research planning", "structured extraction", "evidence collection"],
            ["browser operator or web research pattern"],
            ["absorb into browser_operator action plan and evidence model"],
            ["do not lose browser navigation/research/extraction logic"],
        ),
        "builtin.mcp_tool_hub": (
            ["tool protocol", "tool discovery", "tool invocation contract"],
            ["MCP/tool hub pattern"],
            ["absorb into mcp_tool_hub registry and adapter contracts"],
            ["do not lose tool schema and invocation design"],
        ),
        "builtin.memory_rag_core": (
            ["retrieval augmented memory", "semantic search", "knowledge grounding"],
            ["memory/RAG architecture pattern"],
            ["absorb into memory_rag_core and repo memory layer"],
            ["do not lose retrieval evidence and memory design"],
        ),
        "builtin.workflow_orchestrator": (
            ["multi-step workflow orchestration", "stateful task execution", "dependency planning"],
            ["workflow orchestration pattern"],
            ["absorb into workflow_orchestrator and task_state"],
            ["do not lose workflow state and dependency logic"],
        ),
        "builtin.local_model_runtime": (
            ["local model runtime", "inference profile", "model execution"],
            ["local model runtime pattern"],
            ["absorb into local_model_runtime and model gateway"],
            ["do not lose local/offline runtime assumptions"],
        ),
        "builtin.prompt_skill_engine": (
            ["prompt skill packaging", "instruction templates", "task-specific prompts"],
            ["prompt skill organization pattern"],
            ["absorb into prompt_skill_engine"],
            ["do not lose reusable instruction structure"],
        ),
        "builtin.security_sandbox": (
            ["policy guard", "approval boundary", "sandbox safety"],
            ["security approval/sandbox pattern"],
            ["absorb into security_sandbox and approval gate"],
            ["do not lose permission and audit logic"],
        ),
        "builtin.eval_benchmark": (
            ["benchmark scoring", "quality evaluation", "regression tracking"],
            ["evaluation pattern"],
            ["absorb into eval_benchmark"],
            ["do not lose measurable quality gates"],
        ),
    }
    values = mapping.get(module_id, (
        ["agent runtime reference", "design pattern"],
        ["general agent implementation pattern"],
        ["absorb into matching builtin module"],
        ["do not lose source rationale and implementation idea"],
    ))
    common["core_logic"] = list(values[0])
    common["unique_capability"] = [f"{title}: {values[1][0]}"]
    common["rebuild_value"] = list(values[2])
    common["what_must_not_be_lost"] = list(values[3])
    return common


def main() -> None:
    raw = normalize_raw_star_payload(load_json(RAW, []))
    latest_records = [repo_to_star_record(x) for x in raw if repo_full_name(x)]
    latest_by_name = {x["full_name"]: x for x in latest_records}

    # Previous snapshot
    prev_payload = load_json(PREV, [])
    if isinstance(prev_payload, dict):
        prev_items = prev_payload.get("repositories") or prev_payload.get("repos") or prev_payload.get("items") or []
    else:
        prev_items = prev_payload
    prev_names: set[str] = set()
    for item in prev_items:
        if isinstance(item, dict):
            name = repo_full_name(item)
            if name:
                prev_names.add(name)

    # Find new repos
    new_names = sorted(set(latest_by_name) - prev_names)
    new_records = [latest_by_name[x] for x in new_names]

    # Fetch README excerpts for new repos
    for i, record in enumerate(new_records):
        record["readme_excerpt"] = readme_excerpt(record["full_name"])
        if (i + 1) % 10 == 0:
            print(f"  README fetched: {i + 1}/{len(new_records)}")

    write_json(NEW, {
        "version": "c26-star-sync",
        "synced_at": datetime.utcnow().isoformat() + "Z",
        "previous_count": len(prev_names),
        "latest_count": len(latest_records),
        "new_count": len(new_records),
        "new_repositories": new_records,
    })

    # Load existing data files
    default_skills = load_json(DEFAULT_SKILLS, {"version": "unknown", "skills": []})
    skills = default_skills.setdefault("skills", [])
    existing_skill_ids = {x.get("id") for x in skills}

    skill_state = load_json(SKILL_STATE, {"version": "unknown", "skills": {}})
    state_map = skill_state.setdefault("skills", {})

    modules_data = load_json(MODULES, {"version": "unknown", "modules": []})
    modules = modules_data.setdefault("modules", [])
    modules_by_id = {m.get("id"): m for m in modules}

    source_logic = load_json(SOURCE_LOGIC, {
        "version": "c26-r2b",
        "source_core_logic_map": [],
        "module_summaries": {},
    })
    source_items = source_logic.setdefault("source_core_logic_map", [])

    fusion_assignments = []
    added_skill_count = 0
    added_reference_count = 0

    for record in new_records:
        module_id, score, matched = classify_repo(record)
        sid = skill_id_from_full_name(record["full_name"])
        tags = tags_for_module(module_id, record)

        skill = {
            "id": sid,
            "title": record["full_name"],
            "description": record.get("description") or record.get("readme_excerpt", "")[:240],
            "source": "github_star_sync",
            "source_path": record.get("html_url"),
            "repo_full_name": record["full_name"],
            "language": record.get("language"),
            "stars": record.get("stargazers_count", 0),
            "tags": tags,
            "enabled": True,
            "default": True,
            "target_builtin_module": module_id,
            "classification_score": score,
            "classification_hits": matched,
            "created_at": datetime.utcnow().isoformat() + "Z",
        }

        if sid not in existing_skill_ids:
            skills.append(skill)
            existing_skill_ids.add(sid)
            added_skill_count += 1

        state_map.setdefault(sid, {
            "enabled": True,
            "pinned": False,
            "usage_count": 0,
            "rating": None,
            "source": "github_star_sync",
            "updated_at": datetime.utcnow().isoformat() + "Z",
        })

        module = modules_by_id.get(module_id)
        if module:
            refs = module.setdefault("source_references", [])
            if not any(x.get("skill_id") == sid for x in refs):
                ref = {
                    "skill_id": sid,
                    "title": record["full_name"],
                    "source_path": record.get("html_url"),
                    "stars": record.get("stargazers_count", 0),
                    "score": score,
                    "tags": tags,
                    "source": "github_star_sync",
                    "classification_hits": matched,
                }
                refs.append(ref)
                module["source_reference_count"] = len(refs)
                added_reference_count += 1

                logic = {
                    "target_builtin_module": module_id,
                    "target_builtin_title": module.get("title"),
                    "skill_id": sid,
                    "title": record["full_name"],
                    "source_path": record.get("html_url"),
                    "stars": record.get("stargazers_count", 0),
                    "score": score,
                    "tags": tags,
                    **core_logic_for(module_id, record),
                }
                module.setdefault("source_core_logic_map", []).append(logic)
                source_items.append(logic)

        fusion_assignments.append({
            "repo": record["full_name"],
            "skill_id": sid,
            "target_builtin_module": module_id,
            "score": score,
            "hits": matched,
            "tags": tags,
        })

    # Update versions
    default_skills["version"] = "c26-star-sync-fusion"
    default_skills["updated_at"] = datetime.utcnow().isoformat() + "Z"
    default_skills["skill_count"] = len(skills)

    skill_state["version"] = "c26-star-sync-fusion"
    skill_state["updated_at"] = datetime.utcnow().isoformat() + "Z"

    modules_data["version"] = "c26-star-sync-fusion"
    modules_data["updated_at"] = datetime.utcnow().isoformat() + "Z"

    module_summaries: dict[str, dict[str, int]] = {}
    for m in modules:
        logic_items = m.get("source_core_logic_map", [])
        module_summaries[m.get("id", "")] = {
            "source_count": len(m.get("source_references", [])),
            "core_logic_count": sum(len(x.get("core_logic", [])) for x in logic_items),
            "must_not_lose_count": sum(len(x.get("what_must_not_be_lost", [])) for x in logic_items),
        }

    source_logic["version"] = "c26-star-sync-fusion"
    source_logic["updated_at"] = datetime.utcnow().isoformat() + "Z"
    source_logic["source_count"] = len(source_items)
    source_logic["module_summaries"] = module_summaries

    # Write all data files
    write_json(DEFAULT_SKILLS, default_skills)
    write_json(SKILL_STATE, skill_state)
    write_json(MODULES, modules_data)
    write_json(SOURCE_LOGIC, source_logic)

    fusion_result = {
        "version": "c26-star-sync-fusion",
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "new_repo_count": len(new_records),
        "added_skill_count": added_skill_count,
        "added_reference_count": added_reference_count,
        "assignments": fusion_assignments,
        "note": "New GitHub starred repositories are fused into owned builtin modules. External source identity is kept as internal evidence only.",
    }
    write_json(FUSION_RESULT, fusion_result)

    audit: dict[str, Any] = {
        "checked_at": datetime.utcnow().isoformat() + "Z",
        "previous_count": len(prev_names),
        "latest_count": len(latest_records),
        "new_count": len(new_records),
        "added_skill_count": added_skill_count,
        "added_reference_count": added_reference_count,
        "module_assignment_summary": {},
        "new_repositories": [x["full_name"] for x in new_records],
        "assignments": fusion_assignments,
    }
    for item in fusion_assignments:
        mid = item["target_builtin_module"]
        audit["module_assignment_summary"][mid] = audit["module_assignment_summary"].get(mid, 0) + 1
    write_json(AUDIT, audit)

    # Replace previous snapshot only after successful processing
    write_json(PREV, {
        "version": "c26-star-sync-fusion",
        "synced_at": datetime.utcnow().isoformat() + "Z",
        "repositories": latest_records,
    })

    # Generate report
    lines = [
        "# C26 Star Sync Fusion",
        "",
        "## Summary",
        "",
        f"- previous_count: {audit['previous_count']}",
        f"- latest_count: {audit['latest_count']}",
        f"- new_count: {audit['new_count']}",
        f"- added_skill_count: {audit['added_skill_count']}",
        f"- added_reference_count: {audit['added_reference_count']}",
        "",
        "## Module Assignment Summary",
        "",
        "| Module | New Repos |",
        "|---|---:|",
    ]
    for mid, count in sorted(audit["module_assignment_summary"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"| {mid} | {count} |")
    lines += [
        "",
        "## New Repositories",
        "",
        "| Repo | Target Builtin Module | Score | Hits |",
        "|---|---|---:|---|",
    ]
    for item in fusion_assignments:
        lines.append(
            f"| {item['repo']} | {item['target_builtin_module']} | {item['score']} | {', '.join(item['hits']) or '-'} |"
        )
    lines += [
        "",
        "## Rule",
        "",
        "New starred repositories are not exposed as separate runtime dependencies by default.",
        "",
        "They are fused into owned builtin modules and preserved as internal capability evidence.",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")

    print(json.dumps({
        "previous_count": audit["previous_count"],
        "latest_count": audit["latest_count"],
        "new_count": audit["new_count"],
        "added_skill_count": audit["added_skill_count"],
        "added_reference_count": audit["added_reference_count"],
        "module_assignment_summary": audit["module_assignment_summary"],
        "new_repositories": audit["new_repositories"],
        "total_skill_count": len(skills),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
