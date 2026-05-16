# C25-C14-B10 Renderer Data-driven Templates

## Goal
Remove task_type/intent-specific answer rendering branches from renderer.py.

## Before
renderer.py had **9 hardcoded intent branches**:
- `time_now`, `date_math`, `weather`, `restricted_action`, `web_fact`
- `project_knowledge`, `catalog_knowledge`
- `project_architecture_services`, `project_architecture_capabilities`, `project_architecture_summary`
- `capability_status`, `local_chat`

Each branch contained fixed Chinese text templates and intent-specific rendering logic.

## Implemented

### 1. External renderer templates
- **File**: `data/agent_policy/renderer_templates.json`
- **Version**: `c25-c14-b10`
- Contains `default` templates (empty, tool_error, model_unavailable)
- Contains `tool_summaries` templates for 11 tool types

### 2. Rewritten renderer.py
Data-driven rendering with priority chain:
1. `model.generate` tool result (preferred — final model answer)
2. All successful tool results rendered with external templates
3. Error information from failed tools
4. Default empty template

Key design:
- No `if plan.intent ==` branches
- Templates loaded from external JSON with cache
- `_text_from_value()` extracts text from various result formats
- `_format_template()` applies template with `{text}` placeholder
- Backward-compatible `render_answer(plan, results)` signature preserved

### 3. Bug fix in `_format_template`
Fixed duplicate `text` keyword argument when payload dict also contains `text` key.
Solution: filter `text` from safe_payload before `**kwargs` expansion.

## Validation

| Test | Result |
|------|--------|
| py_compile | ✅ PASS |
| templates version | ✅ c25-c14-b10 |
| model.generate preferred | ✅ PASS |
| repo_memory.search template | ✅ PASS |
| weather.query template | ✅ PASS |
| time.now template | ✅ PASS |
| error handling | ✅ PASS |
| empty results | ✅ PASS |
| multiple tools | ✅ PASS |
| render_tool_result standalone | ✅ PASS |
| capability.status template | ✅ PASS |
| hardcode guard | ✅ PASS |

## Audit

| Metric | Before | After |
|--------|--------|-------|
| task_type/intent matches | 75 | 2 (comments only) |
| if/elif intent branches | 9 | 0 |
| fixed Chinese text strings | ~20 | 0 (moved to templates) |

## Files Changed
- `services/agent_runtime_service/app/renderer.py` — rewritten
- `data/agent_policy/renderer_templates.json` — new
- `data/agent_policy/hardcode_guard.json` — added renderer_templates.json
- `data/agent_core_audit/c25/schema_planner/c25_c14_b10_renderer_data_driven_templates.json` — audit
