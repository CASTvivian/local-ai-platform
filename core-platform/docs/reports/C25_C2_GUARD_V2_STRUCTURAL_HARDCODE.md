# C25-C2-GUARD-V2 Structural Runtime Hardcode Guard

## Status

Implemented.

## Change

The old guard only blocked selected concrete words.
This version blocks structural anti-patterns:
- string literals in conditions over user-query variables
- string literals in comparisons or membership tests over user-query variables
- runtime routing literal assignments such as alias, keyword, pattern, or typo tables
- JS/TS/Rust includes-based query routing
- business/entity/question/date literals inside runtime code

## Principle

Runtime code must not decide behavior from hardcoded user phrases.

Allowed runtime code:
- tool schema
- capability schema
- provider adapter
- validator
- executor
- sandbox
- permission policy
- store/replay

Disallowed runtime code:
- if user says X then do Y
- if a city/product/game/company/date phrase appears then do Y
- hardcoded phrase lists for intent routing
- entity alias tables in runtime

Concrete phrases/entities belong in:
- external policy/config
- memory/retrieval
- provider result
- model planner output
- tests/docs
