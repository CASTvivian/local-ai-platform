# C25 Windows Final Smoke Prep

## Goal
Build latest Windows MSI for final smoke test.

## Build Status: SUCCESS ✅

| Item | Value |
|------|-------|
| Commit | `72f13f4` |
| Run ID | 25965706969 |
| Run URL | https://github.com/CASTvivian/local-ai-platform/actions/runs/25965706969 |
| Conclusion | **success** |
| MSI Size | 5.1 MB |
| desktop_lib.exe | 8.4 MB |
| BUILD_INFO.commit | `72f13f4` ✅ (matches HEAD) |

## Fix Applied
- Removed `data/capability_registry` from `tauri.conf.json` resources (was gitignored, causing Windows CI build failure)
- `capability_registry` directory is auto-created at runtime by `registry.py` line 33: `root.mkdir(parents=True, exist_ok=True)`

## Pre-Build Checks
| Check | Result |
|-------|--------|
| py_compile (9 core modules) | PASS |
| JS syntax (4 files) | PASS |
| hardcode guard | PASS |
| Tauri resources (28 tracked) | PASS |
| runtime config regenerate (19 services) | PASS |

## Windows Real Machine Test

Install MSI, then run:

```powershell
$Root = "$env:LOCALAPPDATA\Local AI Platform\maomiai-runtime"

# Step 1: Bootstrap runtime resources
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\bootstrap_runtime.ps1" -Action runtime_resources

# Step 2: Check all service status
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\status_all.ps1"

# Step 3: Health checks
curl.exe http://127.0.0.1:18131/health
curl.exe http://127.0.0.1:18080/health
curl.exe http://127.0.0.1:18125/health
curl.exe http://127.0.0.1:18121/health
curl.exe http://127.0.0.1:18126/health
curl.exe http://127.0.0.1:18100/health
```

## Desktop App Smoke Test

Open desktop app and test:

1. **基础对话**: 你好，请用一句话介绍你自己
2. **时间能力**: 今天是几月几号，现在几点
3. **技能搜索**: 我们现在有哪些 Agent 和 MCP 相关仓库资产
4. **代码智能体**: 请用代码智能体检查项目文件并生成 patch

## Expected Results

- ✅ runtime_resources ok
- ✅ 18131 health ok
- ✅ agent runtime answer ok
- ✅ builtin.code_agent_core approval gate triggers for high-risk execution
- ✅ Memory RAG and Browser Operator available via capability registry

## Diagnostic Script (Post-Install)

```powershell
$Root = "$env:LOCALAPPDATA\Local AI Platform\maomiai-runtime"
Write-Host "== runtime resources =="
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\bootstrap_runtime.ps1" -Action runtime_resources
Write-Host "== status all =="
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\status_all.ps1"
Write-Host "== health =="
curl.exe http://127.0.0.1:18131/health
curl.exe http://127.0.0.1:18080/health
curl.exe http://127.0.0.1:18125/health
curl.exe http://127.0.0.1:18121/health
curl.exe http://127.0.0.1:18126/health
curl.exe http://127.0.0.1:18100/health
Write-Host "== logs =="
Get-Content "$Root\logs\windows\agent_runtime_service.err.log" -Tail 80 -ErrorAction SilentlyContinue
Get-Content "$Root\logs\windows\model_gateway.err.log" -Tail 80 -ErrorAction SilentlyContinue
Get-Content "$Root\logs\windows\repo_memory_service.err.log" -Tail 80 -ErrorAction SilentlyContinue
```

## Milestone Context

This is the **productization phase** entry point. Claude/Claw-style core capability alignment is **COMPLETE** (14/14 covered, 0 partial, 0 gap, 0 high_risk). The project is now defined as:

> 不是 Claude/Claw 的复制版，而是吸收 Claude/Claw 核心能力后，重构成我们自己的本地 AI Agent 平台。

Next steps after real-machine smoke:
1. C26-OFFLINE-MODEL-PACK
2. Mac/Win dual-platform final packaging
3. Demo script for roadshows
4. External messaging: 自有化本地 AI Agent 平台
