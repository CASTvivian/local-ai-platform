// P3.14-D3-X4-B extracted Repo Memory page

function renderRepoMemoryPage(content) {
  content.innerHTML = pageHero("Repo Memory", "18125：仓库记忆、修复历史、上下文快照、知识搜索。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr auto;gap:10px;align-items:center;">
        <input class="field" id="repoMemory搜索" placeholder="搜索 repo 名称 / path / tag / service" oninput="renderRepoMemoryList()" />
        <input class="field" id="repoMemoryTagFilter" placeholder="Tag 过滤，例如 p3" oninput="renderRepoMemoryList()" />
        <input class="field" id="repoMemoryServiceFilter" placeholder="Service 过滤，例如 18125" oninput="renderRepoMemoryList()" />
        <button class="btn-primary" onclick="loadRepoMemoryPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>注册 Repo</h2>
        <input class="field" id="repoName" placeholder="Repo 名称，例如 core-platform" />
        <input class="field" id="repoPath" placeholder="Repo 路径，例如 /Users/.../core-platform" />
        <textarea class="field" id="repoDesc" placeholder="Repo 描述"></textarea>
        <input class="field" id="repo标签" placeholder="tags，逗号分隔，例如 p3,desktop,backend" />
        <input class="field" id="repoServices" placeholder="services，逗号分隔，例如 18120,18125,18126" />
        <button class="btn-primary" onclick="registerRepoMemory()">注册 Repo</button>
        <div id="repo注册Result" class="mono" style="margin-top:12px;"></div>
      </div>
      <div class="page-card">
        <h2>Repo 详情</h2>
        <div id="repoMemory详情" class="mono">请选择一个 Repo。</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>Repo 列表</h2>
        <div id="repoMemoryList" class="card-list">加载中...</div>
      </div>
      <div class="page-card">
        <h2>记录 Fix</h2>
        <input class="field" id="fixTitle" placeholder="修复标题，例如 修复 18120 ingest_text_test 500" />
        <textarea class="field" id="fixProblem" placeholder="问题描述"></textarea>
        <textarea class="field" id="fixSolution" placeholder="解决方案"></textarea>
        <input class="field" id="fixFiles" placeholder="变更文件，逗号分隔" />
        <input class="field" id="fixTests" placeholder="测试命令，逗号分隔" />
        <select class="field" id="fixResult">
          <option value="success">success</option>
          <option value="partial">partial</option>
          <option value="failed">failed</option>
        </select>
        <button class="btn-primary" onclick="recordRepoFix()">记录 Fix</button>
      </div>
      <div class="page-card">
        <h2>Context Snapshot</h2>
        <input class="field" id="snapshotTitle" placeholder="快照标题，例如 P3.14-D3 当前状态" />
        <textarea class="field" id="snapshot摘要" placeholder="上下文摘要"></textarea>
        <input class="field" id="snapshotFiles" placeholder="相关文件，逗号分隔" />
        <input class="field" id="snapshotServices" placeholder="相关服务，逗号分隔" />
        <button class="btn-soft" onclick="saveRepoSnapshot()">保存 Snapshot</button>
        <button class="btn-primary" onclick="compressRepoContext()">Compress Context</button>
        <div id="repoContextResult" class="mono" style="margin-top:12px;"></div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>Knowledge Base</h2>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">
          <div>
            <input class="field" id="knowledgeTitle" placeholder="知识标题，例如 Workflow Store 持久化问题" />
            <input class="field" id="knowledgeCategory" placeholder="分类，例如 bugfix / architecture / ops" />
            <input class="field" id="knowledge标签" placeholder="tags，逗号分隔" />
            <textarea class="field" id="knowledgeContent" placeholder="知识内容"></textarea>
            <button class="btn-primary" onclick="addRepoKnowledge()">添加知识</button>
          </div>
          <div>
            <input class="field" id="knowledgeQuery" placeholder="搜索知识，例如 store.json 持久化" />
            <button class="btn-soft" onclick="searchRepoKnowledge()">搜索知识</button>
            <div id="knowledge搜索Result" class="card-list" style="margin-top:12px;">暂无搜索结果</div>
          </div>
        </div>
      </div>
    </div>`;
  loadRepoMemoryPage();
}

function getRepoDisplayFields(x) {
  return {
    id: x.id || "",
    name: x.name || x.id || "Untitled Repo",
    path: x.path || "",
    description: x.description || "",
    tags: x.tags || [],
    services: x.services || [],
    created_at: x.created_at || "",
    updated_at: x.updated_at || "",
  };
}

function renderRepoMemoryList() {
  const box = document.getElementById("repoMemoryList");
  if (!box) return;
  const q = (document.getElementById("repoMemory搜索")?.value || "").toLowerCase().trim();
  const tagFilter = (document.getElementById("repoMemoryTagFilter")?.value || "").toLowerCase().trim();
  const serviceFilter = (document.getElementById("repoMemoryServiceFilter")?.value || "").toLowerCase().trim();
  let items = repoMemoryPageItems || [];
  items = items.filter(x => {
    const f = getRepoDisplayFields(x);
    const text = JSON.stringify(f).toLowerCase();
    if (q && !text.includes(q)) return false;
    if (tagFilter) {
      const tagsText = (f.tags || []).join(",").toLowerCase();
      if (!tagsText.includes(tagFilter)) return false;
    }
    if (serviceFilter) {
      const svcText = (f.services || []).join(",").toLowerCase();
      if (!svcText.includes(serviceFilter)) return false;
    }
    return true;
  });
  if (!items.length) {
    box.textContent = "暂无匹配 Repo";
    return;
  }
  box.innerHTML = items.map(x => {
    const f = getRepoDisplayFields(x);
    const active = selectedRepoId === f.id ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(f.name)}</b><br/>
        <span class="mono">${escapeHtml(f.id)}</span><br/>
        ${f.description ? `<div style="margin-top:6px;">${escapeHtml(f.description)}</div>` : ""}
        ${f.path ? `<div class="mono" style="margin-top:6px;">${escapeHtml(f.path)}</div>` : ""}
        ${(f.tags || []).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join("")}
        ${(f.services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectRepoMemory('${f.id}')">详情</button>
          <button class="btn-soft" onclick="loadRepoFixes('${f.id}')">Fixes</button>
          <button class="btn-soft" onclick="compressRepoContext('${f.id}')">Compress</button>
        </div>
      </div>
    `;
  }).join("");
}

