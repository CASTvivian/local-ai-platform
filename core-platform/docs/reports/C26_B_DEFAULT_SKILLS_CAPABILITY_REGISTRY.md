# C26-B Default Skills into Capability Registry

## Goal
Make generated default skills available to capability matching so that queries like "有哪些 MCP 工具" or "浏览器自动化相关能力" can match skill-brain assets via `capability.match`.

## Implemented

### New functions in `capability/registry.py`

1. **`_default_skills_path()`** — resolves path to `data/skill_brain/default_skills.json`
2. **`load_default_skills()`** — loads enabled skills from JSON, returns list of dicts
3. **`_skill_to_capability(skill)`** — converts a skill dict to a capability dict with:
   - `id`: `skill.<skill_id>` prefix
   - `type`: `default_skill`
   - `runtime`: `skill_brain`
   - `metadata`: source_type, source_path, source_repo, html_url, skill_tags, tools, risk, language, stars, original_tags, buckets

### Modified functions

4. **`list_capabilities()`** — now appends default skills (deduped by id) to the capability list
5. **`match_capabilities()`** — now includes default skills in the candidate pool and enriches alias_map with skill `tags` + `original_tags`

## Validation

| Check | Result |
|-------|--------|
| py_compile | ✅ PASS |
| default_skill_count | ✅ 147 |
| skill_capability_count | ✅ 148 (1 existing + 147 new) |
| total_capability_count | ✅ 161 |
| hardcode guard | ✅ PASS |
| "有哪些 MCP 工具" | ✅ skill matches found |
| "有没有本地模型相关技能" | ✅ skill matches found |
| "浏览器自动化相关能力" | ✅ skill matches found (Mano P) |
| "代码智能体相关仓库" | ✅ skill matches found (Hello agents) |
| "Claude Code 技能" | ✅ skill matches found (everything-claude-code) |

## Architecture

```
data/skill_brain/default_skills.json
  → load_default_skills()
  → _skill_to_capability()
  → list_capabilities()  (appended, deduped)
  → match_capabilities() (pooled with schema caps, scored together)
```

Skill capabilities use `id` prefix `skill.*` to distinguish from schema capabilities.

## Meaning

Collected repositories are no longer just static memory assets.
They are now **default runtime capabilities** discoverable by `capability.match`.

## Next

- **C26-C**: Desktop Skill Store — show default skills in UI, skill detail page
- **C26-D**: Planner uses skill tags in planning context
- **C26-E**: Repo memory auto-update from skill-brain
