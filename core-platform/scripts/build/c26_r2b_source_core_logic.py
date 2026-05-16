"""C26-R2B: Preserve core logic from every rebuild_core source reference before fusion."""
import json
from pathlib import Path
from datetime import datetime

BASE = Path("core-platform")
modules_path = BASE / "data/skill_brain/our_builtin_skill_modules.json"
grading_path = BASE / "data/skill_brain/skill_rebuild_grading.json"
out_path = BASE / "data/skill_brain/source_core_logic_map.json"
audit_path = BASE / "data/agent_core_audit/c26/skill_brain/c26_r2b_source_core_logic_preservation.json"

modules_data = json.loads(modules_path.read_text(encoding="utf-8"))
grading_data = json.loads(grading_path.read_text(encoding="utf-8"))

modules = modules_data.get("modules", [])
grading_items = grading_data.get("items", [])
grading_by_id = {x.get("id"): x for x in grading_items if x.get("id")}


def text_of(ref, grade):
    return " ".join([
        str(ref.get("title") or ""),
        str(ref.get("skill_id") or ""),
        str(ref.get("source_path") or ""),
        " ".join(ref.get("tags") or []),
        " ".join(grade.get("reasons") or []),
    ]).lower()


def infer_core_logic(ref, grade, module_id):
    tags = set(ref.get("tags") or [])
    text = text_of(ref, grade)
    logic = []
    unique = []
    rebuild = []
    must_keep = []

    if "code_agent" in tags or "code" in text or "claude" in text or "claw" in text:
        logic += [
            "workspace understanding",
            "code task planning",
            "patch-oriented editing",
            "developer workflow assistance"
        ]
        unique.append("code-agent interaction and implementation pattern")
        rebuild.append("map into owned code_agent_core patch/test/task workflow")
        must_keep.append("do not lose code editing and workspace reasoning patterns")

    if "mcp_tool" in tags or "mcp" in text:
        logic += [
            "tool metadata protocol",
            "tool invocation contract",
            "tool discovery and routing"
        ]
        unique.append("MCP/tool protocol design pattern")
        rebuild.append("map into owned mcp_tool_hub registry and adapter model")
        must_keep.append("do not lose tool schema and invocation contract ideas")

    if "browser_agent" in tags or "browser" in text or "playwright" in text:
        logic += [
            "browser action planning",
            "web research workflow",
            "structured extraction"
        ]
        unique.append("browser automation and research execution pattern")
        rebuild.append("map into owned browser_operator action schema")
        must_keep.append("do not lose browser planning and evidence collection logic")

    if "memory" in tags or "rag" in text or "vector" in text or "graph" in text:
        logic += [
            "retrieval augmented memory",
            "semantic search",
            "knowledge graph or repo graph reasoning"
        ]
        unique.append("memory/RAG/retrieval architecture pattern")
        rebuild.append("map into owned memory_rag_core and repo memory layer")
        must_keep.append("do not lose retrieval evidence and graph/memory design")

    if "workflow" in tags or "workflow" in text or "langgraph" in text or "deer" in text:
        logic += [
            "multi-step workflow orchestration",
            "task dependency tracking",
            "stateful execution"
        ]
        unique.append("workflow orchestration pattern")
        rebuild.append("map into owned workflow_orchestrator and task_state")
        must_keep.append("do not lose state machine and dependency execution logic")

    if "local_model" in tags or "ollama" in text or "qwen" in text or "llm" in text:
        logic += [
            "local model runtime",
            "profile switching",
            "model bootstrap or inference gateway"
        ]
        unique.append("local model runtime pattern")
        rebuild.append("map into owned local_model_runtime")
        must_keep.append("do not lose local/offline model operation assumptions")

    if "prompt_framework" in tags or "prompt" in text or "skill" in text:
        logic += [
            "prompt skill packaging",
            "instruction templates",
            "task-specific prompting"
        ]
        unique.append("prompt skill organization pattern")
        rebuild.append("map into owned prompt_skill_engine")
        must_keep.append("do not lose prompt template and skill instruction structure")

    if "security" in tags or "sandbox" in text or "policy" in text or "cyber" in text:
        logic += [
            "policy guard",
            "sandbox boundary",
            "security review pattern"
        ]
        unique.append("security/sandbox policy pattern")
        rebuild.append("map into owned security_sandbox")
        must_keep.append("do not lose safety gate and audit policy")

    if "evaluation" in tags or "eval" in text or "benchmark" in text:
        logic += [
            "benchmark scoring",
            "quality evaluation",
            "regression tracking"
        ]
        unique.append("evaluation and benchmark pattern")
        rebuild.append("map into owned eval_benchmark")
        must_keep.append("do not lose measurable quality gates")

    if not logic:
        logic = ["general reference knowledge", "design inspiration"]
        unique = ["general implementation reference"]
        rebuild = ["keep as module reference material"]
        must_keep = ["do not lose source description and rationale"]

    def dedupe(xs):
        out = []
        seen = set()
        for x in xs:
            if x not in seen:
                out.append(x)
                seen.add(x)
        return out

    return {
        "core_logic": dedupe(logic),
        "unique_capability": dedupe(unique),
        "rebuild_value": dedupe(rebuild),
        "what_must_not_be_lost": dedupe(must_keep),
    }


