// P3.14-D3-X3-A extracted service health module
// C25-C14-B7-C: URLs from centralized runtime config.

const CORE_SERVICES = (function () {
  // Build service list from runtime config if available
  if (window.MAOMIAI_RUNTIME_CONFIG && window.MAOMIAI_RUNTIME_CONFIG.services) {
    var svcMap = {
      autoRouter:        "Auto Router",
      referenceSkill:    "Reference Skill",
      capabilityLearning:"Capability Learning",
      runtimeExecution:  "Runtime Execution",
      policyEngine:      "Policy Engine",
      traceObservability:"Trace Observability",
      evalGateway:       "Eval Gateway",
      documentIngestion: "Document Ingestion",
      skillStore:        "Skill Store",
      jobOrchestrator:   "Job Orchestrator",
      artifactRegistry:  "Artifact Registry",
      codeReviewGate:    "Code Review Gate",
      repoMemory:        "Repo Memory",
      workflowStore:     "Workflow Store",
      designSystem:      "Design System"
    };
    var result = [];
    for (var key in svcMap) {
      if (window.MAOMIAI_RUNTIME_CONFIG.services[key]) {
        result.push({ name: svcMap[key], port: window.MAOMIAI_RUNTIME_CONFIG.services[key].port });
      }
    }
    if (result.length > 0) return result;
  }
  // Fallback
  return [
    { name: "Auto Router", port: 18093 },
    { name: "Reference Skill", port: 18101 },
    { name: "Capability Learning", port: 18102 },
    { name: "Runtime Execution", port: 18104 },
    { name: "Policy Engine", port: 18110 },
    { name: "Trace Observability", port: 18111 },
    { name: "Eval Gateway", port: 18112 },
    { name: "Document Ingestion", port: 18120 },
    { name: "Skill Store", port: 18121 },
    { name: "Job Orchestrator", port: 18122 },
    { name: "Artifact Registry", port: 18123 },
    { name: "Code Review Gate", port: 18124 },
    { name: "Repo Memory", port: 18125 },
    { name: "Workflow Store", port: 18126 },
    { name: "Design System", port: 18127 },
  ];
})();

async function checkServiceHealth(service) {
  const host = (window.MAOMIAI_RUNTIME_CONFIG && window.MAOMIAI_RUNTIME_CONFIG.host) || "127.0.0.1";
  const url = `http://${host}:${service.port}/health`;
  try {
    const res = await fetch(url, { signal: AbortSignal.timeout(1800) });
    const json = await res.json();
    return { ...service, ok: !!json.ok, detail: json };
  } catch (e) {
    return { ...service, ok: false, error: e.message };
  }
}
async function refreshHealth() {
  const box = document.getElementById("serviceGrid") || document.getElementById("healthGrid");
  if (box) box.innerHTML = `<div class="mono">checking services...</div>`;
  const list = typeof CORE_SERVICES !== "undefined" ? CORE_SERVICES : (typeof SERVICES !== "undefined" ? SERVICES : []);
  const results = await Promise.all(list.map(checkServiceHealth));
  renderServiceHealth(results);
  return results;
}
function renderServiceHealth(results) {
  const box = document.getElementById("serviceGrid") || document.getElementById("healthGrid");
  if (!box) return;
  box.innerHTML = results.map(s => `
    <div class="service-row">
      <span class="dot ${s.ok ? "ok" : "bad"}"></span>
      <div>
        <b>${escapeHtml(s.name || String(s.port))}</b><br/>
        <span class="mono">${escapeHtml(String(s.port))}</span>
      </div>
    </div>
  `).join("");
  const top = document.getElementById("serviceStatus");
  if (top) {
    const okCount = results.filter(x => x.ok).length;
    top.textContent = `${okCount}/${results.length} services`;
  }
}
async function loadServiceHealth() {
  return refreshHealth();
}
