#!/usr/bin/env python3
"""C26-R2-FUSION: Merge 83 rebuild_core repos into own builtin fusion modules."""
from __future__ import annotations
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
GRADING = ROOT / "data" / "skill_brain" / "skill_rebuild_grading.json"
OUT = ROOT / "data" / "skill_brain" / "our_builtin_skill_modules.json"
AUDIT = ROOT / "data" / "agent_core_audit" / "c26" / "skill_brain" / "c26_r2_fusion_own_builtin_modules.json"

# match_tags: list of (tag, weight) — specialist tags get higher weight
# so browser_agent (80) beats agent_runtime (20) when both present
MODULES = {
    "builtin.code_agent_core": {
        "title": "代码智能体核心模块",
        "match_tags": [("code_agent", 60), ("prompt_framework", 30)],
        "keywords": ["claude", "claw", "coding", "copilot", "developer", "ide"],
        "merged_capabilities": [
            "workspace file understanding",
            "code patch planning",
            "diff review",
            "repair loop",
            "task todo tracking",
            "developer workflow automation"
        ],
        "implementation_plan": [
            "Use references only for capability design.",
            "Implement owned workspace read/patch/build/test APIs.",
            "Connect task_state + patch_engine + repair_loop.",
            "Expose as builtin.code_agent_core capability."
        ]
    },
    "builtin.agent_runtime_core": {
        "title": "通用 Agent Runtime 模块",
        "match_tags": [("agent_runtime", 20)],
        "keywords": ["autogpt", "openclaw", "planner", "executor", "agent framework"],
        "merged_capabilities": [
            "autonomous task execution",
            "planner/executor separation",
            "observation and replan loop",
            "tool use orchestration"
        ],
        "implementation_plan": [
            "Merge reference patterns into schema-driven planner.",
            "Keep execution through tool registry.",
            "Use replay timeline and task state for observability."
        ]
    },
    "builtin.mcp_tool_hub": {
        "title": "MCP 工具协议模块",
        "match_tags": [("mcp_tool", 70)],
        "keywords": ["mcp server", "tool protocol"],
        "merged_capabilities": [
            "MCP tool metadata registry",
            "tool invocation contract",
            "tool discovery",
            "safe adapter model"
        ],
        "implementation_plan": [
            "Normalize MCP tool metadata.",
            "Register MCP tools into capability registry.",
            "Route invocations through execution registry."
        ]
    },
    "builtin.browser_operator": {
        "title": "浏览器自动化模块",
        "match_tags": [("browser_agent", 80)],
        "keywords": ["browser", "playwright", "scrape", "crawler", "fetch"],
        "merged_capabilities": [
            "web page research",
            "browser action planning",
            "structured extraction",
            "safe browsing guard"
        ],
        "implementation_plan": [
            "Build owned browser action schema.",
            "Integrate web.search / browser.fetch tools.",
            "Add audit trail for browser actions."
        ]
    },
    "builtin.memory_rag_core": {
        "title": "记忆与 RAG 检索模块",
        "match_tags": [("memory", 70)],
        "keywords": ["rag", "vector", "embedding", "graph database", "knowledge retrieval"],
        "merged_capabilities": [
            "repo memory",
            "document retrieval",
            "semantic search",
            "knowledge summarization",
            "skill context retrieval"
        ],
        "implementation_plan": [
            "Use repo_memory_service as base.",
            "Add skill-aware retrieval context.",
            "Support local knowledge evidence tracking."
        ]
    },
    "builtin.workflow_orchestrator": {
        "title": "工作流编排模块",
        "match_tags": [("workflow", 65)],
        "keywords": ["langgraph", "deer flow", "pipeline", "orchestration", "automation"],
        "merged_capabilities": [
            "multi-step workflow",
            "conditional steps",
            "task dependency graph",
            "execution status tracking"
        ],
        "implementation_plan": [
            "Connect task_state to workflow_store.",
            "Represent workflows as schema plans.",
            "Add replay and audit for each step."
        ]
    },
    "builtin.local_model_runtime": {
        "title": "本地模型运行模块",
        "match_tags": [("local_model", 55)],
        "keywords": ["ollama", "qwen", "inference engine", "local llm"],
        "merged_capabilities": [
            "local model profile",
            "model gateway",
            "model bootstrap",
            "offline model pack support"
        ],
        "implementation_plan": [
            "Use model_gateway and runtime_config.",
            "Add offline preseed package.",
            "Expose model profile health and switch."
        ]
    },
    "builtin.prompt_skill_engine": {
        "title": "Prompt 技能引擎模块",
        "match_tags": [("prompt_framework", 50)],
        "keywords": ["prompt engineering", "skill prompt", "instructions template"],
        "merged_capabilities": [
            "skill prompt templates",
            "task-specific instructions",
            "structured prompt policy",
            "tool-use guidance"
        ],
        "implementation_plan": [
            "Convert reference prompt patterns into owned templates.",
            "Store under agent_policy.",
            "Load templates by capability tags."
        ]
    },
    "builtin.security_sandbox": {
        "title": "安全沙箱与策略模块",
        "match_tags": [("security", 85)],
        "keywords": ["sandbox", "approval gate", "cybersecurity", "policy enforcement"],
        "merged_capabilities": [
            "sandbox policy",
            "approval gate",
            "high-risk action detection",
            "audit guard"
        ],
        "implementation_plan": [
            "Use sandbox_policy and hardcode_guard.",
            "Add enterprise configurable policies.",
            "Integrate with shell and file patch actions."
        ]
    },
    "builtin.eval_benchmark": {
        "title": "评估与基准模块",
        "match_tags": [("evaluation", 85)],
        "keywords": ["eval", "benchmark", "scoring", "quality metrics"],
        "merged_capabilities": [
            "capability scoring",
            "task success metrics",
            "regression checks",
            "quality audit"
        ],
        "implementation_plan": [
            "Use eval gateway and audit reports.",
            "Create regression tasks for agent capabilities.",
            "Track score over releases."
        ]
    },
    "builtin.ui_desktop_operator": {
        "title": "桌面 UI 操作模块",
        "match_tags": [("ui_component", 55)],
        "keywords": ["desktop", "tauri", "react frontend", "desktop app"],
        "merged_capabilities": [
            "desktop skill store",
            "replay UI",
            "runtime status UI",
            "local model setup UI"
        ],
        "implementation_plan": [
            "Use Tauri desktop app.",
            "Expose skill store and replay.",
            "Improve runtime diagnostics."
        ]
    },
    "builtin.artifact_report_engine": {
        "title": "产物与报告生成模块",
        "match_tags": [("general_skill", 30)],
        "keywords": ["artifact", "report", "document generation", "markdown output"],
        "merged_capabilities": [
            "audit report generation",
            "artifact registry",
            "downloadable outputs",
            "project delivery package"
        ],
        "implementation_plan": [
            "Use artifact registry service.",
            "Create structured report templates.",
            "Connect task completion to artifact output."
        ]
    }
}

