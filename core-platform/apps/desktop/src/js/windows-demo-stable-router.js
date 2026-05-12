(function () {
  console.log("[MAOMIAI] windows-demo-stable-router loaded");
  const CONTENT_IDS = ["content", "mainContent", "app-content"];
  const MODEL_CATALOG_FALLBACK = [
    { profile: "standard", title: "标准对话能力", model: "qwen2.5:7b" },
    { profile: "light", title: "轻量快速能力", model: "qwen2.5:1.5b" },
    { profile: "code", title: "代码能力", model: "qwen2.5-coder:7b" },
    { profile: "reasoning", title: "推理分析能力", model: "deepseek-r1:7b" },
    { profile: "english", title: "英文通用能力", model: "llama3.1:8b" },
    { profile: "small", title: "小型通用能力", model: "llama3.2:3b" }
  ];
  function $(id) {
    return document.getElementById(id);
  }
  function getContent() {
    for (const id of CONTENT_IDS) {
      const el = $(id);
      if (el) return el;
    }
    const main = document.querySelector("main") || document.querySelector(".main") || document.body;
    let el = document.createElement("div");
    el.id = "content";
    el.className = "content";
    main.appendChild(el);
    return el;
  }
  function escapeHtml(v) {
    return String(v ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }
  function getCatalog() {
    return window.__MAOMIAI_MODEL_CATALOG__ || MODEL_CATALOG_FALLBACK;
  }
  function getCurrentProfile() {
    return localStorage.getItem("maomiai_current_model_profile") || window.__MAOMIAI_CURRENT_MODEL_PROFILE__ || "standard";
  }
  function setCurrentProfile(profile) {
    const next = profile || "standard";
    localStorage.setItem("maomiai_current_model_profile", next);
    window.__MAOMIAI_CURRENT_MODEL_PROFILE__ = next;
    if (typeof window.setCurrentModelProfile === "function") {
      try { window.setCurrentModelProfile(next); } catch (_) {}
    }
  }
  function getCurrentModel() {
    const profile = getCurrentProfile();
    return getCatalog().find(x => x.profile === profile) || getCatalog()[0] || MODEL_CATALOG_FALLBACK[0];
  }
  function extractAssistantText(data) {
    if (!data) return "";
    if (typeof data === "string") return data;
    return (
      data.response ||
      data.output ||
      data.text ||
      data.content ||
      data.message ||
      data.answer ||
      data?.choices?.[0]?.message?.content ||
      data?.choices?.[0]?.text ||
      data?.data?.response ||
      data?.data?.output ||
      ""
    );
  }
  function setActiveNav(view) {
    document.querySelectorAll("[data-view], .nav button, aside button, .sidebar button").forEach(btn => {
      const v = btn.getAttribute("data-view") || btn.dataset?.view;
      if (v === view) btn.classList.add("active");
      else btn.classList.remove("active");
    });
  }
  function page(title, subtitle, body) {
    const content = getContent();
    content.innerHTML = `
      <section class="demo-page">
        <div class="demo-hero">
          <h1>${escapeHtml(title)}</h1>
          <p>${escapeHtml(subtitle || "")}</p>
        </div>
        <div class="demo-body">${body || ""}</div>
      </section>
    `;
  }
  function getPromptInput() {
    return $("prompt") || $("composerInput") || $("chatInput") || document.querySelector("textarea");
  }
  function focusPrompt(clear = false) {
    const input = getPromptInput();
    if (!input) return;
    if (clear) input.value = "";
    input.focus();
  }
  function currentChatSession() {
    if (typeof window.currentSession === "function") {
      try {
        return window.currentSession();
      } catch (_) {}
    }
    return null;
  }
  function appendAssistantMessage(text) {
    if (typeof window.systemMessage === "function") {
      try {
        window.systemMessage(text);
        return;
      } catch (_) {}
    }
    const session = currentChatSession();
    if (session && Array.isArray(session.messages)) {
      session.messages.push({ role: "assistant", text, ts: Date.now() });
      try { window.saveState?.(); } catch (_) {}
      try { window.render?.(); } catch (_) {}
    }
  }
  function replaceLastAssistantMessage(text) {
    const session = currentChatSession();
    if (session && Array.isArray(session.messages)) {
      for (let i = session.messages.length - 1; i >= 0; i -= 1) {
        const msg = session.messages[i];
        if (msg.role === "assistant") {
          msg.text = text;
          try { window.saveState?.(); } catch (_) {}
          try { window.render?.(); } catch (_) {}
          return;
        }
      }
    }
    appendAssistantMessage(text);
  }
  function injectChatModelSelector() {
    const topbar = document.querySelector(".topbar");
    if (!topbar) return;
    const actions = topbar.querySelector(".top-actions");
    if (!actions) return;
    let wrapper = document.getElementById("chatModelSelector");
    const current = getCurrentModel();
    const options = getCatalog().map(item => {
      const selected = item.profile === current.profile ? "selected" : "";
      return `<option value="${escapeHtml(item.profile)}" ${selected}>${escapeHtml(item.title)}</option>`;
    }).join("");
    if (!wrapper) {
      wrapper = document.createElement("div");
      wrapper.id = "chatModelSelector";
      wrapper.className = "chat-model-selector";
      actions.prepend(wrapper);
    }
    wrapper.innerHTML = `
      <span>当前能力</span>
      <select id="chatModelSelect">${options}</select>
    `;
    const select = document.getElementById("chatModelSelect");
    if (select) {
      select.onchange = () => {
        setCurrentProfile(select.value);
        const model = getCurrentModel();
        appendAssistantMessage(`已切换当前能力：${model.title}`);
      };
    }
  }
  async function sendChatFallback() {
    const input = getPromptInput();
    const prompt = (input?.value || "").trim();
    if (!prompt) return;
    const modelInfo = getCurrentModel();
    if (typeof window.userMessage === "function") {
      try {
        window.userMessage(prompt);
      } catch (_) {}
    }
    if (input) input.value = "";
    try {
      appendAssistantMessage(`正在使用「${modelInfo.title}」思考中...`);
      const attempts = [
        { url: "http://127.0.0.1:18080/generate", body: { prompt, profile: modelInfo.profile, model: modelInfo.model } },
        { url: "http://127.0.0.1:18080/generate", body: { prompt } },
        { url: "http://127.0.0.1:18080/chat", body: { messages: [{ role: "user", content: prompt }], profile: modelInfo.profile, model: modelInfo.model } }
      ];
      let lastError = "本地模型网关没有返回内容。";
      for (const attempt of attempts) {
        try {
          const res = await fetch(attempt.url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(attempt.body)
          });
          const raw = await res.text();
          let data = null;
          try { data = JSON.parse(raw); } catch (_) { data = raw; }
          if (!res.ok) {
            lastError = `${attempt.url} HTTP ${res.status}: ${raw}`;
            continue;
          }
          const text = extractAssistantText(data);
          if (text) {
            replaceLastAssistantMessage(text);
            return;
          }
          lastError = `${attempt.url} 返回为空：${raw}`;
        } catch (e) {
          lastError = `${attempt.url} 请求失败：${String(e)}`;
        }
      }
      replaceLastAssistantMessage(`发送失败：${lastError}。请确认本地模型已下载，并且本地模型网关 18080 已启动。`);
    } catch (e) {
      replaceLastAssistantMessage(`发送失败：${String(e)}。请确认本地模型已下载，并且本地模型网关 18080 已启动。`);
    }
  }
  function renderChat() {
    if (typeof window.__oldSetView === "function") {
      try {
        window.__oldSetView("chat");
        focusPrompt(true);
        setTimeout(injectChatModelSelector, 30);
        return;
      } catch (e) {
        console.warn(e);
      }
    }
    if (typeof window.renderChatPage === "function") {
      try {
        window.renderChatPage(getContent());
        focusPrompt(true);
        setTimeout(injectChatModelSelector, 30);
        return;
      } catch (e) { console.warn(e); }
    }
    page("MAOMIAI 本地 AI", "输入任务，软件会调用本地 AI 能力完成处理。", `
      <div class="demo-card">
        <h2>新对话</h2>
        <p>请在底部输入框输入问题，例如：你好，请介绍一下你自己。</p>
      </div>
    `);
    setTimeout(injectChatModelSelector, 30);
  }
  function renderFiles() {
    if (typeof window.renderArtifactsPage === "function") {
      try { return window.renderArtifactsPage(getContent()); } catch (e) { console.warn(e); }
    }
    page("文件与结果", "集中查看本地 AI 生成的文件、报告、代码和处理结果。", `
      <div class="demo-grid">
        <div class="demo-card">
          <h2>结果产物</h2>
          <p>后续对话、代码检查、文档处理生成的结果会显示在这里。</p>
        </div>
        <div class="demo-card">
          <h2>本地存储</h2>
          <p>优先保存在本机，便于客户演示私有化和本地部署能力。</p>
        </div>
      </div>
    `);
  }
  function renderCodeReview() {
    if (typeof window.renderCodeReviewPage === "function") {
      try { return window.renderCodeReviewPage(getContent()); } catch (e) { console.warn(e); }
    }
    page("代码检查", "用于代码审查、风险命令检查、错误分析和项目修复建议。", `
      <div class="demo-card">
        <h2>代码检查测试</h2>
        <textarea id="demoCodeInput" class="demo-textarea" placeholder="粘贴需要检查的代码或命令，例如 rm -rf /"></textarea>
        <button class="primary" data-action="demo-code-check">开始检查</button>
        <pre id="demoCodeResult" class="demo-result">等待输入。</pre>
      </div>
    `);
  }
  function renderSettings() {
    page("设置", "配置本地运行、服务启动、模型能力和演示环境。", `
      <div class="demo-grid">
        <div class="demo-card">
          <h2>运行模式</h2>
          <p>当前为本地运行模式，优先调用本机后端和本地模型能力。</p>
        </div>
        <div class="demo-card">
          <h2>服务状态</h2>
          <p>请在右侧检查器的服务页查看后端服务健康状态。</p>
        </div>
      </div>
    `);
  }
  function renderLocalModels() {
    if (typeof window.renderModelSetupPage === "function") {
      try {
        window.renderModelSetupPage();
        return;
      } catch (e) {
        console.error("[MAOMIAI] renderModelSetupPage failed", e);
      }
    }
    page("本地模型", "选择需要的本地 AI 能力，软件会自动下载、部署并连接。", `
      <div class="demo-grid">
        <div class="model-store-card">
          <h3>标准对话能力</h3>
          <p>适合中文问答、总结、写作、任务规划。</p>
          <button class="primary" data-action="download-model-profile" data-profile="standard">下载并启用</button>
        </div>
        <div class="model-store-card">
          <h3>代码能力</h3>
          <p>适合代码生成、代码检查、错误分析和项目修复。</p>
          <button class="primary" data-action="download-model-profile" data-profile="code">下载并启用</button>
        </div>
        <div class="model-store-card">
          <h3>轻量快速能力</h3>
          <p>适合低配置电脑、快速问答和演示测试。</p>
          <button class="primary" data-action="download-model-profile" data-profile="light">下载并启用</button>
        </div>
      </div>
      <div id="modelSetupResult" class="model-setup-result"></div>
    `);
  }
  function route(view) {
    const normalized = String(view || "chat");
    setActiveNav(normalized);
    if (normalized === "chat" || normalized === "new-chat" || normalized === "new") {
      renderChat();
      return;
    }
    if (
      normalized === "models" ||
      normalized === "model" ||
      normalized === "local-model" ||
      normalized === "local-models" ||
      normalized === "本地模型"
    ) {
      renderLocalModels();
      return;
    }
    if (
      normalized === "artifacts" ||
      normalized === "files" ||
      normalized === "documents" ||
      normalized === "文件与结果"
    ) {
      renderFiles();
      return;
    }
    if (normalized === "code-review" || normalized === "code" || normalized === "代码检查") {
      renderCodeReview();
      return;
    }
    if (normalized === "settings" || normalized === "setting" || normalized === "设置") {
      renderSettings();
      return;
    }
    if (typeof window.__oldSetView === "function") {
      try {
        return window.__oldSetView(normalized);
      } catch (e) {
        console.warn("[MAOMIAI] old setView failed", e);
      }
    }
    page("功能页面", `视图：${normalized}`, `
      <div class="demo-card">
        <p>该功能已注册，但当前演示包使用兜底页面显示。</p>
      </div>
    `);
  }
  function inferViewFromText(text) {
    const t = String(text || "").trim();
    if (t.includes("新对话") || t.includes("新建会话")) return "chat";
    if (t.includes("本地模型") || t.includes("模型")) return "models";
    if (t.includes("文件") || t.includes("结果") || t.includes("产物")) return "artifacts";
    if (t.includes("代码")) return "code-review";
    if (t.includes("设置")) return "settings";
    return null;
  }
  function installNavAttributes() {
    const candidates = Array.from(document.querySelectorAll("button, a, .nav-item, .sidebar-item, [role='button']"));
    for (const el of candidates) {
      const text = (el.textContent || "").trim();
      if (!el.getAttribute("data-view")) {
        const inferred = inferViewFromText(text);
        if (inferred) el.setAttribute("data-view", inferred);
      }
      if (text.includes("本地模型")) {
        el.setAttribute("data-view", "models");
        el.style.cursor = "pointer";
      }
      if (text.includes("文件与结果")) {
        el.setAttribute("data-view", "artifacts");
        el.style.cursor = "pointer";
      }
      if (text.includes("代码检查")) {
        el.setAttribute("data-view", "code-review");
        el.style.cursor = "pointer";
      }
      if (text.includes("新对话")) {
        el.setAttribute("data-view", "chat");
        el.style.cursor = "pointer";
      }
      if (text.includes("设置")) {
        el.setAttribute("data-view", "settings");
        el.style.cursor = "pointer";
      }
    }
  }
  function bindGlobalClicks() {
    document.addEventListener("pointerdown", (event) => {
      const target = event.target.closest("[data-view]");
      if (!target) return;
      const view = target.getAttribute("data-view");
      if (!view) return;
      event.preventDefault();
      event.stopPropagation();
      route(view);
    }, true);
    document.addEventListener("click", (event) => {
      const target = event.target.closest("[data-view]");
      if (!target) return;
      const view = target.getAttribute("data-view");
      if (!view) return;
      event.preventDefault();
      event.stopPropagation();
      route(view);
    }, true);
    document.addEventListener("click", (event) => {
      const actionEl = event.target.closest("[data-action]");
      if (!actionEl) return;
      const action = actionEl.getAttribute("data-action");
      if (action === "demo-code-check") {
        event.preventDefault();
        const input = $("demoCodeInput");
        const result = $("demoCodeResult");
        if (result) {
          result.textContent = `已收到检查内容：\n${input?.value || ""}\n\n演示包会将该内容提交到代码检查服务。`;
        }
      }
    }, true);
    document.addEventListener("click", (event) => {
      const btn = event.target.closest("button");
      if (!btn) return;
      const text = (btn.textContent || "").trim();
      if (text === "发送" || text.includes("发送")) {
        event.preventDefault();
        event.stopPropagation();
        sendChatFallback();
      }
    }, true);
    document.addEventListener("keydown", (event) => {
      const target = event.target;
      if (!target || target !== getPromptInput()) return;
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendChatFallback();
      }
    }, true);
  }
  function boot() {
    if (!window.__oldSetView && typeof window.setView === "function") {
      window.__oldSetView = window.setView;
    }
    window.setView = route;
    window.routeView = route;
    window.__MAOMIAI_STABLE_ROUTE__ = route;
    window.__MAOMIAI_GET_CURRENT_MODEL__ = getCurrentModel;
    installNavAttributes();
    bindGlobalClicks();
    setTimeout(installNavAttributes, 300);
    setTimeout(installNavAttributes, 1200);
    setInterval(installNavAttributes, 2500);
    console.log("[MAOMIAI] stable router ready");
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
