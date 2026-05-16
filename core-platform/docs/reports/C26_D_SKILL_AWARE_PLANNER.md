# C26-D Skill-aware Planner

## Goal

Let planner discover default skills during planning, so the system can proactively leverage C26-B's 147 default skills when answering user queries.

## Implemented

`schema_planner.py` now ensures a `capability.match` context step is present in **both** planning paths:

### New Functions

1. **`_skill_context_steps(message)`** — Generates a `capability.match` step with `include_skills: True` for skill discovery.
2. **`_ensure_skill_context(message, steps)`** — Prepends a capability.match step only if one is not already present in the plan (deduplication).

### Integration Points

1. **Schema scoring path** (`_schema_only_default_plan`) — `_ensure_skill_context` is called before final model.generate composition, replacing the old conditional fallback that only added capability.match when nothing else scored.
2. **Model structured output path** (`_normalize_model_plan`) — `_ensure_skill_context` is applied to model-generated steps so the planner model cannot accidentally omit skill discovery.

### Design Principles

- **No keyword routing**: No hardcoded Chinese/English query words.
- **No query-type branching**: Uses the same `capability.match` mechanism for all queries.
- **Deduplication**: If a step already includes `capability.match`, no duplicate is added.
- **Schema-driven**: Skill discovery goes through the existing capability registry which already includes `skill.*` from C26-B.

## Validation

All 5 test queries passed:

| Query | Tools | Skill Matches |
|-------|-------|---------------|
| 有没有 Claude Code 相关技能 | weather.query, capability.match, time.date_math, model.generate | 8 (incl. everything-claude-code) |
| 有哪些 MCP 工具 | repo_memory.search, capability.match, model.generate | 5 |
| 找一个适合浏览器自动化的仓 | capability.match, model.generate | 2 (incl. Mano P) |
| 我想做一个代码智能体，应该用哪些仓 | capability.match, model.generate | 2 (incl. Hello agents) |
| 有没有本地模型相关技能 | capability.match, model.generate | 1 |

- ✅ `capability.match` present in all plans
- ✅ `skill.*` matches returned for all queries
- ✅ Hardcode guard passed
- ✅ py_compile passed

## Meaning

Default repository assets are now not only listed as skills — they are **discoverable by the planner** through the capability context path. This closes the loop: brain assets → default skills → capability registry → planner context → execution.

## Next

C26-C: Desktop Skill Store — show default skills in the UI with details and enable/disable controls.
