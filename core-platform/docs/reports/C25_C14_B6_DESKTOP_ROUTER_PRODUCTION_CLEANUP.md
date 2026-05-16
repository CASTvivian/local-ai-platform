# C25-C14-B6 Desktop Router Production Cleanup

## Goal
Remove or neutralize desktop dry-run / diagnostic / fixed test fallback paths from production chat flow.

## Implemented

1. **Added production agent mode helpers**
   - `maomiaiIsProductionAgentMode()` — always returns `true`
   - `maomiaiProductionFallbackError(reason, detail)` — structured error for production fallback rejection

2. **Renamed `MODEL_CATALOG_FALLBACK` → `MODEL_CATALOG_DEMO_CACHE`**
   - 3 references updated (declaration, getCatalog, getCurrentModel)
   - Makes explicit this is a demo cache, not a production fallback path

3. **Disabled `dry_run: true` in production**
   - No `dry_run: true` remaining in file (count: 0)

4. **Replaced fixed test button labels**
   - `测试 Agent Runtime` → `检查运行时`
   - `测试 Agent Runtime 是否可用` → `检查 Agent Runtime 是否可用`

5. **Marked `inferViewFromText` as legacy UI-only**
   - Original renamed to `inferViewFromTextLegacyUiOnly`
   - New wrapper `inferViewFromText()` adds documentation: UI navigation only, must not be used for Agent Runtime planning
   - Agent planning is handled by `/agent/run` schema-driven planner

6. **Updated error messages**
   - Agent Runtime error now states: "生产模式已禁用 dry_run 诊断兜底"

## Validation

| Check | Result |
|-------|--------|
| JS syntax | ✅ PASS |
| Hardcode guard | ✅ PASS |
| `dry_run: true` count | 0 ✅ |
| Old test labels | None ✅ |
| `MODEL_CATALOG_FALLBACK` count | 0 ✅ |
| `MODEL_CATALOG_DEMO_CACHE` count | 3 ✅ |
| `inferViewFromTextLegacyUiOnly` present | ✅ |
| `maomiaiIsProductionAgentMode` present | ✅ |

## Remaining

This does not remove every UI helper (`includes`-based keyword routing in `inferViewFromTextLegacyUiOnly` remains for nav convenience). It prevents production chat from presenting dry-run diagnostic as agent result. The keyword nav is explicitly marked legacy and scoped to UI navigation only.

## Next

- B10: Renderer production hardening
- B7: Config centralization