function commaList(id) {
  return (document.getElementById(id)?.value || "")
    .split(",")
    .map(x => x.trim())
    .filter(Boolean);
}

async function registerRepoMemory() {
  const box = document.getElementById("repo注册Result");
  if (box) box.textContent = "registering...";
  try {
    const payload = {
      name: document.getElementById("repoName").value.trim(),
      path: document.getElementById("repoPath").value.trim(),
      description: document.getElementById("repoDesc").value.trim(),
      tags: commaList("repo标签"),
      services: commaList("repoServices"),
    };
    const json = await postJson(`${API.repoMemory}/repo/register`, payload);
    if (box) box.textContent = JSON.stringify(json, null, 2);
    await loadRepoMemoryPage();
    const id = json.item?.id || json.repo?.id || json.id;
    if (id) await selectRepoMemory(id);
    systemMessage("Repo 已注册：" + (payload.name || ""));
  } catch (e) {
    if (box) box.textContent = "register repo failed: " + e.message;
  }
}

async function selectRepoMemory(id) {
  selectedRepoId = id;
  renderRepoMemoryList();
  const box = document.getElementById("repoMemory详情");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.repoMemory}/repo/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    const item = json.item || json.repo || json;
    const f = getRepoDisplayFields(item);
    const fixes = await fetch(`${API.repoMemory}/fix/list?repo_id=${encodeURIComponent(id)}`, { signal: AbortSignal.timeout(8000) })
      .then(r => r.json())
      .catch(e => ({ ok:false, error:e.message, items:[] }));
    if (box) {
      box.innerHTML = `
        <div><b>${escapeHtml(f.name)}</b></div>
        <div class="mono" style="margin:8px 0;">${escapeHtml(f.id)}</div>
        ${f.description ? `<div>${escapeHtml(f.description)}</div>` : ""}
        ${f.path ? `<div class="mono" style="margin-top:8px;">${escapeHtml(f.path)}</div>` : ""}
        ${(f.tags || []).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join("")}
        ${(f.services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
        <h3 style="margin-top:16px;">Fix History</h3>
        <div class="card-list">
          ${(fixes.items || fixes.fixes || []).length ? (fixes.items || fixes.fixes || []).map(fix => `
            <div class="mini-card">
              <b>${escapeHtml(fix.title || fix.id)}</b>
              <span class="badge">${escapeHtml(fix.result || "unknown")}</span><br/>
              <div>${escapeHtml(fix.problem || "")}</div>
              <div class="mono">${escapeHtml((fix.files_changed || []).join(", "))}</div>
            </div>
          `).join("") : "暂无 Fix 记录"}
        </div>
        <h3 style="margin-top:16px;">Raw</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(item, null, 2))}</pre>
      `;
    }
  } catch (e) {
    if (box) box.textContent = "load repo detail failed: " + e.message;
  }
}

