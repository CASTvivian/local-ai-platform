# C25-C14-B7-E Runtime Config Build Hook

## Goal
Ensure desktop runtime config is generated before build/package.

## Implemented

### npm scripts (package.json)
```text
generate:runtime-config   → python3 ../../scripts/build/generate_desktop_runtime_config.py
prebuild                  → npm run generate:runtime-config
pretauri                  → npm run generate:runtime-config
```

### Windows workflow (build-win-release.yml)
Added explicit `Generate runtime config` step before `Build Tauri Windows bundle`:
```yaml
- name: Generate runtime config
  working-directory: ./core-platform/apps/desktop
  shell: pwsh
  run: |
    npm run generate:runtime-config
```

## Validation

| Check | Result |
|---|---|
| Generator runs via npm | ✅ |
| Generated JS syntax passes | ✅ |
| AUTO-GENERATED marker exists | ✅ |
| Hardcode guard passes | ✅ |
| Service count = 19 | ✅ |
| package.json has generate:runtime-config | ✅ |
| prebuild hook set | ✅ |
| pretauri hook set | ✅ |
| Workflow has generate step | ✅ |

## Build Flow

```text
runtime_config.json → generate_desktop_runtime_config.py → runtime-config.js
                                                    ↑
npm run tauri build  (pretauri hook auto-generates)
npm run build        (prebuild hook auto-generates)
CI Windows workflow   (explicit step before tauri build)
```

## Remaining

B7-F can integrate Mac build scripts and any release scripts, but this is enough for normal npm/Tauri builds.