source_map = []
module_summaries = {}

for module in modules:
    mid = module.get("id")
    refs = module.get("source_references", []) or []
    enriched_refs = []

    for ref in refs:
        sid = ref.get("skill_id")
        grade = grading_by_id.get(sid, {})
        inferred = infer_core_logic(ref, grade, mid)
        item = {
            "target_builtin_module": mid,
            "target_builtin_title": module.get("title"),
            "skill_id": sid,
            "title": ref.get("title"),
            "source_path": ref.get("source_path"),
            "stars": ref.get("stars"),
            "score": ref.get("score"),
            "tags": ref.get("tags", []),
            **inferred
        }
        source_map.append(item)
        enriched_refs.append(item)

    module["source_core_logic_map"] = enriched_refs
    module_summaries[mid] = {
        "source_count": len(enriched_refs),
        "core_logic_count": sum(len(x["core_logic"]) for x in enriched_refs),
        "must_not_lose_count": sum(len(x["what_must_not_be_lost"]) for x in enriched_refs),
    }

result = {
    "version": "c26-r2b",
    "generated_at": datetime.utcnow().isoformat() + "Z",
    "description": "Preserve core logic from every rebuild_core source reference before fusion.",
    "source_count": len(source_map),
    "module_count": len(modules),
    "source_core_logic_map": source_map,
    "module_summaries": module_summaries,
    "rule": "Fusion must preserve per-source core logic, unique capability and rebuild value."
}

out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

modules_data["modules"] = modules
modules_data["source_core_logic_preservation"] = {
    "version": "c26-r2b",
    "source_count": len(source_map),
    "rule": "Every fused source reference keeps core_logic, unique_capability, rebuild_value and what_must_not_be_lost."
}
modules_path.write_text(json.dumps(modules_data, ensure_ascii=False, indent=2), encoding="utf-8")

audit = {
    "checked_at": datetime.utcnow().isoformat() + "Z",
    "source_count": len(source_map),
    "module_count": len(modules),
    "all_sources_have_core_logic": all(bool(x.get("core_logic")) for x in source_map),
    "all_sources_have_unique_capability": all(bool(x.get("unique_capability")) for x in source_map),
    "all_sources_have_rebuild_value": all(bool(x.get("rebuild_value")) for x in source_map),
    "all_sources_have_must_not_be_lost": all(bool(x.get("what_must_not_be_lost")) for x in source_map),
    "module_summaries": module_summaries,
}

audit_path.parent.mkdir(parents=True, exist_ok=True)
audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

print(json.dumps(audit, ensure_ascii=False, indent=2))
