// D7-C3-A: ChatGPT-like product UI layer.
// This layer improves the default chat page without changing backend services.
(function () {
  function esc(v) {
    return String(v ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
  function getContent() {
    return document.getElementById("content") || document.querySelector("main .content");
  }
  function getPrompt() {
    return document.getElementById("prompt") || document.getElementById("composerInput") || document.querySelector("textarea");
  }
  function getSessionMeta() {
    return document.getElementById("sessionMeta");
  }
  function renderWelcome() {
    const content = getContent();
    if (!content) return;
    const hasMessages =
      content.querySelector(".msg") ||
      content.querySelector(".chat-msg") ||
      content.querySelector(".task-card");
    if (hasMessages) return;
    content.innerHTML = `
      <div class="gpt-home">
        <div class="gpt-logo">M</div>
        <h1>今天想让 MAOMIAI 帮你做什么？</h1>
        <p>直接用自然语言描述任务。系统会自动判断是否需要调用文档处理、代码检查、工作流或本地模型。</p>
        <div class="gpt-suggestions">
          <button onclick="fillPrompt('帮我总结这个项目目前完成了哪些功能，并列出下一步计划')">
            <strong>总结项目进度</strong>
            <span>梳理当前代码、文档和阶段状态</span>
          </button>
          <button onclick="fillPrompt('帮我检查这段代码有没有风险，并给出修改建议')">
            <strong>检查代码风险</strong>
            <span>自动进入代码检查链路</span>
          </button>
          <button onclick="fillPrompt('帮我整理最近生成的文件和结果，输出一份交付清单')">
            <strong>整理文件结果</strong>
            <span>查看产物、报告和构建结果</span>
          </button>
          <button onclick="fillPrompt('我要处理一个文档，请自动判断解析、总结和分块方式')">
            <strong>处理文档</strong>
            <span>无需单独进入文档页面</span>
          </button>
        </div>
      </div>
    `;
  }
  function fillPrompt(text) {
    const input = getPrompt();
    if (!input) return;
    input.value = text;
    input.focus();
  }
  function forceChatDefault() {
    try {
      if (typeof window.setView === "function") {
        const saved = localStorage.getItem("currentView");
        const hidden = new Set(["launch", "brain", "skills", "documents", "workflows", "repo-memory", "design-system"]);
        if (!saved || hidden.has(saved)) {
          localStorage.setItem("currentView", "chat");
        }
      }
    } catch (_) {}
  }
  function patchSubmitHint() {
    const input = getPrompt();
    if (input) {
      input.placeholder = "给 MAOMIAI 发送消息，或让它处理文档、检查代码、整理结果...";
    }
    const meta = getSessionMeta();
    if (meta && (!meta.textContent || meta.textContent.includes("view:"))) {
      meta.textContent = "新会话";
    }
  }
  // Public helper.
  window.fillPrompt = fillPrompt;
  document.addEventListener("DOMContentLoaded", () => {
    forceChatDefault();
    patchSubmitHint();
    setTimeout(() => {
      patchSubmitHint();
      renderWelcome();
    }, 200);
    setTimeout(() => {
      patchSubmitHint();
      renderWelcome();
    }, 1000);
  });
  const oldRender = window.render;
  if (typeof oldRender === "function") {
    window.render = function patchedRender() {
      const r = oldRender.apply(this, arguments);
      setTimeout(() => {
        patchSubmitHint();
        const current = window.currentView || localStorage.getItem("currentView") || "chat";
        if (current === "chat") renderWelcome();
      }, 20);
      return r;
    };
  }
  console.log("[D7-C3-A] ChatGPT-like UI loaded");
})();
