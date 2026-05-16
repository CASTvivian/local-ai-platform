# C25 Mac Final Smoke

## Goal
Run final macOS `.app` smoke test after C25-C14 rebuild and final Mac package build.

## Checks
- open `.app`
- service health
- `/agent/run`
- `/agent/team/run`

## Result

### Service Health (7/7 PASS)

| Service | Port | Status |
|---------|------|--------|
| ollama | 11434 | ✅ ok |
| model_gateway | 18080 | ✅ ok |
| model_bootstrap | 18100 | ✅ ok |
| skill_store | 18121 | ✅ ok |
| repo_memory | 18125 | ✅ ok |
| workflow_store | 18126 | ✅ ok |
| agent_runtime | 18131 | ✅ ok |

### Agent Run Tests (3/3 PASS)

| Test ID | Message | Result |
|---------|---------|--------|
| chat | 你好，请用一句话介绍你自己 | ✅ Qwen 自我介绍 |
| time | 今天是几月几号，现在几点 | ✅ 返回时间 |
| repo | 我们现在有哪些 Agent 和 MCP 相关仓库资产 | ✅ repo_memory.search |

### Team Run Test (1/1 PASS)

| Test | Result |
|------|--------|
| default_local_team | ✅ Researcher + Builder + Reviewer 全部返回 |

## Summary JSON

```text
core-platform/data/agent_core_audit/c25/final/c25_mac_final_smoke.json
```

## Verdict

**ALL PASS** — Mac final build smoke test passed.

## Next

If this passes, proceed to Windows MSI final build and smoke.
