use std::process::Command;

fn run_shell_script(script_path: &str) {
    let output = Command::new("sh")
        .arg(script_path)
        .output();

    match output {
        Ok(out) => {
            println!("script stdout: {}", String::from_utf8_lossy(&out.stdout));
            eprintln!("script stderr: {}", String::from_utf8_lossy(&out.stderr));
        }
        Err(err) => {
            eprintln!("failed to run script {}: {}", script_path, err);
        }
    }
}

#[tauri::command]
fn start_backend() -> String {
    let script = "/Users/mofamaomi/Documents/本地ai/core-platform/scripts/start_all.sh";
    run_shell_script(script);
    "backend start triggered".to_string()
}

#[tauri::command]
fn stop_backend() -> String {
    let script = "/Users/mofamaomi/Documents/本地ai/core-platform/scripts/stop_all.sh";
    run_shell_script(script);
    "backend stop triggered".to_string()
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|_app| {
            println!("Local AI Platform starting...");
            let start_script = "/Users/mofamaomi/Documents/本地ai/core-platform/scripts/start_all.sh";
            run_shell_script(start_script);
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![start_backend, stop_backend])
        .on_window_event(|_window, event| {
            if let tauri::WindowEvent::Destroyed = event {
                let stop_script = "/Users/mofamaomi/Documents/本地ai/core-platform/scripts/stop_all.sh";
                println!("Stopping backend services...");
                run_shell_script(stop_script);
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
