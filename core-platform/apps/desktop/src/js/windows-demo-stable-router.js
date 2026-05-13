(function () {
  console.log("[MAOMIAI] windows-demo-stable-router loaded C14");

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
    return catalog.find((x) => x.profile === profile) || catalog[0] || MODEL_CATALOG_FALLBACK[0];
  }

  function getTauriInvoke() {
    return window.__TAURI__?.core?.invoke || window.__TAURI_INTERNALS__?.invoke || null;
  }

  function extractAssistantText(data) {
    if (!data) return "";
    if (typeof data === "string") return data;
    return (
      data.response ||
      data.output ||
      data.text ||
      data.content ||
      data?.message?.content ||
      data.message ||
      data.answer ||
      data?.raw?.response ||
      data?.raw?.message?.content ||
      data?.data?.response ||
      data?.data?.output ||
      data?.choices?.[0]?.message?.content ||
      data?.choices?.[0]?.text ||
      ""
    );
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

  function updateChatMessagesOnly() {
    const box = $("demoChatMessages");
    if (!box) return;
    const messages = (window.__MAOMIAI_CHAT_MESSAGES__ || [])
      .map(
        (m) => `
      <div class="demo-chat-msg ${escapeHtml(m.role)}">
        <strong>${m.role === "user" ? "你" : "本地 AI"}</strong>
        <div>${escapeHtml(m.content)}</div>
      </div>
    `
      )
      .join("");
    box.innerHTML = messages || '<div class="demo-card"><p>请输入问题，测试本地 AI 是否可用。</p></div>';
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
            <p>新会话</p>
          </div>
          <div class="chat-model-selector">
            <span>当前能力</span>
            <select id="chatModelSelect">${options}</select>
          </div>
        </div>
        <div class="demo-chat-actions">
          <button class="primary" data-action="maomiai-test-infer">测试本地推理</button>
          <button class="secondary" data-action="maomiai-clear-chat">清空会话</button>
        </div>
        <details id="maomiaiDebugBox" class="maomiai-debug-box">
          <summary>调试状态（点击展开）</summary>
          <pre>等待发送。当前能力：${escapeHtml(current.title)} / ${escapeHtml(current.model)}</pre>
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

  async function callDirectLocalInference(prompt, modelInfo) {
    const invoke = getTauriInvoke();
    const debugBase = {
      stage: "start",
      hasTauriInvoke: !!invoke,
      profile: modelInfo.profile,
      model: modelInfo.model,
      prompt,
    };
    updateDebug("发送链路：开始", debugBase);
    if (!invoke) {
      throw new Error("Tauri invoke 不可用，当前不是桌面运行环境或 preload 未注入。");
    }

    updateDebug("发送链路：调用 generate_local_ai_response", debugBase);
    const raw = await invoke("generate_local_ai_response", {
      profile: modelInfo.profile,
      prompt,
    });
    updateDebug("发送链路：收到 Tauri 原始返回", raw);

    const parsed = safeParse(raw);
    updateDebug("发送链路：解析后的返回", parsed);
    if (parsed && parsed.ok === false && parsed.message) {
      throw new Error(parsed.message + (parsed.error ? ` / ${parsed.error}` : ""));
    }

    const text = extractAssistantText(parsed);
    if (text) return text;
    if (typeof raw === "string" && raw.trim()) return raw;
    throw new Error("本地推理没有返回可显示内容。");
  }

  async function callGatewayFallback(prompt, modelInfo) {
    const payloads = [
      {
        url: "http://127.0.0.1:18080/generate",
        body: { prompt, profile: modelInfo.profile, model: modelInfo.model },
      },
      {
        url: "http://127.0.0.1:18080/generate",
        body: { prompt },
      },
    ];

    let lastError = null;
    for (const item of payloads) {
      try {
        const res = await fetch(item.url, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(item.body),
        });
        const raw = await res.text();
        const data = safeParse(raw);
        if (!res.ok) {
          lastError = `${item.url} HTTP ${res.status}: ${raw}`;
          continue;
        }
        const text = extractAssistantText(data);
        if (text) return text;
        lastError = `${item.url} 返回为空：${raw}`;
      } catch (e) {
        lastError = `${item.url} 请求失败：${String(e)}`;
      }
    }
    throw new Error(lastError || "18080 网关没有返回内容。");
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

    const modelInfo = getCurrentModel();
    if (input && !forceText) {
      input.value = "";
    }
    pushChat("user", value);
    pushChat("assistant", `正在使用「${modelInfo.title}」生成回复...`);

    try {
      const text = await callDirectLocalInference(value, modelInfo);
      updateLastAssistant(text);
      return;
    } catch (directError) {
      updateDebug("直接本地推理失败，尝试 18080 兜底", {
        error: String(directError),
        profile: modelInfo.profile,
        model: modelInfo.model,
      });
      try {
        const text = await callGatewayFallback(value, modelInfo);
        updateLastAssistant(text);
        return;
      } catch (gatewayError) {
        updateLastAssistant(`推理失败：${String(directError)}\n\n18080 兜底也失败：${String(gatewayError)}`);
      }
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
      <div class="demo-card"><h2>运行模式</h2><p>当前为本地运行模式。</p></div>
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
    const v = String(view || "chat");
    if (["chat", "new-chat", "new"].includes(v)) return renderChat();
    if (["models", "model", "local-model", "local-models"].includes(v)) return renderLocalModels();
    if (["artifacts", "files", "documents"].includes(v)) return renderFiles();
    if (["code-review", "code"].includes(v)) return renderCodeReview();
    if (["settings", "setting"].includes(v)) return renderSettings();
    renderChat();
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
          if (result) {
            result.textContent = `已收到检查内容：\n${input?.value || ""}`;
          }
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
    window.__MAOMIAI_GET_CURRENT_MODEL__ = getCurrentModel;
    window.__MAOMIAI_TEST_INFER__ = () => sendChatMessage("你好，请用一句话介绍你自己");
    installNavAttributes();
    bind();
    setTimeout(installNavAttributes, 300);
    setTimeout(installNavAttributes, 1200);
    setInterval(installNavAttributes, 2500);
    console.log("[MAOMIAI] stable router ready C14");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();

console.log("[MAOMIAI] C15 Chinese prompt file fix loaded");
