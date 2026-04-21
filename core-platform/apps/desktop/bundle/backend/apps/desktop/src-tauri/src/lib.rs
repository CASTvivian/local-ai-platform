use std::path::PathBuf;
use std::process::Command;

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
pub fn run() {
    tauri::Builder::default()
        .invoke_handler(tauri::generate_handler![start_backend])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
