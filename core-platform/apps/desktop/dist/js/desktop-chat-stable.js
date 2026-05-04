// P3.14-D4-D3-E: Stable chat/session/model fallback.
// Last loaded. Owns chat page, composer send, local persistence, and repo-memory override.
(function () {
  const STORE_KEY = "maomiai_desktop_chat_sessions_v1";
  const API_BASE = {
    modelGateway: "http://127.0.0.1:18080",
    autoRouter: "http://127.0.0.1:18093",
    runtime: "http://127.0.0.1:18104",
    repoMemory: "http://127.0.0.1:18125",
  };
  function h(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
  function json(value) {
    try {
      return JSON.stringify(value, null, 2);
    } catch {
      return String(value);
    }
  }
  async function getJson(url, timeout = 5000) {
    const res = await fetch(url, { signal: AbortSignal.timeout(timeout) });
    const text = await res.text();
    let data = {};
    try { data = JSON.parse(text); } catch { data = { raw: text }; }
    if (!res.ok) throw new Error(`${res.status} ${url}\n${text}`);
    return data;
  }
  async function postJson(url, body, timeout = 30000) {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body || {}),
      signal: AbortSignal.timeout(timeout),
    });
    const text = await res.text();
    let data = {};
    try { data = JSON.parse(text); } catch { data = { raw: text }; }
    if (!res.ok) throw new Error(`${res.status} ${url}\n${text}`);
    return data;
  }
  function contentEl() {
    return (
      document.getElementById("content") ||
      document.getElementById("workspace") ||
      document.getElementById("mainContent") ||
      document.querySelector("main .content") ||
      document.querySelector("main")
    );
  }
  function inputEl() {
    return (
      document.getElementById("composerInput") ||
      document.querySelector(".composer textarea") ||
      document.querySelector("textarea") ||
      document.querySelector('input[type="text"]')
    );
  }
  function sendBtn() {
    return (
      document.getElementById("sendButton") ||
      Array.from(document.querySelectorAll("button")).find(b => (b.textContent || "").trim() === "发送")
    );
  }
  function nowId(prefix) {
    return `${prefix}_${Date.now().toString(36)}_${Math.random().toString(16).slice(2, 8)}`;
  }
  function loadStore() {
    try {
      const raw = localStorage.getItem(STORE_KEY);
      if (raw) return JSON.parse(raw);
    } catch {}
    return {
      currentSessionId: "default",
      sessions: [
        {
          id: "default",
          title: "默认会话",
          created_at: Date.now(),
          updated_at: Date.now(),
          messages: [],
        },
      ],
    };
  }
  function saveStore(store) {
    localStorage.setItem(STORE_KEY, JSON.stringify(store));
  }
  function currentSession(store = loadStore()) {
    let s = store.sessions.find(x => x.id === store.currentSessionId);
    if (!s) {
      s = {
        id: "default",
        title: "默认会话",
        created_at: Date.now(),
        updated_at: Date.now(),
        messages: [],
      };
      store.currentSessionId = s.id;
      store.sessions.unshift(s);
      saveStore(store);
    }
    return s;
  }
  function addMessage(role, content, meta = {}) {
    const store = loadStore();
    const s = currentSession(store);
    s.messages.push({
      id: nowId("msg"),
      role,
      content,
      meta,
      created_at: Date.now(),
    });
    s.updated_at = Date.now();
    if (role === "user" && (!s.title || s.title === "默认会话")) {
      s.title = String(content).slice(0, 18) || "默认会话";
    }
    saveStore(store);
    renderSessionsList();
    renderChatPage();
  }
  function updateLastAssistant(content, meta = {}) {
    const store = loadStore();
    const s = currentSession(store);
    const last = [...s.messages].reverse().find(x => x.role === "assistant");
    if (last) {
      last.content = content;
      last.meta = meta;
      last.updated_at = Date.now();
    } else {
      s.messages.push({
        id: nowId("msg"),
        role: "assistant",
        content,
        meta,
        created_at: Date.now(),
      });
    }
    s.updated_at = Date.now();
    saveStore(store);
    renderChatPage();
  }
  function renderSessionsList() {
    const store = loadStore();
    const holders = Array.from(document.querySelectorAll(".sessions, #sessions, #sessionList"));
    if (!holders.length) return;
    const html = store.sessions.map(s => `
      <button class="session-item ${s.id === store.currentSessionId ? "active" : ""}" data-session-id="${h(s.id)}">
        ${h(s.title || "未命名会话")}
      </button>
    `).join("");
    for (const holder of holders) {
      holder.innerHTML = html;
      holder.querySelectorAll("[data-session-id]").forEach(btn => {
        btn.onclick = () => {
          const st = loadStore();
          st.currentSessionId = btn.getAttribute("data-session-id");
          saveStore(st);
          renderSessionsList();
          renderChatPage();
        };
      });
    }
  }
  function chatHtml() {
    const store = loadStore();
    const s = currentSession(store);
    const messages = s.messages.length
      ? s.messages.map(m => `
        <div class="stable-chat-message ${m.role}">
          <div class="stable-chat-role">${m.role === "user" ? "你" : m.role === "assistant" ? "本地 AI" : "系统"}</div>
          <div class="stable-chat-content">${h(m.content)}</div>
        </div>
      `).join("")
      : `
        <div class="stable-chat-empty">
          <h1>本地 AI 工作台</h1>
          <p>请选择左侧功能，或在底部输入任务。</p>
        </div>
      `;
    return `
      <div class="stable-chat-wrap">
        <div id="stableChatTimeline" class="stable-chat-timeline">
          ${messages}
        </div>
      </div>
    `;
  }
  function renderChatPage(target) {
    const el = target || contentEl();
    if (!el) return;
    el.innerHTML = chatHtml();
    const timeline = document.getElementById("stableChatTimeline");
    if (timeline) timeline.scrollTop = timeline.scrollHeight;
  }
  async function callLocalModel(prompt) {
    const payloadCandidates = [
      {
        model: "qwen2.5:7b",
        prompt,
        stream: false,
      },
      {
        messages: [{ role: "user", content: prompt }],
        model: "qwen2.5:7b",
        stream: false,
      },
      {
        input: prompt,
        model: "qwen2.5:7b",
      },
    ];
    const paths = ["/generate", "/chat", "/v1/chat/completions", "/complete"];
    let lastErr = null;
    for (const path of paths) {
      for (const body of payloadCandidates) {
        try {
          const data = await postJson(`${API_BASE.modelGateway}${path}`, body, 45000);
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
            return { ok: true, text: String(text), raw: data, endpoint: path };
          }
          return { ok: true, text: json(data), raw: data, endpoint: path };
        } catch (e) {
          lastErr = e;
        }
      }
    }
    throw lastErr || new Error("model_gateway no supported endpoint");
  }
  async function callRouteRuntime(prompt) {
    const result = { route: null, runtime: null };
    try {
      result.route = await postJson(`${API_BASE.autoRouter}/route`, { prompt, task: prompt }, 10000);
    } catch (e) {
      result.route = { ok: false, error: String(e) };
    }
    try {
      result.runtime = await postJson(`${API_BASE.runtime}/execute`, {
        task: prompt,
        prompt,
        dry_run: true,
        route: result.route,
        metadata: { source: "desktop-chat-stable" },
      }, 20000);
    } catch (e) {
      result.runtime = { ok: false, error: String(e), prompt };
    }
    return result;
  }
  async function stableSendMessage() {
    const input = inputEl();
    const text = String(input?.value || "").trim();
    if (!text) return;
    if (input) input.value = "";
    addMessage("user", text);
    addMessage("assistant", "正在调用本地模型...");
    try {
      const model = await callLocalModel(text);
      updateLastAssistant(model.text, { model });
      if (typeof window.previewText === "function") {
        window.previewText("本地模型响应", json(model.raw), "json");
      }
      return;
    } catch (modelErr) {
      updateLastAssistant("本地模型暂不可用，正在返回执行链路诊断...");
      try {
        const diag = await callRouteRuntime(text);
        const reply = [
          "本地模型暂未接通或 model_gateway 不可用。",
          "",
          "以下是当前执行链路诊断：",
          "",
          json(diag),
        ].join("\n");
        updateLastAssistant(reply, { model_error: String(modelErr), diag });
        if (typeof window.previewText === "function") {
          window.previewText("执行链路诊断", json({ model_error: String(modelErr), diag }), "json");
        }
      } catch (diagErr) {
        updateLastAssistant(`发送失败：${String(diagErr)}`, { model_error: String(modelErr), diag_error: String(diagErr) });
      }
    }
  }
  function bindComposer() {
    const btn = sendBtn();
    const input = inputEl();
    if (btn && !btn.__chatStableBound) {
      btn.__chatStableBound = true;
      btn.addEventListener("click", e => {
        e.preventDefault();
        e.stopPropagation();
        stableSendMessage();
      }, true);
    }
    if (input && !input.__chatStableBound) {
      input.__chatStableBound = true;
      input.addEventListener("keydown", e => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          stableSendMessage();
        }
      }, true);
    }
  }
  async function renderRepoMemoryStable(content) {
    const el = content || contentEl();
    el.innerHTML = `
      <div class="stable-page">
        <div class="page-hero">
          <h1>仓库记忆</h1>
          <p>沉淀仓库结构、修复历史、知识条目和上下文快照。</p>
        </div>
        <div class="page-card">
          <h2>仓库列表</h2>
          <div id="repoStableList" class="mono">正在加载...</div>
        </div>
      </div>
    `;
    const box = document.getElementById("repoStableList");
    try {
      const data = await getJson(`${API_BASE.repoMemory}/repo/list`, 8000);
      const items = data.items || [];
      box.innerHTML = items.length
        ? items.map(x => `
          <div class="mini-card">
            <b>${h(x.name || x.id)}</b><br/>
            <span class="badge">${h(x.id)}</span>
            <div>${h(x.description || "")}</div>
            <div class="mono">${h(x.path || "")}</div>
          </div>
        `).join("")
        : `<div class="empty-state">暂无仓库记忆。你可以后续通过代码修复流程自动沉淀。</div>`;
    } catch (e) {
      box.innerHTML = `<pre class="mono">${h(e.stack || String(e))}</pre>`;
    }
  }
  // Force override old/broken functions.
  window.renderChatView = renderChatPage;
  window.renderRepoMemoryPage = renderRepoMemoryStable;
  window.sendMessage = stableSendMessage;
  window.robustSendMessage = stableSendMessage;
  window.stableSendMessage = stableSendMessage;
  window.renderChatPageStable = renderChatPage;
  window.renderSessionsListStable = renderSessionsList;
  // Patch setView to force repo-memory + chat.
  const previousSetView = window.setView;
  window.setView = async function patchedSetView(view) {
    if (view === "chat" || view === "new-chat") {
      renderChatPage();
      return;
    }
    if (view === "repo-memory") {
      await renderRepoMemoryStable(contentEl());
      return;
    }
    if (typeof previousSetView === "function") {
      return previousSetView(view);
    }
  };
  document.addEventListener("DOMContentLoaded", () => {
    bindComposer();
    renderSessionsList();
    if (!contentEl()?.innerHTML.trim()) renderChatPage();
  });
  setTimeout(() => {
    bindComposer();
    renderSessionsList();
  }, 300);
  setTimeout(() => {
    bindComposer();
    renderSessionsList();
  }, 1200);
  console.log("[desktop-chat-stable] loaded");
})();
