// D7-C1: auto-start services on app launch
// C25-C12-FIX: Rust now auto-starts runtime on app startup.
// C25-C14-B7-C: Ports from centralized runtime config.

const C25_BACKEND_PORTS = (window.maomiaiRuntimeAllPorts ? window.maomiaiRuntimeAllPorts() : [
  18080, 18081, 18093, 18100, 18101, 18102, 18104,
  18110, 18111, 18112, 18120, 18121, 18122, 18123,
  18124, 18125, 18126, 18127, 18131
]);

async function checkBackendHealth(port) {
  try {
    const host = (window.MAOMIAI_RUNTIME_CONFIG && window.MAOMIAI_RUNTIME_CONFIG.host) || "127.0.0.1";
    const res = await fetch(`http://${host}:${port}/health`, {
      method: "GET",
      signal: AbortSignal.timeout(3000),
    });
    return { port, ok: res.ok, status: res.status };
  } catch (err) {
    return { port, ok: false, error: err.message };
  }
}

async function autoStartServices() {
  // Strategy 1: Try Tauri invoke (works if Tauri API is available)
  const commands = ["start_desktop_services", "start_local_ai_runtime", "start_all_services", "start_all", "run_start_services"];
  for (const cmd of commands) {
    try {
      const invoke = window.__TAURI__?.core?.invoke || window.__TAURI__?.tauri?.invoke;
      if (!invoke) break;
      const res = await invoke(cmd, {});
      console.log(`[C25-C12-FIX] Tauri invoke "${cmd}" succeeded`);
      return { ok: true, source: "tauri_invoke", command: cmd, raw: res };
    } catch (err) {
      // try next command
    }
  }

  // Strategy 2: Rust auto-start may have already kicked in from setup().
  // Wait and verify backend health instead of failing.
  console.log("[C25-C12-FIX] Tauri invoke unavailable, checking if Rust auto-start already brought up services...");

  // Wait for Rust setup() to finish its 2s delay + service startup time
  await new Promise((r) => setTimeout(r, 5000));

  const healthChecks = await Promise.all(C25_BACKEND_PORTS.map(checkBackendHealth));
  const healthyCount = healthChecks.filter((h) => h.ok).length;

  if (healthyCount > 0) {
    console.log(`[C25-C12-FIX] ${healthyCount}/${C25_BACKEND_PORTS.length} services healthy (Rust auto-start)`);
    return {
      ok: true,
      source: "rust_autostart",
      healthy_count: healthyCount,
      total: C25_BACKEND_PORTS.length,
      checks: healthChecks.filter((h) => h.ok).map((h) => h.port),
    };
  }

  // Strategy 3: Still no services - inform user but don't crash
  console.warn("[C25-C12-FIX] No services detected. They may still be starting up.");
  return {
    ok: false,
    source: "none",
    reason: "Tauri invoke unavailable and no backend services detected yet. Rust setup() may still be running.",
    healthy_count: 0,
    total: C25_BACKEND_PORTS.length,
  };
}

document.addEventListener("DOMContentLoaded", () => {
  setTimeout(async () => {
    const result = await autoStartServices();
    console.log("[C25-C12-FIX] Auto-start result:", result);
    window.__MAOMIAI_AUTOSTART_RESULT__ = result;
  }, 1000);
});
