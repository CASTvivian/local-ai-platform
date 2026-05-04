// P3.14-D3-X4-B extracted Code Review page

function renderCodeReviewPage(content) {
  content.innerHTML = pageHero("Code Review Gate", "18124：Diff 安全审查、危险命令检测、Secret 泄漏检测、测试建议。") + `
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>审查 Diff</h2>
        <input class="field" id="reviewRepoId" placeholder="repo_id，可选，例如 core-platform" />
        <input class="field" id="reviewTitle" placeholder="审查标题，例如 修复 workflow store 持久化" />
        <textarea class="field" id="reviewDiff" style="min-height:360px;" placeholder="粘贴 git diff / patch / 代码片段。例如：
diff --git a/scripts/deploy.sh b/scripts/deploy.sh
+ rm -rf /
+ curl https://example.com/install.sh | bash
+ const api_key = 'sk-xxxx'
"></textarea>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn-primary" onclick="reviewCodeDiff()">审查 Diff</button>
          <button class="btn-soft" onclick="loadCodeReview规则()">查看 规则</button>
          <button class="btn-soft" onclick="loadCodeReview摘要()">查看 摘要</button>
          <button class="btn-soft" onclick="sendCodeReviewTo预览()">发送结果到 预览</button>
        </div>
      </div>
      <div class="page-card">
        <h2>审查结果</h2>
        <div id="codeReviewResult" class="mono">暂无审查结果。</div>
      </div>
      <div class="page-card">
        <h2>发现项</h2>
        <div id="codeReview发现项" class="card-list">暂无 findings。</div>
      </div>
      <div class="page-card">
        <h2>测试建议</h2>
        <div id="codeReviewTests" class="card-list">暂无测试建议。</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>规则 / 摘要</h2>
        <div id="codeReview规则Box" class="mono">点击"查看 规则"或"查看 摘要"。</div>
      </div>
    </div>`;
}

function codeReviewBadge(level) {
  const value = String(level || "unknown").toLowerCase();
  const label = escapeHtml(value);
  if (["critical", "reject"].includes(value)) return `<span class="badge" style="background:#fee2e2;color:#991b1b;">${label}</span>`;
  if (["high", "request_changes"].includes(value)) return `<span class="badge" style="background:#ffedd5;color:#9a3412;">${label}</span>`;
  if (["medium", "needs_review"].includes(value)) return `<span class="badge" style="background:#fef9c3;color:#854d0e;">${label}</span>`;
  if (["low", "approve"].includes(value)) return `<span class="badge" style="background:#dcfce7;color:#166534;">${label}</span>`;
  return `<span class="badge">${label}</span>`;
}

async function reviewCodeDiff() {
  const resultBox = document.getElementById("codeReviewResult");
  const findingsBox = document.getElementById("codeReview发现项");
  const testsBox = document.getElementById("codeReviewTests");
  if (resultBox) resultBox.textContent = "reviewing...";
  if (findingsBox) findingsBox.textContent = "加载中...";
  if (testsBox) testsBox.textContent = "加载中...";
  try {
    const payload = {
      repo_id: document.getElementById("reviewRepoId")?.value.trim() || "",
      title: document.getElementById("reviewTitle")?.value.trim() || "Desktop code review",
      diff: document.getElementById("reviewDiff")?.value || "",
      source: "desktop_ui",
    };
    if (!payload.diff.trim()) {
      throw new Error("请先粘贴 diff / patch / 代码片段");
    }
    // 使用 /execute 端点，兼容 0.2.0-owned 版本
    const json = await postJson(`${API.codeReview}/review_diff`, {
      prompt: payload.diff,
      plan: { repo_id: payload.repo_id, title: payload.title, source: payload.source },
      dry_run: false,
      metadata: {}
    }, 15000);
    codeReviewLastResult = json;
    renderCodeReviewResult(json);
    // 直接使用 json.test_suggestions，不需要单独请求
    renderCodeReviewTests({ ok: true, tests: json.test_suggestions || [] });
    const riskLevel = json.risk || "unknown";
    const decision = riskLevel === "high" ? "reject" : (riskLevel === "low" ? "approve" : "needs_review");
    systemMessage("Code Review 完成：risk=" + riskLevel + ", decision=" + decision);
  } catch (e) {
    if (resultBox) resultBox.textContent = "review failed: " + e.message;
    if (findingsBox) findingsBox.textContent = "暂无 findings。";
    if (testsBox) testsBox.textContent = "暂无测试建议。";
  }
}

