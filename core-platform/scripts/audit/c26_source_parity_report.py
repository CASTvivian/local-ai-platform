import json
from pathlib import Path

audit_path = Path("core-platform/data/agent_core_audit/c26/source_parity/c26_source_parity_audit_lite.json")
data = json.loads(audit_path.read_text(encoding="utf-8"))

rows = []
for r in data["rows"]:
    rows.append(
        f"| {r['id']} | {r['status']} | {r['ours_score']} | {', '.join(r['ours_hits']) or '-'} | {', '.join(r['claude_hits']) or '-'} | {', '.join(r['claw_hits']) or '-'} | {r['high_risk_gap']} |"
    )

report = f"""# C26 Source Parity Audit Lite

## Roots

```json
{json.dumps({
  "current_root": data["current_root"],
  "claude_roots": data["claude_roots"],
  "claw_roots": data["claw_roots"],
  "claude_file_counts": data["claude_file_counts"],
  "claw_file_counts": data["claw_file_counts"]
}, ensure_ascii=False, indent=2)}
```

## Summary

```json
{json.dumps(data["summary"], ensure_ascii=False, indent=2)}
```

## Verdict

```json
{json.dumps(data["verdict"], ensure_ascii=False, indent=2)}
```

## Capability Rows

| Area | Status | Ours Score | Ours Hits | Claude Hits | Claw Hits | High Risk |
|------|--------|-----------|-----------|-------------|-----------|-----------|
{chr(10).join(rows)}

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
"""

Path("core-platform/docs/reports/C26_SOURCE_PARITY_AUDIT_LITE.md").write_text(report, encoding="utf-8")
print("report written")
