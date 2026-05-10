# P3.14-D7 Windows Package Content and Full Delivery

## Status

✅ Created full Windows delivery package for debugging and customer delivery

## Understanding the Two Package Types

### GitHub Artifact (Build Output Only)
Contains only the Tauri build products:
- `Local AI Platform_0.1.0_x64-setup.exe` - NSIS installer
- `Local AI Platform_0.1.0_x64_en-US.msi` - MSI installer
- `desktop_lib.exe` - Raw executable

These are sufficient for normal installation. Runtime resources should be bundled **inside** the installers.

### Full Delivery Package (For Debugging & Customer Delivery)
Additional debugging and manual testing files:
- All installers (setup.exe, msi, desktop_lib.exe)
- Windows runtime scripts (ensure_runtime, bootstrap_runtime, start_all, stop_all, status_all)
- Backend services source code (8 services)
- Manual testing PowerShell scripts
- README documentation
- BUILD_INFO.json

## Why Only Three Files Appeared Before

GitHub Actions artifact normally contains only build outputs:

- `setup.exe` (1.8 MB)
- `msi` (2.8 MB)
- `raw exe` (8.3 MB)

Runtime resources are expected to be inside the installer bundle after installation.

For debugging and customer delivery, a **full delivery folder** is now created separately.

## Tauri Configuration (tauri.conf.json)

The `bundle.resources` configuration includes:

```json
"resources": [
  "resources/scripts/start_all.sh",
  "resources/scripts/stop_all.sh",
  "../../../scripts/windows/ensure_runtime.ps1",
  "../../../scripts/windows/bootstrap_runtime.ps1",
  "../../../scripts/windows/start_all.ps1",
  "../../../scripts/windows/stop_all.ps1",
  "../../../scripts/windows/status_all.ps1",
  "../../../services/model_bootstrap_service",
  "../../../services/model_gateway"
]
```

**Note**: The paths are relative to `apps/desktop/src-tauri/` directory.

## Source Package

```text
core-platform/releases/windows-d7-verified-complete/
├── Local AI Platform_0.1.0_x64-setup.exe    (1.8 MB)
├── Local AI Platform_0.1.0_x64_en-US.msi     (2.8 MB)
├── desktop_lib.exe                           (8.3 MB)
└── BUILD_INFO.json                           (173 B)
```

## Full Delivery Package

```text
core-platform/releases/windows-d7-full-delivery/
├── BUILD_INFO.json                           (173 B)
├── README.md                                 (Documentation)
├── installers/
│   ├── Local AI Platform_0.1.0_x64-setup.exe (1.8 MB)
│   ├── Local AI Platform_0.1.0_x64_en-US.msi  (2.8 MB)
│   └── desktop_lib.exe                      (8.3 MB)
├── runtime/
│   ├── manual_start_backend.ps1              (Manual backend start)
│   ├── manual_status_backend.ps1             (Manual backend status check)
│   ├── scripts/windows/
│   │   ├── ensure_runtime.ps1               (Runtime environment check)
│   │   ├── bootstrap_runtime.ps1            (Bootstrap Python + uvicorn)
│   │   ├── start_all.ps1                    (Start all backend services)
│   │   ├── stop_all.ps1                     (Stop all services)
│   │   └── status_all.ps1                   (Check service port status)
│   └── services/
│       ├── model_bootstrap_service/         (Port 18100)
│       ├── model_gateway/                   (Port 18080)
│       ├── skill_store_service/              (Port 18121)
│       ├── artifact_registry_service/        (Port 18123)
│       ├── code_review_gate_service/         (Port 18124)
│       ├── repo_memory_service/              (Port 18125)
│       ├── workflow_store_service/           (Port 18126)
│       └── design_system_service/           (Port 18127)
└── docs/
```

**Package Size**: 13 MB (uncompressed) / 6.8 MB (compressed tar.gz)

## Verified Source Files

### Windows Runtime Scripts ✅
- ✅ core-platform/scripts/windows/ensure_runtime.ps1
- ✅ core-platform/scripts/windows/bootstrap_runtime.ps1
- ✅ core-platform/scripts/windows/start_all.ps1
- ✅ core-platform/scripts/windows/stop_all.ps1
- ✅ core-platform/scripts/windows/status_all.ps1

