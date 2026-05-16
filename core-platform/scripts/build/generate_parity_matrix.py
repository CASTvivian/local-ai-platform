#!/usr/bin/env python3
"""C26-P0-A Claude/Claw Parity Matrix 2.0 — detailed capability gap audit."""
import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path("core-platform")

CAPABILITIES = [
    ("workspace.file_tree", "Workspace file tree awareness", ["file tree", "workspace", "directory", "repo"], ["services/agent_runtime_service/app/filesystem", "services/repo_memory_service"]),
    ("workspace.file_read", "Read project files safely", ["filesystem.read", "read file"], ["services/agent_runtime_service/app/filesystem", "data/agent_policy/planner_tool_schema.json"]),
    ("workspace.file_write", "Write project files with approval", ["filesystem.write", "approval"], ["services/agent_runtime_service/app/filesystem", "services/agent_runtime_service/app/security"]),
    ("workspace.diff_review", "Diff review and patch summary", ["diff", "patch", "review"], ["services/agent_runtime_service/app", "docs/reports"]),
    ("workspace.repo_memory", "Repo memory search", ["repo_memory.search", "brain_assets", "repo memory"], ["services/repo_memory_service", "data/brain_assets"]),
    ("planner.schema", "Schema-driven planner", ["schema_planner", "planner_tool_schema"], ["services/agent_runtime_service/app/planning/schema_planner.py", "data/agent_policy/planner_tool_schema.json"]),
    ("planner.structured_output", "Planner model structured output", ["_normalize_model_plan", "_extract_json_object"], ["services/agent_runtime_service/app/planning/schema_planner.py"]),
    ("planner.replan", "Observation and replan loop", ["replan", "observation", "validator"], ["services/agent_runtime_service/app/loop", "services/agent_runtime_service/app/service.py"]),
    ("planner.todo_state", "Todo/task state machine", ["todo", "task state", "checklist"], ["services/agent_runtime_service/app", "data"]),
    ("planner.session_resume", "Session resume", ["session", "resume", "run_store"], ["services/agent_runtime_service/app/store"]),
    ("executor.registry_dispatch", "Tool registry dispatch", ["tool_dispatch_registry", "execute_registered_tool"], ["services/agent_runtime_service/app/execution/tool_dispatch_registry.py", "services/agent_runtime_service/app/executor.py"]),
    ("executor.shell", "Shell execution with sandbox", ["shell.exec", "sandbox"], ["services/agent_runtime_service/app/runtime", "data/sandbox_policy"]),
    ("executor.build_test_loop", "Build/test/repair loop", ["test", "build", "repair", "rerun"], ["services/agent_runtime_service/app", "docs/reports"]),
    ("executor.approval_gate", "Approval gate for risky actions", ["approval", "requires_review"], ["services/agent_runtime_service/app/security", "services/agent_runtime_service/app/runtime"]),
    ("executor.artifacts", "Artifact generation and report chain", ["artifact", "report", "audit"], ["services/artifact_registry_service", "docs/reports"]),
    ("renderer.data_driven", "Data-driven renderer", ["renderer_templates", "render_tool_result"], ["services/agent_runtime_service/app/renderer.py", "data/agent_policy/renderer_templates.json"]),
    ("replay.timeline", "Run timeline replay", ["timeline", "replay"], ["services/agent_runtime_service/app/replay"]),
    ("trace.observability", "Trace observability", ["trace", "observability"], ["services/trace_observability_service", "services/agent_runtime_service/app"]),
    ("mcp.runtime", "MCP runtime and invoke", ["mcp", "invoke"], ["services/agent_runtime_service/app/mcp"]),
    ("skills.default_generation", "Default skills generated from repo assets", ["default_skills", "skill_brain"], ["data/skill_brain/default_skills.json", "scripts/build/generate_default_skills.py"]),
    ("skills.capability_registry", "Default skills exposed as capabilities", ["skill.", "load_default_skills"], ["services/agent_runtime_service/app/capability/registry.py"]),
    ("skills.planner_context", "Planner discovers skills", ["_skill_context_steps", "include_skills"], ["services/agent_runtime_service/app/planning/schema_planner.py"]),
    ("skills.desktop_store", "Desktop skill store", ["renderDefaultSkillStorePage", "skill-brain"], ["apps/desktop/src/js/windows-demo-stable-router.js", "apps/desktop/src/styles/main.css"]),
    ("skills.own_builtin", "Own rebuilt builtin skills", ["our_builtin_skills", "builtin_skill"], ["data/skill_brain", "data/agent_policy"]),
    ("skills.lifecycle_state", "Skill lifecycle state (enable/disable/pin/usage)", ["skill_state", "set_skill_enabled", "record_skill_usage"], ["data/skill_brain/skill_state.json", "services/agent_runtime_service/app/capability/registry.py"]),
    ("model.ollama", "Ollama local model runtime", ["ollama", "11434"], ["services/model_gateway", "data/runtime_config/runtime_config.json"]),
    ("model.gateway", "Model gateway", ["model_gateway", "18080"], ["services/model_gateway"]),
    ("model.bootstrap", "Model bootstrap/download", ["model_bootstrap", "18100"], ["services/model_bootstrap_service", "scripts/windows/bootstrap_runtime.ps1"]),
    ("model.offline_pack", "Offline model preseed pack", ["offline", "preseed", "model pack"], ["data", "docs/reports"]),
    ("desktop.mac", "macOS packaged app", ["scripts/mac", "macos", "dmg"], ["scripts/mac", "releases/macos-c25-final"]),
    ("desktop.windows", "Windows MSI package", ["scripts/windows", "msi"], ["scripts/windows", "releases"]),
    ("desktop.runtime_autostart", "Desktop runtime autostart", ["start_all", "autostart"], ["apps/desktop/src-tauri/src/lib.rs", "scripts/mac", "scripts/windows"]),
    ("desktop.runtime_config_generated", "Generated desktop runtime config", ["AUTO-GENERATED", "generate_desktop_runtime_config"], ["apps/desktop/src/js/config/runtime-config.js", "scripts/build/generate_desktop_runtime_config.py"]),
    ("policy.sandbox_config", "Sandbox policy config", ["sandbox_policy", "blocked"], ["data/sandbox_policy", "services/agent_runtime_service/app/runtime"]),
    ("policy.audit_guard", "Runtime hardcode guard", ["check_runtime_no_hardcode", "hardcode_guard"], ["scripts/quality/check_runtime_no_hardcode.py", "data/agent_policy/hardcode_guard.json"]),
    ("policy.enterprise_config", "Enterprise configurable policy", ["policy", "config"], ["data/agent_policy", "services/agent_runtime_service/app/security"]),
    ("team.runtime", "Multi-agent runtime", ["team", "coordinator", "researcher", "builder", "reviewer"], ["services/agent_runtime_service/app/team", "data/agent_team"]),
    ("team.failure_isolation", "Team failure isolation", ["fallback", "failed", "timeline"], ["services/agent_runtime_service/app/team"]),
    ("own.skill_rebuild_matrix", "External repo to own skill rebuild matrix", ["rebuild", "own", "reference"], ["data/skill_brain", "docs/reports"]),
    ("own.core_skill_modules", "Own built-in skill modules", ["builtin", "skill module"], ["services/agent_runtime_service/app", "data/skill_brain"]),
    ("own.continuous_audit", "Self audit and project integrity check", ["audit", "integrity", "final"], ["data/agent_core_audit", "docs/reports"]),
]


