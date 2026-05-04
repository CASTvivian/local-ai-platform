// P3.14-D7-B: Session Manager Regression Fix
// This file is the single owner of chat sessions and composer behavior.
(function () {
  const STORE_KEY = "maomiai_chat_session_manager_v3";
  const ENDPOINTS = {
    modelGenerate: "http://127.0.0.1:18080/generate",
    modelChat: "http://127.0.0.1:18080/chat",
    openaiChat: "http://127.0.0.1:18080/v1/chat/completions",
  };
  const CONTEXT_LIMIT = 16;
  function esc(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
  function uid(prefix) {
    return `${prefix}_${Date.now().toString(36)}_${Math.random().toString(16).slice(2, 10)}`;
  }
  function ts() {
    return Date.now();
  }
  function makeSession(title = "新会话") {
    return {
      id: uid("session"),
      title,
      created_at: ts(),
      updated_at: ts(),
      messages: [],
    };
  }
  function normalizeStore(raw) {
    if (!raw || typeof raw !== "object") {
      const s = makeSession();
      return { currentSessionId: s.id, sessions: [s] };
    }
    if (!Array.isArray(raw.sessions) || raw.sessions.length === 0) {
      const s = makeSession();
      return { currentSessionId: s.id, sessions: [s] };
    }
    raw.sessions = raw.sessions.map((s) => ({
      id: s.id || uid("session"),
      title: s.title || "未命名会话",
      created_at: s.created_at || ts(),
      updated_at: s.updated_at || ts(),
      messages: Array.isArray(s.messages) ? s.messages : [],
    }));
    if (!raw.currentSessionId || !raw.sessions.some((s) => s.id === raw.currentSessionId)) {
      raw.currentSessionId = raw.sessions[0].id;
    }
    return raw;
  }
  function loadStore() {
    try {
      const raw = localStorage.getItem(STORE_KEY);
      if (!raw) {
        const s = makeSession();
        return { currentSessionId: s.id, sessions: [s] };
      }
      const data = JSON.parse(raw);
      return normalizeStore(data);
    } catch {
      const s = makeSession();
      return { currentSessionId: s.id, sessions: [s] };
    }
  }
  function saveStore(store) {
    const normalized = normalizeStore(store);
    localStorage.setItem(STORE_KEY, JSON.stringify(normalized));
    return normalized;
  }
  function currentSession(store = loadStore()) {
    return store.sessions.find((s) => s.id === store.currentSessionId) || store.sessions[0];
  }
  function contentEl() {
    return (
      document.getElementById("content") ||
      document.querySelector("main .content") ||
      document.querySelector("main")
    );
  }
  function inputEl() {
    return (
      document.getElementById("composerInput") ||
      document.getElementById("promptInput") ||
      document.querySelector(".composer textarea") ||
      document.querySelector("textarea") ||
      document.querySelector('input[type="text"]')
    );
  }
  function sendButton() {
    return (
      document.getElementById("sendButton") ||
      Array.from(document.querySelectorAll("button")).find((b) => (b.textContent || "").trim() === "发送")
    );
  }
  function sessionsContainer() {
    return (
      document.getElementById("sessions") ||
      document.getElementById("sessionList") ||
      document.querySelector(".sessions")
    );
  }
  function renderSessions() {
    const store = loadStore();
    const holder = sessionsContainer();
    if (!holder) return;
    holder.innerHTML = `
      <div class="session-toolbar">
        <button class="btn-soft" type="button" onclick="chatCreateNewSession()">新建会话</button>
      </div>
      <div class="session-list">
        ${store.sessions.map((s) => `
          <div class="session-row ${s.id === store.currentSessionId ? "active" : ""}">
            <button class="session-title" type="button" onclick="chatSwitchSession('${esc(s.id)}')" title="${esc(s.id)}">
              ${esc(s.title || "未命名会话")}
            </button>
            <button class="session-delete" type="button" onclick="chatDeleteSession('${esc(s.id)}')" title="删除">×</button>
          </div>
        `).join("")}
      </div>
    `;
  }
  function renderChat(target) {
    const el = target || contentEl();
    if (!el) return;
    const store = loadStore();
    const session = currentSession(store);
    const messages = session.messages.length
      ? session.messages.map((m) => `
        <div class="chat-msg ${esc(m.role)}">
          <div class="chat-role">${m.role === "user" ? "你" : m.role === "assistant" ? "本地 AI" : "系统"}</div>
          <div class="chat-body">${esc(m.content)}</div>
        </div>
      `).join("")
      : `
        <div class="chat-empty">
          <h1>本地 AI 工作台</h1>
          <p>这是一个新的会话。你可以直接输入任务或问题。</p>
        </div>
      `;
    el.innerHTML = `
      <div class="chat-page">
        <div class="chat-session-header">
          <div>
            <h1>${esc(session.title || "新会话")}</h1>
            <p>当前会话：${esc(session.id)}</p>
          </div>
          <div class="chat-session-actions">
            <button class="btn-soft" type="button" onclick="chatCreateNewSession()">新建会话</button>
            <button class="btn-soft" type="button" onclick="chatClearCurrentSession()">清空当前会话</button>
          </div>
        </div>
        <div id="chatMessages" class="chat-messages">${messages}</div>
      </div>
    `;
    const box = document.getElementById("chatMessages");
    if (box) box.scrollTop = box.scrollHeight;
  }
  function renderAll() {
    renderSessions();
    renderChat();
    bindComposer();
  }
  function createNewSession() {
    const store = loadStore();
    const s = makeSession();
    store.sessions.unshift(s);
    store.currentSessionId = s.id;
    saveStore(store);
    renderAll();
    focusInput();
  }
  function switchSession(id) {
    const store = loadStore();
    if (store.sessions.some((s) => s.id === id)) {
      store.currentSessionId = id;
      saveStore(store);
    }
    renderAll();
    focusInput();
  }
  function deleteSession(id) {
    let store = loadStore();
    if (store.sessions.length <= 1) {
      const fresh = normalizeStore(null);
      saveStore(fresh);
      renderAll();
      return;
    }
    store.sessions = store.sessions.filter((s) => s.id !== id);
    if (!store.sessions.some((s) => s.id === store.currentSessionId)) {
      store.currentSessionId = store.sessions[0].id;
    }
    saveStore(store);
    renderAll();
  }
  function clearCurrentSession() {
    const store = loadStore();
    const s = currentSession(store);
    s.messages = [];
    s.title = "新会话";
    s.updated_at = ts();
    saveStore(store);
    renderAll();
  }
  function appendMessage(role, content, meta = {}) {
    const store = loadStore();
    const s = currentSession(store);
    const msg = {
      id: uid("msg"),
      role,
      content: String(content ?? ""),
      meta,
      created_at: ts(),
    };
    s.messages.push(msg);
    if (role === "user" && (!s.title || s.title === "新会话" || s.title === "默认会话")) {
      s.title = String(content || "新会话").slice(0, 24) || "新会话";
    }
    s.updated_at = ts();
    saveStore(store);
    renderAll();
    return msg.id;
  }
  function replaceMessage(messageId, content, meta = {}) {
    const store =话 loadStore();
    const s = currentSession(store);
    const msg = s.messages.find((m) => m.id === messageId);
    if (msg) {
      msg.content = String(content ?? "");
      msg.meta = meta;
      msg.updated_at = ts();
      s.updated_at = ts();
      saveStore(store);
      renderAll();
    }
  }
  function getRecentContextMessages(limit = CONTEXT_LIMIT) {
    const s = currentSession();
    return s.messages
      .filter((m) => m.role === "user" || m.role === "assistant")
      .slice(-limit)
      .map((m) => ({
        role: m.role === "assistant" ? "assistant" : "user",
        content: m.content,
      }));
  }
  function buildPromptFromContext(messages) {
    return messages
      .map((m) => `${m.role === "assistant" ? "助手" : "用户"}：${m.content}`)
      .join("\n") + "\n助手：";
  }
  async function postJson(url, body, timeout = 60000) {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body || {}),
      signal: AbortSignal.timeout(timeout),
    });
    const text = await res.text();
    let data = {};
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text };
    }
    if (!res.ok) {
      throw new Error(`${res.status} ${url}\n${text}`);
    }
    return data;
  }
  async function callModelWithContext() {
    const messages = getRecentContextMessages(CONTEXT_LIMIT);
    const endpointAttempts = [
      {
        url: ENDPOINTS.modelChat,
        body: { model: "qwen2.5:7b", messages, stream: false },
      },
      {
        url: ENDPOINTS.openaiChat,
        body: { model: "qwen2.5:7b", messages, stream: false },
      },
      {
        url: ENDPOINTS.modelGenerate,
        body: { model: "qwen2.5:7b", prompt: buildPromptFromContext(messages), stream: false },
      },
    ];
    let lastErr = null;
    for (const attempt of endpointAttempts) {
      try {
        const data = await postJson(attempt.url, attempt.body);
        const text =
          data.response ||
          data.output ||
          data.text ||
          data.content ||
          data.message?.content ||
          data.choices?.[0]?.message?.content ||
          data.choices?.[0]?.text ||
          data.result;
        if (text) {
          return { text: String(text), raw: data, endpoint: attempt.url };
        }
        return { text: JSON.stringify(data, null, 2), raw: data, endpoint: attempt.url };
      } catch (e) {
        lastErr = e;
      }
    }
    throw lastErr || new Error("模型网关没有可用接口");
  }
  async function sendCurrentMessage() {
    const input = inputEl();
    const text = String(input?.value || "").trim();
    if (!text) return;
    if (input) input.value = "";
    const pendingId = appendMessage("assistant", "正在调用本地模型，并带入当前会话上下文...", { pending: true });
    try {
      const result = await callModelWithContext();
      replaceMessage(pendingId, result.text, {
        endpoint: result.endpoint,
        raw: result.raw,
      });
      if (typeof window.previewText === "function") {
        window.previewText("本地模型回复", JSON.stringify(result.raw, null, 2), "json");
      }
    } catch (err) {
      replaceMessage(
        pendingId,
        `本地模型调用失败：${String(err)}\n\n请检查 18080 model_gateway / 11434 Ollama / qwen2.5:7b。`,
        { error: String(err) }
      );
    }
  }
  function bindComposer() {
    const btn = sendButton();
    const input = inputEl();
    if (btn && !btn.__sessionManagerBound) {
      btn.__sessionManagerBound = true;
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        e.stopPropagation();
        sendCurrentMessage();
      }, true);
    }
    if (input && !input.__sessionManagerBound) {
      input.__sessionManagerBound = true;
      input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          sendCurrentMessage();
        }
      }, true);
    }
  }
  function focusInput() {
    setTimeout(() => {
      const input = inputEl();
      if (input) input.focus();
    }, 50);
  }
  // Public API
  window.chatCreateNewSession = createNewSession;
  window.chatSwitchSession = switchSession;
  window.chatDeleteSession = deleteSession;
  window.chatClearCurrentSession = clearCurrentSession;
  window.chatRender = renderAll;
  window.getRecentContextMessages = getRecentContextMessages;
  window.sendMessage = sendCurrentMessage;
  window.robustSendMessage = sendCurrentMessage;
  window.stableSendMessage = sendCurrentMessage;
  const previousSetView = window.setView;
  window.setView = async function patchedSetView(view) {
    if (view === "chat" || view === "new-chat") {
      renderAll();
      return;
    }
    if (typeof previousSetView === "function") {
      return previousSetView(view);
    }
  };
  document.addEventListener("DOMContentLoaded", () => {
    renderSessions();
    bindComposer();
    if (!contentEl()?.innerHTML.trim()) {
      renderAll();
    }
  });
  setTimeout(() => {
    renderSessions();
    bindComposer();
  }, 300);
  setTimeout(() => {
    renderSessions();
    bindComposer();
  }, 1200);
  console.log("[chat-session-manager D7-B] loaded");
})();
