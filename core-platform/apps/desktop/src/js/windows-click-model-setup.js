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
  async function checkLocalModelStatus(options = {}) {
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
  
  function renderProgressSteps(title, steps, activeIndex = 0, extra = "") {
    const rows = steps.map((step, index) => {
      const cls = index < activeIndex ? "done" : (index === activeIndex ? "active" : "");
      const icon = index < activeIndex ? "✓" : (index === activeIndex ? "…" : "○");
      return `<div class="model-progress-step ${cls}">
        <span class="model-progress-icon">${icon}</span>
        <span>${escapeHtml(step)}</span>
      </div>`;
    }).join("");
    return `<div class="model-progress-card">
      <div class="model-progress-title">${escapeHtml(title)}</div>
      <div class="model-progress-bar"><div class="model-progress-fill" style="width:${Math.min(100, Math.max(8, ((activeIndex + 1) / steps.length) * 100))}%"></div></div>
      <div class="model-progress-steps">${rows}</div>
      ${extra ? `<div class="model-progress-extra">${extra}</div>` : ""}
    </div>`;
  }
  function setProgress(title, steps, activeIndex, extra = "") {
    const el = document.getElementById("modelSetupResult");
    if (!el) return;
    el.innerHTML = renderProgressSteps(title, steps, activeIndex, extra);
  }
  function safeParseJsonText(text) {
    if (!text || typeof text !== "string") return null;
    try { return JSON.parse(text); } catch (_) { return null; }
  }
  async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  async function recheckAfterInstall() {
    const steps = [
      "等待安装程序完成",
      "检查本地推理后端",
      "检查本地 AI 后端",
      "刷新状态"
    ];
    for (let i = 0; i < 3; i++) {
      setProgress("正在重新检查本地 AI 状态", steps, Math.min(i + 1, steps.length - 1));
      await sleep(2000);
      try {
        const status = await checkLocalModelStatus({ silent: true });
        if (status?.ready || status?.gateway?.ok || status?.bootstrap?.ok) {
          setResult("本地 AI 状态已更新", "ok", "检测到本地后端已有响应。现在可以准备标准对话能力。", status);
          return status;
        }
      } catch (_) {}
    }
    setResult(
      "安装后仍未连接",
      "bad",
      "安装命令已经执行，但本地后端仍未连接。可能需要等待安装器完成、重启 MAOMIAI，或手动打开本地推理后端。",
      {
        ok: false,
        next_steps: [
          "确认安装器已经完成。",
          "关闭并重新打开 MAOMIAI。",
          "如果 Windows 开始菜单里有本地推理后端，请手动打开一次。",
          "然后回到本页点击重新检查。"
        ]
      }
    );
    return null;
  }

async function installLocalInferenceBackend() {
    if (window.__maomiaiInstallingLocalBackend) {
      setResult("正在安装中", "loading", "安装流程已经在执行，请不要重复点击。", {
        ok: false,
        message: "安装流程正在执行中。"
      });
      return;
    }
    window.__maomiaiInstallingLocalBackend = true;
    const steps = [
      "准备安装命令",
      "请求 Windows 执行安装",
      "等待安装程序完成",
      "自动重新检查状态"
    ];
    try {
      setProgress("正在安装本地推理后端", steps, 0);
      const result = {
        ok: false,
        stage: "install_local_inference_backend",
        tauri: null,
        api: null,
        message: "",
        next_steps: []
      };
      await sleep(300);
      setProgress("正在安装本地推理后端", steps, 1);
      try {
        const invoke =
          window.__TAURI__?.core?.invoke ||
          window.__TAURI_INTERNALS__?.invoke;
        if (invoke) {
          const out = await invoke("install_local_inference_backend");
          const parsed = safeParseJsonText(out);
          result.tauri = { ok: true, output: out, parsed };
          result.ok = true;
          result.message = parsed?.message || "安装命令已执行。";
          setProgress(
            "安装命令已执行",
            steps,
            2,
            `<div class="model-progress-note">请等待 Windows 安装程序完成。完成后系统会自动重新检查。</div>`
          );
          await sleep(2500);
          setProgress("正在重新检查", steps, 3);
          await recheckAfterInstall();
          return result;
        }
        result.tauri = {
          ok: false,
          message: "当前环境没有可用的 Tauri invoke。"
        };
      } catch (e) {
        const parsed = safeParseJsonText(String(e));
        result.tauri = {
          ok: false,
          error: String(e),
          parsed,
          message: parsed?.message || "Tauri 直接安装命令执行失败。"
        };
      }
      setProgress("正在尝试后端安装接口", steps, 1);
      try {
        const apiResult = await postJson(`${API.bootstrap}/bootstrap/install_ollama`, {}, 30000);
        result.api = apiResult;
        if (apiResult?.ok) {
          result.ok = true;
          result.message = "后端安装命令已执行。安装完成后请重新检查。";
          setProgress("安装命令已执行", steps, 2);
          await sleep(2500);
          await recheckAfterInstall();
          return result;
        }
      } catch (e) {
        result.api = {
          ok: false,
          error: String(e),
          message: "18100 安装接口不可用。"
        };
      }
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
    } finally {
      window.__maomiaiInstallingLocalBackend = false;
    }
  }

  async function startLocalModelDownload(profile = "standard") {
    if (window.__maomiaiDownloadingModel) {
      setResult("正在准备能力", "loading", "当前已有下载任务在执行，请不要重复点击。", {
        ok: false,
        profile
      });
      return;
    }
    window.__maomiaiDownloadingModel = true;
    const labelMap = {
      standard: "标准对话能力",
      code: "代码能力",
      light: "轻量快速能力"
    };
    const label = labelMap[profile] || "标准对话能力";
    const steps = [
      "检查本地推理后端",
      "启动本地推理服务",
      `下载 ${label}`,
      "验证能力是否可用",
      "连接到聊天"
    ];
    try {
      setProgress(`正在准备 ${label}`, steps, 0);
      await sleep(500);
      setProgress(`正在准备 ${label}`, steps, 1);
      let result = null;
      try {
        result = await postJson(`${API.bootstrap}/bootstrap/start`, { profile }, 1000 * 60 * 60);
      } catch (e) {
        result = {
          ok: false,
          error: String(e),
          message: "本地 AI 后端暂未连接，无法开始下载。请先点击安装本地推理后端，或重启 MAOMIAI。"
        };
      }
      setProgress(`正在下载 ${label}`, steps, 2, `<div class="model-progress-note">下载时间取决于网络环境和能力包大小，请保持窗口打开。</div>`);
      if (!result?.ok) {
        setResult(
          `${label} 准备失败`,
          "bad",
          result?.message || "下载或验证失败。",
          {
            ok: false,
            profile,
            result,
            next_steps: [
              "确认本地推理后端已经安装。",
              "点击\"检查本地 AI 状态\"。",
              "如果仍不可用，请重启 MAOMIAI 后重试。"
            ]
          }
        );
        return result;
      }
      setProgress(`正在验证 ${label}`, steps, 3);
      await sleep(1000);
      const status = await checkLocalModelStatus({ silent: true });
      setProgress(`${label} 已准备完成`, steps, 4);
      await sleep(800);
      setResult(
        `${label} 已准备完成`,
        "ok",
        "本地 AI 能力已下载并连接。现在可以返回对话直接使用。",
        {
          ok: true,
          profile,
          result,
          status,
          next_steps: [
            "点击返回对话。",
            "输入问题测试本地 AI 回复。"
          ]
        }
      );
      return result;
    } finally {
      window.__maomiaiDownloadingModel = false;
    }
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
          <button data-action="download-model-standard">
            <strong>下载标准对话能力</strong>
            <span>适合日常问答、总结、文档理解和任务规划。</span>
          </button>
          <button data-action="download-model-code">
            <strong>下载代码能力</strong>
            <span>适合代码生成、代码审查、错误分析和项目修复。</span>
          </button>
          <button data-action="download-model-light">
            <strong>下载轻量快速能力</strong>
            <span>适合低配置电脑和快速响应场景。</span>
          </button>
          <button data-action="install-local-inference">
            <strong>安装本地推理后端</strong>
            <span>如果尚未安装本地推理后端，点击此按钮安装。</span>
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
    if (action === "download-model-standard") {
      e.preventDefault();
      startLocalModelDownload("standard");
      return;
    }
    if (action === "download-model-code") {
      e.preventDefault();
      startLocalModelDownload("code");
      return;
    }
    if (action === "download-model-light") {
      e.preventDefault();
      startLocalModelDownload("light");
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
