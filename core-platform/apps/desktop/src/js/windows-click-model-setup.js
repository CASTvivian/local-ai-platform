(function () {
  const API = {
    bootstrap: "http://127.0.0.1:18100",
    gateway: "http://127.0.0.1:18080"
  };
  window.__MAOMIAI_MODEL_STATUS__ = window.__MAOMIAI_MODEL_STATUS__ || null;
  window.__MAOMIAI_MODEL_JOBS__ = window.__MAOMIAI_MODEL_JOBS__ || {};
  window.__MAOMIAI_CURRENT_MODEL_PROFILE__ = localStorage.getItem("maomiai_current_model_profile") || "standard";
  const MODEL_CATALOG = [
    {
      profile: "standard",
      title: "标准对话能力",
      model: "qwen2.5:7b",
      tag: "推荐默认",
      size: "中等",
      hardware: "建议 16GB 内存以上",
      desc: "适合中文问答、总结、写作、文档理解、普通任务规划，是默认推荐能力。",
      type: "chat"
    },
    {
      profile: "light",
      title: "轻量快速能力",
      model: "qwen2.5:1.5b",
      tag: "低配优先",
      size: "小",
      hardware: "低配置电脑可用",
      desc: "适合低配电脑、快速响应、简单问答和轻量任务。",
      type: "chat"
    },
    {
      profile: "code",
      title: "代码能力",
      model: "qwen2.5-coder:7b",
      tag: "开发推荐",
      size: "中等",
      hardware: "建议 16GB 内存以上",
      desc: "适合代码生成、代码审查、报错分析、项目修复和技术方案整理。",
      type: "code"
    },
    {
      profile: "reasoning",
      title: "推理分析能力",
      model: "deepseek-r1:7b",
      tag: "复杂分析",
      size: "中等",
      hardware: "建议 16GB 内存以上",
      desc: "适合复杂问题拆解、逻辑推理、策略分析和多步骤规划。",
      type: "reasoning"
    },
    {
      profile: "english",
      title: "英文通用能力",
      model: "llama3.1:8b",
      tag: "英文/通用",
      size: "中等",
      hardware: "建议 16GB 内存以上",
      desc: "适合英文问答、通用任务、跨语言测试和国际化场景。",
      type: "chat"
    },
    {
      profile: "small",
      title: "小型通用能力",
      model: "llama3.2:3b",
      tag: "轻量通用",
      size: "小",
      hardware: "低配置电脑可用",
      desc: "适合轻量问答、快速测试和低配置机器。",
      type: "chat"
    },
    {
      profile: "embed",
      title: "文档向量能力",
      model: "nomic-embed-text",
      tag: "知识库",
      size: "小",
      hardware: "普通配置可用",
      desc: "适合文档检索、知识库、RAG。本能力不是聊天模型，用于文档向量化。",
      type: "embedding"
    },
    {
      profile: "embed_multi",
      title: "多语言文档向量能力",
      model: "bge-m3",
      tag: "多语言知识库",
      size: "中等",
      hardware: "普通配置可用",
      desc: "适合中文、英文、多语言文档检索和企业知识库。本能力不是聊天模型。",
      type: "embedding"
    }
  ];
  function escapeHtml(v) {
    return String(v ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  async function postJson(url, payload, timeout = 120000) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);
    try {
      const res = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload || {}),
        signal: controller.signal
      });
      const text = await res.text();
      try { return JSON.parse(text); } catch (_) { return { ok: res.ok, raw: text }; }
    } finally {
      clearTimeout(timer);
    }
  }
  async function getJson(url, timeout = 10000) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), timeout);
    try {
      const res = await fetch(url, { signal: controller.signal });
      const text = await res.text();
      try { return JSON.parse(text); } catch (_) { return { ok: res.ok, raw: text }; }
    } finally {
      clearTimeout(timer);
    }
  }
  function setResult(title, type, message, data) {
    const el = document.getElementById("modelSetupResult");
    if (!el) return;
    el.innerHTML = `
      <div class="model-result-card ${escapeHtml(type || "")}">
        <h3>${escapeHtml(title)}</h3>
        <p>${escapeHtml(message || "")}</p>
        ${data ? `<pre>${escapeHtml(JSON.stringify(data, null, 2))}</pre>` : ""}
      </div>
    `;
  }
  function renderProgress(title, steps, activeIndex, note = "") {
    const rows = steps.map((step, i) => {
      const cls = i < activeIndex ? "done" : (i === activeIndex ? "active" : "");
      const icon = i < activeIndex ? "✓" : (i === activeIndex ? "…" : "○");
      return `<div class="model-progress-step ${cls}">
        <span class="model-progress-icon">${icon}</span>
        <span>${escapeHtml(step)}</span>
      </div>`;
    }).join("");
    const pct = Math.min(100, Math.max(8, ((activeIndex + 1) / steps.length) * 100));
    return `
      <div class="model-progress-card">
        <div class="model-progress-title">${escapeHtml(title)}</div>
        <div class="model-progress-bar"><div class="model-progress-fill" style="width:${pct}%"></div></div>
        <div class="model-progress-steps">${rows}</div>
        ${note ? `<div class="model-progress-extra">${escapeHtml(note)}</div>` : ""}
      </div>
    `;
  }
  function setProgress(title, steps, activeIndex, note = "") {
    const el = document.getElementById("modelSetupResult");
    if (!el) return;
    el.innerHTML = renderProgress(title, steps, activeIndex, note);
  }
  function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  function getTauriInvoke() {
    return window.__TAURI__?.core?.invoke || window.__TAURI_INTERNALS__?.invoke || null;
  }
  function directRuntimeHint(error) {
    const msg = String(error || "");
    if (msg.includes("bootstrap_runtime.ps1") || msg.includes("运行时脚本")) {
      return "本地运行时脚本没有正确释放。请安装最新版本后重试。";
    }
    if (msg.includes("ExecutionPolicy") || msg.includes("PowerShell")) {
      return "Windows PowerShell 执行受限，请以管理员身份或允许脚本执行后重试。";
    }
    return msg;
  }
  function parseRuntimeJson(text) {
    if (!text) return null;
    const raw = String(text).trim();
    try { return JSON.parse(raw); } catch (_) {}
    const first = raw.indexOf("{");
    const last = raw.lastIndexOf("}");
    if (first >= 0 && last > first) {
      try { return JSON.parse(raw.slice(first, last + 1)); } catch (_) {}
    }
    return { ok: false, raw };
  }
  function isModelInstalled(modelName, status) {
    const raw = JSON.stringify(status || {});
    return raw.includes(modelName);
  }
  function getModelStatusText(modelName, status) {
    const raw = JSON.stringify(status || {});
    if (raw.includes(modelName)) return "已安装";
    return "未安装";
  }
  function getCurrentModelProfile() {
    return localStorage.getItem("maomiai_current_model_profile") || "standard";
  }
  function setCurrentModelProfile(profile) {
    const next = profile || "standard";
    localStorage.setItem("maomiai_current_model_profile", next);
    window.__MAOMIAI_CURRENT_MODEL_PROFILE__ = next;
  }
  function getModelByProfile(profile) {
    return MODEL_CATALOG.find(x => x.profile === profile) || MODEL_CATALOG[0];
  }
  function setCurrentModelFromButton(profile) {
    const item = getModelByProfile(profile);
    const status = window.__MAOMIAI_MODEL_STATUS__ || null;
    if (!isModelInstalled(item.model, status)) {
      setResult("该能力尚未安装", "bad", `请先下载 ${item.title}，下载完成后才能设为当前使用。`, {
        profile: item.profile,
        model: item.model
      });
      return;
    }
    setCurrentModelProfile(profile);
    setResult("当前能力已切换", "ok", `当前对话将优先使用：${item.title}`, {
      profile: item.profile,
      title: item.title,
      model: item.model
    });
    renderModelStore(window.__MAOMIAI_MODEL_STATUS__ || null);
  }
  function renderModelStore(status = null) {
    const effectiveStatus = status || window.__MAOMIAI_MODEL_STATUS__ || null;
    const content = document.getElementById("content");
    if (!content) return;
    const cards = MODEL_CATALOG.map(item => {
      const state = effectiveStatus ? getModelStatusText(item.model, effectiveStatus) : "待检查";
      const stateClass = state === "已安装" ? "installed" : "missing";
      const current = getCurrentModelProfile() === item.profile;
      const installed = state === "已安装";
      return `
        <div class="model-store-card" data-profile="${escapeHtml(item.profile)}">
          <div class="model-store-card-head">
            <div>
              <h3>${escapeHtml(item.title)}</h3>
              <div class="model-store-model">${escapeHtml(item.model)}</div>
            </div>
            <div class="model-card-badges">
              <span class="model-store-tag">${escapeHtml(item.tag)}</span>
              ${current ? `<span class="model-current-badge">当前使用</span>` : ""}
            </div>
          </div>
          <p>${escapeHtml(item.desc)}</p>
          <div class="model-store-meta">
            <span>大小：${escapeHtml(item.size)}</span>
            <span>${escapeHtml(item.hardware)}</span>
            <span class="model-state ${stateClass}">${escapeHtml(state)}</span>
          </div>
          <div class="model-card-actions">
            <button class="primary model-download-btn" data-action="download-model-profile" data-profile="${escapeHtml(item.profile)}">
              ${state === "已安装" ? "重新验证" : "下载并启用"}
            </button>
            <button class="secondary model-use-btn" ${installed ? "" : "disabled"} data-action="set-current-model-profile" data-profile="${escapeHtml(item.profile)}">
              ${installed ? (current ? "当前使用中" : "设为当前使用") : "未安装不可用"}
            </button>
          </div>
        </div>
      `;
    }).join("");
    content.innerHTML = `
      <section class="model-store-page">
        <div class="model-store-hero">
          <div class="model-logo">M</div>
          <h1>本地模型</h1>
          <p>选择你需要的能力，软件会自动下载、部署并连接。客户不需要打开终端，也不需要手动输入命令。</p>
        </div>
        <div class="model-store-actions">
          <button class="secondary" data-action="check-local-model-status">检查本地 AI 状态</button>
          <button class="secondary" data-action="install-local-inference">安装本地推理后端</button>
          <button class="secondary" data-action="return-chat">返回对话</button>
        </div>
        <div id="modelSetupResult" class="model-setup-result"></div>
        <div class="model-store-grid">
          ${cards}
        </div>
      </section>
    `;
  }
  async function checkLocalModelStatus(options = {}) {
    if (!options.silent) {
      setResult("正在检查本地 AI", "loading", "正在检查本地推理后端、模型列表和本地网关。", null);
    }
    const result = { ok: false, direct: null, bootstrap: null, gateway: null, ready: false };
    const invoke = getTauriInvoke();
    if (invoke) {
      try {
        const out = await invoke("local_ai_status_direct");
        result.direct = parseRuntimeJson(out);
      } catch (e) {
        result.direct = { ok: false, error: String(e) };
      }
    }
    try {
      result.bootstrap = await getJson(`${API.bootstrap}/bootstrap/status`, 3000);
    } catch (e) {
      result.bootstrap = { ok: false, error: String(e), message: "18100 暂未连接。" };
    }
    try {
      result.gateway = await getJson(`${API.gateway}/health`, 3000);
    } catch (e) {
      result.gateway = { ok: false, error: String(e), message: "18080 暂未连接。" };
    }
    result.ready = !!(result.direct?.ready || result.direct?.serve?.ok || result.bootstrap?.ready || result.gateway?.ok);
    result.ok = result.ready;
    window.__MAOMIAI_MODEL_STATUS__ = result;
    if (!options.silent) {
      renderModelStore(result);
      if (result.ready) {
        setResult("本地 AI 可用", "ok", "本地推理后端已有响应。你可以下载或启用所需能力。", result);
      } else {
        setResult("本地 AI 暂未连接", "bad", "系统会尝试自动安装或启动本地运行环境。请点击安装本地推理后端，或直接选择一个能力下载。", result);
      }
    }
    return result;
  }
  async function installLocalInferenceBackend() {
    if (window.__maomiaiInstallingLocalBackend) {
      setResult("正在安装中", "loading", "安装流程已经在执行，请不要重复点击。", null);
      return;
    }
    window.__maomiaiInstallingLocalBackend = true;
    const steps = ["准备安装", "执行安装", "启动服务", "重新检查"];
    try {
      setProgress("正在安装本地推理后端", steps, 0);
      const invoke = getTauriInvoke();
      if (!invoke) {
        setResult("无法调用系统安装器", "bad", "当前环境无法调用 Tauri 命令。请下载完整安装包后重试。", null);
        return;
      }
      setProgress("正在执行安装命令", steps, 1);
      const out = await invoke("install_local_inference_backend");
      const parsed = parseRuntimeJson(out);
      setProgress("正在启动本地推理服务", steps, 2);
      await sleep(2000);
      setProgress("正在重新检查", steps, 3);
      const status = await checkLocalModelStatus({ silent: true });
      if (status.ready || parsed?.ok) {
        setResult("本地推理后端已准备", "ok", "本地推理后端已安装或启动。现在可以下载模型能力。", { parsed, status });
      } else {
        setResult("安装后仍未连接", "bad", "安装命令已经执行，但服务暂未就绪。请等待安装完成后重新检查，或重启 MAOMIAI。", { parsed, status });
      }
    } catch (e) {
      setResult("安装失败", "bad", String(e), { error: String(e) });
    } finally {
      window.__maomiaiInstallingLocalBackend = false;
    }
  }
  async function startLocalModelDownload(profile = "standard") {
    if (window.__maomiaiDownloadingModel) {
      setResult("正在准备能力", "loading", "已有下载任务正在执行，请不要重复点击。", null);
      return;
    }
    const item = MODEL_CATALOG.find(x => x.profile === profile) || MODEL_CATALOG[0];
    window.__maomiaiDownloadingModel = true;
    const steps = ["检查环境", "启动本地推理服务", `下载 ${item.title}`, "验证能力", "连接到聊天"];
    try {
      const invoke = getTauriInvoke();
      if (!invoke) {
        setResult(`${item.title} 下载失败`, "bad", "当前环境无法调用 Tauri 运行时下载命令。", { profile });
        return;
      }
      setProgress(`正在准备 ${item.title}`, steps, 0);
      await sleep(300);
      setProgress("正在启动下载任务", steps, 1);
      const out = await invoke("start_local_model_download", { profile });
      const parsed = parseRuntimeJson(out);
      if (!parsed?.ok) {
        setResult(`${item.title} 启动下载失败`, "bad", parsed?.message || "无法启动后台下载任务。", parsed || { raw: out });
        return parsed;
      }
      window.__MAOMIAI_MODEL_JOBS__[profile] = parsed;
      let lastStatus = parsed;
      for (let i = 0; i < 720; i++) {
        await sleep(2000);
        let polled;
        try {
          const statusRaw = await invoke("local_model_download_status", { profile });
          polled = parseRuntimeJson(statusRaw);
        } catch (e) {
          polled = { ok: false, error: String(e) };
        }
        lastStatus = polled;
        const progress = Number(polled?.progress || 10);
        const clamped = Math.max(0, Math.min(100, progress));
        setProgress(`正在下载 ${item.title}`, steps, 2, `当前进度：${clamped}%`);
        if (polled?.status === "done" || polled?.installed || clamped >= 100) {
          setProgress(`正在验证 ${item.title}`, steps, 3);
          await sleep(800);
          const status = await checkLocalModelStatus({ silent: true });
          window.__MAOMIAI_MODEL_STATUS__ = status;
          setCurrentModelProfile(profile);
          setProgress(`${item.title} 已准备完成`, steps, 4);
          await sleep(600);
          setResult(`${item.title} 已准备完成`, "ok", "模型已下载并已设为当前使用。现在可以返回对话直接使用。", {
            started: parsed,
            status: polled,
            finalStatus: status
          });
          renderModelStore(status);
          return polled;
        }
        if (polled?.status === "failed") {
          setResult(`${item.title} 下载失败`, "bad", polled?.message || "后台下载任务失败。", polled);
          return polled;
        }
      }
      setResult(`${item.title} 下载仍在进行`, "loading", "下载任务仍在后台进行。你可以稍后重新进入本地模型页面查看状态。", lastStatus);
      return lastStatus;
    } catch (e) {
      setResult(`${item.title} 下载失败`, "bad", String(e), { profile, error: String(e) });
    } finally {
      window.__maomiaiDownloadingModel = false;
    }
  }
  function bindModelStoreEvents() {
    document.addEventListener("click", (event) => {
      const target = event.target.closest("[data-action]");
      if (!target) return;
      const action = target.getAttribute("data-action");
      if (action === "check-local-model-status") {
        event.preventDefault();
        checkLocalModelStatus();
      }
      if (action === "install-local-inference") {
        event.preventDefault();
        installLocalInferenceBackend();
      }
      if (action === "download-model-profile") {
        event.preventDefault();
        const profile = target.getAttribute("data-profile") || "standard";
        startLocalModelDownload(profile);
      }
      if (action === "set-current-model-profile") {
        event.preventDefault();
        const profile = target.getAttribute("data-profile") || "standard";
        setCurrentModelFromButton(profile);
      }
      if (action === "return-chat") {
        event.preventDefault();
        if (typeof window.setView === "function") window.setView("chat");
      }
    }, true);
  }
  window.renderModelSetupPage = function () {
    renderModelStore(window.__MAOMIAI_MODEL_STATUS__ || null);
    setTimeout(() => {
      checkLocalModelStatus({ silent: true })
        .then(status => {
          window.__MAOMIAI_MODEL_STATUS__ = status;
          renderModelStore(status);
        })
        .catch(() => {});
    }, 100);
  };
  window.checkLocalModelStatus = checkLocalModelStatus;
  window.installLocalInferenceBackend = installLocalInferenceBackend;
  window.startLocalModelDownload = startLocalModelDownload;
  window.getCurrentModelProfile = getCurrentModelProfile;
  window.setCurrentModelProfile = setCurrentModelProfile;
  window.getModelByProfile = getModelByProfile;
  window.isMaomiaiModelInstalled = isModelInstalled;
  window.__MAOMIAI_MODEL_CATALOG__ = MODEL_CATALOG;
  bindModelStoreEvents();
})();
