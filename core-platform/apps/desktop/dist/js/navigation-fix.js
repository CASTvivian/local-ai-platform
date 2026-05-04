// P3.14-D4-D3-B: robust left navigation binding.
(function () {
  const PAGE_RENDERERS = {
    chat: null,
    launch: "renderLaunchPage",
    brain: "renderBrainPage",
    skills: "renderSkillsPage",
    documents: "renderDocumentsPage",
    workflows: "renderWorkflowsPage",
    artifacts: "renderArtifactsPage",
    "code-review": "renderCodeReviewPage",
    "repo-memory": "renderRepoMemoryPage",
    "design-system": "renderDesignSystemPage",
    models: "renderModelsPage",
    settings: "renderSettingsPage",
  };

  function findMainContent() {
    return (
      document.getElementById("content") ||
      document.querySelector(".content")
    );
  }

  function showNavigationError(view, error) {
    const content = findMainContent();
    const message = error && error.stack ? error.stack : String(error || "unknown error");
    if (content) {
      content.innerHTML = `
        <div style="margin:28px auto;max-width:880px;padding:22px;border:1px solid #fecaca;border-radius:18px;background:#fff7f7;color:#991b1b;">
          <h2>页面加载失败</h2>
          <p>视图：${escapeHtmlSafe(view)}</p>
          <pre style="white-space:pre-wrap;font-size:12px;">${escapeHtmlSafe(message)}</pre>
        </div>
      `;
    }
    console.error("[navigation-fix] page render failed", view, error);
  }

  function escapeHtmlSafe(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function markActive(view) {
    document.querySelectorAll("[data-view]").forEach((el) => {
      const active = el.getAttribute("data-view") === view;
      el.classList.toggle("active", active);
      el.classList.toggle("nav-active", active);
    });
  }

  async function renderFallbackChat(content) {
    const c = findMainContent();
    if (c) {
      c.innerHTML = `
        <div style="padding:28px;max-width:880px;margin:0 auto;">
          <h1>本地 AI 工作台</h1>
          <p style="color:#6b7280;">请选择左侧功能，或在底部输入任务。</p>
        </div>
      `;
    }
  }

  async function robustSetView(view) {
    try {
      if (!view) view = "chat";
      if (typeof window.currentView !== "undefined") {
        window.currentView = view;
      }
      markActive(view);
      const content = findMainContent();
      if (!content) {
        throw new Error("无法找到主内容容器：#content 或 .content 不存在");
      }
      if (view === "chat" || view === "new-chat") {
        if (typeof window.renderPage === "function") {
          await window.renderPage(content, "chat");
        } else if (typeof window.render === "function") {
          await window.render(content);
        } else {
          await renderFallbackChat(content);
        }
        return;
      }
      const rendererName = PAGE_RENDERERS[view];
      const renderer = rendererName ? window[rendererName] : null;
      if (typeof renderer === "function") {
        await renderer(content);
        return;
      }
      if (typeof window.renderPage === "function") {
        await window.renderPage(content, view);
        return;
      }
      throw new Error(`页面渲染函数不存在：${rendererName || view}`);
    } catch (error) {
      showNavigationError(view, error);
    }
  }

  function bindNavigationClicks() {
    document.querySelectorAll("[data-view]").forEach((el) => {
      if (el.__maomiaiNavBound) return;
      el.__maomiaiNavBound = true;
      el.addEventListener("click", function (event) {
        event.preventDefault();
        event.stopPropagation();
        const view = el.getAttribute("data-view");
        robustSetView(view);
      });
    });
  }

  window.setView = robustSetView;
  window.robustSetView = robustSetView;
  window.bindNavigationClicks = bindNavigationClicks;

  document.addEventListener("DOMContentLoaded", bindNavigationClicks);
  setTimeout(bindNavigationClicks, 200);
  setTimeout(bindNavigationClicks, 1000);
  console.log("[navigation-fix] loaded");
})();
