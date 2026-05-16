# C25-C14-B2 Legacy Planner Isolation

## Goal

Remove legacy rule routing from public `planner.py`.  Isolate all keyword-matching, LLM planner bridge, and fallback logic into a separate legacy module.

## Implemented

### Files Changed

| File | Action |
|------|--------|
| `app/planner.py` | Rewritten — schema-first only, no legacy code |
| `app/planning/legacy_rule_planner.py` | **New** — isolated legacy functions |
| `data/agent_policy/hardcode_guard.json` | Updated — legacy file in allowed_files |
| `data/agent_core_audit/c25/schema_planner/c25_c14_b2_legacy_planner_isolation.json` | **New** — audit record |

### Functions Moved to `legacy_rule_planner.py`

1. `_keyword_plan()` — hardcoded Chinese query keyword matching
2. `_llm_plan()` — LLM planner bridge
3. `_fallback_local_chat()` — final fallback to model.generate
4. `build_plan_legacy()` — composite legacy chain (keyword → LLM → fallback)
5. `normalize_query()` (duplicate) — entity alias normalization

### planner.py After Isolation

- `normalize_query()` — retained (shared policy-based normalization)
- `_schema_plan_to_agent_plan()` — schema plan → AgentPlan converter
- `_schema_error_fallback_plan()` — NEW: schema error fallback (NOT legacy)
- `build_plan_schema_first()` — schema-driven entry (no legacy fallback)
- `build_plan()` — public API, schema-first default, legacy only via env

### Key Behavioral Change

**Before (C25-C14-B1):** `build_plan_schema_first()` would fall through to `build_plan_legacy()` if schema planner produced no steps.

**After (C25-C14-B2):** `build_plan_schema_first()` falls through to `_schema_error_fallback_plan()` which simply delegates to `model.generate`.  Legacy is only reachable through `MAOMIAI_LEGACY_PLANNER=1`.

### Hardcode Guard

- `check_runtime_no_hardcode.py` **PASSES** — planner.py is clean
- `legacy_rule_planner.py` added to `allowed_files` (keyword rules are expected there)
- planner.py docstring mentions forbidden patterns for documentation only (not in code)

## Validation

| Check | Result |
|-------|--------|
| py_compile planner.py | ✅ PASS |
| py_compile legacy_rule_planner.py | ✅ PASS |
| py_compile schema_loader.py | ✅ PASS |
| py_compile schema_planner.py | ✅ PASS |
| Default build_plan → schema_driven | ✅ PASS (3 test inputs) |
| MAOMIAI_LEGACY_PLANNER=1 → legacy_rule_forced | ✅ PASS |
| planner.py code has no legacy functions | ✅ PASS |
| Hardcode guard structural check | ✅ PASS |
| Executor has no query parsing | ✅ PASS (0 matches) |

## Executor Audit

Executor (`app/executor.py`) does NOT infer user intent. It:
- Executes tools from `plan.tools` list in order
- Dispatches by tool name to specific handlers
- Never parses user query text for routing decisions

Risk: **LOW** — executor is a pure step executor, not a planner.

## Remaining

- C25-C14-B3: Make schema planner more intelligent (model-based capability matching without code keyword parsing)
- Consider removing `legacy_rule_planner.py` entirely after migration stabilization period
- Schema planner default still uses broad `capability.match → repo_memory.search → model.generate` pattern
