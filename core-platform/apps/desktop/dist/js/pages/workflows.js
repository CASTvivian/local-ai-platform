// P3.14-D3-X4-A extracted Workflow Store page

function renderWorkflowsPage(content) {
  content.innerHTML = pageHero("Workflows", "18126：工作流模板、JSON 导入导出、Dry-run、运行时需求、节点计划。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr auto;gap:10px;align-items:center;">
        <input class="field" id="workflow搜索" placeholder="搜索工作流名称 / ID / source / service / model" oninput="renderWorkflowPageList()" />
        <input class="field" id="workflowServiceFilter" placeholder="服务过滤，例如 18120" oninput="renderWorkflowPageList()" />
        <input class="field" id="workflowModelFilter" placeholder="模型过滤，例如 qwen" oninput="renderWorkflowPageList()" />
        <button class="btn-primary" onclick="loadWorkflowsPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>注册 / 导入工作流 JSON</h2>
        <textarea class="field" id="workflowJsonText" style="min-height:280px;" placeholder='{
  "name": "rag-report-flow",
  "version": "0.3.1",
  "description": "企业级RAG报告工作流",
  "source": "desktop_ui",
  "nodes": [
    {"id":"start","type":"start","name":"Start"},
    {"id":"retrieve","type":"document_retrieval","name":"Retrieve Documents","config":{"top_k":5}},
    {"id":"model","type":"model_invocation","name":"Generate Report","config":{"model":"qwen2.5:7b"}},
    {"id":"end","type":"end","name":"End"}
  ],
  "edges": [
    {"id":"e1","source":"start","target":"retrieve"},
    {"id":"e2","source":"retrieve","target":"model"},
    {"id":"e3","source":"model","target":"end"}
  ],
  "runtime_requirements": {
    "services": ["18120","18125","18104"],
    "models": ["qwen2.5:7b","nomic-embed-text"],
    "tools": ["document_ingestion","runtime_execution"],
    "permissions": ["read_documents"],
    "estimated_timeout_sec": 600
  }
}'></textarea>
        <button class="btn-soft" onclick="validateWorkflowJson()">验证 JSON</button>
        <button class="btn-primary" onclick="registerWorkflowJson()">注册工作流</button>
        <button class="btn-soft" onclick="importWorkflowJson()">作为导入工作流</button>
        <div id="workflowActionResult" class="mono" style="margin-top:12px;"></div>
      </div>
      <div class="page-card">
        <h2>工作流详情</h2>
        <div id="workflowPage详情" class="mono">请选择一个工作流。</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>工作流列表</h2>
        <div id="workflowList" class="card-list">加载中...</div>
      </div>
    </div>`;
  loadWorkflowsPage();
}

function loadWorkflows() {
  return loadWorkflowsPage();
}

async function loadWorkflowsPage() {
  const box = document.getElementById("workflowList");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.workflow}/list`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    workflowPageItems = json.items || json.workflows || [];
    renderWorkflowPageList();
  } catch (e) {
    if (box) box.textContent = "load workflows failed: " + e.message;
  }
}

function getWorkflowDisplayFields(x) {
  const def = x.definition || x.workflow || x;
  const runtime = def.runtime_requirements || {};
  const nodes = def.nodes || [];
  const edges = def.edges || [];
  return {
    id: x.id || def.id || "",
    name: x.name || def.name || x.id || "Untitled Workflow",
    version: x.version || def.version || "0.1.0",
    description: x.description || def.description || "",
    source: x.source || def.source || "unknown",
    enabled: x.enabled !== false,
    nodes,
    edges,
    services: runtime.services || [],
    models: runtime.models || [],
    tools: runtime.tools || [],
    permissions: runtime.permissions || [],
    timeout: runtime.estimated_timeout_sec || 300,
    definition: def,
  };
}

