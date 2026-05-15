(function () {
  console.log("[MAOMIAI] agent runtime main path loaded C25-A1");

  const MODEL_CATALOG_FALLBACK = [
    { profile: "standard", title: "标准对话能力", model: "qwen2.5:7b" },
    { profile: "light", title: "轻量快速能力", model: "qwen2.5:1.5b" },
    { profile: "code", title: "代码能力", model: "qwen2.5-coder:7b" },
    { profile: "reasoning", title: "推理分析能力", model: "deepseek-r1:7b" },
    { profile: "english", title: "英文通用能力", model: "llama3.1:8b" },
    { profile: "small", title: "小型通用能力", model: "llama3.2:3b" },
  ];

  function $(id) {
    return document.getElementById(id);
  }

  function escapeHtml(v) {
    return String(v ?? "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function getContent() {
    return $("content") || $("mainContent") || document.querySelector("main") || document.body;
  }

  function getCatalog() {
    return window.__MAOMIAI_MODEL_CATALOG__ || MODEL_CATALOG_FALLBACK;
  }

  function getInstalledCatalog() {
    const status = window.__MAOMIAI_MODEL_STATUS__ || null;
    const raw = JSON.stringify(status || {});
    const installed = getCatalog().filter((item) => raw.includes(item.model));
    return installed.length ? installed : getCatalog();
  }

  function getCurrentProfile() {
    return localStorage.getItem("maomiai_current_model_profile") || window.__MAOMIAI_CURRENT_MODEL_PROFILE__ || "standard";
  }

  function setCurrentProfile(profile) {
    const p = profile || "standard";
    localStorage.setItem("maomiai_current_model_profile", p);
    window.__MAOMIAI_CURRENT_MODEL_PROFILE__ = p;
  }

  function getCurrentModel() {
    const profile = getCurrentProfile();
    const catalog = getInstalledCatalog();
    return catalog.find((item) => item.profile === profile) || catalog[0] || MODEL_CATALOG_FALLBACK[0];
  }

  function decodeMaomiaiEnvelope(obj) {
    if (!obj || !obj.maomiai_payload_b64) return obj;
    try {
      const bin = atob(obj.maomiai_payload_b64);
      const bytes = new Uint8Array(bin.length);
      for (let i = 0; i < bin.length; i += 1) bytes[i] = bin.charCodeAt(i);
      const text = new TextDecoder("utf-8").decode(bytes);
      return JSON.parse(text);
    } catch (e) {
      return {
        ok: false,
        message: "Failed to decode MAOMIAI runtime payload.",
        error: String(e),
        envelope: obj,
      };
    }
  }

  function safeParse(raw) {
    if (raw == null) return null;
    if (typeof raw !== "string") return raw;
    const text = raw.trim();
    try {
      return decodeMaomiaiEnvelope(JSON.parse(text));
    } catch (_) {}
    const first = text.indexOf("{");
    const last = text.lastIndexOf("}");
    if (first >= 0 && last > first) {
      try {
        return decodeMaomiaiEnvelope(JSON.parse(text.slice(first, last + 1)));
      } catch (_) {}
    }
    return { ok: false, raw: text };
  }

  function ensureChatState() {
    window.__MAOMIAI_CHAT_MESSAGES__ = window.__MAOMIAI_CHAT_MESSAGES__ || [];
  }

  function updateChatMessagesOnly() {
    const box = $("demoChatMessages");
    if (!box) return;
    const messages = (window.__MAOMIAI_CHAT_MESSAGES__ || [])
      .map(
        (message) => `
      <div class="demo-chat-msg ${escapeHtml(message.role)}">
        <strong>${message.role === "user" ? "你" : "本地 AI"}</strong>
        <div>${escapeHtml(message.content)}</div>
      </div>
    `
      )
      .join("");
    box.innerHTML = messages || '<div class="demo-card"><p>请输入问题，测试 Agent Runtime 是否可用。</p></div>';
  }

  function pushChat(role, content) {
    ensureChatState();
    window.__MAOMIAI_CHAT_MESSAGES__.push({ role, content: String(content ?? "") });
    updateChatMessagesOnly();
  }

  function updateLastAssistant(content) {
    ensureChatState();
    const messages = window.__MAOMIAI_CHAT_MESSAGES__;
    const last = messages[messages.length - 1];
    if (last && last.role === "assistant") {
      last.content = String(content ?? "");
    } else {
      messages.push({ role: "assistant", content: String(content ?? "") });
    }
    updateChatMessagesOnly();
  }

  function updateDebug(title, data) {
    const box = $("maomiaiDebugBox");
    if (!box) return;
    box.innerHTML = `
      <summary>${escapeHtml(title)}（点击展开）</summary>
      <pre>${escapeHtml(typeof data === "string" ? data : JSON.stringify(data, null, 2))}</pre>
    `;
  }

  function findComposerInput() {
    const active = document.activeElement;
    if (active && (active.tagName === "TEXTAREA" || active.tagName === "INPUT")) {
      return active;
    }
    const selectors = [
      "#composerInput",
      "#chatInput",
      "textarea[placeholder*='MAOMIAI']",
      "textarea[placeholder*='发送']",
      "textarea[placeholder*='输入']",
      "textarea",
      "input[type='text']",
    ];
    for (const selector of selectors) {
      const el = document.querySelector(selector);
      if (el) return el;
    }
    return null;
  }

  async function maomiaiAgentRuntimeHealth() {
    try {
      const response = await fetch("http://127.0.0.1:18131/health", { method: "GET" });
      return { ok: response.ok, status: response.status };
    } catch (err) {
      return { ok: false, error: err.message || String(err) };
    }
  }

  async function maomiaiTryStartWindowsRuntime() {
    const invoke = window.__TAURI__?.core?.invoke || window.__TAURI__?.tauri?.invoke;
    if (!invoke) {
      return { ok: false, error: "tauri_invoke_unavailable" };
    }
    try {
      const result = await invoke("start_local_ai_runtime", {});
      return typeof result === "string" ? safeParse(result) : result;
    } catch (err) {
      return { ok: false, error: err.message || String(err) };
    }
  }

  async function maomiaiEnsureAgentRuntimeBeforeSend() {
    const initialHealth = await maomiaiAgentRuntimeHealth();
    if (initialHealth.ok) {
      return { ok: true, already_running: true, initial_health: initialHealth };
    }
    const startResult = await maomiaiTryStartWindowsRuntime();
    await new Promise((resolve) => setTimeout(resolve, 3000));
    const finalHealth = await maomiaiAgentRuntimeHealth();
    return {
      ok: !!finalHealth.ok,
      initial_health: initialHealth,
      start_result: startResult,
      final_health: finalHealth,
    };
  }

  async function runAgentRuntime(userText) {
    const model = getCurrentModel();
    const runtimeReady = await maomiaiEnsureAgentRuntimeBeforeSend();
    if (!runtimeReady.ok) {
      throw new Error(`Agent Runtime auto-start failed: ${JSON.stringify(runtimeReady)}`);
    }
    const response = await fetch("http://127.0.0.1:18131/agent/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        input: userText,
        message: userText,
        session_id: window.__MAOMIAI_SESSION_ID__ || "desktop-default",
        source: "desktop-chat",
        current_profile: localStorage.getItem("maomiai_current_model_profile") || model.profile || "light",
        profile: localStorage.getItem("maomiai_current_model_profile") || model.profile || "light",
        model: model.model,
      }),
    });
    const raw = await response.text();
    const parsed = safeParse(raw);
    if (!response.ok) {
      throw new Error(`Agent Runtime HTTP ${response.status}: ${raw}`);
    }
    return parsed;
  }

  function extractAgentText(result) {
    if (!result) return "Agent runtime returned empty response.";
    return (
      result.final_answer ||
      result.answer ||
      result.response ||
      result.output ||
      result.text ||
      result?.data?.final_answer ||
      result?.data?.answer ||
      JSON.stringify(result, null, 2)
    );
  }

  async function routeUserMessage(query) {
    updateDebug("Agent Runtime", {
      endpoint: "http://127.0.0.1:18131/agent/run",
      session_id: window.__MAOMIAI_SESSION_ID__ || "desktop-default",
      current_profile: localStorage.getItem("maomiai_current_model_profile") || getCurrentModel().profile,
    });
    const result = await runAgentRuntime(query);
    maomiaiCaptureRunIdFromResult(result);
    updateDebug("Agent Runtime Result", result);
    return extractAgentText(result);
  }

  // ===== MAOMIAI Agent Replay UI =====
  window.__MAOMIAI_LAST_RUN_ID__ = window.__MAOMIAI_LAST_RUN_ID__ || null;

  function maomiaiEscapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function maomiaiShortJson(value, maxLen = 900) {
    let text = "";
    try {
      text = JSON.stringify(value ?? {}, null, 2);
    } catch (err) {
      text = String(value ?? "");
    }
    if (text.length > maxLen) {
      return text.slice(0, maxLen) + "\n... truncated";
    }
    return text;
  }

  async function fetchAgentTimeline(runId) {
    const response = await fetch(`http://127.0.0.1:18131/agent/replay/timeline/${encodeURIComponent(runId)}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" }
    });
    return await response.json();
  }

  function renderAgentTimeline(timeline) {
    if (!timeline || !timeline.ok) {
      return `
        <div class="agent-replay-empty">
          <div class="agent-replay-title">暂无可回放记录</div>
          <div class="agent-replay-subtitle">${maomiaiEscapeHtml(timeline?.message || timeline?.error || "未找到 run timeline")}</div>
        </div>
      `;
    }
    const events = Array.isArray(timeline.events) ? timeline.events : [];
    const eventHtml = events.map((ev) => {
      const type = maomiaiEscapeHtml(ev.type || "event");
      const title = maomiaiEscapeHtml(ev.title || ev.type || "event");
      const detail = maomiaiEscapeHtml(maomiaiShortJson(ev.detail || {}));
      return `
        <div class="agent-timeline-event">
          <div class="agent-timeline-head">
            <span class="agent-timeline-index">#${maomiaiEscapeHtml(ev.index)}</span>
            <span class="agent-timeline-type">${type}</span>
          </div>
          <div class="agent-timeline-title">${title}</div>
          <details class="agent-timeline-detail">
            <summary>查看详情</summary>
            <pre>${detail}</pre>
          </details>
        </div>
      `;
    }).join("");
    return `
      <div class="agent-replay-panel">
        <div class="agent-replay-header">
          <div>
            <div class="agent-replay-title">Agent 执行回放</div>
            <div class="agent-replay-subtitle">Run: ${maomiaiEscapeHtml(timeline.run_id || "-")}</div>
          </div>
          <div class="agent-replay-status">${maomiaiEscapeHtml(timeline.status || "unknown")}</div>
        </div>
        ${timeline.final_answer ? `
          <div class="agent-replay-answer">
            <div class="agent-replay-answer-label">最终回答</div>
            <div class="agent-replay-answer-text">${maomiaiEscapeHtml(timeline.final_answer)}</div>
          </div>
        ` : ""}
        <div class="agent-timeline-list">
          ${eventHtml || `<div class="agent-replay-empty">暂无事件</div>`}
        </div>
      </div>
    `;
  }

  async function openAgentReplay(runId) {
    const targetRunId = runId || window.__MAOMIAI_LAST_RUN_ID__;
    const app = document.querySelector("#app") || document.body;
    if (!targetRunId) {
      app.innerHTML = `
        <div class="agent-replay-page">
          <div class="agent-replay-empty">
            <div class="agent-replay-title">暂无可回放 Run</div>
            <div class="agent-replay-subtitle">请先在新对话里发送一次任务，然后再打开 Agent 回放。</div>
            <button class="primary-btn" data-action="new-chat">返回新对话</button>
          </div>
        </div>
      `;
      return;
    }
    app.innerHTML = `
      <div class="agent-replay-page">
        <div class="agent-replay-loading">正在加载 Agent 执行回放...</div>
      </div>
    `;
    try {
      const timeline = await fetchAgentTimeline(targetRunId);
      app.innerHTML = `
        <div class="agent-replay-page">
          <div class="agent-replay-actions">
            <button class="secondary-btn" data-action="new-chat">返回对话</button>
            <button class="secondary-btn" data-action="refresh-agent-replay" data-run-id="${maomiaiEscapeHtml(targetRunId)}">刷新回放</button>
          </div>
          ${renderAgentTimeline(timeline)}
        </div>
      `;
    } catch (err) {
      app.innerHTML = `
        <div class="agent-replay-page">
          <div class="agent-replay-empty">
            <div class="agent-replay-title">Agent 回放加载失败</div>
            <div class="agent-replay-subtitle">${maomiaiEscapeHtml(err.message || String(err))}</div>
            <button class="primary-btn" data-action="new-chat">返回新对话</button>
          </div>
        </div>
      `;
    }
  }

  function injectAgentReplayButton() {
    const chatRoot = document.querySelector(".chat-header, .topbar, .chat-toolbar, header");
    if (!chatRoot || document.querySelector("[data-action='open-agent-replay']")) return;
    const btn = document.createElement("button");
    btn.className = "secondary-btn agent-replay-open-btn";
    btn.dataset.action = "open-agent-replay";
    btn.textContent = "Agent 回放";
    chatRoot.appendChild(btn);
  }

  function maomiaiCaptureRunIdFromResult(result) {
    const runId =
      result?.run_id ||
      result?.raw?.run_id ||
      result?.data?.run_id ||
      result?.result?.run_id ||
      result?.steps?.[0]?.run_id ||
      result?.raw?.run?.run_id;
    if (runId) {
      window.__MAOMIAI_LAST_RUN_ID__ = runId;
      try {
        localStorage.setItem("maomiai_last_run_id", runId);
      } catch (err) {}
    }
  }

  try {
    window.__MAOMIAI_LAST_RUN_ID__ = localStorage.getItem("maomiai_last_run_id") || window.__MAOMIAI_LAST_RUN_ID__;
  } catch (err) {}

  setInterval(injectAgentReplayButton, 1200);

  // Agent replay click actions
  document.addEventListener("click", async (event) => {
    const target = event.target && event.target.closest ? event.target.closest("[data-action]") : null;
    if (!target) return;
    const action = target.dataset.action;
    if (action === "open-agent-replay") {
      event.preventDefault();
      event.stopPropagation();
      await openAgentReplay(window.__MAOMIAI_LAST_RUN_ID__);
      return;
    }
    if (action === "refresh-agent-replay") {
      event.preventDefault();
      event.stopPropagation();
      await openAgentReplay(target.dataset.runId || window.__MAOMIAI_LAST_RUN_ID__);
      return;
    }
  }, true);

  function renderChat() {
    ensureChatState();
    const content = getContent();
    const current = getCurrentModel();
    const catalog = getInstalledCatalog();
    const options = catalog
      .map((item) => {
        const selected = item.profile === current.profile ? "selected" : "";
        return `<option value="${escapeHtml(item.profile)}" ${selected}>${escapeHtml(item.title)}</option>`;
      })
      .join("");
    content.innerHTML = `
      <section class="demo-chat-page">
        <div class="demo-chat-head">
          <div>
            <h1>MAOMIAI 本地 AI</h1>
            <p>Agent Runtime 已接管</p>
          </div>
          <div class="chat-model-selector">
            <span>当前能力</span>
            <select id="chatModelSelect">${options}</select>
          </div>
        </div>
        <div class="demo-chat-actions">
          <button class="primary" data-action="maomiai-test-infer">测试 Agent Runtime</button>
          <button class="secondary" data-action="maomiai-test-time">测试时间工具</button>
          <button class="secondary" data-action="maomiai-test-memory">测试项目知识</button>
          <button class="secondary" data-action="maomiai-clear-chat">清空会话</button>
        </div>
        <details id="maomiaiDebugBox" class="maomiai-debug-box">
          <summary>调试状态（点击展开）</summary>
          <pre>Agent Runtime ready. 当前能力：${escapeHtml(current.title)} / ${escapeHtml(current.model)}</pre>
        </details>
        <div id="demoChatMessages" class="demo-chat-messages"></div>
      </section>
    `;
    const select = $("chatModelSelect");
    if (select) {
      select.addEventListener("change", () => {
        setCurrentProfile(select.value);
        const model = getCurrentModel();
        pushChat("assistant", `已切换当前能力：${model.title}`);
        renderChat();
      });
    }
    updateChatMessagesOnly();
  }

  async function sendChatMessage(forceText) {
    ensureChatState();
    const input = findComposerInput();
    const value = String(forceText || input?.value || "").trim();
    if (!value) {
      updateDebug("发送被捕获，但输入为空", {
        hasInput: !!input,
        activeTag: document.activeElement?.tagName || null,
      });
      return;
    }
    if (input && !forceText) input.value = "";
    pushChat("user", value);
    pushChat("assistant", "正在进入 Agent Runtime...");
    try {
      const answer = await routeUserMessage(value);
      updateLastAssistant(answer);
    } catch (e) {
      updateDebug("Agent Runtime Error", String(e));
      updateLastAssistant(`Agent Runtime 调用失败：${String(e)}\n\n请确认 18131 agent_runtime_service 已启动。`);
    }
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

  function renderFiles() {
    page("文件与结果", "集中查看本地 AI 生成的文件、报告、代码和处理结果。", `
      <div class="demo-card"><h2>结果产物</h2><p>后续生成的内容会显示在这里。</p></div>
    `);
  }

  function renderCodeReview() {
    page("代码检查", "用于代码审查、风险命令检查、错误分析和项目修复建议。", `
      <div class="demo-card">
        <h2>代码检查测试</h2>
        <textarea id="demoCodeInput" class="demo-textarea" placeholder="粘贴需要检查的代码或命令"></textarea>
        <button class="primary" data-action="demo-code-check">开始检查</button>
        <pre id="demoCodeResult" class="demo-result">等待输入。</pre>
      </div>
    `);
  }

  function renderSettings() {
    page("设置", "配置本地运行、服务启动、模型能力和演示环境。", `
      <div class="demo-card"><h2>运行模式</h2><p>当前为本地运行模式，Agent Runtime 已接管。</p></div>
    `);
  }

  function renderLocalModels() {
    if (typeof window.renderModelSetupPage === "function") {
      try {
        window.renderModelSetupPage();
        return;
      } catch (e) {
        console.error(e);
      }
    }
    page("本地模型", "模型商店加载中。", '<div class="demo-card"><p>请稍后重试。</p></div>');
  }

  function route(view) {
    const target = String(view || "chat");
    if (["chat", "new-chat", "new"].includes(target)) return renderChat();
    if (["models", "model", "local-model", "local-models"].includes(target)) return renderLocalModels();
    if (["artifacts", "files", "documents"].includes(target)) return renderFiles();
    if (["code-review", "code"].includes(target)) return renderCodeReview();
    if (["settings", "setting"].includes(target)) return renderSettings();
    return renderChat();
  }

  function inferViewFromText(text) {
    const value = String(text || "").trim();
    if (value.includes("新对话") || value.includes("新建会话")) return "chat";
    if (value.includes("本地模型") || value.includes("模型")) return "models";
    if (value.includes("文件") || value.includes("结果") || value.includes("产物")) return "artifacts";
    if (value.includes("代码")) return "code-review";
    if (value.includes("设置")) return "settings";
    return null;
  }

  function installNavAttributes() {
    document.querySelectorAll("button, a, .nav-item, .sidebar-item, [role='button'], li, div").forEach((el) => {
      const text = (el.textContent || "").trim();
      const view = inferViewFromText(text);
      if (view && text.length < 20 && !el.getAttribute("data-view")) {
        el.setAttribute("data-view", view);
        el.style.cursor = "pointer";
      }
    });
  }

  function bind() {
    document.addEventListener(
      "pointerdown",
      (event) => {
        const target = event.target.closest("[data-view]");
        if (!target) return;
        event.preventDefault();
        event.stopPropagation();
        route(target.getAttribute("data-view"));
      },
      true
    );
    document.addEventListener(
      "click",
      (event) => {
        const actionEl = event.target.closest("[data-action]");
        const action = actionEl?.getAttribute("data-action");
        if (action === "maomiai-test-infer") {
          event.preventDefault();
          event.stopPropagation();
          sendChatMessage("你好，请用一句话介绍你自己");
          return;
        }
        if (action === "maomiai-test-time") {
          event.preventDefault();
          event.stopPropagation();
          sendChatMessage("今天是几月几号，现在几点");
          return;
        }
        if (action === "maomiai-test-memory") {
          event.preventDefault();
          event.stopPropagation();
          sendChatMessage("我们现在有哪些 Agent 和 MCP 相关仓库资产");
          return;
        }
        if (action === "maomiai-clear-chat") {
          event.preventDefault();
          event.stopPropagation();
          window.__MAOMIAI_CHAT_MESSAGES__ = [];
          renderChat();
          return;
        }
        if (action === "demo-code-check") {
          const input = $("demoCodeInput");
          const result = $("demoCodeResult");
          if (result) result.textContent = `已收到检查内容：\n${input?.value || ""}`;
          return;
        }
        const target = event.target.closest("[data-view]");
        if (target) {
          event.preventDefault();
          event.stopPropagation();
          route(target.getAttribute("data-view"));
        }
      },
      true
    );
    document.addEventListener(
      "click",
      (event) => {
        const btn = event.target.closest("button");
        if (!btn) return;
        const text = (btn.textContent || "").trim();
        if (text === "发送" || text.includes("发送")) {
          event.preventDefault();
          event.stopPropagation();
          sendChatMessage();
        }
      },
      true
    );
    document.addEventListener(
      "keydown",
      (event) => {
        if ((event.ctrlKey || event.metaKey) && event.key === "Enter") {
          event.preventDefault();
          sendChatMessage();
        }
      },
      true
    );
  }

  function boot() {
    window.setView = route;
    window.routeView = route;
    window.sendChatMessage = sendChatMessage;
    window.__MAOMIAI_CONTEXT_ROUTER__ = routeUserMessage;
    window.__MAOMIAI_GET_CURRENT_MODEL__ = getCurrentModel;
    window.__MAOMIAI_TEST_INFER__ = () => sendChatMessage("你好，请用一句话介绍你自己");
    installNavAttributes();
    bind();
    setTimeout(installNavAttributes, 300);
    setTimeout(installNavAttributes, 1200);
    setInterval(installNavAttributes, 2500);
    console.log("[MAOMIAI] agent runtime main path ready C25-A1");
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
