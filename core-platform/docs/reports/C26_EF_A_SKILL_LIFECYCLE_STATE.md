# C26-EF-A Skill Lifecycle State

## Goal
Combine automatic skill updates with user control via lifecycle state management.

## Implemented

### Generated: `data/skill_brain/skill_state.json`

Each skill now has lifecycle state:

| Field | Type | Meaning |
|-------|------|---------|
| `enabled` | bool | Skill participates in planner |
| `pinned` | bool | User pinned — gets ranking boost |
| `rating` | float/null | User or system rating |
| `usage_count` | int | How many times the skill was used |
| `last_used_at` | ISO8601/null | Last usage timestamp |
| `lifecycle` | string | `enabled` / `disabled` / `discovered` |

### Capability Registry Changes

New functions in `registry.py`:

- `load_skill_state()` — load skill lifecycle state from JSON
- `save_skill_state(state)` — persist lifecycle state
- `get_skill_state(skill_id)` — get one skill's state
- `set_skill_enabled(skill_id, enabled)` — enable/disable a skill
- `set_skill_pinned(skill_id, pinned)` — pin/unpin a skill
- `record_skill_usage(skill_id)` — increment usage count + update timestamp

Behavior changes:

- `_skill_to_capability()` merges lifecycle state into capability metadata
- `list_capabilities()` excludes disabled skills
- `match_capabilities()` gives pinned (+0.08), usage (+0.005/count, max 0.05), rating (+rating/100, max 0.05) boosts

## Validation

| Test | Result |
|------|--------|
| default_skill_count | 147 |
| skill_state_count | 147 |
| Disable skill → capability count -1 | PASS |
| Enable skill → capability count restored | PASS |
| Pin + usage recorded | PASS |
| Match returns results | PASS |
| py_compile | PASS |
| hardcode guard | PASS |

## Next

C26-EF-B: Desktop UI toggle (enabled/disabled), pin skill, show usage/rating