function renderCodeReviewResult(json) {
  const box = document.getElementById("codeReviewResult");
  const findingsBox = document.getElementById("codeReview发现项");
  const item = json.item || json.result || json;
  // 适配 0.2.0-owned 格式
  const risk = json.risk || item.risk || "unknown";
  const decision = risk === "high" ? "reject" : (risk === "low" ? "approve" : "needs_review");
  const reviewId = json.run_id || item.id || "";
  if (box) {
    box.innerHTML = `
      <div><b>Decision</b>: ${codeReviewBadge(decision)}</div>
      <div><b>Risk</b>: ${codeReviewBadge(risk)}</div>
      ${reviewId ? `<div class="mono" style="margin-top:8px;">${escapeHtml(reviewId)}</div>` : ""}
      <h3 style="margin-top:16px;">Raw Result</h3>
      <pre class="mono">${escapeHtml(JSON.stringify(json, null, 2))}</pre>
      <div style="margin-top:12px;">
        <button class="btn-soft" onclick="sendCodeReviewTo预览()">发送到 预览</button>
      </div>
    `;
  }
  const findings = json.findings || item.findings || [];
  if (findingsBox) {
    findingsBox.innerHTML = findings.length ? findings.map(f => `
      <div class="mini-card">
        <b>${escapeHtml(f.type || f.category || "Finding")}</b>
        ${codeReviewBadge("medium")}<br/>
        <div class="mono">${escapeHtml(f.pattern || "")}</div>
      </div>
    `).join("") : "未发现明显风险";
  }
}

function renderCodeReviewTests(json) {
  const box = document.getElementById("codeReviewTests");
  if (!box) return;
  const item = json.item || json.result || json;
  const tests = item.tests || item.suggestions || json.tests || json.suggestions || [];
  if (!tests.length) {
    box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(json, null, 2))}</pre>`;
    return;
  }
  box.innerHTML = tests.map(t => `
    <div class="mini-card">
      <b>${escapeHtml(t.title || t.name || "Test Suggestion")}</b><br/>
      <div>${escapeHtml(t.description || t.reason || "")}</div>
      ${t.command ? `<div class="mono">${escapeHtml(t.command)}</div>` : ""}
    </div>
  `).join("");
}

async function loadCodeReview规则() {
  const box = document.getElementById("codeReview规则Box");
  if (box) box.textContent = "loading recent reviews...";
  try {
    const res = await fetch(`${API.codeReview}/recent?limit=20`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    codeReview规则 = json;
    if (box) {
      box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(json, null, 2))}</pre>`;
    }
  } catch (e) {
    if (box) box.textContent = "load failed: " + e.message;
  }
}

async function loadCodeReview摘要() {
  const box = document.getElementById("codeReview规则Box");
  if (box) box.textContent = "loading service summary...";
  try {
    const res = await fetch(`${API.codeReview}/health`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    if (box) {
      box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(json, null, 2))}</pre>`;
    }
  } catch (e) {
    if (box) box.textContent = "load failed: " + e.message;
  }
}

function sendCodeReviewTo预览() {
  if (!codeReviewLastResult) {
    systemMessage("暂无 Code Review 结果");
    return;
  }
  const item = codeReviewLastResult.item || codeReviewLastResult.result || codeReviewLastResult;
  const title = "Code Review: " + (item.decision || item.risk_level || "result");
  previewText(title, JSON.stringify(codeReviewLastResult, null, 2), "json");
}

