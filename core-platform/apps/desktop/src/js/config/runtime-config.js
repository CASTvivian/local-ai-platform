// C25-C14-B7-C: Centralized runtime config for desktop JS.
// All service URLs come from this single source.
// To change ports, edit this file (or generate it from runtime_config.json in B7-D).
(function () {
  var config = {
    version: "c25-c14-b7c",
    host: "127.0.0.1",
    services: {
      ollama:            { port: 11434, baseUrl: "http://127.0.0.1:11434", healthPath: "/api/tags" },
      modelGateway:      { port: 18080, baseUrl: "http://127.0.0.1:18080", healthPath: "/health" },
      autoRouter:        { port: 18093, baseUrl: "http://127.0.0.1:18093", healthPath: "/health" },
      modelBootstrap:    { port: 18100, baseUrl: "http://127.0.0.1:18100", healthPath: "/health" },
      referenceSkill:    { port: 18101, baseUrl: "http://127.0.0.1:18101", healthPath: "/health" },
      capabilityLearning:{ port: 18102, baseUrl: "http://127.0.0.1:18102", healthPath: "/health" },
      runtimeExecution:  { port: 18104, baseUrl: "http://127.0.0.1:18104", healthPath: "/health" },
      policyEngine:      { port: 18110, baseUrl: "http://127.0.0.1:18110", healthPath: "/health" },
      traceObservability:{ port: 18111, baseUrl: "http://127.0.0.1:18111", healthPath: "/health" },
      evalGateway:       { port: 18112, baseUrl: "http://127.0.0.1:18112", healthPath: "/health" },
      documentIngestion: { port: 18120, baseUrl: "http://127.0.0.1:18120", healthPath: "/health" },
      skillStore:        { port: 18121, baseUrl: "http://127.0.0.1:18121", healthPath: "/health" },
      jobOrchestrator:   { port: 18122, baseUrl: "http://127.0.0.1:18122", healthPath: "/health" },
      artifactRegistry:  { port: 18123, baseUrl: "http://127.0.0.1:18123", healthPath: "/health" },
      codeReviewGate:    { port: 18124, baseUrl: "http://127.0.0.1:18124", healthPath: "/health" },
      repoMemory:        { port: 18125, baseUrl: "http://127.0.0.1:18125", healthPath: "/health" },
      workflowStore:     { port: 18126, baseUrl: "http://127.0.0.1:18126", healthPath: "/health" },
      designSystem:      { port: 18127, baseUrl: "http://127.0.0.1:18127", healthPath: "/health" },
      agentRuntime:      { port: 18131, baseUrl: "http://127.0.0.1:18131", healthPath: "/health" }
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

  // Expose to window for all desktop JS modules
  window.MAOMIAI_RUNTIME_CONFIG = config;
  window.maomiaiRuntimeService = service;
  window.maomiaiRuntimeBaseUrl = baseUrl;
  window.maomiaiRuntimeHealthUrl = healthUrl;
  window.maomiaiRuntimeApiUrl = apiUrl;
  window.maomiaiRuntimeServiceNames = serviceNames;
  window.maomiaiRuntimeAllPorts = allPorts;
  window.maomiaiRuntimeServiceByPort = serviceByPort;
})();
