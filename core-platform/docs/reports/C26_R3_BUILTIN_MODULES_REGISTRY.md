# C26-R3 Builtin Modules Registry

## Goal
Expose own fusion modules as `builtin.*` capabilities in the capability registry, ranked above external-reference `skill.*` capabilities.

## Implemented

Capability registry now loads:

```
data/skill_brain/our_builtin_skill_modules.json
```

And exposes each module as:

```
builtin.code_agent_core
builtin.agent_runtime_core
builtin.mcp_tool_hub
builtin.browser_operator
builtin.memory_rag_core
builtin.workflow_orchestrator
builtin.local_model_runtime
builtin.prompt_skill_engine
builtin.security_sandbox
builtin.eval_benchmark
builtin.ui_desktop_operator
builtin.artifact_report_engine
```

### Priority

`builtin.*` modules are ranked above external-reference `skill.*` capabilities via a +0.12 score boost.

### Meaning

External repositories are now only reference sources. The planner prefers owned fusion modules.

### Changes to registry.py

1. Added `_builtin_modules_path()` — path to our_builtin_skill_modules.json
2. Added `load_builtin_modules()` — loads 12 fusion modules from JSON
3. Added `_builtin_module_to_capability()` — converts module dict to capability dict with `source_type=own_builtin_module`, `builtin=True`, `builtin_priority=1.0`
4. Modified `list_capabilities()` — appends builtin modules before skill.* entries
5. Modified `match_capabilities()` — adds builtin modules to candidate pool, adds builtin alias map from merged_capabilities and source reference tags, adds +0.12 score boost for `builtin=True`

## Validation

- py_compile: PASS
- hardcode guard: PASS
- builtin_module_count: 12
- builtin_capability_count: 12
- skill_capability_count: 148
- total_capability_count: 173
- 5/5 test queries hit builtin.* as top match:
  - "我想做代码智能体" → builtin.code_agent_core (#1)
  - "有没有 MCP 工具协议能力" → builtin.mcp_tool_hub (#1)
  - "浏览器自动化怎么做" → builtin.browser_operator (#1)
  - "本地记忆和 RAG 能力" → builtin.memory_rag_core (#1)
  - "本地模型运行能力" → builtin.local_model_runtime (#1)

## Next

C26-R4: Connect builtin modules to concrete owned implementation modules, add execution contracts for builtin modules.
