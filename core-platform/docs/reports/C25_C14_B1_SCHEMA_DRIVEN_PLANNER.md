# C25-C14-B1 Schema-driven Planner Foundation

## Goal

Move planner direction away from hardcoded keyword/intent routing toward schema-driven planning.

## Architecture Change

```
Before (legacy):
  build_plan(message)
    → _keyword_plan()  (hardcoded Chinese keywords)
    → _llm_plan()      (LLM planner via model gateway)
    → _fallback_local_chat()

After (C25-C14-B1):
  build_plan(message)
    → build_plan_schema_first()     [DEFAULT]
        → build_schema_plan()       (schema_planner.py)
            → _call_planner_model() (optional LLM, env-gated)
            → _schema_only_default_plan() (capability.match → repo_memory.search → model.generate)
    → build_plan_legacy()           [FALLBACK only]
        → _keyword_plan()           (LEGACY, marked planner_mode=legacy)
        → _llm_plan()
        → _fallback_local_chat()

  MAOMIAI_LEGACY_PLANNER=1 → force legacy chain for rollback/debug
```

## New Files

| File | Purpose |
|------|---------|
| `data/agent_policy/planner_tool_schema.json` | Tool/capability schema registry (10 tools, 8 capabilities) |
| `app/planning/schema_loader.py` | Load schema, list tool names, compact for prompt |
| `app/planning/schema_planner.py` | Schema-driven planner engine |

## Modified Files

| File | Change |
|------|--------|
| `app/planner.py` | `build_plan()` defaults to schema-driven; legacy chain renamed to `build_plan_legacy()` |

## Key Design Decisions

1. **No keyword parsing in schema planner**: `_schema_only_default_plan()` uses only schema-level tool descriptions, never parses user query for business entities
2. **capability.match first step**: Every request starts by matching against the capability schema, which discovers the right tools at execution time
3. **Optional LLM enhancement**: `MAOMIAI_SCHEMA_PLANNER_MODEL=1` enables planner model for richer plans (off by default)
4. **Explicit legacy marking**: All legacy paths tag output with `planner_mode=legacy_rule_forced` or `planner_mode=legacy_rule_fallback`
5. **Rollback via env var**: `MAOMIAI_LEGACY_PLANNER=1` forces the old keyword/LLM chain

## Validation Results

- ✅ py_compile passed for all 3 new/modified files
- ✅ `build_schema_plan()` returns `planner_mode=schema_driven` for all test inputs
- ✅ `build_plan()` public API returns `planner_mode=schema_driven` by default
- ✅ `MAOMIAI_LEGACY_PLANNER=1` correctly forces legacy path with `planner_mode=legacy_rule_forced`
- ✅ Schema loads: 10 tools, 8 capabilities
- ✅ Legacy body retained and marked for B2 cleanup

## Schema Summary

**10 Tools**: time.now, time.date_math, repo_memory.search, capability.match, web.search, weather.query, model.generate, filesystem.read, filesystem.write, shell.exec

**8 Capabilities**: general.chat, project.knowledge, repo.memory, fresh.info, time.current, time.relative, weather.current, developer.task

**5 Policy Rules**:
- `runtime_code_must_not_parse_user_query_by_keywords`: true
- `planner_should_use_schema_descriptions`: true
- `executor_must_execute_plan_not_infer_user_intent`: true
- `restricted_tools_require_approval`: true
- `fallback_must_be_marked_legacy`: true

## Known Remaining Issues (for C25-C14-B2)

1. Legacy keyword rule body (`_keyword_plan`) still exists — must be removed or archived
2. Legacy `_llm_plan` and `_fallback_local_chat` still exist as fallback chain
3. `executor.py` still has tool-by-tool if/elif dispatch (not schema-driven)
4. Time/date queries return `schema_general` not `time_now` — this is correct per schema design; `capability.match` discovers the right tool at execution time

## Next: C25-C14-B2

- Move legacy planner into archived/debug-only module or delete it
- Make hardcode guard fail if planner.py contains query keyword logic
- Ensure executor executes plan only (schema-driven dispatch)
