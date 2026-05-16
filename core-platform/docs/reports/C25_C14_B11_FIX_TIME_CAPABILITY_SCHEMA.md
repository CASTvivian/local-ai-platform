# C25-C14-B11-FIX Time Capability Schema

## Problem

After B11, `registry.py` no longer had hardcoded Chinese keyword scoring, but the external capability schema (`capability_registry.json`) missed explicit time/date capabilities. This caused requests such as "现在几点" and "今天是几月几号" to rely on weak lexical overlap and not reliably match `time.current`.

## Fix

Added two external schema capabilities to `data/agent_policy/capability_registry.json`:

### time.current
- **id**: `time.current`
- **name**: 本地时间日期能力
- **type**: tool
- **description**: Read current local date, time, timezone, clock information, and host machine current time.
- **runtime**: mcp
- **target**: time.now
- **aliases**: time, date, clock, now, current time, current date, local time, local date, 几点, 时间, 日期, 现在几点, 当前时间, 今天
- **priority**: 95
- **tags**: time, date, clock, now, current

### time.relative
- **id**: `time.relative`
- **name**: 相对日期计算能力
- **type**: tool
- **description**: Calculate relative date or date offset after planner resolves the offset argument.
- **runtime**: mcp
- **target**: time.date_math
- **aliases**: relative date, date offset, days later, days before, date math, 几天后, 几天前, 相对日期, 日期计算
- **priority**: 90
- **tags**: time, date, relative, offset, calculation

Also synced runtime cache at `data/capability_registry/capabilities.json`.

**No Python runtime keyword table was added.** `registry.py` remains clean — no Chinese keyword scoring code.

## Validation

| Check | Result |
|-------|--------|
| py_compile registry.py | ✅ PASS |
| capability_count | 14 |
| schema_version | c25-c14-b11-fix-time-capability |
| time.current in list_capabilities | ✅ PASS |
| time.relative in list_capabilities | ✅ PASS |
| "现在几点" → top match | ✅ time.current (priority 95) |
| "今天是几月几号" → top match | ✅ time.current (priority 95) |
| hardcode guard | ✅ PASS |
| registry.py has no Chinese keyword table | ✅ CONFIRMED |

### Match Results

| Input | Top Match |
|-------|-----------|
| 现在几点 | time.current (95) |
| 今天是几月几号 | time.current (95) |
| 请帮我分析代码结构 | code.standard (85) |
| 我们有哪些项目资产 | repo.memory (95) |

## Note on Scoring

Current scoring uses lexical term overlap + CJK n-gram matching. Short queries like "现在几点" produce many small n-grams, causing several capabilities to share the same base score. The `priority_bonus` (0.095 for priority=95) provides tiebreaking but is small. B4 (Planner Model Structured Output) will improve this significantly by using an LLM to select the right capability instead of relying on term overlap alone.

## Files Changed

- `core-platform/data/agent_policy/capability_registry.json` — added time.current, time.relative, bumped version
- `core-platform/data/capability_registry/capabilities.json` — synced runtime cache
- `core-platform/data/agent_core_audit/c25/schema_planner/c25_c14_b11_fix_time_capability_schema.json` — audit JSON
- `core-platform/docs/reports/C25_C14_B11_FIX_TIME_CAPABILITY_SCHEMA.md` — this report

## Next

Proceed to **C25-C14-B4: Planner Model Structured Output** — use schema + LLM planner to produce plan steps and arguments, avoid runtime query if/else.
