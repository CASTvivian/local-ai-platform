// P3.14-D4-D3-D: Desktop Runtime Stable Override
// Last-loaded safety layer. Overrides unstable page modules and composer flow.
(function () {
  const API_BASE = {
    autoRouter: "http://127.0.0.1:18093",
    runtime: "http://127.0.0.1:18104",
    skill: "http://127.0.0.1:18121",
    artifact: "http://127.0.0.1:18123",
    codeReview: "http://127.0.0.1:18124",
    repoMemory: "http://127.0.0.1:18125",
    workflow: "http://127.0.0.1:18126",
    designSystem: "http://127.0.0.1:18127",
  };
  function h(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }
  function j(value) {
    try {
      return JSON.stringify(value, null, 2);
    } catch {
      return String(value);
    }
  }
  async function getJson(url) {
    const res = await fetch(url, { signal: AbortSignal.timeout(5000) });
    const text = await res.text();
    let data = {};
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text };
    }
    if (!res.ok) throw new Error(`${res.status} ${url}\n${text}`);
    return data;
  }
  async function postJson(url, body) {
    const res = await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body || {}),
      signal: AbortSignal.timeout(10000),
    });
    const text = await res.text();
    let data = {};
    try {
      data = JSON.parse(text);
    } catch {
      data = { raw: text };
    }
    if (!res.ok) throw new Error(`${res.status} ${url}\n${text}`);
    return data;
  }
  function shell(title, subtitle, inner) {
    return `
      <div class="stable-page">
        <div class="page-hero">
          <h1>${h(title)}</h1>
          ${subtitle ? `<p>${h(subtitle)}</p>` : ""}
        </div>
        ${inner || ""}
      </div>
    `;
  }
  function card(title, inner) {
    return `
      <div class="page-card">
        ${title ? `<h2>${h(title)}</h2>` : ""}
        ${inner || ""}
      </div>
    `;
  }
  function mono(value) {
    return `<pre class="mono" style="white-space:pre-wrap;overflow:auto;max-height:420px;">${h(typeof value === "string" ? value : j(value))}</pre>`;
  }
  function badge(text, kind = "") {
    return `<span class="badge ${kind}">${h(text)}</span>`;
  }
  function listItems(items, render) {
    if (!items || !items.length) return `<div class="empty-state">暂无数据</div>`;
    return `<div class="card-list">${items.map(render).join("")}</div>`;
  }
  function setContent(content, html) {
    if (!content) content = document.getElementById("content");
    if (!content) return;
    content.innerHTML = html;
  }
  function showError(content, title, err) {
    setContent(
      content,
      shell(
        "页面加载失败",
        title,
        card("错误信息", mono(err && err.stack ? err.stack : String(err || "unknown error")))
      )
    );
  }
  function sendToPreview(title, data, type = "json") {
    if (typeof window.previewText === "function") {
      window.previewText(title, typeof data === "string" ? data : j(data), type);
    } else {
      console.log("[preview]", title, data);
    }
  }
  async function renderSimpleListPage(content, cfg) {
    setContent(content, shell(cfg.title, cfg.subtitle, card("加载中", `<div class="mono">正在读取 ${h(cfg.url)}</div>`)));
    try {
      const data = await getJson(cfg.url);
      const items = data.items || data.workflows || data.skills || data.artifacts || data.repos || data.designs || [];
      setContent(
        content,
        shell(
          cfg.title,
          cfg.subtitle,
          `
          <div class="page-grid">
            ${card("状态", `
              ${badge("接口正常", "badge-enterprise")}
              ${badge(`数量：${items.length}`)}
              <button class="btn-soft" onclick="${cfg.reloadFn}(document.getElementById('content'))">刷新</button>
              <button class="btn-soft" onclick="stableSendPreview('${h(cfg.title)}', ${h(JSON.stringify(JSON.stringify(data)))})">发送到预览</button>
            `)}
            ${card("列表", listItems(items, cfg.renderItem))}
          </div>
          `
        )
      );
    } catch (err) {
      showError(content, cfg.title, err);
    }
  }
  window.stableSendPreview = function (title, encoded) {
    try {
      const data = JSON.parse(encoded);
      sendToPreview(title, data, "json");
    } catch {
      sendToPreview(title, encoded, "text");
    }
  };
  window.renderSkillsPage = async function renderSkillsPage(content) {
    return renderSimpleListPage(content, {
      title: "技能商店",
      subtitle: "管理 SKILL.md、技能启用状态和 Agent 绑定。",
      url: `${API_BASE.skill}/list`,
      reloadFn: "renderSkillsPage",
      renderItem: (x) => `
        <div class="mini-card">
          <b>${h(x.name || x.id)}</b><br/>
          ${badge(x.status || "unknown")}
          ${badge(x.version || "-")}
          <div class="mono">${h(x.description || "")}</div>
        </div>
      `,
    });
  };
  window.renderWorkflowsPage = async function renderWorkflowsPage(content) {
    return renderSimpleListPage(content, {
      title: "工作流",
      subtitle: "管理工作流模板、节点、边和运行时需求。",
      url: `${API_BASE.workflow}/list`,
      reloadFn: "renderWorkflowsPage",
      renderItem: (x) => `
        <div class="mini-card">
          <b>${h(x.name || x.id)}</b><br/>
          ${badge(x.version || "-")}
          ${badge((x.nodes || []).length + " nodes")}
          ${badge((x.edges || []).length + " edges")}
          <div class="mono">${h(x.description || "")}</div>
        </div>
      `,
    });
  };
  window.renderArtifactsPage = async function renderArtifactsPage(content) {
    return renderSimpleListPage(content, {
      title: "产物中心",
      subtitle: "查看执行结果、报告、补丁、图片、安装包等产物。",
      url: `${API_BASE.artifact}/list`,
      reloadFn: "renderArtifactsPage",
      renderItem: (x) => `
        <div class="mini-card">
          <b>${h(x.name || x.id)}</b><br/>
          ${badge(x.type || "artifact")}
          ${badge(x.lifecycle || "active")}
          <div class="mono">${h(x.path || x.source || "")}</div>
        </div>
      `,
    });
  };
  window.renderRepoMemoryPage = async function renderRepoMemoryPage(content) {
    return renderSimpleListPage(content, {
      title: "仓库记忆",
      subtitle: "沉淀仓库结构、修复历史、知识条目和上下文快照。",
      url: `${API_BASE.repoMemory}/repo/list`,
      reloadFn: "renderRepoMemoryPage",
      renderItem: (x) => `
        <div class="mini-card">
          <b>${h(x.name || x.id)}</b><br/>
          ${(x.tags || []).map(t => badge(t)).join(" ")}
          <div class="mono">${h(x.path || x.description || "")}</div>
        </div>
      `,
    });
  };
  window.renderCodeReviewPage = async function renderCodeReviewPage(content) {
    setContent(
      content,
      shell(
        "代码审查",
        "检测危险命令、密钥泄露、动态执行、路径穿越等风险。",
        `
        <div class="page-grid">
          ${card("输入 Diff / 代码片段", `
            <textarea id="stableCodeDiff" class="field" style="min-height:220px;width:100%;" placeholder="粘贴 git diff 或代码片段..."></textarea>
            <div style="margin-top:10px;">
              <button class="btn-primary" onclick="stableReviewCode()">执行审查</button>
              <button class="btn-soft" onclick="renderCodeReviewPage(document.getElementById('content'))">清空</button>
            </div>
          `)}
          ${card("审查结果", `<div id="stableCodeReviewResult" class="mono">暂无</div>`)}
        </div>
        `
      )
    );
  };
  window.stableReviewCode = async function stableReviewCode() {
    const box = document.getElementById("stableCodeReviewResult");
    const diff = document.getElementById("stableCodeDiff")?.value || "";
    if (!diff.trim()) {
      box.innerHTML = "请输入 diff 或代码片段。";
      return;
    }
    box.innerHTML = "正在审查...";
    try {
      const data = await postJson(`${API_BASE.codeReview}/review_diff`, { diff });
      box.innerHTML = mono(data);
      sendToPreview("代码审查结果", data, "json");
    } catch (err) {
      box.innerHTML = mono(err.stack || String(err));
    }
  };
  window.renderDesignSystemPage = async function renderDesignSystemPage(content) {
    return renderSimpleListPage(content, {
      title: "设计系统",
      subtitle: "管理 DESIGN.md、UI Tokens、组件规范和品牌风格。",
      url: `${API_BASE.designSystem}/list`,
      reloadFn: "renderDesignSystemPage",
      renderItem: (x) => `
        <div class="mini-card">
          <b>${h(x.name || x.id)}</b><br/>
          ${badge(x.version || "-")}
          ${badge((x.components || []).length + " components")}
          <div class="mono">${h(x.description || x.brand?.name || "")}</div>
        </div>
      `,
    });
  };
  window.renderModelsPage = async function renderModelsPage(content) {
    let models = [];
    let profiles = [];
    try {
      const [m, p] = await Promise.all([
        fetch("./../manifests/model_registry/models_catalog.json").then(r => r.json()).catch(() => []),
        fetch("./../manifests/model_registry/device_profiles.json").then(r => r.json()).catch(() => []),
      ]);
      models = Array.isArray(m) ? m : [];
      profiles = Array.isArray(p) ? p : [];
    } catch {}
    setContent(
      content,
      shell(
        "模型设置",
        "P4 模型注册、下载、校验和 Gateway v2 的入口。",
        `
        <div class="page-grid">
          ${card("设备档位", listItems(profiles, p => `
            <div class="mini-card">
              <b>${h(p.name || p.id)}</b><br/>
              ${badge(p.id || "-")}
              <div class="mono">${h(p.description || "")}</div>
            </div>
          `))}
          ${card("模型目录", listItems(models, m => `
            <div class="mini-card">
              <b>${h(m.name || m.id)}</b><br/>
              ${badge(m.type || "-")}
              ${badge(m.size || m.size_gb || "-")}
              <div class="mono">${h(m.description || m.recommended_reason || "")}</div>
            </div>
          `))}
        </div>
        `
      )
    );
  };
  window.renderLaunchPage = async function renderLaunchPage(content) {
    setContent(
      content,
      shell(
        "启动中心",
        "桌面服务启动、停止和状态检查命令。",
        `
        <div class="page-grid">
          ${card("常用命令", mono(`# 启动服务
bash scripts/desktop/start_desktop_services.sh
# 停止服务
bash scripts/desktop/stop_desktop_services.sh
# 查看状态
bash scripts/desktop/status_desktop_services.sh
# 健康验收
bash scripts/acceptance/p3_14_d4_a_desktop_services_health_check.sh`))}
        </div>
        `
      )
    );
  };
  window.renderBrainPage = async function renderBrainPage(content) {
    if (typeof window.refreshHealth === "function") {
      await window.refreshHealth();
    }
    setContent(
      content,
      shell(
        "大脑状态",
        "查看本地 AI 工作台核心服务状态。",
        card("提示", "请在右侧检查器的「服务」页签查看完整健康状态。")
      )
    );
  };
  window.renderDocumentsPage = async function renderDocumentsPage(content) {
    setContent(
      content,
      shell(
        "文档处理",
        "文档摄取、分块、缓存和后续 RAG 能力入口。",
        `
        <div class="page-grid">
          ${card("文本摄取测试", `
            <textarea id="stableDocText" class="field" style="min-height:180px;width:100%;" placeholder="输入要摄取的文本..."></textarea>
            <button class="btn-primary" onclick="stableIngestText()">摄取文本</button>
          `)}
          ${card("结果", `<div id="stableDocResult" class="mono">暂无</div>`)}
        </div>
        `
      )
    );
  };
  window.stableIngestText = async function stableIngestText() {
    const text = document.getElementById("stableDocText")?.value || "";
    const box = document.getElementById("stableDocResult");
    if (!text.trim()) {
      box.innerHTML = "请输入文本。";
      return;
    }
    box.innerHTML = "正在摄取...";
    try {
      const data = await postJson("http://127.0.0.1:18120/ingest_text_test", { text });
      box.innerHTML = mono(data);
      sendToPreview("文档摄取结果", data, "json");
    } catch (err) {
      box.innerHTML = mono(err.stack || String(err));
    }
  };
  window.renderSettingsPage = async function renderSettingsPage(content) {
    setContent(
      content,
      shell(
        "设置",
        "审批模式、共享学习、模型默认值等配置入口。",
        card("当前设置", `
          ${badge("人工审批")}
          ${badge("共享学习 ON")}
          ${badge("qwen2.5:7b")}
        `)
      )
    );
  };
  async function stableSendMessage() {
    const input =
      document.getElementById("composerInput") ||
      document.querySelector("textarea") ||
      document.querySelector('input[type="text"]');
    const text = String(input?.value || "").trim();
    if (!text) return;
    if (input) input.value = "";
    const content = document.getElementById("content");
    setContent(
      content,
      shell(
        "任务执行",
        text,
        card("状态", `<div id="stableTaskResult" class="mono">正在路由任务...</div>`)
      )
    );
    const box = document.getElementById("stableTaskResult");
    try {
      const route = await postJson(`${API_BASE.autoRouter}/route`, { prompt: text, task: text });
      box.innerHTML = mono({ step: "route", result: route });
      let runtime = null;
      try {
        runtime = await postJson(`${API_BASE.runtime}/execute`, {
          task: text,
          prompt: text,
          dry_run: true,
          route,
          metadata: { source: "desktop-runtime-stable" },
        });
      } catch (e) {
        runtime = { ok: false, error: String(e) };
      }
      box.innerHTML = mono({ route, runtime });
      sendToPreview("任务执行结果", { route, runtime }, "json");
    } catch (err) {
      box.innerHTML = mono(err.stack || String(err));
    }
  }
  window.sendMessage = stableSendMessage;
  window.robustSendMessage = stableSendMessage;
  function bindSend() {
    const button =
      document.getElementById("sendButton") ||
      Array.from(document.querySelectorAll("button")).find(b => (b.textContent || "").trim() === "发送");
    const input =
      document.getElementById("composerInput") ||
      document.querySelector("textarea") ||
      document.querySelector('input[type="text"]');
    if (button && !button.__stableSendBound) {
      button.__stableSendBound = true;
      button.addEventListener("click", e => {
        e.preventDefault();
        e.stopPropagation();
        stableSendMessage();
      });
    }
    if (input && !input.__stableEnterBound) {
      input.__stableEnterBound = true;
      input.addEventListener("keydown", e => {
        if (e.key === "Enter" && !e.shiftKey) {
          e.preventDefault();
          stableSendMessage();
        }
      });
    }
  }
  document.addEventListener("DOMContentLoaded", bindSend);
  setTimeout(bindSend, 200);
  setTimeout(bindSend, 1000);
  console.log("[desktop-runtime-stable] loaded");
})();
