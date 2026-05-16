use std::process::Command;
use tauri::Manager;

#[tauri::command]
fn start_backend() -> Result<String, String> {
    let exe = std::env::current_exe().map_err(|e| e.to_string())?;
    let app_dir = exe.parent().ok_or("no exe parent")?.to_path_buf();

    // 兼容 nsis/msi 解包目录：优先同目录，再尝试 resources
    let script_candidates = vec![
        app_dir.join("scripts").join("start_all.bat"),
        app_dir.join("..").join("scripts").join("start_all.bat"),
        app_dir.join("resources").join("scripts").join("start_all.bat"),
    ];

    let script_path = script_candidates
        .into_iter()
        .find(|p| p.exists())
        .ok_or("start_all.bat not found in bundle")?;

    let output = Command::new("cmd")
        .args(["/C", &script_path.to_string_lossy()])
        .output()
        .map_err(|e| e.to_string())?;

    let stdout = String::from_utf8_lossy(&output.stdout).to_string();
    let stderr = String::from_utf8_lossy(&output.stderr).to_string();

    Ok(format!(
        "Local AI Platform starting...\nscript: {}\nscript stdout:\n{}\nscript stderr:\n{}",
        script_path.display(),
        stdout,
        stderr
    ))
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]

#[tauri::command]
fn start_desktop_services(app: tauri::AppHandle) -> Result<String, String> {
    use std::process::Command;
    let resource_dir = app
        .path()
        .resource_dir()
        .map_err(|e| format!("resource_dir error: {}", e))?;
    #[cfg(target_os = "windows")]
    {
        let script = resource_dir.join("scripts").join("windows").join("start_all.ps1");
        let fallback = resource_dir.join("resources").join("scripts").join("windows").join("start_all.ps1");
        let script_path = if script.exists() { script } else { fallback };
        if !script_path.exists() {
            return Err(format!("Windows startup script not found: {:?}", script_path));
        }
        let output = Command::new("powershell")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-File")
            .arg(script_path)
            .output()
            .map_err(|e| format!("failed to run powershell startup: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(format!("{}\n{}", stdout, stderr))
        } else {
            Err(format!("{}\n{}", stdout, stderr))
        }
    }
    #[cfg(not(target_os = "windows"))]
    {
        let script = resource_dir.join("resources").join("scripts").join("start_all.sh");
        if !script.exists() {
            return Err(format!("startup script not found: {:?}", script));
        }
        let output = Command::new("bash")
            .arg(script)
            .output()
            .map_err(|e| format!("failed to start services: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(format!("{}\n{}", stdout, stderr))
        } else {
            Err(format!("{}\n{}", stdout, stderr))
        }
    }
}
#[tauri::command]
fn stop_desktop_services(app: tauri::AppHandle) -> Result<String, String> {
    use std::process::Command;
    let resource_dir = app
        .path()
        .resource_dir()
        .map_err(|e| format!("resource_dir error: {}", e))?;
    #[cfg(target_os = "windows")]
    {
        let script = resource_dir.join("scripts").join("windows").join("stop_all.ps1");
        let fallback = resource_dir.join("resources").join("scripts").join("windows").join("stop_all.ps1");
        let script_path = if script.exists() { script } else { fallback };
        if !script_path.exists() {
            return Err(format!("Windows stop script not found: {:?}", script_path));
        }
        let output = Command::new("powershell")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-File")
            .arg(script_path)
            .output()
            .map_err(|e| format!("failed to run powershell stop: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(format!("{}\n{}", stdout, stderr))
        } else {
            Err(format!("{}\n{}", stdout, stderr))
        }
    }
    #[cfg(not(target_os = "windows"))]
    {
        let script = resource_dir.join("resources").join("scripts").join("stop_all.sh");
        if !script.exists() {
            return Err(format!("stop script not found: {:?}", script));
        }
        let output = Command::new("bash")
            .arg(script)
            .output()
            .map_err(|e| format!("failed to stop services: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(format!("{}\n{}", stdout, stderr))
        } else {
            Err(format!("{}\n{}", stdout, stderr))
        }
    }
}



fn write_embedded_windows_bootstrap() -> Result<std::path::PathBuf, String> {
    #[cfg(target_os = "windows")]
    {
        use std::fs;
        use std::io::Write;
        // Compile-time embed. This avoids Tauri resource path problems on Windows installers.
        let script_content = include_str!("../../../../scripts/windows/bootstrap_runtime.ps1");
        let exe = std::env::current_exe().map_err(|e| format!("无法获取程序路径: {}", e))?;
        let app_dir = exe.parent().ok_or("无法获取程序目录")?;
        let runtime_dir = app_dir.join("maomiai-runtime").join("scripts").join("windows");
        fs::create_dir_all(&runtime_dir)
            .map_err(|e| format!("无法创建运行时目录 {:?}: {}", runtime_dir, e))?;
        let script_path = runtime_dir.join("bootstrap_runtime.ps1");
        let mut file = fs::File::create(&script_path)
            .map_err(|e| format!("无法写入 bootstrap_runtime.ps1: {}", e))?;
        file.write_all(script_content.as_bytes())
            .map_err(|e| format!("写入 bootstrap_runtime.ps1 失败: {}", e))?;
        Ok(script_path)
    }
    #[cfg(not(target_os = "windows"))]
    {
        Err("该运行时脚本仅用于 Windows。".to_string())
    }
}

fn quote_powershell_path(path: &std::path::Path) -> String {
    format!("'{}'", path.display().to_string().replace('\'', "''"))
}

fn run_powershell_encoded(command_text: &str) -> Result<std::process::Output, String> {
    use base64::Engine;
    use std::process::Command;
    let encoded_utf16: Vec<u16> = command_text.encode_utf16().collect();
    let encoded_bytes: Vec<u8> = encoded_utf16.iter().flat_map(|c| c.to_le_bytes()).collect();
    let encoded_command = base64::engine::general_purpose::STANDARD.encode(encoded_bytes);
    Command::new("powershell.exe")
        .args([
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-EncodedCommand",
            &encoded_command,
        ])
        .output()
        .map_err(|e| e.to_string())
}

#[cfg(target_os = "windows")]
fn find_windows_runtime_root(app: &tauri::AppHandle) -> Result<std::path::PathBuf, String> {
    let resource_dir = app
        .path()
        .resource_dir()
        .map_err(|e| format!("resource_dir error: {}", e))?;
    let exe = std::env::current_exe().map_err(|e| e.to_string())?;
    let app_dir = exe.parent().ok_or("no exe parent")?.to_path_buf();
    let mut candidates = vec![
        resource_dir.clone(),
        resource_dir.join("resources"),
        app_dir.join("maomiai-runtime"),
    ];
    if let Ok(local_appdata) = std::env::var("LOCALAPPDATA") {
        candidates.push(
            std::path::PathBuf::from(local_appdata)
                .join("Local AI Platform")
                .join("maomiai-runtime"),
        );
    }
    candidates
        .into_iter()
        .find(|p| p.join("services").exists())
        .ok_or_else(|| format!("runtime services root not found near {}", resource_dir.display()))
}

#[cfg(target_os = "windows")]
fn find_windows_start_all_script(app: &tauri::AppHandle) -> Result<std::path::PathBuf, String> {
    let resource_dir = app
        .path()
        .resource_dir()
        .map_err(|e| format!("resource_dir error: {}", e))?;
    let exe = std::env::current_exe().map_err(|e| e.to_string())?;
    let app_dir = exe.parent().ok_or("no exe parent")?.to_path_buf();
    let mut candidates = vec![
        resource_dir.join("scripts").join("windows").join("start_all.ps1"),
        resource_dir
            .join("resources")
            .join("scripts")
            .join("windows")
            .join("start_all.ps1"),
        app_dir
            .join("maomiai-runtime")
            .join("scripts")
            .join("windows")
            .join("start_all.ps1"),
    ];
    if let Ok(local_appdata) = std::env::var("LOCALAPPDATA") {
        candidates.push(
            std::path::PathBuf::from(local_appdata)
                .join("Local AI Platform")
                .join("maomiai-runtime")
                .join("scripts")
                .join("windows")
                .join("start_all.ps1"),
        );
    }
    candidates
        .into_iter()
        .find(|p| p.exists())
        .ok_or_else(|| "start_all.ps1 not found in runtime resources".to_string())
}

#[tauri::command]
fn start_local_ai_runtime(app: tauri::AppHandle) -> Result<String, String> {
    #[cfg(target_os = "windows")]
    {
        let script = find_windows_start_all_script(&app)?;
        let root = find_windows_runtime_root(&app)?;
        let command_text = format!(
            "& {} -Root {}",
            quote_powershell_path(&script),
            quote_powershell_path(&root)
        );
        let output = run_powershell_encoded(&command_text)?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(stdout)
        } else {
            Err(format!("start_all.ps1 failed: {}", stderr))
        }
    }
    #[cfg(not(target_os = "windows"))]
    {
        let _ = app;
        Ok("{\"ok\":false,\"message\":\"start_local_ai_runtime is only available on Windows.\"}".to_string())
    }
}

fn run_windows_start_all_background(app: tauri::AppHandle) {
    #[cfg(target_os = "windows")]
    {
        std::thread::spawn(move || {
            // Small delay so the Tauri window is fully loaded first
            std::thread::sleep(std::time::Duration::from_secs(2));
            let script = match find_windows_start_all_script(&app) {
                Ok(path) => path,
                Err(e) => {
                    eprintln!("[C25-C12-FIX] find_windows_start_all_script failed: {}", e);
                    return;
                }
            };
            let root = match find_windows_runtime_root(&app) {
                Ok(path) => path,
                Err(e) => {
                    eprintln!("[C25-C12-FIX] find_windows_runtime_root failed: {}", e);
                    return;
                }
            };
            let command_text = format!(
                "& {} -Root {}",
                quote_powershell_path(&script),
                quote_powershell_path(&root)
            );
            match run_powershell_encoded(&command_text) {
                Ok(output) => {
                    let stdout = String::from_utf8_lossy(&output.stdout).to_string();
                    let stderr = String::from_utf8_lossy(&output.stderr).to_string();
                    eprintln!("[C25-C12-FIX] start_all.ps1 completed. stdout={} stderr={}", stdout.len(), stderr.len());
                }
                Err(e) => {
                    eprintln!("[C25-C12-FIX] run_powershell_encoded failed: {}", e);
                }
            }
        });
    }
    #[cfg(target_os = "macos")]
    {
        std::thread::spawn(move || {
            // Small delay so the Tauri window is fully loaded first
            std::thread::sleep(std::time::Duration::from_secs(2));
            let resource_dir = match app.path().resource_dir() {
                Ok(d) => d,
                Err(e) => {
                    eprintln!("[C25-MAC] macOS resource_dir failed: {}", e);
                    return;
                }
            };
            // Search for scripts/mac/start_all.sh in multiple locations:
            // 1. Bundled resource: <resource_dir>/scripts/mac/start_all.sh
            // 2. Nested resource: <resource_dir>/resources/scripts/mac/start_all.sh
            // 3. Dev-time: walk up from exe to find core-platform/scripts/mac/start_all.sh
            let candidates = vec![
                resource_dir.join("scripts").join("mac").join("start_all.sh"),
                resource_dir.join("resources").join("scripts").join("mac").join("start_all.sh"),
            ];
            // Also try walking up from exe directory (dev mode)
            if let Ok(exe) = std::env::current_exe() {
                if let Some(exe_dir) = exe.parent() {
                    // Walk up to find project root
                    let mut dir = exe_dir;
                    for _ in 0..8 {
                        let candidate = dir.join("core-platform").join("scripts").join("mac").join("start_all.sh");
                        if candidate.exists() {
                            eprintln!("[C25-MAC] found start_all.sh via exe walk: {:?}", candidate);
                            match std::process::Command::new("bash")
                                .arg(&candidate)
                                .spawn()
                            {
                                Ok(_) => eprintln!("[C25-MAC] start_all.sh spawned: {:?}", candidate),
                                Err(e) => eprintln!("[C25-MAC] start_all.sh spawn failed: {}", e),
                            }
                            return;
                        }
                        if let Some(parent) = dir.parent() {
                            dir = parent;
                        } else {
                            break;
                        }
                    }
                }
            }
            let script = match candidates.into_iter().find(|p| p.exists()) {
                Some(p) => p,
                None => {
                    eprintln!("[C25-MAC] start_all.sh not found in any candidate path");
                    return;
                }
            };
            match std::process::Command::new("bash")
                .arg(&script)
                .spawn()
            {
                Ok(_) => eprintln!("[C25-MAC] start_all.sh spawned: {:?}", script),
                Err(e) => eprintln!("[C25-MAC] start_all.sh spawn failed: {}", e),
            }
        });
    }
    #[cfg(not(any(target_os = "windows", target_os = "macos")))]
    {
        let _ = app;
    }
}

fn run_windows_bootstrap(action: &str, profile: Option<String>) -> Result<String, String> {
    use std::process::Command;
    #[cfg(target_os = "windows")]
    {
        let script = write_embedded_windows_bootstrap()?;
        let exe = std::env::current_exe().map_err(|e| format!("无法获取程序路径: {}", e))?;
        let app_dir = exe.parent().ok_or("无法获取程序目录")?;
        let root = app_dir.join("maomiai-runtime");
        let mut command = Command::new("powershell");
        command
            .arg("-NoProfile")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-File")
            .arg(&script)
            .arg("-Action")
            .arg(action)
            .arg("-Root")
            .arg(&root);
        if let Some(p) = profile {
            command.arg("-Profile").arg(p);
        }
        let output = command
            .output()
            .map_err(|e| format!("执行本地运行时脚本失败: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(stdout)
        } else {
            Err(format!(
                "{{\"ok\":false,\"message\":\"本地运行时脚本执行失败\",\"script\":\"{}\",\"root\":\"{}\",\"stdout\":{:?},\"stderr\":{:?}}}",
                script.display(),
                root.display(),
                stdout,
                stderr
            ))
        }
    }
    #[cfg(not(target_os = "windows"))]
    {
        Ok("{\"ok\":false,\"message\":\"该命令仅用于 Windows 打包环境。\"}".to_string())
    }
}

fn run_windows_bootstrap_with_prompt(
    action: &str,
    profile: Option<String>,
    prompt: Option<String>,
) -> Result<String, String> {
    use std::process::Command;
    #[cfg(target_os = "windows")]
    {
        let script = write_embedded_windows_bootstrap()?;
        let exe = std::env::current_exe().map_err(|e| format!("无法获取程序路径: {}", e))?;
        let app_dir = exe.parent().ok_or("无法获取程序目录")?;
        let root = app_dir.join("maomiai-runtime");
        let mut command = Command::new("powershell");
        command
            .arg("-NoProfile")
            .arg("-ExecutionPolicy")
            .arg("Bypass")
            .arg("-File")
            .arg(&script)
            .arg("-Action")
            .arg(action)
            .arg("-Root")
            .arg(&root);
        if let Some(p) = profile {
            command.arg("-Profile").arg(p);
        }
        if let Some(text) = prompt {
            use base64::Engine;
            let encoded = base64::engine::general_purpose::STANDARD.encode(text.as_bytes());
            command.env("MAOMIAI_PROMPT_B64", encoded);
        }
        let output = command
            .output()
            .map_err(|e| format!("执行本地推理命令失败: {}", e))?;
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(stdout)
        } else {
            Err(format!(
                "{{\"ok\":false,\"message\":\"本地推理命令执行失败\",\"stdout\":{:?},\"stderr\":{:?}}}",
                stdout, stderr
            ))
        }
    }
    #[cfg(not(target_os = "windows"))]
    {
        Ok("{\"ok\":false,\"message\":\"该命令仅用于 Windows 打包环境。\"}".to_string())
    }
}

#[tauri::command]
fn local_ai_status_direct() -> Result<String, String> {
    run_windows_bootstrap("status", None)
}

#[tauri::command]
fn install_local_inference_backend() -> Result<String, String> {
    run_windows_bootstrap("install_ollama", None)
}

#[tauri::command]
fn download_local_model_capability(profile: String) -> Result<String, String> {
    run_windows_bootstrap("pull_model", Some(profile))
}

#[tauri::command]
fn start_local_model_download(profile: String) -> Result<String, String> {
    run_windows_bootstrap("start_pull_model", Some(profile))
}

#[tauri::command]
fn local_model_download_status(profile: String) -> Result<String, String> {
    run_windows_bootstrap("job_status", Some(profile))
}

#[tauri::command]
fn generate_local_ai_response(profile: String, prompt: String) -> Result<String, String> {
    run_windows_bootstrap_with_prompt("generate_text", Some(profile), Some(prompt))
}


pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            run_windows_start_all_background(app.handle().clone());
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![
            start_backend,
            start_desktop_services,
            start_local_ai_runtime,
            stop_desktop_services,
            local_ai_status_direct,
            install_local_inference_backend,
            download_local_model_capability,
            start_local_model_download,
            local_model_download_status,
            generate_local_ai_response
        ])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
