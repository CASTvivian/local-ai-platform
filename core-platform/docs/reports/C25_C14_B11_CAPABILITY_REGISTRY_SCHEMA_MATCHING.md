# C25-C14-B11 Capability Registry Schema-driven Matching

## Problem

The fixed logic audit found that `capability/registry.py` used hardcoded Chinese keyword scoring tables (lines 235-249 in the old version):

```python
if any(keyword in normalized_query for keyword in ["代码", "编程", "bug", "报错", "开发"]):
    if "code" in capability.tags:
        score += 30
if any(keyword in normalized_query for keyword in ["推理", "分析", "判断", "策略"]):
    if "reasoning" in capability.tags:
        score += 30
# ... 5 more keyword groups with score += 30/35
```

This is a textbook case of hardcoded user-question routing via Chinese keyword tables.

## Fix

### 1. External capability registry schema

Created `data/agent_policy/capability_registry.json` with:
- 12 capabilities with full metadata
- `aliases` field for each capability (bilingual)
- No scoring bias values in the schema
- Version `c25-c14-b11`

### 2. Rewrote `capability/registry.py`

- **Removed**: All 5 hardcoded Chinese keyword scoring blocks (`score += 30/35`)
- **Added**: `_terms()` — generic term extraction with CJK n-gram support
- **Added**: `_capability_text()` — collects all descriptive text from capability + aliases
- **Added**: Schema-driven `match_capabilities()` using lexical overlap scoring
- **Kept**: All backward-compatible functions with same signatures:
  - `load_capabilities()` → `List[Capability]`
  - `list_capabilities(enabled_only)` → `List[dict]`
  - `get_capability(id)` → `Optional[Capability]`
  - `save_capabilities(items)`
  - `upsert_capability(capability)`
  - `match_capabilities(query, intent, tags, limit)` → `List[Capability]`

### 3. Scoring method

```
base_score = |overlap(query_terms, cap_text_terms)| / min(|query_terms|, |cap_text_terms|)
tag_bonus   = 0.1 per matching explicit tag
intent_bonus = 0.15 if intent terms overlap capability terms
priority_bonus = priority / 1000 (tiebreaker, 0.04–0.095 range)
```

No fixed bias values. No hardcoded keyword lists in Python.

## Validation

| Check | Result |
|-------|--------|
| py_compile | ✅ OK |
| capability_count | 12 |
| list_capabilities | ✅ Returns all 12 |
| match_capabilities | ✅ Returns ranked list |
| get_capability | ✅ Returns by ID |
| hardcode guard | ✅ Passed |
| Chinese keyword grep | ✅ No fixed keyword table |

### Match test results

| Query | Top match | 2nd match | 3rd match |
|-------|-----------|-----------|-----------|
| 请帮我分析代码结构 | code.standard | reasoning.standard | repo.memory |
| 我们有哪些项目资产 | repo.memory | code.standard | web.search |
| 帮我查公开资料 | browser.fetch | web.search | repo.memory |
| 现在几点 | repo.memory | web.search | weather.query |

### Note on "现在几点"

The query "现在几点" currently matches repo.memory/web.search/weather.query because no `time.current` capability is registered. This is a data gap, not a code issue. Adding a time capability to the schema would fix it. The B4 planner-model step would also handle this.

## Files Changed

| File | Action |
|------|--------|
| `data/agent_policy/capability_registry.json` | Created |
| `services/agent_runtime_service/app/capability/registry.py` | Rewritten |
| `data/agent_policy/hardcode_guard.json` | Updated (added capability_registry.json to allowed_files) |
| `data/agent_core_audit/c25/schema_planner/c25_c14_b11_capability_registry_schema_matching.json` | Created |

## Remaining

This is still lexical schema matching, not full planner-model reasoning.
The next step should be B4: planner model structured output.