async function loadRepoFixes(id) {
  selectedRepoId = id;
  await selectRepoMemory(id);
}

async function recordRepoFix() {
  if (!selectedRepoId) {
    systemMessage("请先选择 Repo");
    return;
  }
  try {
    const payload = {
      repo_id: selectedRepoId,
      title: document.getElementById("fixTitle").value.trim(),
      problem: document.getElementById("fixProblem").value.trim(),
      solution: document.getElementById("fixSolution").value.trim(),
      files_changed: commaList("fixFiles"),
      tests_run: commaList("fixTests"),
      result: document.getElementById("fixResult").value,
    };
    const json = await postJson(`${API.repoMemory}/fix/record`, payload);
    systemMessage("Fix 已记录：" + (json.item?.title || payload.title));
    await selectRepoMemory(selectedRepoId);
  } catch (e) {
    systemMessage("记录 Fix 失败：" + e.message);
  }
}

async function saveRepoSnapshot() {
  if (!selectedRepoId) {
    systemMessage("请先选择 Repo");
    return;
  }
  const box = document.getElementById("repoContextResult");
  if (box) box.textContent = "saving snapshot...";
  try {
    const payload = {
      repo_id: selectedRepoId,
      title: document.getElementById("snapshotTitle").value.trim(),
      summary: document.getElementById("snapshot摘要").value.trim(),
      files: commaList("snapshotFiles"),
      services: commaList("snapshotServices"),
    };
    const json = await postJson(`${API.repoMemory}/context/snapshot`, payload);
    if (box) box.textContent = JSON.stringify(json, null, 2);
    systemMessage("Context Snapshot 已保存");
  } catch (e) {
    if (box) box.textContent = "snapshot failed: " + e.message;
  }
}

async function compressRepoContext(id = null) {
  const repoId = id || selectedRepoId;
  if (!repoId) {
    systemMessage("请先选择 Repo");
    return;
  }
  const box = document.getElementById("repoContextResult");
  if (box) box.textContent = "compressing...";
  try {
    const json = await postJson(`${API.repoMemory}/context/compress`, {
      repo_id: repoId,
      max_chars: 3000,
    });
    if (box) box.textContent = JSON.stringify(json, null, 2);
    previewText("Repo Context Compress: " + repoId, JSON.stringify(json, null, 2), "json");
  } catch (e) {
    if (box) box.textContent = "compress failed: " + e.message;
  }
}

async function addRepoKnowledge() {
  const repoId = selectedRepoId || "";
  try {
    const payload = {
      repo_id: repoId,
      title: document.getElementById("knowledgeTitle").value.trim(),
      category: document.getElementById("knowledgeCategory").value.trim() || "general",
      content: document.getElementById("knowledgeContent").value.trim(),
      tags: commaList("knowledge标签"),
      source: "desktop_ui",
    };
    const json = await postJson(`${API.repoMemory}/knowledge/add`, payload);
    systemMessage("知识已添加：" + (json.item?.title || payload.title));
    await searchRepoKnowledge();
  } catch (e) {
    systemMessage("添加知识失败：" + e.message);
  }
}

async function searchRepoKnowledge() {
  const box = document.getElementById("knowledge搜索Result");
  if (box) box.textContent = "searching...";
  try {
    const query = document.getElementById("knowledgeQuery").value.trim();
    const json = await postJson(`${API.repoMemory}/knowledge/search`, {
      query,
      repo_id: selectedRepoId || "",
      limit: 20,
    });
    const items = json.items || json.results || [];
    repoMemoryKnowledgeItems = items;
    if (box) {
      box.innerHTML = items.length ? items.map(k => `
        <div class="mini-card">
          <b>${escapeHtml(k.title || k.id)}</b>
          <span class="badge">${escapeHtml(k.category || "general")}</span><br/>
          <div>${escapeHtml(k.content || "")}</div>
          ${(k.tags || []).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join("")}
          <div style="margin-top:8px;">
            <button class="btn-soft" onclick='previewText(${JSON.stringify("Knowledge: " + (k.title || k.id))}, ${JSON.stringify(k.content || JSON.stringify(k, null, 2))}, "markdown")'>预览</button>
          </div>
        </div>
      `).join("") : "暂无知识结果";
    }
  } catch (e) {
    if (box) box.textContent = "search failed: " + e.message;
  }
}

