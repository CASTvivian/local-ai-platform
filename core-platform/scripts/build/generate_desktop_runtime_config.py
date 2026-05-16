"""C25-C14-B7-D: Generate desktop runtime-config.js from runtime_config.json.

Reads:   data/runtime_config/runtime_config.json
Writes:  apps/desktop/src/js/config/runtime-config.js

Usage:   python3 scripts/build/generate_desktop_runtime_config.py
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = ROOT / "data" / "runtime_config" / "runtime_config.json"
OUT_PATH = ROOT / "apps" / "desktop" / "src" / "js" / "config" / "runtime-config.js"


def camel_service_name(name: str) -> str:
    """Convert snake_case service name to camelCase JS key.

    Examples:
        model_gateway -> modelGateway
        ollama -> ollama
        agent_runtime_service -> agentRuntimeService
    """
    parts = name.split("_")
    return parts[0] + "".join(x[:1].upper() + x[1:] for x in parts[1:])


def main() -> None:
    data = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    # Build services dict with camelCase keys (js_key overrides auto-conversion)
    services = {}
    for name, item in (data.get("services") or {}).items():
        js_key = item.get("js_key") or camel_service_name(name)
        services[js_key] = {
            "port": item.get("port"),
            "baseUrl": item.get("base_url"),
            "healthPath": item.get("health_path", "/health"),
        }

    # Sort services by port for consistent output
    services = dict(sorted(services.items(), key=lambda kv: kv[1].get("port", 0)))

    js_config = {
        "version": data.get("version"),
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": "data/runtime_config/runtime_config.json",
        "host": data.get("host", "127.0.0.1"),
        "services": services,
        "modelProfiles": data.get("model_profiles", {}),
        "defaults": data.get("defaults", {}),
        "packaging": data.get("packaging", {}),
    }

    # Generate JS IIFE
    body = """\
// AUTO-GENERATED FILE. DO NOT EDIT BY HAND.
// Source: data/runtime_config/runtime_config.json
// Generator: scripts/build/generate_desktop_runtime_config.py
// GeneratedAt: """ + js_config["generatedAt"] + """
(function () {
  var config = """ + json.dumps(js_config, ensure_ascii=False, indent=2) + """;

  /**
   * Get service config by name.
   * @param {string} name - Service key (e.g. "agentRuntime", "modelGateway")
   * @returns {object|null}
   */
  function service(name) {
    return config.services[name] || null;
  }

  /**
   * Get base URL for a service.
   * @param {string} name
   * @returns {string}
   */
  function baseUrl(name) {
    var s = service(name);
    return s ? s.baseUrl : "";
  }

  /**
   * Get health check URL for a service.
   * @param {string} name
   * @returns {string}
   */
  function healthUrl(name) {
    var s = service(name);
    if (!s) return "";
    return s.baseUrl.replace(/\\/+$/, "") + "/" + (s.healthPath || "/health").replace(/^\\/+/, "");
  }

  /**
   * Build an API URL for a service + path.
   * @param {string} name - Service key
   * @param {string} path - API path (e.g. "agent/run")
   * @returns {string}
   */
  function apiUrl(name, path) {
    var s = service(name);
    if (!s) return path || "";
    return s.baseUrl.replace(/\\/+$/, "") + "/" + (path || "").replace(/^\\/+/, "");
  }

  /**
   * Get all service names.
   * @returns {string[]}
   */
  function serviceNames() {
    return Object.keys(config.services);
  }

  /**
   * Get all service ports as an array of numbers.
   * @returns {number[]}
   */
  function allPorts() {
    return serviceNames().map(function (n) { return config.services[n].port; });
  }

  /**
   * Get service config by port number.
   * @param {number} port
   * @returns {object|null}
   */
  function serviceByPort(port) {
    for (var name in config.services) {
      if (config.services[name].port === port) return config.services[name];
    }
    return null;
  }

  /**
   * Get model profile by name (falls back to defaults.profile, then "light").
   * @param {string} [name]
   * @returns {object|null}
   */
  function modelProfile(name) {
    var profiles = config.modelProfiles || {};
    var defaults = config.defaults || {};
    var selected = name || defaults.profile || "light";
    return profiles[selected] || null;
  }

  // Expose to window for all desktop JS modules
  window.MAOMIAI_RUNTIME_CONFIG = config;
  window.maomiaiRuntimeService = service;
  window.maomiaiRuntimeBaseUrl = baseUrl;
  window.maomiaiRuntimeHealthUrl = healthUrl;
  window.maomiaiRuntimeApiUrl = apiUrl;
  window.maomiaiRuntimeServiceNames = serviceNames;
  window.maomiaiRuntimeAllPorts = allPorts;
  window.maomiaiRuntimeServiceByPort = serviceByPort;
  window.maomiaiRuntimeModelProfile = modelProfile;
})();
"""

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(body, encoding="utf-8")
    print(f"generated: {OUT_PATH}")
    print(f"services: {len(services)}")
    print(f"version: {data.get('version')}")


if __name__ == "__main__":
    main()
