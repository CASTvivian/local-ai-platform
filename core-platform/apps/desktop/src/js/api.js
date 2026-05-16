// P3.14-D3-X2 extracted API helpers
// C25-C14-B7-C: URLs now from window.MAOMIAI_RUNTIME_CONFIG
const API = {
  router:       window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("autoRouter")       : "http://127.0.0.1:18093",
  runtime:      window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("runtimeExecution")  : "http://127.0.0.1:18104",
  trace:        window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("traceObservability"): "http://127.0.0.1:18111",
  artifact:     window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("artifactRegistry")  : "http://127.0.0.1:18123",
  eval:         window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("evalGateway")       : "http://127.0.0.1:18112",
  skill:        window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("skillStore")        : "http://127.0.0.1:18121",
  doc:          window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("documentIngestion") : "http://127.0.0.1:18120",
  designSystem: window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("designSystem")      : "http://127.0.0.1:18127",
  codeReview:   window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("codeReviewGate")    : "http://127.0.0.1:18124",
  repoMemory:   window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("repoMemory")        : "http://127.0.0.1:18125",
  workflow:     window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("workflowStore")     : "http://127.0.0.1:18126",
  model:        window.maomiaiRuntimeBaseUrl ? window.maomiaiRuntimeBaseUrl("modelBootstrap")    : "http://127.0.0.1:18100"
};
async function postJson(url, body, timeoutMs = 12000) {
  const res = await fetch(url, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(body || {}),
    signal: AbortSignal.timeout(timeoutMs),
  });
  return await res.json();
}
async function getJson(url, timeoutMs = 12000) {
  const res = await fetch(url, {
    method: "GET",
    signal: AbortSignal.timeout(timeoutMs),
  });
  return await res.json();
}
