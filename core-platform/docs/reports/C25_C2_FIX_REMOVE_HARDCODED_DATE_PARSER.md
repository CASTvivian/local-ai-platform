# C25-C2 Fix: Remove Hardcoded Date Parser

## Status

Implemented.

## Problem

The planner still contained deterministic date parsing:
- relative-date words
- Chinese number mapping
- regex date offsets

That kept part of the planner as rule-based routing.

## Fix

`planner.py` now:
1. Normalizes only through external `entity_aliases.json`.
2. Calls the LLM planner.
3. Accepts a structured JSON plan.
4. Falls back only to `local_chat` if the LLM planner fails.
5. Does not perform hardcoded date, business, weather, product, or project routing.

Date math is now expected from LLM planner as structured output:

```json
{
  "intent": "date_math",
  "tools": ["time.now", "time.date_math"],
  "args": {
    "offset_days": 3
  }
}
```

## Next

C25-C3 should implement observation/replan loop so the Agent can continue after tool results.
