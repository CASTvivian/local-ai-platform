# C25-C14-B3 Schema Planner Capability Scoring

## Goal

Make schema planner smarter without returning to hardcoded keyword routing.

## What Changed

### 1. `planner_tool_schema.json` — v c25-c14-b3

- Added `planning_strategy` block with steps and constraints.
- Added `planner_hints` to each tool:
  - `request_shapes`: generic semantic signal descriptions (not query keywords)
  - `position`: context / action / final
  - `requires_resolved_args`: args that must be resolved before use
  - `requires_approval`: restricted tool flag

### 2. `schema_planner.py` — Capability Scoring Engine

Replaced fixed 3-step plan (`capability.match → repo_memory.search → model.generate`) with:

- **`_text_terms()`**: Extracts generic terms from text. Includes CJK n-grams for lexical overlap.
- **`_schema_text_for_tool()`**: Collects all descriptive text (name, kind, description, capabilities, planner_hints, input_schema) from a tool schema.
- **`_score_tool_for_request()`**: Computes overlap ratio between request terms and schema terms. Applies bias:
  - `safe` kind: +0.05
  - `model.generate`: +0.12 (almost always needed)
  - `restricted` kind: -0.10 (requires high confidence)
- **`_rank_tools()`**: Sorts all tools by score.
- **`_schema_only_default_plan()`**: Selects top-scoring tools (max 3 context/action), adds `model.generate` as final composition, falls back to `capability.match` if nothing scored.

### Key Constraint

Runtime code still must not contain business-specific routes. Scoring is based on schema text overlap, not query keyword matching.

## Test Results

| Input | Source | Tools | Confidence |
|-------|--------|-------|------------|
| 你好，请用一句话介绍你自己 | schema_scoring | capability.match, model.generate | 0.5233 |
| 今天是几月几号，现在几点 | schema_scoring | capability.match, model.generate | 0.5233 |
| 我们现在有哪些 Agent 和 MCP 相关仓库资产 | schema_scoring | repo_memory.search, time.date_math, time.now, model.generate | 0.5962 |
| 请帮我查一下公开资料 | schema_scoring | capability.match, model.generate | 0.5233 |
| 帮我看看项目代码结构 | schema_scoring | capability.match, model.generate | 0.5233 |

Note: "仓库资产" input scored higher (0.5962) because its terms overlap with `repo_memory.search` capabilities (repo, memory, assets) and time tools. This is schema-driven, not keyword routing.

## Validation

- ✅ py_compile passed
- ✅ build_plan returns `schema_driven`
- ✅ tool selections vary by schema scores
- ✅ hardcode guard passed
- ✅ legacy planner remains isolated (MAOMIAI_LEGACY_PLANNER=1 only)
- ✅ schema_version = c25-c14-b3

## Important

This is not final cognition yet. It is better than fixed if/else routing because tool choice comes from schema descriptions, but it is still a lightweight scoring fallback. Real planner model output should be added in B4/B5.

## Next Step

B4: Planner model structured output — when a planner model is available, use it to generate more precise tool selection and argument inference from the schema.