function renderWorkflowPageList() {
  const box = document.getElementById("workflowList");
  if (!box) return;
  const q = (document.getElementById("workflow搜索")?.value || "").toLowerCase().trim();
  const serviceFilter = (document.getElementById("workflowServiceFilter")?.value || "").toLowerCase().trim();
  const modelFilter = (document.getElementById("workflowModelFilter")?.value || "").toLowerCase().trim();
  let items = workflowPageItems || [];
  items = items.filter(x => {
    const f = getWorkflowDisplayFields(x);
    const text = JSON.stringify(f).toLowerCase();
    if (q && !text.includes(q)) return false;
    if (serviceFilter) {
      const serviceText = (f.services || []).join(",").toLowerCase();
      if (!serviceText.includes(serviceFilter)) return false;
    }
    if (modelFilter) {
      const modelText = (f.models || []).join(",").toLowerCase();
      if (!modelText.includes(modelFilter)) return false;
    }
    return true;
  });
  if (!items.length) {
    box.textContent = "暂无匹配工作流";
    return;
  }
  box.innerHTML = items.map(x => {
    const f = getWorkflowDisplayFields(x);
    const active = selectedWorkflowId === f.id ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(f.name)}</b><br/>
        <span class="mono">${escapeHtml(f.id)}</span><br/>
        ${f.description ? `<div style="margin-top:6px;">${escapeHtml(f.description)}</div>` : ""}
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        <span class="badge">${f.enabled ? "enabled" : "disabled"}</span>
        <span class="badge">nodes:${f.nodes.length}</span>
        <span class="badge">edges:${f.edges.length}</span>
        ${(f.services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
        ${(f.models || []).map(m => `<span class="badge">model:${escapeHtml(m)}</span>`).join("")}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectWorkflow('${f.id}')">详情</button>
          <button class="btn-soft" onclick="dryRunWorkflow('${f.id}')">Dry-run</button>
          <button class="btn-soft" onclick="exportWorkflow('${f.id}')">导出 JSON</button>
          <button class="btn-soft" onclick='previewText(${JSON.stringify("Workflow: " + f.name)}, ${JSON.stringify(JSON.stringify(f.definition, null, 2))}, "json")'>预览</button>
        </div>
      </div>
    `;
  }).join("");
}

async function selectWorkflow(id) {
  selectedWorkflowId = id;
  renderWorkflowPageList();
  const box = document.getElementById("workflowPage详情");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.workflow}/get/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    const item = json.item || json.workflow || json;
    const f = getWorkflowDisplayFields(item);
    if (box) {
      box.innerHTML = `
        <div><b>${escapeHtml(f.name)}</b></div>
        <div class="mono" style="margin:8px 0;">${escapeHtml(f.id)}</div>
        ${f.description ? `<div>${escapeHtml(f.description)}</div>` : ""}
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        <span class="badge">timeout:${escapeHtml(f.timeout)}</span>
        <h3 style="margin-top:16px;">Runtime Requirements</h3>
        <div>
          ${(f.services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
          ${(f.models || []).map(m => `<span class="badge">model:${escapeHtml(m)}</span>`).join("")}
          ${(f.tools || []).map(t => `<span class="badge">tool:${escapeHtml(t)}</span>`).join("")}
          ${(f.permissions || []).map(p => `<span class="badge">perm:${escapeHtml(p)}</span>`).join("")}
        </div>
        <h3 style="margin-top:16px;">Nodes</h3>
        <div class="card-list">
          ${f.nodes.map(n => `
            <div class="mini-card">
              <b>${escapeHtml(n.name || n.id)}</b><br/>
              <span class="mono">${escapeHtml(n.id)}</span>
              <span class="badge">${escapeHtml(n.type)}</span>
              <pre class="mono">${escapeHtml(JSON.stringify(n.config || {}, null, 2))}</pre>
            </div>
          `).join("")}
        </div>
        <h3 style="margin-top:16px;">Edges</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(f.edges, null, 2))}</pre>
        <div style="margin-top:12px;">
          <button class="btn-soft" onclick="dryRunWorkflow('${f.id}')">Dry-run</button>
          <button class="btn-soft" onclick="exportWorkflow('${f.id}')">导出到 预览</button>
          <button class="btn-soft" onclick='previewText(${JSON.stringify("Workflow: " + f.name)}, ${JSON.stringify(JSON.stringify(f.definition, null, 2))}, "json")'>预览定义</button>
        </div>
      `;
    }
  } catch (e) {
    if (box) box.textContent = "load workflow detail failed: " + e.message;
  }
}

function getWorkflowJsonInput() {
  const box = document.getElementById("workflowJsonText");
  if (!box) throw new Error("workflowJsonText not found");
  const raw = box.value.trim();
  if (!raw) throw new Error("请输入 Workflow JSON");
  return JSON.parse(raw);
}

async function validateWorkflowJson() {
  const box = document.getElementById("workflowActionResult");
  if (box) box.textContent = "validating...";
  try {
    const workflow = getWorkflowJsonInput();
    const res = await postJson(`${API.workflow}/validate`, workflow);
    if (box) box.textContent = JSON.stringify(res, null, 2);
  } catch (e) {
    if (box) box.textContent = "validate failed: " + e.message;
  }
}

async function registerWorkflowJson() {
  const box = document.getElementById("workflowActionResult");
  if (box) box.textContent = "registering...";
  try {
    const workflow = getWorkflowJsonInput();
    const res = await postJson(`${API.workflow}/register`, workflow);
    if (box) box.textContent = JSON.stringify(res, null, 2);
    await loadWorkflowsPage();
    const id = res.item?.id;
    if (id) await selectWorkflow(id);
    systemMessage("Workflow 已注册：" + (res.item?.name || ""));
  } catch (e) {
    if (box) box.textContent = "register failed: " + e.message;
  }
}

async function importWorkflowJson() {
  const box = document.getElementById("workflowActionResult");
  if (box) box.textContent = "importing...";
  try {
    const workflow = getWorkflowJsonInput();
    const res = await postJson(`${API.workflow}/import`, { workflow, source: "desktop_import" });
    if (box) box.textContent = JSON.stringify(res, null, 2);
    await loadWorkflowsPage();
    const id = res.item?.id;
    if (id) await selectWorkflow(id);
    systemMessage("Workflow 已导入：" + (res.item?.name || ""));
  } catch (e) {
    if (box) box.textContent = "import failed: " + e.message;
  }
}

async function dryRunWorkflow(id) {
  const box = document.getElementById("workflowPage详情");
  try {
    const res = await postJson(`${API.workflow}/dry_run`, {
      workflow_id: id,
      input: {
        source: "desktop_ui",
        session_id: currentSession().id,
      }
    });
    previewText("Workflow Dry-run: " + id, JSON.stringify(res, null, 2), "json");
    if (box) {
      const current = box.innerHTML;
      box.innerHTML = current + `
        <h3 style="margin-top:16px;">Dry-run Result</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(res, null, 2))}</pre>
      `;
    }
  } catch (e) {
    systemMessage("Workflow dry-run failed: " + e.message);
  }
}

async function exportWorkflow(id) {
  try {
    const res = await fetch(`${API.workflow}/export/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    previewText("Workflow 导出: " + id, JSON.stringify(json.workflow || json, null, 2), "json");
  } catch (e) {
    systemMessage("Workflow export failed: " + e.message);
  }
}

function registerWorkflow() {
  return registerWorkflowJson();
}