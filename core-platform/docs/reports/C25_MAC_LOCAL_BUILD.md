# C25 Mac Local Build

## Status
✅ Local macOS package built successfully for demo testing.

## Git HEAD
`d52ce18e1dccda8febabbbe5c8d9a19633b7cf19`

## Build Fix Applied
Removed `brain_assets/repos/` (13GB git repos with permission issues) from Tauri resources.
Changed `../../../data/brain_assets` to individual subdirs:
- `../../../data/brain_assets/manifests` (376K)
- `../../../data/brain_assets/model_catalog` (8K)
- `../../../data/brain_assets/reports` (5.7M)
- `../../../data/brain_assets/video_catalog` (4K)

`repos/` is resolved at runtime via `MAOMIAI_CORE_PLATFORM_DIR` env var.

## Artifact Path
`core-platform/releases/macos-c25-latest`

## Artifacts
| File | Size |
|------|------|
| `macos/Local AI Platform.app` | 105M (bundle) |
| `dmg/Local AI Platform_0.1.0_aarch64.dmg` | 5.8M |
| `BUILD_INFO.json` | 175B |

## BUILD_INFO
```json
{
  "commit": "d52ce18e1dccda8febabbbe5c8d9a19633b7cf19",
  "built_at": "2026-05-16T01:14:41Z",
  "platform": "macos",
  "arch": "aarch64",
  "label": "c25-mac-local-build"
}
```

## Pre-Build Verification
- ✅ Git HEAD synced with origin/main
- ✅ Mac acceptance result: all 11 checks passed (ollama, model_gateway, agent_runtime, repo_memory, skill_store, workflow_store, model_bootstrap, chat, time, repo, team_run)
- ✅ Hardcode guard passed (planner route strings are intentional)
- ✅ JS syntax check passed (windows-demo-stable-router.js, windows-click-model-setup.js)
- ✅ npm install succeeded (13 packages, 0 vulnerabilities)
- ✅ Tauri build succeeded (10 warnings, 0 errors)

## Expected Test
1. Open `Local AI Platform.app`
2. Confirm local model is available through Ollama
3. Send: `你好，请用一句话介绍你自己`
4. Send: `今天是几月几号，现在几点`
5. Send: `我们现在有哪些 Agent 和 MCP 相关仓库资产`
6. Confirm Agent Runtime main chain works

## Note
The `brain_assets/repos/` directory is NOT bundled in the app.
At runtime, `MAOMIAI_CORE_PLATFORM_DIR` must point to the `core-platform/` directory
so that repo_memory_service can locate brain assets correctly.
