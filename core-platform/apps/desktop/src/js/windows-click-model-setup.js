// P3.14-D7-C3-C: Windows click fallback + visible local AI setup feedback.
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
  function contentEl() {
    return document.getElementById("content") || document.querySelector(".content");
  }
  function promptEl() {
    return document.getElementById("prompt") || document.querySelector("textarea");
  }
  function setResult(title, status, detail, raw) {
    let box = document.getElementById("modelSetupResult");
    if (!box) {
      const content = contentEl();
      if (!content) return;
      box = document.createElement("div");
      box.id = "modelSetupResult";
      box.className = "model-setup-result";
      content.appendChild(box);
    }
    const statusClass = status === "ok" ? "ok" : status === "loading" ? "loading" : "bad";
    box.innerHTML = `
      <div class="model-result-card ${statusClass}">
        <div class="model-result-title">${esc(title)}</div>
        <div class="model-result-detail">${esc(detail)}</div>
        ${raw ? `<pre>${esc(typeof raw === "string" ? raw : JSON.stringify(raw, null, 2))}</pre>` : ""}
        <div class="model-result-actions">
          <button data-action="check-model-status">重新检查</button>
          <button data-action="install-local-inference">安装本地推理后端</button>
          <button data-action="back-to-chat">返回对话</button>
        </div>
      </div>
    `;
  }
  async function getJson(url, timeout = 10000) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), timeout);
    try {
      const res = await fetch(url, { signal: ctrl.signal });
      const text = await res.text();
      try {
        return JSON.parse(text);
      } catch {
        return { ok: res.ok, raw: text };
      }
    } finally {
      clearTimeout(timer);
    }
  }
  async function postJson(url, body, timeout = 60000) {
    const ctrl = new AbortController();
    const timer = setTimeout(() => ctrl.abort(), timeout);
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body || {}),
        signal: ctrl.signal,
      });
      const text = await res.text();
      try {
        return JSON.parse(text);
      } catch {
        return { ok: res.ok, raw: text };
      }
    } finally {
      clearTimeout(timer);
    }
  }
  function explainBackendUnavailable(raw) {
    return {
      ok: false,
      message: "本地 AI 后端暂未连接。",
      next_steps: [
        "确认桌面后端服务已经启动；首次使用时可能需要下载运行环境。",
        "回到右侧服务面板查看服务健康状态。",
        "如果是第一次安装，请先运行随包附带的启动脚本，或等待后续版本自动启动服务。",
      ],
      raw,
    };
  }
  async function checkLocalModelStatus() {
    setResult("正在检查本地 AI", "loading", "正在连接本地服务，请稍候...", null);
    const result = {
      title: "本地 AI 状态检查",
      bootstrap: null,
      gateway: null,
      ready: false,
    };
    try {
      result.bootstrap = await getJson(`${API.bootstrap}/bootstrap/status`, 8000);
    } catch (e) {
      result.bootstrap = explainBackendUnavailable(String(e));
    }
    try {
      result.gateway = await postJson(`${API.modelGateway}/generate`, {
        model: "default",
        prompt: "请用一句中文回答：本地 AI 是否可用？",
        stream: false,
      }, 30000);
    } catch (e) {
      result.gateway = explainBackendUnavailable(String(e));
    }
    const reply = result.gateway?.response || result.gateway?.text || result.gateway?.raw || "";
    result.ready = Boolean(reply && !result.gateway?.message?.includes("暂未连接"));
    if (result.ready) {
      setResult("本地 AI 可用", "ok", "本地模型网关已连接，可以回到对话继续使用。", result);
    } else {
      setResult("本地 AI 暂未连接", "bad", "当前 App 界面正常，但本地后端服务还没有连接成功。系统会尝试自动准备运行环境，请稍后重试。", result);
    }
    return result;
  }
  async function installLocalInferenceBackend() {
    setResult("正在安装本地推理后端", "loading", "正在请求系统安装。Windows 可能会弹出 PowerShell 或安全确认，请允许执行。", null);
    const result = {
      ok: false,
      stage: "install_local_inference_backend",
      tauri: null,
      api: null,
      message: "",
      next_steps: []
    };
    // 1) Prefer direct Tauri command. This does not depend on 18100.
    try {
      const invoke =
        window.__TAURI__?.core?.invoke ||
        window.__TAURI_INTERNALS__?.invoke;
      if (invoke) {
        const out = await invoke("install_local_inference_backend");
        result.tauri = { ok: true, output: out };
        result.ok = true;
        result.message = "安装命令已执行。安装完成后，请重新点击\"检查本地 AI 状态\"。";
        result.next_steps = [
          "等待安装程序完成。",
          "安装完成后重新打开 MAOMIAI 或点击重新检查。",
          "如果仍不可用，请手动打开官方下载页安装。"
        ];
        setResult("安装命令已执行", "ok", result.message, result);
        return result;
      }
      result.tauri = {
        ok: false,
        message: "当前环境没有可用的 Tauri invoke。"
      };
    } catch (e) {
      result.tauri = {
        ok: false,
        error: String(e),
        message: "Tauri 直接安装命令执行失败。"
      };
    }
    // 2) Try backend API fallback if 18100 is available.
    try {
      const apiResult = await postJson(`${API.bootstrap}/bootstrap/install_ollama`, {}, 30000);
      result.api = apiResult;
      if (apiResult?.ok) {
        result.ok = true;
        result.message = "后端安装命令已执行。安装完成后请重新检查。";
        setResult("安装命令已执行", "ok", result.message, result);
        return result;
      }
    } catch (e) {
      result.api = {
        ok: false,
        error: String(e),
        message: "18100 安装接口不可用。"
      };
    }
    // 3) Last fallback: open official page or show command.
    try {
      window.open("https://ollama.com/download/windows", "_blank");
    } catch (_) {}
    result.ok = false;
    result.message = "无法自动安装本地推理后端，已尝试打开官方下载页。";
    result.install_url = "https://ollama.com/download/windows";
    result.install_command = "irm https://ollama.com/install.ps1 | iex";
    result.next_steps = [
      "请打开官方下载页安装 Windows 版本。",
      "或在 PowerShell 中执行安装命令。",
      "安装完成后重新打开 MAOMIAI。",
      "回到本地 AI 准备页点击重新检查。"
    ];
    setResult("需要手动安装本地推理后端", "bad", result.message, result);
    return result;
  }

  async function startLocalModelDownload(kind) {
    const label = kind === "code" ? "代码能力" : "标准对话能力";
    setResult(`正在准备${label}`, "loading", "正在请求本地模型准备服务...", null);
    let result;
    try {
      result = await postJson(`${API.bootstrap}/bootstrap/start`, {
        profile: kind || "standard",
        models: kind === "code" ? ["code-capability"] : ["standard-chat"],
      }, 15000);
    } catch (e) {
      result = explainBackendUnavailable(String(e));
    }
    if (result?.ok) {
      setResult(`${label}准备中`, "ok", "已提交本地准备任务，请稍后重新检查状态。", result);
    } else {
      setResult(`${label}暂未开始`, "bad", "模型准备服务未连接。请先启动本地服务后重试。", result);
    }
    return result;
  }
  function renderModelSetupPage() {
    const content = contentEl();
    if (!content) return;
    content.innerHTML = `
      <div class="gpt-home model-setup-home">
        <div class="gpt-logo">M</div>
        <h1>本地 AI 准备</h1>
        <p>检查本地 AI 能力是否可用，或按用途准备对话、代码能力。普通用户无需理解具体模型名称。</p>
        <div class="model-setup-grid">
          <button data-action="check-model-status">
            <strong>检查本地 AI 状态</strong>
            <span>确认本地服务、推理后端和当前能力是否可用。</span>
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
            <span>检查或准备完成后，回到主对话继续使用。</span>
          </button>
        </div>
        <div id="modelSetupResult" class="model-setup-result">
          <div class="model-result-card">
            <div class="model-result-title">尚未检查</div>
            <div class="model-result-detail">点击上方按钮开始检查或准备本地 AI。</div>
          </div>
        </div>
      </div>
    `;
  }
  function fillPrompt(text) {
    const input = promptEl();
    if (!input) return;
    input.value = text;
    input.focus();
  }
  function ensureHomeHasModelCard() {
    const grid = document.querySelector(".gpt-suggestions");
    if (!grid || grid.__modelCardInjected) return;
    const btn = document.createElement("button");
    btn.setAttribute("data-action", "open-model-setup");
    btn.innerHTML = `
      <strong>准备本地 AI</strong>
      <span>检查本地能力是否可用，或准备对话/代码能力。</span>
    `;
    grid.appendChild(btn);
    grid.__modelCardInjected = true;
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
    const buttons = Array.from(document.querySelectorAll("button"));
    const send = buttons.find((b) => (b.textContent || "").trim() === "发送");
    if (!send || send.__sendPatchedD7C3C) return;
    send.__sendPatchedD7C3C = true;
    send.addEventListener("click", (e) => {
      const input = promptEl();
      if (!input || !input.value.trim()) return;
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
  function handleAction(e) {
    const target = e.target.closest("button, [data-action], [data-view]");
    if (!target) return;
    const action = target.getAttribute("data-action");
    const view = target.getAttribute("data-view");
    if (action === "install-local-inference") {
      e.preventDefault();
      installLocalInferenceBackend();
      return;
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
      return;
    }
    if (view && typeof window.setView === "function") {
      e.preventDefault();
      window.setView(view);
    }
  }
  function tick() {
    ensureHomeHasModelCard();
    patchSuggestionButtons();
    patchSendButton();
  }
  window.renderModelSetupPage = renderModelSetupPage;
  window.checkLocalModelStatus = checkLocalModelStatus;
  window.startLocalModelDownload = startLocalModelDownload;
  window.installLocalInferenceBackend = installLocalInferenceBackend;
  // pointerdown makes Windows WebView clicks feel more reliable.
  document.addEventListener("pointerdown", handleAction, true);
  document.addEventListener("click", handleAction, true);
  document.addEventListener("DOMContentLoaded", () => {
    tick();
    setTimeout(tick, 300);
    setTimeout(tick, 1200);
  });
  setInterval(tick, 2000);
  console.log("[D7-C3-C] product model setup feedback loaded");
})();
