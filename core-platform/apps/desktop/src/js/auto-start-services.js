// P3.14-D7-C1: Auto-start services on desktop app open.
(function () {
  async function invokeTauri(command, args) {
    try {
      if (window.__TAURI__?.core?.invoke) {
        return await window.__TAURI__.core.invoke(command, args || {});
      }
      if (window.__TAURI__?.invoke) {
        return await window.__TAURI__.invoke(command, args || {});
      }
    } catch (err) {
      throw err;
    }
    throw new Error("Tauri invoke unavailable");
  }

  async function autoStartServices() {
    const result = {
      ok: false,
      mode: "unavailable",
      message: "未检测到桌面启动命令，服务状态请查看右侧「服务」面板。",
    };
    const commands = [
      "start_desktop_services",
      "start_all_services",
      "start_all",
      "run_start_services",
    ];
    for (const cmd of commands) {
      try {
        const res = await invokeTauri(cmd, {});
        result.ok = true;
        result.mode = cmd;
        result.message = "后台服务已自动启动。";
        result.raw = res;
        break;
      } catch (err) {
        result.last_error = String(err);
      }
    }
    window.__MAOMIAI_AUTO_START_RESULT__ = result;
    setTimeout(() => {
      if (typeof window.refreshHealth === "function") {
        window.refreshHealth();
      } else if (typeof window.refreshServices === "function") {
        window.refreshServices();
      }
    }, 1800);
    return result;
  }

  window.autoStartServices = autoStartServices;
  document.addEventListener("DOMContentLoaded", () => {
    autoStartServices().then((res) => {
      console.log("[auto-start-services]", res);
    });
  });
})();
