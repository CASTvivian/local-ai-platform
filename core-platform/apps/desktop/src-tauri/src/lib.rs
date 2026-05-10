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
        let stdout = String::from_utf8_lossy(&output.stdout).to_string();
        let stderr = String::from_utf8_lossy(&output.stderr).to_string();
        if output.status.success() {
            Ok(format!(
                "本地推理后端安装命令已执行。\n\nstdout:\n{}\n\nstderr:\n{}",
                stdout, stderr
            ))
        } else {
            let _ = Command::new("cmd")
                .arg("/C")
                .arg("start")
                .arg("https://ollama.com/download/windows")
                .spawn();
            Err(format!(
                "自动安装命令执行失败，已尝试打开官方下载页。\n\nstdout:\n{}\n\nstderr:\n{}",
                stdout, stderr
            ))
        }
    }
    #[cfg(target_os = "macos")]
    {
        let output = Command::new("open")
            .arg("https://ollama.com/download")
            .output()
            .map_err(|e| format!("failed to open download page: {}", e))?;
        if output.status.success() {
            Ok("已打开本地推理后端官方下载页。".to_string())
        } else {
            Err("无法打开官方下载页，请手动访问 https://ollama.com/download".to_string())
        }
    }
    #[cfg(all(not(target_os = "windows"), not(target_os = "macos")))]
    {
        Ok("请手动安装本地推理后端：https://ollama.com/download".to_string())
    }
}


pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![start_backend, start_desktop_services, stop_desktop_services, install_local_inference_backend])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}