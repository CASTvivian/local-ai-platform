# C25 Windows Latest Full Pack
## Goal
Build latest Windows MSI with all required local runtime dependencies bundled.
## Result
- Run ID: `25966166018`
- MSI: `core-platform/releases/windows-latest-full-pack/local-ai-platform-win/Local AI Platform_0.1.0_x64_en-US.msi`
- desktop_lib.exe: `core-platform/releases/windows-latest-full-pack/local-ai-platform-win/desktop_lib.exe`
- BUILD_INFO: `core-platform/releases/windows-latest-full-pack/local-ai-platform-win/BUILD_INFO.json`
## Build Details
- MSI size: 5.1 MB
- desktop_lib.exe size: 8.4 MB
- BUILD_INFO.commit: 095d69d (matches HEAD)
- Conclusion: success
## Required Bundled Resources
Checked before build:
- scripts/windows (ensure_runtime, bootstrap_runtime, start_all, stop_all, status_all)
- services/model_bootstrap_service
- services/model_gateway
- services/agent_runtime_service
- services/repo_memory_service
- services/skill_store_service
- services/workflow_store_service
- services/artifact_registry_service
- services/code_review_gate_service
- services/design_system_service
- services/document_ingestion_service
- services/agent_orchestrator
- data/runtime_config
- data/agent_policy
- data/skill_brain
- data/sandbox_policy
- data/agent_team
- data/brain_assets/manifests
- data/brain_assets/model_catalog
- data/brain_assets/reports
- data/brain_assets/video_catalog
- data/github_stars
## Pre-build Validation
- py_compile: PASS (12 modules)
- JS syntax: PASS (5 files)
- hardcode guard: PASS
- tauri resources: 28 tracked, 0 missing
- physical paths: all exist, 0 missing
- runtime config: 19 services, auto-generated
## Windows Smoke
Install MSI, then run:
```powershell
$Root = "$env:LOCALAPPDATA\Local AI Platform\maomiai-runtime"
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\bootstrap_runtime.ps1" -Action runtime_resources
powershell -ExecutionPolicy Bypass -File "$Root\scripts\windows\status_all.ps1"
curl.exe http://127.0.0.1:18131/health
curl.exe http://127.0.0.1:18080/health
curl.exe http://127.0.0.1:18125/health
curl.exe http://127.0.0.1:18121/health
curl.exe http://127.0.0.1:18126/health
curl.exe http://127.0.0.1:18100/health
```
Desktop tests:
1. 你好，请用一句话介绍你自己
2. 今天是几月几号，现在几点
3. 我们现在有哪些 Agent 和 MCP 相关仓库资产
4. 请用代码智能体检查项目文件并生成 patch
5. 帮我做浏览器自动化和网页研究
