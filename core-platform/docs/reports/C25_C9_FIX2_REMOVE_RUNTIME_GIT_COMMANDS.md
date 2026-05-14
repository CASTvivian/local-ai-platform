# C25-C9-FIX2 Remove Runtime Git Commands from Windows Workflow

## Problem

Windows workflow still failed with:
```text
git.exe failed with exit code 128
```

Even after disabling submodules, manual git commands inside workflow can still trigger broken submodule / dataless / nested-repo failures.

## Root Cause Analysis

After C25-C9-FIX, the workflow still contained:
1. `actions/checkout@v6` (normalized to @v4 for stability)
2. `git log -1 --oneline` in "Show commit and tree" step
3. `git rev-parse --short HEAD` in "Prepare frontend dist" step
4. Missing `persist-credentials: false` in checkout config

## Fix

1. ✅ Normalize checkout to `actions/checkout@v4`
2. ✅ `submodules: false` (already present)
3. ✅ `lfs: false` (already present)
4. ✅ `persist-credentials: false` (added)
5. ✅ Remove `git log -1 --oneline` → replaced with `Write-Host "Commit SHA: $env:MAOMIAI_BUILD_COMMIT"`
6. ✅ Remove `git rev-parse --short HEAD` → replaced with `$env:MAOMIAI_BUILD_COMMIT.Substring(0, 7)`
7. ✅ No manual `git status`, `git submodule`, `git fetch`, `git checkout` (already clean)
8. ✅ Build metadata uses `$env:MAOMIAI_BUILD_COMMIT` (from `MAOMIAI_BUILD_COMMIT: ${{ github.sha }}`)

## Workflow Changes

### Before
```yaml
- uses: actions/checkout@v6
  with:
    fetch-depth: 1
    submodules: false
    lfs: false
    clean: true

- name: Show commit and tree
  run: |
    git log -1 --oneline
    Get-ChildItem ...

- name: Prepare frontend dist
  run: |
    $sha = git rev-parse --short HEAD
    ...
```

### After
```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 1
    submodules: false
    lfs: false
    clean: true
    persist-credentials: false

- name: Show commit and tree
  run: |
    Write-Host "Commit SHA: $env:MAOMIAI_BUILD_COMMIT"
    Write-Host "Ref: $env:MAOMIAI_BUILD_REF"
    Get-ChildItem ...

- name: Prepare frontend dist
  run: |
    $sha = $env:MAOMIAI_BUILD_COMMIT.Substring(0, 7)
    ...
```

## Verification

```bash
# No dangerous git commands
✅ "git status --short" - NOT FOUND
✅ "git rev-parse HEAD" - NOT FOUND
✅ "git submodule" - NOT FOUND (only "submodules: false" config)
✅ "git fetch" - NOT FOUND
✅ "git checkout" - NOT FOUND (only "actions/checkout@v4" action)
✅ "git log" - NOT FOUND

# Required configurations present
✅ "actions/checkout@v4" - FOUND
✅ "submodules: false" - FOUND
✅ "lfs: false" - FOUND
✅ "persist-credentials: false" - FOUND
✅ "MAOMIAI_BUILD_COMMIT" - FOUND
```

## Expected Result

Next Windows workflow run must:
1. ❌ NOT contain `git.exe exit code 128`
2. ✅ End with `conclusion=success`
3. ✅ Produce Windows artifacts (.msi, .exe)
4. ✅ BUILD_INFO.json contains correct commit SHA (from `github.sha`)
5. ✅ BUILD_INFO.json commit equals latest main branch SHA

## Actual Result - ✅ SUCCESS

**Build Run**: https://github.com/CASTvivian/local-ai-platform/actions/runs/25875775034

### Build Status
- **Status**: ✅ `completed`
- **Conclusion**: ✅ `success`
- **Started**: 2026-05-14T17:45:29Z
- **Completed**: 2026-05-14T17:52:05Z
- **Duration**: ~6.6 minutes
- **Commit SHA**: `a4a8ee04d7b0156bcc341b8899a1e192da981b49`

### Artifacts
- **Name**: `local-ai-platform-win`
- **Size**: 7,393,403 bytes (7.0 MB)
- **Files**:
  - `Local AI Platform_0.1.0_x64-setup.exe` (1.9 MB)
  - `Local AI Platform_0.1.0_x64_en-US.msi` (2.9 MB)
  - `desktop_lib.exe` (8.3 MB)
  - `BUILD_INFO.json` (150 bytes)

### BUILD_INFO.json Verification
```json
{
  "workflow": "build-win-release",
  "commit": "a4a8ee0",
  "label": "win-artifact-only",
  "built_at": "2026-05-14T17:46:38.6903847+00:00"
}
```

**Commit Match**: ✅ BUILD_INFO commit `a4a8ee0` matches latest main `a4a8ee0`

### Git Exit Code Check
✅ No `git.exe exit code 128` errors in build logs
✅ Checkout succeeded with sparse-checkout
✅ Submodule cleanup succeeded

## Root Cause Resolution

The `git.exe exit code 128` was caused by:
1. `actions/checkout@v4` internally runs `git submodule foreach` during auth cleanup
2. Even with `submodules: false`, this command still executes
3. Broken `.gitmodules` with missing URLs caused exit 128

**Solution**:
- Use `sparse-checkout` to only checkout needed paths (avoids submodule processing)
- Add explicit step to remove `.gitmodules` and clean `.git/config` submodule refs
- Build metadata uses `$env:MAOMIAI_BUILD_COMMIT` from `github.sha`

## Next Steps

1. ✅ **C25-C9-FIX2 COMPLETED** - Windows build workflow now succeeds
2. ➡️ **Proceed to C25-C10** - Windows final acceptance on real machine
3. 📦 Windows artifacts ready for installation testing

## Related

- P3.14-C25-C9-FIX: Initial git diagnostics removal (incomplete)
- P3.14-C25-C10: Windows final acceptance