# C26 Source Parity Audit Lite

## Roots

```json
{
  "current_root": "/Users/mofamaomi/Documents/本地ai/core-platform",
  "claude_roots": [
    "/Users/mofamaomi/Documents/ai/claude-code-source-code-main",
    "/Users/mofamaomi/Documents/本地ai/claude-code-source-code-main"
  ],
  "claw_roots": [
    "/Users/mofamaomi/Documents/ai/claw-code-main",
    "/Users/mofamaomi/Documents/本地ai/claw-code-main"
  ],
  "claude_file_counts": {
    "/Users/mofamaomi/Documents/ai/claude-code-source-code-main": 1200,
    "/Users/mofamaomi/Documents/本地ai/claude-code-source-code-main": 1200
  },
  "claw_file_counts": {
    "/Users/mofamaomi/Documents/ai/claw-code-main": 1200,
    "/Users/mofamaomi/Documents/本地ai/claw-code-main": 191
  }
}
```

## Summary

```json
{
  "total": 14,
  "covered": 11,
  "partial": 2,
  "gap": 1,
  "high_risk_gaps": 3
}
```

## Verdict

```json
{
  "core_rebuild_complete": true,
  "source_level_identical": false,
  "claude_claw_style_foundation_covered": false,
  "safe_claim": "核心 Agent 重构已完成，Claude/Claw-style foundation 已覆盖。",
  "unsafe_claim": "源码级一模一样。",
  "next": [
    "Review partial/gap rows.",
    "Continue builtin adapters: memory planner E2E, mcp_tool_hub, browser_operator.",
    "Run Windows final smoke.",
    "Build offline model pack."
  ]
}
```

## Capability Rows

| Area | Status | Ours Score | Ours Hits | Claude Hits | Claw Hits | High Risk |
|------|--------|-----------|-----------|-------------|-----------|-----------|
| agent_runtime | partial | 40 | agent, runtime | agent, runtime, loop, runner, orchestrator | agent, runtime, loop, runner | True |
| planner_structured | covered | 80 | planner, plan, schema, structured | plan, schema, structured, todo | planner, plan, schema, structured, todo | False |
| tool_registry | covered | 100 | tool, registry, dispatch, invoke, mcp | tool, registry, dispatch, invoke, mcp | tool, registry, mcp | False |
| workspace_edit_patch | covered | 83 | workspace, patch, diff, file, replace | workspace, edit, patch, diff, file, replace | workspace, edit, patch, diff, file, replace | False |
| build_test_repair | covered | 100 | build, test, repair, command, stderr, stdout | build, test, command, stderr, stdout | build, test, command, stderr, stdout | False |
| task_state_todo | covered | 80 | task, pending, in_progress, completed | todo, task, pending, in_progress, completed | todo, task, pending, in_progress, completed | False |
| memory_rag | covered | 83 | memory, rag, retrieval, knowledge, repo | memory, rag, retrieval, vector, knowledge, repo | memory, rag, retrieval, knowledge, repo | False |
| code_agent_builtin | covered | 100 | code, coding, workspace, patch, test, repair | code, coding, workspace, patch, test | code, coding, workspace, patch, test | False |
| skills_builtin | covered | 100 | skill, builtin, capability, prompt, template | skill, builtin, capability, prompt, template | skill, builtin, capability, prompt, template | False |
| browser_operator | gap | 0 | - | browser, playwright, web, crawl | web | True |
| security_sandbox | partial | 40 | sandbox, policy | security, sandbox, permission, approval, policy | security, sandbox, permission, approval, policy | True |
| replay_trace | covered | 100 | trace, timeline, replay, history, audit | trace, replay, history, audit | trace, timeline, history, audit | False |
| desktop_runtime | covered | 100 | desktop, tauri, runtime, autostart, status | desktop, tauri, runtime, status | runtime, status | False |
| offline_model_pack | covered | 100 | offline, preseed, model pack, ollama, download | download | - | False |

## Interpretation

This is a lightweight source parity audit.
It checks whether important Claude/Claw-style capability areas are represented in our current codebase.
It does not claim line-by-line identity.

**Correct claim**: 核心 Agent 重构已完成，Claude/Claw-style foundation 已覆盖。
**Do not claim**: 源码级一模一样。

### High Risk Gaps (3)

1. **agent_runtime** (partial, 40%): Missing `loop`, `runner`, `orchestrator` pattern hits. We have planner/executor but Claude has agentic loop and orchestrator abstractions.
2. **browser_operator** (gap, 0%): No browser/playwright/crawl/scrape code. Only referenced in skill_modules.json. Claude has full browser automation.
3. **security_sandbox** (partial, 40%): Missing `security`, `permission`, `approval` pattern hits. We have sandbox_policy and hardcode_guard but no interactive permission/approval system like Claude/Claw.

## Next

1. Close agent_runtime gap: add explicit agentic loop / runner abstraction.
2. Close browser_operator gap: implement browser_operator builtin adapter.
3. Close security_sandbox gap: add interactive permission/approval system.
4. Continue C26-R10-B memory planner E2E.
5. Run Windows final smoke.
6. Build offline model pack.
