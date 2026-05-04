// P3.14-D3-X4-A extracted Artifacts page

function renderArtifactsPage(content) {
  content.innerHTML = pageHero("Artifacts", "18123：产物登记、搜索、过滤、生命周期、文件状态、打开/定位。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr auto;gap:10px;align-items:center;">
        <input class="field" id="artifact搜索" placeholder="搜索产物名称 / ID / source / path" oninput="renderArtifactPageList()" />
        <select class="field" id="artifactTypeFilter" onchange="renderArtifactPageList()">
          <option value="">全部类型</option>
          <option value="execution_result">execution_result</option>
          <option value="report">report</option>
          <option value="diff">diff</option>
          <option value="document">document</option>
          <option value="image">image</option>
          <option value="video">video</option>
          <option value="audio">audio</option>
          <option value="json">json</option>
        </select>
        <select class="field" id="artifact生命周期Filter" onchange="renderArtifactPageList()">
          <option value="">全部生命周期</option>
          <option value="draft">draft</option>
          <option value="active">active</option>
          <option value="archived">archived</option>
          <option value="deleted">deleted</option>
        </select>
        <button class="btn-primary" onclick="loadArtifactsPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>产物列表</h2>
        <div id="artifactPageList" class="card-list">加载中...</div>
      </div>
      <div class="page-card">
        <h2>产物详情</h2>
        <div id="artifactPage详情" class="mono">请选择一个产物。</div>
      </div>
    </div>`;
  switchInspector("artifacts");
  loadArtifactsPage();
}

async function loadArtifactsPage() {
  const list = document.getElementById("artifactPageList");
  if (list) list.textContent = "加载中...";
  try {
    let json;
    try {
      const res = await fetch(`${API.artifact}/list`, { signal: AbortSignal.timeout(8000) });
      json = await res.json();
    } catch (_) {
      const res = await fetch(`${API.artifact}/recent`, { signal: AbortSignal.timeout(8000) });
      json = await res.json();
    }
    artifactPageItems = json.items || json.artifacts || [];
    renderArtifactPageList();
    // 同步右侧 inspector
    if (document.getElementById("artifactBox")) {
      await loadArtifacts();
    }
  } catch (e) {
    if (list) list.textContent = "load artifacts failed: " + e.message;
  }
}

function getArtifactDisplayFields(x) {
  const payload = x.payload || {};
  return {
    id: x.id || payload.id || "",
    name: x.name || payload.name || x.id || "Untitled Artifact",
    type: x.type || payload.type || "unknown",
    source: x.source || payload.source || "unknown",
    lifecycle: x.lifecycle || payload.lifecycle || "active",
    path: x.path || payload.path || "",
    trace_id: x.trace_id || payload.trace_id || "",
    run_id: x.run_id || payload.run_id || "",
    created_at: x.created_at || payload.created_at || "",
  };
}

function renderArtifactPageList() {
  const box = document.getElementById("artifactPageList");
  if (!box) return;
  const q = (document.getElementById("artifact搜索")?.value || "").toLowerCase().trim();
  const typeFilter = document.getElementById("artifactTypeFilter")?.value || "";
  const lifecycleFilter = document.getElementById("artifact生命周期Filter")?.value || "";
  let items = artifactPageItems || [];
  items = items.filter(x => {
    const f = getArtifactDisplayFields(x);
    const text = JSON.stringify(f).toLowerCase();
    if (q && !text.includes(q)) return false;
    if (typeFilter && f.type !== typeFilter) return false;
    if (lifecycleFilter && f.lifecycle !== lifecycleFilter) return false;
    return true;
  });
  if (!items.length) {
    box.textContent = "暂无匹配产物";
    return;
  }
  box.innerHTML = items.map(x => {
    const f = getArtifactDisplayFields(x);
    const active = selectedArtifactId === f.id ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(f.name)}</b><br/>
        <span class="mono">${escapeHtml(f.id)}</span><br/>
        <span class="badge">${escapeHtml(f.type)}</span>
        <span class="badge">${escapeHtml(f.lifecycle)}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        ${f.path ? `<div class="mono" style="margin-top:6px;">${escapeHtml(f.path)}</div>` : ""}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectArtifact('${f.id}')">详情</button>
          <button class="btn-soft" onclick='previewArtifact(${JSON.stringify(JSON.stringify(x))})'>预览</button>
          <button class="btn-soft" onclick="changeArtifact生命周期('${f.id}', 'active')">Active</button>
          <button class="btn-soft" onclick="changeArtifact生命周期('${f.id}', 'archived')">Archive</button>
        </div>
      </div>
    `;
  }).join("");
}

async function selectArtifact(id) {
  selectedArtifactId = id;
  renderArtifactPageList();
  const box = document.getElementById("artifactPage详情");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.artifact}/artifact/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    const item = json.item || json.artifact || json;
    const f = getArtifactDisplayFields(item);
    let file状态 = {};
    try {
      const fsRes = await fetch(`${API.artifact}/artifact/${id}/file_status`, { signal: AbortSignal.timeout(5000) });
      file状态 = await fsRes.json();
    } catch (e) {
      file状态 = { ok: false, error: e.message };
    }
    if (box) {
      box.innerHTML = `
        <div><b>${escapeHtml(f.name)}</b></div>
        <div class="mono" style="margin:8px 0;">${escapeHtml(f.id)}</div>
        <span class="badge">${escapeHtml(f.type)}</span>
        <span class="badge">${escapeHtml(f.lifecycle)}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        <div style="margin-top:12px;">
          <button class="btn-soft" onclick='previewArtifact(${JSON.stringify(JSON.stringify(item))})'>发送到 预览</button>
          <button class="btn-soft" onclick="changeArtifact生命周期('${f.id}', 'active')">设为 Active</button>
          <button class="btn-soft" onclick="changeArtifact生命周期('${f.id}', 'archived')">归档</button>
          <button class="btn-soft" onclick="changeArtifact生命周期('${f.id}', 'deleted')">删除标记</button>
        </div>
        <h3 style="margin-top:16px;">File 状态</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(file状态, null, 2))}</pre>
        <div class="task-actions" style="padding:8px 0;">
          <button class="btn-soft" ${file状态.exists ? "" : "disabled"} onclick="openArtifactPath('${escapeJs(file状态.path || "")}')">打开文件</button>
          <button class="btn-soft" ${file状态.exists ? "" : "disabled"} onclick="revealArtifactPath('${escapeJs(file状态.path || "")}')">在文件夹中显示</button>
          <button class="btn-soft" ${file状态.path ? "" : "disabled"} onclick="navigator.clipboard.writeText('${escapeJs(file状态.path || "")}')">复制路径</button>
        </div>
        <h3 style="margin-top:16px;">Raw</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(item, null, 2))}</pre>
      `;
    }
  } catch (e) {
    if (box) box.textContent = "load detail failed: " + e.message;
  }
}

async function changeArtifact生命周期(id, lifecycle) {
  try {
    const res = await fetch(`${API.artifact}/artifact/${id}/lifecycle`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ lifecycle }),
      signal: AbortSignal.timeout(8000)
    });
    const json = await res.json();
    if (!json.ok) throw new Error(JSON.stringify(json));
    systemMessage(`产物 ${id} 已更新生命周期为 ${lifecycle}`);
    await loadArtifactsPage();
    await selectArtifact(id);
  } catch (e) {
    systemMessage("更新产物生命周期失败：" + e.message);
  }
}