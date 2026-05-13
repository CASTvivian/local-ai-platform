(function () {
  console.log("[MAOMIAI] runtime context router loaded C21-B");

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

  function getTauriInvoke() {
    return window.__TAURI__?.core?.invoke || window.__TAURI_INTERNALS__?.invoke || null;
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

  function extractAssistantText(data) {
    if (!data) return "";
    if (typeof data === "string") return data;
    return (
      data.response ||
      data.output ||
      data.text ||
      data.content ||
      data.answer ||
      data?.message?.content ||
      data?.raw?.message?.content ||
      data?.raw?.response ||
      data?.data?.response ||
      data?.data?.output ||
      data?.choices?.[0]?.message?.content ||
      data?.choices?.[0]?.text ||
      data.message ||
      ""
    );
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
    box.innerHTML = messages || '<div class="demo-card"><p>请输入问题，测试本地 AI 是否可用。</p></div>';
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

  function classifyIntent(text) {
    const q = String(text || "").trim().toLowerCase();
    const hasAny = (items) => items.some((item) => q.includes(item.toLowerCase()));
    if (hasAny(["今天几号", "今天是几号", "今天日期", "现在几点", "当前时间", "几月几号", "星期几", "日期"])) {
      return { type: "time", reason: "date_or_time_query" };
    }
    if (hasAny(["天气", "气温", "下雨", "广州天气", "深圳天气", "北京天气", "上海天气"])) {
      return { type: "realtime_blocked", tool: "weather", reason: "weather_requires_live_tool" };
    }
    if (hasAny(["上网", "联网", "搜索", "查一下", "最新", "新闻", "今天的", "现在的", "实时", "官网"])) {
      return { type: "realtime_blocked", tool: "web_search", reason: "web_search_not_enabled" };
    }
    if (
      hasAny([
        "我们仓",
        "本地项目",
        "项目里",
        "repo",
        "repository",
        "github",
        "stars",
        "收藏的仓",
        "rag",
        "mcp",
        "agent",
        "智能体",
        "参考仓",
        "资产",
        "repo memory",
        "知识库",
        "模型目录",
        "视频模型",
        "context engine",
      ])
    ) {
      return { type: "repo_memory", reason: "project_or_asset_query" };
    }
    if (hasAny(["能做什么", "你能完成什么", "你有什么能力", "你的能力", "平台能力", "现在完成了什么"])) {
      return { type: "capability", reason: "capability_query" };
    }
    return { type: "local_chat", reason: "normal_chat" };
  }

  function answerTimeQuestion() {
    const now = new Date();
    const weekdays = ["星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六"];
    return (
      `现在是本机时间：${now.getFullYear()}年${now.getMonth() + 1}月${now.getDate()}日，${weekdays[now.getDay()]}，` +
      `${String(now.getHours()).padStart(2, "0")}:${String(now.getMinutes()).padStart(2, "0")}。`
    );
  }

  function answerRealtimeBlocked(intent, query) {
    if (intent.tool === "weather") {
      return [
        "我现在不能直接给你编天气。",
        "",
        "原因：当前 Windows 演示包还没有接入实时天气工具。",
        "",
        "正确流程应该是：",
        "1. 识别这是实时天气问题；",
        "2. 调用天气 API 或联网搜索；",
        "3. 返回带日期和来源的结果。",
        "",
        "目前我可以明确告诉你：实时天气工具尚未启用，所以不能把模型猜测当成真实天气。",
      ].join("\n");
    }
    return [
      "我现在不能直接联网查询，也不能凭空编一个结果。",
      "",
      "原因：当前演示包还没有启用 Web Search / Browser 工具。",
      "",
      `你的问题是：${query}`,
      "",
      "下一阶段 C21-C 会接入联网搜索工具。接入后，这类问题会走实时搜索，而不是直接让本地模型猜。",
    ].join("\n");
  }

  function answerCapabilityQuestion() {
    return [
      "当前 MAOMIAI 已经完成的是本地智能体平台 Demo 基座，不是完整最终版。",
      "",
      "已具备：",
      "1. Windows 桌面端打包与安装；",
      "2. 本地模型下载、识别、选择和推理；",
      "3. 本地 GitHub Stars / 仓库资产整理；",
      "4. Repo Memory 资产接口；",
      "5. 本地模型目录、视频模型目录和 Context Engine 架构；",
      "6. 基础的时间问题拦截和防乱答规则。",
      "",
      "仍在补齐：",
      "1. 联网搜索工具；",
      "2. 天气工具；",
      "3. 自动工具调用；",
      "4. Graph Memory；",
      "5. MCP Gateway；",
      "6. 视频生成后端。",
    ].join("\n");
  }

  async function queryRepoMemory(query) {
    const payloads = [
      {
        url: "http://127.0.0.1:18125/brain/search",
        body: { query, limit: 8 },
      },
      {
        url: "http://127.0.0.1:18125/brain/search",
        body: { q: query, limit: 8 },
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
        return data;
      } catch (e) {
        lastError = `${item.url} 请求失败：${String(e)}`;
      }
    }
    throw new Error(lastError || "Repo Memory 查询失败。");
  }

  function summarizeRepoMemoryResult(query, data) {
    const raw = JSON.stringify(data || {}, null, 2);
    const items = data?.results || data?.items || data?.matches || data?.data?.results || data?.data?.items || [];
    if (Array.isArray(items) && items.length) {
      const lines = [`我已从本地 Repo Memory 查询：${query}`, "", "相关资产："];
      for (const item of items.slice(0, 8)) {
        const name = item.full_name || item.repo || item.name || item.title || item.source || "unknown";
        const desc = item.description || item.summary || item.content || item.text || "";
        lines.push(`- ${name}${desc ? `：${String(desc).slice(0, 160)}` : ""}`);
      }
      return lines.join("\n");
    }
    if (data?.asset_count != null) {
      return `本地 Repo Memory 已加载资产数量：${data.asset_count}。你可以继续问 MCP、Agent、RAG、模型目录、视频模型目录等问题。`;
    }
    return ["我查了本地 Repo Memory，但没有整理出明确匹配结果。", "", "原始返回：", raw.slice(0, 1200)].join("\n");
  }

  async function answerRepoMemoryQuestion(query) {
    try {
      const result = await queryRepoMemory(query);
      return summarizeRepoMemoryResult(query, result);
    } catch (e) {
      return [
        "这是项目/仓库相关问题，按规则应该查询本地 Repo Memory。",
        "",
        "但当前 Repo Memory 服务没有成功响应。",
        "",
        `错误：${String(e)}`,
        "",
        "请确认 18125 repo_memory_service 已启动。",
      ].join("\n");
    }
  }

  async function callDirectLocalInference(prompt, modelInfo) {
    const invoke = getTauriInvoke();
    if (!invoke) {
      throw new Error("Tauri invoke 不可用，当前不是桌面运行环境或 preload 未注入。");
    }
    const raw = await invoke("generate_local_ai_response", {
      profile: modelInfo.profile,
      prompt,
    });
    const parsed = safeParse(raw);
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

  async function routeUserMessage(query) {
    const intent = classifyIntent(query);
    updateDebug("Context Router", intent);
    if (intent.type === "time") return answerTimeQuestion();
    if (intent.type === "realtime_blocked") return answerRealtimeBlocked(intent, query);
    if (intent.type === "repo_memory") return await answerRepoMemoryQuestion(query);
    if (intent.type === "capability") return answerCapabilityQuestion();

    const modelInfo = getCurrentModel();
    try {
      return await callDirectLocalInference(query, modelInfo);
    } catch (directError) {
      updateDebug("直接本地推理失败，尝试 18080 兜底", {
        error: String(directError),
        profile: modelInfo.profile,
        model: modelInfo.model,
      });
      try {
        return await callGatewayFallback(query, modelInfo);
      } catch (gatewayError) {
        return `推理失败：${String(directError)}\n\n18080 兜底也失败：${String(gatewayError)}`;
      }
    }
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
            <p>Context Router 已启用</p>
          </div>
          <div class="chat-model-selector">
            <span>当前能力</span>
            <select id="chatModelSelect">${options}</select>
          </div>
        </div>
        <div class="demo-chat-actions">
          <button class="primary" data-action="maomiai-test-infer">测试本地推理</button>
          <button class="secondary" data-action="maomiai-test-time">测试时间工具</button>
          <button class="secondary" data-action="maomiai-test-memory">测试项目知识</button>
          <button class="secondary" data-action="maomiai-clear-chat">清空会话</button>
        </div>
        <details id="maomiaiDebugBox" class="maomiai-debug-box">
          <summary>调试状态（点击展开）</summary>
          <pre>Context Router ready. 当前能力：${escapeHtml(current.title)} / ${escapeHtml(current.model)}</pre>
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
    pushChat("assistant", "正在判断问题类型并处理...");
    const answer = await routeUserMessage(value);
    updateLastAssistant(answer);
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
      <div class="demo-card"><h2>运行模式</h2><p>当前为本地运行模式，Context Router 已启用。</p></div>
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
    console.log("[MAOMIAI] context router ready C21-B");
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
