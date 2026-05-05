# P3.14-D7 Project Integrity and Windows Package Verified

## Status
Verified.

## Canonical Packaging Root
```
core-platform/
```

## Desktop Source
```
core-platform/apps/desktop
```

## Runtime Source
```
core-platform/scripts/windows
core-platform/services
```

## Verified Services

### Local Runtime
- model_gateway (18080)
- model_bootstrap_service (18100)

### Enterprise Services (version 0.3.1-enterprise)
- skill_store_service (18121)
- artifact_registry_service (18123)
- code_review_gate_service (18124)
- repo_memory_service (18125)
- workflow_store_service (18126)
- design_system_service (18127)

## Windows Build
- Run ID: 25364413517
- Commit: cd27199
- Status: SUCCESS
- Artifact:
```
core-platform/releases/windows-d7-verified-complete/
```

## Verification Results

### Files Verified (Local)
- ✅ Desktop UI: index.html, windows-click-model-setup.js
- ✅ Tauri Config: tauri.conf.json with correct resource paths
- ✅ Windows Runtime Scripts (5 files, 567 lines total)
- ✅ Model Gateway Service (main.py)
- ✅ Model Bootstrap Service (main.py)
- ✅ Six Enterprise Services (all at version 0.3.1-enterprise)

### Files Verified (Remote)
- ✅ core-platform/apps/desktop/src/index.html (105KB)
- ✅ core-platform/apps/desktop/src-tauri/tauri.conf.json (1KB)
- ✅ All Windows runtime scripts
- ✅ All backend services (8 files)

### Tauri Resource Paths Verified
- ✅ ../../../scripts/windows/ensure_runtime.ps1
- ✅ ../../../scripts/windows/bootstrap_runtime.ps1
- ✅ ../../../scripts/windows/start_all.ps1
- ✅ ../../../services/model_gateway
- ✅ ../../../services/model_bootstrap_service
- ✅ All 13 resources accessible from src-tauri directory

### Windows Package Downloaded
- ✅ Local AI Platform_0.1.0_x64-setup.exe
- ✅ Local AI Platform_0.1.0_x64_en-US.msi
- ✅ desktop_lib.exe
- ✅ BUILD_INFO.json
- Total size: 13M

## Notes
This report confirms that the required runtime scripts and enterprise services exist both locally and remotely before using the Windows package. The package was successfully built from commit cd27199 with all enterprise services properly included.
