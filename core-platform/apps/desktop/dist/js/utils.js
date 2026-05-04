// P3.14-D3-X2 extracted utilities
function escapeHtml(s) {
  return String(s || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function escapeJs(s) {
  return String(s || "").replace(/\\/g, "\\\\").replace(/'/g, "\\'");
}

function safeJsonStringify(value, spaces = 2) {
  try {
    return JSON.stringify(value, null, spaces);
  } catch (e) {
    return String(value);
  }
}
