use std::process::Command;
use std::path::PathBuf;

fn get_script_dir() -> PathBuf {
    let mut exe_path = std::env::current_exe().unwrap_or_else(|_| PathBuf::from("."));
    exe_path.pop(); // Remove executable name
    exe_path.pop(); // Remove 'bin' or 'release' directory
    exe_path.push("scripts");
    exe_path
}

fn run_shell_script(script_name: &str) {
    let script_dir = get_script_dir();
    let script_path = script_dir.join(script_name);

    #[cfg(target_os = "windows")]
    {
        let output = Command::new("cmd")
            .args(["/C", &format!("{}", script_path.display())])
            .output();

        match output {
            Ok(out) => {
                println!("script stdout: {}", String::from_utf8_lossy(&out.stdout));
                eprintln!("script stderr: {}", String::from_utf8_lossy(&out.stderr));
            }
            Err(err) => {
                eprintln!("failed to run script {}: {}", script_path.display(), err);
            }
        }
    }

    #[cfg(not(target_os = "windows"))]
    {
        let output = Command::new("sh")
            .arg(&script_path)
            .output();

        match output {
            Ok(out) => {
                println!("script stdout: {}", String::from_utf8_lossy(&out.stdout));
                eprintln!("script stderr: {}", String::from_utf8_lossy(&out.stderr));
            }
            Err(err) => {
                eprintln!("failed to run script {}: {}", script_path.display(), err);
            }
        }
    }
}

#[tauri::command]
fn start_backend() -> String {
    #[cfg(target_os = "windows")]
    run_shell_script("start_all.bat");
    #[cfg(not(target_os = "windows"))]
    run_shell_script("start_all.sh");
    "backend start triggered".to_string()
}

#[tauri::command]
fn stop_backend() -> String {
    #[cfg(target_os = "windows")]
    run_shell_script("stop_all.bat");
    #[cfg(not(target_os = "windows"))]
    run_shell_script("stop_all.sh");
    "backend stop triggered".to_string()
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|_app| {
            println!("Local AI Platform starting...");
            // Auto-start backend on launch (can be commented out if not desired)
            #[cfg(target_os = "windows")]
            run_shell_script("start_all.bat");
            #[cfg(not(target_os = "windows"))]
            run_shell_script("start_all.sh");
            Ok(())
        })
        .invoke_handler(tauri::generate_handler![start_backend, stop_backend])
        .on_window_event(|_window, event| {
            if let tauri::WindowEvent::Destroyed = event {
                println!("Stopping backend services...");
                #[cfg(target_os = "windows")]
                run_shell_script("stop_all.bat");
                #[cfg(not(target_os = "windows"))]
                run_shell_script("stop_all.sh");
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
