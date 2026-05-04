// P3.14-D3-X2 extracted API helpers
const API = {
  router: "http://127.0.0.1:18093",
  runtime: "http://127.0.0.1:18104",
  trace: "http://127.0.0.1:18111",
  artifact: "http://127.0.0.1:18123",
  eval: "http://127.0.0.1:18112",
  skill: "http://127.0.0.1:18121",
  doc: "http://127.0.0.1:18120",
  designSystem: "http://127.0.0.1:18127",
  codeReview: "http://127.0.0.1:18124",
  repoMemory: "http://127.0.0.1:18125",
  workflow: "http://127.0.0.1:18126",
  model: "http://127.0.0.1:18100"
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
