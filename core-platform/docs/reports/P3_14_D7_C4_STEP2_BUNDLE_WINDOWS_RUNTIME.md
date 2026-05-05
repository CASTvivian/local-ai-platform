# P3.14-D7-C4 Step 2 Bundle Windows Runtime

## Status
✅ Implemented

## Added
- Windows PowerShell scripts included as Tauri resources:
  - `../../scripts/windows/start_all.ps1`
  - `../../scripts/windows/stop_all.ps1`
  - `../../scripts/windows/status_all.ps1`
- Model bootstrap service included as Tauri resource:
  - `../../services/model_bootstrap_service`
- Model gateway service included as Tauri resource:
  - `../../services/model_gateway`
- Tauri command stubs:
  - `start_desktop_services` - starts local services via PowerShell (Windows) or Bash (macOS)
  - `stop_desktop_services` - stops local services via PowerShell (Windows) or Bash (macOS)

## Purpose
Allow Windows desktop app to attempt starting local services through PowerShell and expose 18100 model bootstrap endpoints.

## Implementation Details
1. **tauri.conf.json** - Added Windows scripts and services to resources array
2. **lib.rs** - Added `start_desktop_services` and `stop_desktop_services` Tauri commands
3. **Rust Command Logic**:
   - Windows: Calls `powershell -ExecutionPolicy Bypass -File <script>`
   - macOS: Calls `bash <script>`
   - Uses `resource_dir()` to locate bundled scripts
4. **Build Verification** - Added resource verification step to Windows build workflow

## Caveat
This still requires Windows runtime validation:
- Python must be available or packaged later.
- Python dependencies must be available or vendored later.
- Local inference backend (Ollama) must be installed for real model pull.

## Next Steps
- P3.14-D7-C4 Step 3: Download new Windows package and test on real Windows machine
- Verify auto-start functionality on Windows
- Test 18100 service startup
- Test "Check Local AI Status" button
- Test "Prepare Standard Conversation" button
