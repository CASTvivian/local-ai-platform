// P3.14-D7-C3-B: Windows click fallback + local model setup entry.
// Loaded last. Avoid relying on inline onclick only.
(function () {
  const API = {
    bootstrap: "http://127.0.0.1:18100",
    modelGateway: "http://127.0.0.1:18080",
  };
  function esc(v) {
    return String(v ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
  function promptEl() {
    return document.getElementById("prompt") ||
      document.getElementById("composerInput") ||
      document.querySelector("textarea");
  }
  function contentEl() {
    return document.getElementById("content") || document.querySelector(".content");
  }
  function preview(title, value) {
    if (typeof window.previewText === "function") {
      window.previewText(title, typeof value === "string" ? value : JSON.stringify(value, null, 2), "json");
      return;
    }
    const box = document.getElementById("previewBox") || document.getElementById("content");
    if (box) {
      box.innerHTML = `<pre class="mono">${esc(typeof value === "string" ? value : JSON.stringify(value, null, 2))}</pre>`;
    }
  }
  async function getJson(url, timeout = 10000) {
    const res = await fetch(url, { signal: AbortSignal.timeout(timeout) });
    const text = await res.text();
    try {
      return JSON.parse(text);
    } catch {
      return { raw: text, ok: res.ok };
    }
  }
  async function postJson(url, body, timeout = 60000) {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body || {}),
      signal: AbortSignal.timeout(timeout),
    });
    const text = await res.text();
    try {
      return JSON.parse(text);
    } catch {
      return { raw: text, ok: res.ok };
    }
  }
  function fillPrompt(text) {
    const input = promptEl();
    if (!input) return;
    input.value = text;
    input.focus();
  }
  async function checkLocalModelStatus() {
    const result = {
      title: "本地模型状态检查",
      bootstrap: null,
      gateway: null,
      message: "",
    };
    try {
      result.bootstrap = await getJson(`${API.bootstrap}/bootstrap/status`, 8000);
    } catch (e) {
      result.bootstrap = {
        ok: false,
        error: String(e),
        hint: "模型准备服务未启动或不可访问。",
      };
    }
    try {
      result.gateway = await postJson(`${API.modelGateway}/generate`, {
        model: "default",
        prompt: "请用一句中文回答：本地模型是否可用？",
        stream: false,
      }, 30000);
    } catch (e) {
      result.gateway = {
        ok: false,
        error: String(e),
        hint: "本地模型网关未启动或模型暂不可用。",
      };
    }
    result.message = result.gateway?.response || result.gateway?.text || result.gateway?.raw || "状态检查完成。";
    preview("本地模型状态", result);
    renderModelSetupResult(result);
    return result;
  }
  async function startLocalModelDownload(kind) {
    const payload = {
      profile: kind || "standard",
      // UI 不展示具体模型名；后端可自行映射 profile 到实际模型。
      models: kind === "code" ? ["code-capability"] : ["standard-chat"],
    };
    let result;
    try {
      result = await postJson(`${API.bootstrap}/bootstrap/start`, payload, 10000);
    } catch (e) {
      result = {
        ok: false,
        error: String(e),
        hint: "模型准备服务暂不可用。请先确认后端服务已启动。",
      };
    }
    preview("本地模型准备", result);
    renderModelSetupResult(result);
    return result;
  }
  function renderModelSetupResult(result) {
    let box = document.getElementById("modelSetupResult");
    if (!box) {
      const content = contentEl();
      if (!content) return;
      box = document.createElement("div");
      box.id = "modelSetupResult";
      box.className = "model-setup-result";
      content.appendChild(box);
    }
    box.innerHTML = `
      <div class="model-result-card">
        <div class="model-result-title">本地模型状态</div>
        <pre>${esc(JSON.stringify(result, null, 2))}</pre>
      </div>
    `;
  }
  function renderModelSetupPage() {
    const content = contentEl();
    if (!content) return;
    content.innerHTML = `
      <div class="gpt-home model-setup-home">
        <div class="gpt-logo">M</div>
        <h1>本地模型准备</h1>
        <p>这里用于检查和准备本地 AI 能力。普通用户无需理解具体模型名称，只需要选择用途即可。</p>
        <div class="model-setup-grid">
          <button data-action="check-model-status">
            <strong>检查本地模型状态</strong>
            <span>确认本地模型网关、推理后端和当前能力是否可用。</span>
          </button>
          <button data-action="download-standard-model">
            <strong>准备标准对话能力</strong>
            <span>适合日常问答、总结、文档理解和任务规划。</span>
          </button>
          <button data-action="download-code-model">
            <strong>准备代码能力</strong>
            <span>适合代码生成、代码审查、错误分析和项目修复。</span>
          </button>
          <button data-action="back-to-chat">
            <strong>返回对话</strong>
            <span>下载或检查完成后，回到主对话继续使用。</span>
          </button>
        </div>
        <div id="modelSetupResult" class="model-setup-result"></div>
      </div>
    `;
  }
  function ensureHomeHasModelCard() {
    const grid = document.querySelector(".gpt-suggestions");
    if (!grid || grid.__modelCardInjected) return;
    const btn = document.createElement("button");
    btn.setAttribute("data-action", "open-model-setup");
    btn.innerHTML = `
      <strong>准备本地模型</strong>
      <span>检查本地 AI 能力，或按用途准备对话/代码能力。</span>
    `;
    grid.appendChild(btn);
    grid.__modelCardInjected = true;
  }
  function handleClick(e) {
    const target = e.target.closest("button, [data-action], [data-view]");
    if (!target) return;
    const action = target.getAttribute("data-action");
    const view = target.getAttribute("data-view");
    if (action || view) {
      console.log("[windows-click-model-setup] click", { action, view });
    }
    if (action === "fill-prompt") {
      e.preventDefault();
      fillPrompt(target.getAttribute("data-prompt") || "");
      return;
    }
    if (action === "open-model-setup" || view === "models") {
      e.preventDefault();
      renderModelSetupPage();
      return;
    }
    if (action === "check-model-status") {
      e.preventDefault();
      checkLocalModelStatus();
      return;
    }
    if (action === "download-standard-model") {
      e.preventDefault();
      startLocalModelDownload("standard");
      return;
    }
    if (action === "download-code-model") {
      e.preventDefault();
      startLocalModelDownload("code");
      return;
    }
    if (action === "back-to-chat") {
      e.preventDefault();
      if (typeof window.setView === "function") window.setView("chat");
      else if (typeof window.chatRender === "function") window.chatRender();
      return;
    }
    // Windows fallback for nav buttons.
    if (view && typeof window.setView === "function") {
      e.preventDefault();
      window.setView(view);
      return;
    }
  }
  function patchSuggestionButtons() {
    const buttons = Array.from(document.querySelectorAll(".gpt-suggestions button"));
    for (const btn of buttons) {
      const onclick = btn.getAttribute("onclick") || "";
      const match = onclick.match(/fillPrompt\('([\s\S]*)'\)/);
      if (match && !btn.getAttribute("data-action")) {
        btn.setAttribute("data-action", "fill-prompt");
        btn.setAttribute("data-prompt", match[1].replace(/\\'/g, "'"));
        btn.removeAttribute("onclick");
      }
    }
  }
  function patchSendButton() {
    const send = Array.from(document.querySelectorAll("button"))
      .find((b) => (b.textContent || "").trim() === "发送");
    if (!send || send.__windowsSendPatched) return;
    send.__windowsSendPatched = true;
    send.addEventListener("click", (e) => {
      const input = promptEl();
      if (!input || !input.value.trim()) return;
      // Prefer session manager if present.
      if (typeof window.sendMessage === "function") {
        e.preventDefault();
        e.stopPropagation();
        window.sendMessage();
        return;
      }
      if (typeof window.submitTask === "function") {
        e.preventDefault();
        e.stopPropagation();
        window.submitTask();
      }
    }, true);
  }
  function tick() {
    ensureHomeHasModelCard();
    patchSuggestionButtons();
    patchSendButton();
  }
  window.renderModelSetupPage = renderModelSetupPage;
  window.checkLocalModelStatus = checkLocalModelStatus;
  window.startLocalModelDownload = startLocalModelDownload;
  document.addEventListener("click", handleClick, true);
  document.addEventListener("DOMContentLoaded", () => {
    tick();
    setTimeout(tick, 300);
    setTimeout(tick, 1200);
  });
  setInterval(tick, 2000);
  console.log("[D7-C3-B] Windows click fix + model setup loaded");
})();
