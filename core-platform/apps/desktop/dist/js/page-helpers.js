// P3.14-D4-D3-C: shared page helpers.
// Loaded before js/pages/*.js to provide shared UI rendering functions.

function escapeHtmlGlobal(value) {
  if (typeof escapeHtml === "function") return escapeHtml(value);
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

function pageHero(title, desc) {
  return `<div class="hero"><h1>${escapeHtmlGlobal(title)}</h1><p>${escapeHtmlGlobal(desc)}</p></div>`;
}

function emptyState(text) {
  return `<div class="empty-state">${escapeHtmlGlobal(text)}</div>`;
}

function renderBadge(text, status = "neutral") {
  const colors = {
    neutral: "#6b7280",
    success: "#16a34a",
    warning: "#f59e0b",
    error: "#dc2626",
    info: "#3b82f6"
  };
  const bg = colors[status] || colors.neutral;
  return `<span class="badge" style="background:${bg};color:#fff;">${escapeHtmlGlobal(text)}</span>`;
}

function systemMessage(text) {
  const s = currentSession();
  s.messages.push({ role: "assistant", text: text || "", ts: Date.now() });
  saveState();
  render();
}

function commaList(arr) {
  if (!Array.isArray(arr) || arr.length === 0) return "";
  return arr.filter(Boolean).join(", ");
}

function monoText(text) {
  return `<span class="mono">${escapeHtmlGlobal(String(text))}</span>`;
}

// Ensure functions are available globally
window.pageHero = pageHero;
window.emptyState = emptyState;
window.renderBadge = renderBadge;
window.systemMessage = systemMessage;
window.commaList = commaList;
window.monoText = monoText;