def read_path(rel):
    p = ROOT / rel
    if not p.exists():
        return ""
    if p.is_dir():
        content = []
        for f in sorted(p.rglob("*"))[:800]:
            if f.is_file() and f.suffix.lower() in {".py", ".js", ".json", ".md", ".toml", ".yml", ".yaml", ".sh", ".ps1"}:
                try:
                    content.append(str(f.relative_to(ROOT)))
                    content.append(f.read_text(encoding="utf-8", errors="ignore")[:6000])
                except Exception:
                    pass
        return "\n".join(content)
    try:
        return p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def main():
    rows = []
    for cid, title, terms, paths in CAPABILITIES:
        text = ""
        evidence = []
        for path in paths:
            p = ROOT / path
            exists = p.exists()
            evidence.append({"path": path, "exists": exists})
            text += "\n" + read_path(path)
        term_hits = []
        missing_terms = []
        for term in terms:
            if re.search(re.escape(term), text, re.I):
                term_hits.append(term)
            else:
                missing_terms.append(term)
        path_ratio = sum(1 for e in evidence if e["exists"]) / max(1, len(evidence))
        hit_ratio = len(term_hits) / max(1, len(terms))
        score = round((path_ratio * 0.55 + hit_ratio * 0.45) * 100)
        if score >= 85:
            status = "implemented"
        elif score >= 55:
            status = "partial"
        else:
            status = "gap"
        rows.append({
            "id": cid, "title": title, "status": status, "score": score,
            "term_hits": term_hits, "missing_terms": missing_terms, "evidence": evidence,
        })

    summary = {
        "total": len(rows),
        "implemented": sum(1 for x in rows if x["status"] == "implemented"),
        "partial": sum(1 for x in rows if x["status"] == "partial"),
        "gap": sum(1 for x in rows if x["status"] == "gap"),
        "avg_score": round(sum(x["score"] for x in rows) / len(rows), 1)
    }

    p0_missing = [
        x for x in rows if x["status"] != "implemented" and x["id"] in {
            "workspace.diff_review", "planner.todo_state", "executor.build_test_loop",
            "model.offline_pack", "skills.own_builtin", "own.skill_rebuild_matrix",
            "own.core_skill_modules", "desktop.windows"
        }
    ]

    result = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "summary": summary,
        "capabilities": rows,
        "p0_missing_or_partial": p0_missing,
        "verdict": {
            "core_rebuild_done": True,
            "claude_claw_full_parity_done": False,
            "own_skill_rebuild_done": False,
            "can_demo_mac": True,
            "next_required": [
                "C26-P0-B workspace diff/patch engine",
                "C26-P0-C build-test-repair loop",
                "C26-P0-D task todo state machine",
                "C26-R1 skill rebuild grading",
                "C26-R2 own builtin skill modules",
                "C25-WIN-FINAL-SMOKE"
            ]
        }
    }

    out = Path("core-platform/data/agent_core_audit/c26/parity")
    out.mkdir(parents=True, exist_ok=True)
    out.joinpath("c26_p0_a_claude_claw_parity_matrix_2.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps({
        "summary": summary,
        "p0_missing_or_partial": [
            {"id": x["id"], "status": x["status"], "score": x["score"], "missing_terms": x["missing_terms"]}
            for x in p0_missing
        ],
        "verdict": result["verdict"]
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