# Priority order: specialist modules first, generic last
# This ensures browser_agent tag matches browser_operator before agent_runtime_core
MODULE_ASSIGNMENT_ORDER = [
    "builtin.security_sandbox",
    "builtin.eval_benchmark",
    "builtin.browser_operator",
    "builtin.memory_rag_core",
    "builtin.mcp_tool_hub",
    "builtin.workflow_orchestrator",
    "builtin.code_agent_core",
    "builtin.local_model_runtime",
    "builtin.ui_desktop_operator",
    "builtin.prompt_skill_engine",
    "builtin.artifact_report_engine",
    "builtin.agent_runtime_core",
]


def text_for(item):
    return " ".join([
        str(item.get("title") or ""),
        str(item.get("id") or ""),
        str(item.get("source_path") or ""),
        " ".join(item.get("tags") or []),
        " ".join(item.get("reasons") or []),
    ]).lower()


def assign_module(item):
    """Assign a skill to the best-matching builtin module.

    Strategy: score each module by (tag_weight * match) + keyword bonus,
    but process specialist modules first so niche tags win over generic ones.
    """
    tags = set(item.get("tags") or [])
    text = text_for(item)
    best_id = None
    best_score = -1
    for module_id in MODULE_ASSIGNMENT_ORDER:
        module = MODULES[module_id]
        score = 0
        for tag, weight in module["match_tags"]:
            if tag in tags:
                score += weight
        for kw in module["keywords"]:
            if kw.lower() in text:
                score += 10
        if score > best_score:
            best_score = score
            best_id = module_id
    if best_score <= 0:
        return "builtin.agent_runtime_core"
    return best_id


def main():
    grading = json.loads(GRADING.read_text(encoding="utf-8"))
    items = grading.get("items", [])
    rebuild_core = [x for x in items if x.get("grade") == "rebuild_core"]

    groups: dict[str, list] = {mid: [] for mid in MODULES}
    for item in rebuild_core:
        module_id = assign_module(item)
        groups.setdefault(module_id, []).append(item)

    modules = []
    for module_id, module_def in MODULES.items():
        refs = groups.get(module_id, [])
        refs.sort(key=lambda x: (-int(x.get("score") or 0), -int(x.get("stars") or 0)))
        modules.append({
            "id": module_id,
            "title": module_def["title"],
            "implementation_status": "planned",
            "fusion_policy": "reference_only_no_runtime_dependency",
            "source_reference_count": len(refs),
            "source_references": [
                {
                    "skill_id": x.get("id"),
                    "title": x.get("title"),
                    "source_path": x.get("source_path"),
                    "stars": x.get("stars"),
                    "score": x.get("score"),
                    "tags": x.get("tags", [])
                }
                for x in refs
            ],
            "merged_capabilities": module_def["merged_capabilities"],
            "implementation_plan": module_def["implementation_plan"],
            "acceptance_criteria": [
                "implemented in our repository",
                "no runtime dependency on external repo",
                "registered in capability registry",
                "usable by schema planner",
                "covered by audit JSON/report",
                "exposed to desktop skill store when relevant"
            ],
            "default_tools": [
                "capability.match",
                "repo_memory.search",
                "model.generate"
            ],
            "created_at": datetime.now(timezone.utc).isoformat()
        })

    assigned_count = sum(m["source_reference_count"] for m in modules)
    result = {
        "version": "c26-r2-fusion",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "description": "Fusion modules that merge all rebuild_core reference repositories into our own builtin skill modules.",
        "source": "data/skill_brain/skill_rebuild_grading.json",
        "rebuild_core_count": len(rebuild_core),
        "assigned_reference_count": assigned_count,
        "module_count": len(modules),
        "modules": modules,
        "note": "External repositories are references only. Runtime implementation must be owned code."
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    audit = {
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "rebuild_core_count": len(rebuild_core),
        "assigned_reference_count": assigned_count,
        "module_count": len(modules),
        "module_summary": {m["id"]: m["source_reference_count"] for m in modules},
        "top_modules": sorted(
            [
                {
                    "id": m["id"],
                    "title": m["title"],
                    "source_reference_count": m["source_reference_count"],
                    "top_sources": m["source_references"][:5]
                }
                for m in modules
            ],
            key=lambda x: -x["source_reference_count"]
        )
    }
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    summary = {
        "rebuild_core_count": len(rebuild_core),
        "assigned_reference_count": assigned_count,
        "module_count": len(modules),
        "module_summary": {m["id"]: m["source_reference_count"] for m in modules}
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
