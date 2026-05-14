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

## Next Steps

1. Commit and push this fix
2. Trigger `build-win-release.yml` workflow
3. Monitor build logs for any git.exe errors
4. Verify artifact contents
5. Proceed to C25-C10 Windows final acceptance if build succeeds

## Related

- P3.14-C25-C9-FIX: Initial git diagnostics removal (incomplete)
- P3.14-C25-C10: Windows final acceptance