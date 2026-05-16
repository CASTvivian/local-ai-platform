# C25-C14-B4 Planner Model Structured Output

## Goal

Move schema planner closer to real agent planning.

### Before B4
- Schema planner defaulted to lexical scoring fallback.
- Planner model path existed but was disabled unless env var explicitly enabled (`1`, `true`, `yes`, `on`).
- Model output was not validated against tool schema — unknown tools could leak into plans.
- No JSON extraction from freeform model text.

### After B4
- Planner model structured output is attempted by default (`auto` mode).
- Model output is normalized against available tool schema:
  - Unknown tools are discarded.
  - `args` must be `object`, else defaulted to `{}`.
  - `steps` must be `list`, else plan rejected.
  - `depends_on` must be `list`, else defaulted to `[]`.
- If model output is missing `model.generate`, it is auto-appended.
- Schema scoring fallback remains when model gateway is unavailable.
- Freeform model text is handled by `_extract_json_object`.

## Implemented

### New Functions
- `_extract_json_object(text)` — Extract JSON from freeform model output (handles wrapped text, markdown fences, etc.)
- `_normalize_model_plan(obj, schema)` — Validate and normalize model output against tool schema:
  - Validates `steps` is a list
  - Filters out unknown tools
  - Auto-appends `model.generate` if missing
  - Clamps confidence to [0.0, 1.0]
  - Returns `None` if no valid steps remain

### Modified Functions
- `_call_planner_model(prompt, schema)` — Now takes `schema` parameter:
  - Default mode changed from empty string to `auto`
  - Disable with `MAOMIAI_SCHEMA_PLANNER_MODEL=off` (or `0`, `false`, `no`, `disabled`)
  - Output is normalized via `_normalize_model_plan`
  - Uses `_extract_json_object` for string responses

### Source Identifier
- Model-generated plans now use `source: "schema_model_structured"` (was `"schema_model"`)
- Schema scoring fallback still uses `source: "schema_scoring"`

## Validation

| Test | Result |
|------|--------|
| py_compile | PASS |
| `_normalize_model_plan` valid input | PASS |
| `_normalize_model_plan` unknown tool rejection | PASS |
| `_extract_json_object` various formats | PASS |
| `build_schema_plan` returns `schema_driven` | PASS |
| `build_schema_plan` fallback to schema_scoring | PASS |
| Hardcode guard | PASS |

### Runtime Test Results (no model gateway)

| Input | Source | Tools |
|-------|--------|-------|
| 你好，请用一句话介绍你自己 | schema_scoring | capability.match, model.generate |
| 今天是几月几号，现在几点 | schema_scoring | capability.match, model.generate |
| 我们现在有哪些 Agent 和 MCP 相关仓库资产 | schema_scoring | repo_memory.search, time.date_math, time.now, model.generate |
| 帮我分析这个项目的架构 | schema_scoring | capability.match, model.generate |
| 请查一下公开资料 | schema_scoring | capability.match, model.generate |

> Note: All tests fall back to `schema_scoring` because model gateway is not running in test environment. When model gateway is healthy, plans will use `schema_model_structured` source.

## Configuration

| Env Var | Default | Values |
|---------|---------|--------|
| `MAOMIAI_SCHEMA_PLANNER_MODEL` | `auto` | `auto` (attempt model, fallback scoring), `off`/`0`/`false`/`disabled` (skip model) |

## Remaining

B4 depends on model_gateway health. If model_gateway is down, schema scoring fallback still runs.

### Next P0 Items
- **B12**: Remove executor capability.status hardcoding
- **B9**: Executor dispatch registry
- **B6**: Desktop fallback cleanup
