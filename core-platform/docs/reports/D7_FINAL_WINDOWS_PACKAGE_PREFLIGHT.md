# D7 Final Windows Package Preflight

## Status

Final Windows build/package evidence chain completed on May 13, 2026.

The release package itself is verified against the current `main` commit.
The local repository still has separate worktree/submodule hygiene issues listed below.

## Git Alignment

- Local HEAD: `89bffc4d7abd7888189b556e30b75b8b05ea149c`
- Remote `origin/main`: `89bffc4d7abd7888189b556e30b75b8b05ea149c`
- Result: PASS, commit pointers are aligned.

## Build

- Workflow: `build-win-release`
- Workflow run: `https://github.com/CASTvivian/local-ai-platform/actions/runs/25782616718`
- Tag label: `win-d7-final-20260513-143253`
- Conclusion: `success`
- Build `headSha`: `89bffc4d7abd7888189b556e30b75b8b05ea149c`
- Result: PASS, GitHub Actions built the same commit as local and remote `main`.

## Artifact

Downloaded to:

```text
core-platform/releases/windows-d7-final-latest
```

Files present:

- `desktop_lib.exe`
- `Local AI Platform_0.1.0_x64-setup.exe`
- `Local AI Platform_0.1.0_x64_en-US.msi`
- `BUILD_INFO.json`

`BUILD_INFO.json`:

```json
{
  "commit": "89bffc4",
  "workflow": "build-win-release",
  "built_at": "2026-05-13T06:33:59.7891887+00:00",
  "label": "win-d7-final-20260513-143253"
}
```

Result: PASS, artifact metadata matches the latest commit by short SHA.

## Runtime Capabilities Expected In This Build

- Embedded Windows bootstrap runtime
- ASCII-only PowerShell runtime
- Base64 JSON output envelope
- Base64 Chinese prompt input
- Direct Ollama inference
- Installed-only model selection
- Non-blocking model download
- Repo Memory brain assets
- Context Engine research docs

## Local Verification Passed

- Required runtime files exist.
- Required code markers exist:
  - `MAOMIAI_PROMPT_B64`
  - `generate_local_ai_response`
  - `maomiai_payload_b64`
  - Simplified Chinese system prompt
  - "测试本地推理"
  - "项目知识查询"
  - `/brain/assets`, `/brain/seed`, `/brain/search`
- `bootstrap_runtime.ps1` contains `0` non-ASCII bytes.
- JSON catalogs parse successfully.
- Desktop JavaScript syntax checks pass.
- `cargo check` passes.

`cargo check` emitted non-blocking Rust warnings related to Windows-gated code paths on macOS.

## Windows Test Checklist

1. Uninstall old Local AI Platform.
2. Remove old residual install directory if needed.
3. Install the setup EXE from the artifact directory.
4. Open the app.
5. Open Local Model page.
6. Click Check Local AI Status.
7. Confirm installed models appear.
8. Set an installed model as current.
9. Open New Chat.
10. Confirm the model selector shows installed models.
11. Send a Chinese prompt.
12. Confirm the answer displays as readable Chinese.
13. Open Project Knowledge Query.
14. Search for `MCP`, `Agent`, and `RAG`.

## Remaining Local Repository Hygiene Issues

These did not block the GitHub Windows build, but they prevent calling the local checkout fully clean:

1. Full `git status` is blocked by a corrupted local Git pack inside `LLaVA-OneVision-1.5`.
   The top-level commit alignment was verified separately, and root status was inspected with submodules ignored.
2. Root worktree differences were observed locally:
   - `core-platform/apps/desktop/src-tauri/Cargo.lock`
   - `core-platform/data/brain_assets/reports/missing_repo_summaries/vnpy__vnpy.md`
   - `core-platform/data/repo_memory/store.json`
   - `core-platform/data/repo_memory/events.jsonl`
   - older downloaded Windows artifact directories
3. `Cargo.lock` locally reflects the `base64` dependency under `desktop_lib`.
   The remote workflow still built successfully from `main`, but the lockfile delta should be reviewed separately for reproducibility cleanup.

## Final Gate Result

- Latest `main` commit alignment: PASS
- GitHub Actions build uses latest commit: PASS
- Downloaded Windows artifact corresponds to latest commit: PASS
- Windows real-machine acceptance: READY TO RUN, not executed from this macOS preflight

