// AUTO-GENERATED FILE. DO NOT EDIT BY HAND.
// Source: data/runtime_config/runtime_config.json
// Generator: scripts/build/generate_desktop_runtime_config.py
// GeneratedAt: 2026-05-16T07:08:26.549471+00:00
(function () {
  var config = {
  "version": "c25-c14-b7d",
  "generatedAt": "2026-05-16T07:08:26.549471+00:00",
  "source": "data/runtime_config/runtime_config.json",
  "host": "127.0.0.1",
  "services": {
    "ollama": {
      "port": 11434,
      "baseUrl": "http://127.0.0.1:11434",
      "healthPath": "/api/tags"
    },
    "modelGateway": {
      "port": 18080,
      "baseUrl": "http://127.0.0.1:18080",
      "healthPath": "/health"
    },
    "autoRouter": {
      "port": 18093,
      "baseUrl": "http://127.0.0.1:18093",
      "healthPath": "/health"
    },
    "modelBootstrap": {
      "port": 18100,
      "baseUrl": "http://127.0.0.1:18100",
      "healthPath": "/health"
    },
    "referenceSkill": {
      "port": 18101,
      "baseUrl": "http://127.0.0.1:18101",
      "healthPath": "/health"
    },
    "capabilityLearning": {
      "port": 18102,
      "baseUrl": "http://127.0.0.1:18102",
      "healthPath": "/health"
    },
    "runtimeExecution": {
      "port": 18104,
      "baseUrl": "http://127.0.0.1:18104",
      "healthPath": "/health"
    },
    "policyEngine": {
      "port": 18110,
      "baseUrl": "http://127.0.0.1:18110",
      "healthPath": "/health"
    },
    "traceObservability": {
      "port": 18111,
      "baseUrl": "http://127.0.0.1:18111",
      "healthPath": "/health"
    },
    "evalGateway": {
      "port": 18112,
      "baseUrl": "http://127.0.0.1:18112",
      "healthPath": "/health"
    },
    "documentIngestion": {
      "port": 18120,
      "baseUrl": "http://127.0.0.1:18120",
      "healthPath": "/health"
    },
    "skillStore": {
      "port": 18121,
      "baseUrl": "http://127.0.0.1:18121",
      "healthPath": "/health"
    },
    "jobOrchestrator": {
      "port": 18122,
      "baseUrl": "http://127.0.0.1:18122",
      "healthPath": "/health"
    },
    "artifactRegistry": {
      "port": 18123,
      "baseUrl": "http://127.0.0.1:18123",
      "healthPath": "/health"
    },
    "codeReviewGate": {
      "port": 18124,
      "baseUrl": "http://127.0.0.1:18124",
      "healthPath": "/health"
    },
    "repoMemory": {
      "port": 18125,
      "baseUrl": "http://127.0.0.1:18125",
      "healthPath": "/health"
    },
    "workflowStore": {
      "port": 18126,
      "baseUrl": "http://127.0.0.1:18126",
      "healthPath": "/health"
    },
    "designSystem": {
      "port": 18127,
      "baseUrl": "http://127.0.0.1:18127",
      "healthPath": "/health"
    },
    "agentRuntime": {
      "port": 18131,
      "baseUrl": "http://127.0.0.1:18131",
      "healthPath": "/health"
    }
  },
  "modelProfiles": {
    "light": {
      "title": "Light local model",
      "provider": "ollama",
      "model": "qwen2.5:1.5b",
      "purpose": "fast local demo and low-resource chat"
    },
    "balanced": {
      "title": "Balanced local model",
      "provider": "ollama",
      "model": "qwen2.5:7b",
      "purpose": "general reasoning and demo"
    },
    "coder": {
      "title": "Coder local model",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b",
      "purpose": "coding, repo analysis, and developer tasks"
    }
  },
  "defaults": {
    "profile": "light",
    "planner_model_mode": "auto",
    "agent_runtime_required": true,
    "dry_run_enabled": false
  },
  "packaging": {
    "single_source": true,
    "mac_start_script": "scripts/mac/start_all.sh",
    "windows_start_script": "scripts/windows/start_all.ps1"
  }
};

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
    return s.baseUrl.replace(/\/+$/, "") + "/" + (s.healthPath || "/health").replace(/^\/+/, "");
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
    return s.baseUrl.replace(/\/+$/, "") + "/" + (path || "").replace(/^\/+/, "");
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