### Backend Services ✅
- ✅ core-platform/services/model_gateway/main.py
- ✅ core-platform/services/model_bootstrap_service/main.py
- ✅ core-platform/services/skill_store_service/main.py
- ✅ core-platform/services/artifact_registry_service/main.py
- ✅ core-platform/services/code_review_gate_service/main.py
- ✅ core-platform/services/repo_memory_service/main.py
- ✅ core-platform/services/workflow_store_service/main.py
- ✅ core-platform/services/design_system_service/main.py

## Manual Backend Testing (For Debugging)

If the desktop app shows "本地 AI 暂未连接" (Local AI not connected):

```powershell
# Navigate to runtime directory
cd runtime

# Start backend manually
powershell -ExecutionPolicy Bypass -File .\manual_start_backend.ps1

# Check backend status
powershell -ExecutionPolicy Bypass -File .\manual_status_backend.ps1
```

## Installation Verification

### After Normal Installation

Check the installed directory for runtime resources:

```powershell
# Typically located at:
C:\Users\<username>\AppData\Local\Programs\localaiplatform\
# or
C:\Program Files\Local AI Platform\

# Check if resources directory exists
Get-ChildItem -Recurse resources\scripts\windows
Get-ChildItem -Recurse resources\services
```

### Expected Installation Structure

```text
Local AI Platform/
├── Local AI Platform.exe
├── resources/
│   ├── scripts/windows/
│   │   ├── ensure_runtime.ps1
│   │   ├── bootstrap_runtime.ps1
│   │   ├── start_all.ps1
│   │   ├── stop_all.ps1
│   │   └── status_all.ps1
│   ├── services/
│   │   ├── model_bootstrap_service/
│   │   │   └── main.py
│   │   └── model_gateway/
│   │       └── main.py
│   └── scripts/
│       ├── start_all.sh
│       └── stop_all.sh
└── ...
```

**If resources directory does not exist after installation**, the Tauri bundling did not include the resources. Use the full delivery package for manual testing.

## Files Included in Full Delivery Package

Total: 21 files across installers, runtime, and docs

**Installers (3 files)**
- Local AI Platform_0.1.0_x64-setup.exe
- Local AI Platform_0.1.0_x64_en-US.msi
- desktop_lib.exe

**Runtime - Scripts (7 files)**
- manual_start_backend.ps1
- manual_status_backend.ps1
- bootstrap_runtime.ps1
- ensure_runtime.ps1
- start_all.ps1
- stop_all.ps1
- status_all.ps1

**Runtime - Services (10 files)**
- model_bootstrap_service/__init__.py
- model_bootstrap_service/main.py
- model_gateway/__init__.py
- model_gateway/main.py
- skill_store_service/main.py
- artifact_registry_service/main.py
- code_review_gate_service/main.py
- repo_memory_service/main.py
- workflow_store_service/main.py
- design_system_service/main.py
- design_system_service/ACCEPTANCE_REPORT.md

**Docs (1 file)**
- README.md

## Next Steps

### For Normal Installation
- Use `installers/Local AI Platform_0.1.0_x64-setup.exe`
- Verify installation directory contains `resources/` folder
- Check if backend starts automatically

### For Backend Troubleshooting
- Use full delivery package: `windows-d7-full-delivery.tar.gz`
- Extract and run `runtime/manual_start_backend.ps1`
- Check service status with `runtime/manual_status_backend.ps1`

### For Customer Delivery
- Provide both the installer and full delivery package
- Installer for normal installation
- Full delivery package for debugging and manual backend control

### To Verify Installer Bundling (On Windows Machine)
- Install the MSI or setup.exe
- Check installed directory for `resources/` folder
- If missing, report Tauri bundling issue

## Build Info

```json
{
  "version": "0.1.0",
  "build_date": "2026-05-05",
  "commit": "d33da8b",
  "platform": "windows-x64"
}
```

## Related Tasks

- P3.14-D7-C4: Fixed Windows package missing runtime files
- P3.14-D7-SYNC-B: Source code normalization completed
- P3.14-D7-A: Desktop interaction regression (ongoing)

---

**Generated**: 2026-05-11
**Package Location**: `core-platform/releases/windows-d7-full-delivery/`
**Archive**: `core-platform/releases/windows-d7-full-delivery.tar.gz` (6.8 MB)
