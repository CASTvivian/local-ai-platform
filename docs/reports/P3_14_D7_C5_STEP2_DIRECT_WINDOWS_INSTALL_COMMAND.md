# P3.14-D7-C5 Step 2 Direct Windows Install Command

## Status
Implemented.

## Problem
The previous install button depended on:
```text
用户点击"安装本地推理后端" → 请求 18100 /bootstrap/install_ollama
```

If 18100 was not running, the install button could not install anything.

## Fix

Added a direct Tauri command:

### 1. Rust Command (`src-tauri/src/lib.rs`)

```rust
#[tauri::command]
fn install_local_inference_backend() -> Result<String, String> {
    use std::process::Command;
    #[cfg(target_os = "windows")]
    {
        let install_cmd = "irm https://ollama.com/install.ps1 | iex";
        let output = Command::new("powershell")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-Command")
            .arg(install_cmd)
            .output()
            .map_err(|e| format!("failed to start installer: {}", e))?;
        // ... success/failure handling with fallback to download page
    }
    // ... macOS/Linux handling
}
```

### 2. Frontend Logic (`src/js/windows-click-model-setup.js`)

```javascript
async function installLocalInferenceBackend() {
    // 1) Prefer direct Tauri command (does NOT depend on 18100)
    try {
      const invoke = window.__TAURI__?.core?.invoke || window.__TAURI_INTERNALS__?.invoke;
      if (invoke) {
        const out = await invoke("install_local_inference_backend");
        // ... show success message
      }
    } catch (e) {
      // Tauri command failed
    }
    
    // 2) Try backend API fallback if 18100 is available
    try {
      const apiResult = await postJson(`${API.bootstrap}/bootstrap/install_ollama`, {}, 30000);
      // ... fallback success
    } catch (e) {
      // 18100 not available
    }
    
    // 3) Last fallback: open official download page
    window.open("https://ollama.com/download/windows", "_blank");
    // ... show manual install instructions
}
```

## Result

The install button no longer depends solely on 18100:
- **Primary path**: Direct Tauri command (works even if 18100 is down)
- **Fallback 1**: 18100 API (if available)
- **Fallback 2**: Open official download page

## Next Steps

1. Build Windows installer with this change
2. Test on a clean Windows machine without Ollama installed
3. Verify install button works even when 18100 is not running
