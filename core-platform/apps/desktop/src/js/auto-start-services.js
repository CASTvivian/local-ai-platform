// D7-C1: auto-start services on app launch
async function autoStartServices() {
  const commands = ["start_desktop_services", "start_all_services", "start_all", "run_start_services"];
  for (const cmd of commands) {
    try {
      const { invoke } = window.__TAURI__?.core ?? window.__TAURI__;
      if (!invoke) break;
      const res = await invoke(cmd, {});
      return { ok: true, command: cmd, raw: res };
    } catch (err) {
      // try next command
    }
  }
  return { ok: false, reason: "No Tauri bridge available or no command succeeded" };
}

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(async () => {
    const result = await autoStartServices();
    console.log("[D7-C1] Auto-start services:", result);
  }, 1000);
});
