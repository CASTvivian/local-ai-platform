// P3.14-D3-X3-C extracted inspector module
function switchInspector(name) {
  const sections = ["services", "trace", "policy", "artifacts", "preview", "eval"];
  for (const s of sections) {
    const el = document.getElementById("inspector-" + s);
    if (el) el.classList.toggle("hidden", s !== name);
  }
  for (const btn of document.querySelectorAll(".tab")) {
    btn.classList.remove("active");
  }
  const labels = {
    services: "Services",
    trace: "Trace",
    policy: "Policy",
    artifacts: "Artifacts",
    preview: "Preview",
    eval: "Eval"
  };
  for (const btn of document.querySelectorAll(".tab")) {
    if (btn.textContent.trim() === labels[name]) btn.classList.add("active");
  }
}

function previewText(title, text, type="text") {
  const box = document.getElementById("previewBox");
  if (!box) return;
  if (type === "markdown") {
    box.textContent = "# " + title + "\\n\\n" + text;
  } else if (type === "diff") {
    box.textContent = "DIFF PREVIEW:\\n\\n" + text;
  } else {
    box.textContent = title + "\\n\\n" + text;
  }
  switchInspector("preview");
}

async function previewArtifact(raw) {
  try {
    const item = JSON.parse(raw);
    const name = item.name || item.id || "Artifact";
    const payload = item.payload || item;
    const path = item.path || payload.path || "";
    const type = item.type || payload.type || "json";
    let body = "";
    if (type === "diff") {
      body = payload.content || payload.diff || JSON.stringify(item, null, 2);
      previewText(name, body, "diff");
    } else if (type === "report" || path.endsWith(".md")) {
      body = payload.content || JSON.stringify(item, null, 2);
      previewText(name, body, "markdown");
    } else {
      body = JSON.stringify(item, null, 2);
      previewText(name, body, "json");
    }
    await loadArtifactFileStatus(item.id);
  } catch (e) {
    previewText("Artifact Preview Error", e.message);
  }
}

async function loadArtifacts() {
  const box = document.getElementById("artifactBox");
  box.textContent = "loading...";
  try {
    let json;
    try {
      const res = await fetch(`${API.artifact}/list`, { signal: AbortSignal.timeout(5000) });
      json = await res.json();
    } catch (_) {
      const res = await fetch(`${API.artifact}/recent`, { signal: AbortSignal.timeout(5000) });
      json = await res.json();
    }
    const items = json.items || json.artifacts || [];
    if (!items.length) {
      box.textContent = JSON.stringify(json, null, 2);
      return;
    }
    box.innerHTML = items.map((x, idx) => {
      const name = x.name || x.id || ("artifact_" + idx);
      const type = x.type || x.payload?.type || "unknown";
      const path = x.path || x.payload?.path || "";
      return `<div class="artifact-item" onclick='previewArtifact(${JSON.stringify(JSON.stringify(x))})'>
        <b>${escapeHtml(name)}</b><br/>
        <span>${escapeHtml(type)}</span><br/>
        <span>${escapeHtml(path)}</span>
      </div>`;
    }).join("");
  } catch (e) {
    box.textContent = "Artifact load failed: " + e.message;
  }
}

async function loadArtifactFileStatus(itemId) {
  try {
    const res = await fetch(`${API.artifact}/artifact/${itemId}/file_status`, { signal: AbortSignal.timeout(5000) });
    const json = await res.json();
    const box = document.getElementById("previewBox");
    const wrap = document.createElement("div");
    wrap.style.marginTop = "14px";
    const info = document.createElement("div");
    info.className = "mono";
    info.textContent = "FILE STATUS:\\n" + JSON.stringify(json, null, 2);
    wrap.appendChild(info);
    const actions = document.createElement("div");
    actions.className = "task-actions";
    actions.style.padding = "12px 0 0 0";
    const path = json.path || "";
    const openBtn = document.createElement("button");
    openBtn.className = "btn-soft";
    openBtn.textContent = "打开文件";
    openBtn.disabled = !json.exists;
    openBtn.onclick = () => openArtifactPath(path);
    const revealBtn = document.createElement("button");
    revealBtn.className = "btn-soft";
    revealBtn.textContent = "在文件夹中显示";
    revealBtn.disabled = !json.exists;
    revealBtn.onclick = () => revealArtifactPath(path);
    const copyBtn = document.createElement("button");
    copyBtn.className = "btn-soft";
    copyBtn.textContent = "复制路径";
    copyBtn.disabled = !path;
    copyBtn.onclick = () => navigator.clipboard.writeText(path);
    actions.appendChild(openBtn);
    actions.appendChild(revealBtn);
    actions.appendChild(copyBtn);
    wrap.appendChild(actions);
    box.appendChild(wrap);
  } catch (e) {
    console.warn("file status failed", e);
  }
}

async function runEval() {
  const box = document.getElementById("evalBox");
  box.textContent = "running eval...";
  try {
    const res = await fetch(`${API.eval}/run`, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({}),
      signal: AbortSignal.timeout(60000)
    });
    const json = await res.json();
    box.textContent = formatEvalResult(json);
    switchInspector("eval");
  } catch (e) {
    box.textContent = "Eval failed: " + e.message;
  }
}

async function loadTrace(traceId) {
  try {
    const res = await fetch(`${API.trace}/timeline/${traceId}`);
    const json = await res.json();
    document.getElementById("traceBox").textContent = formatTraceTimeline(json);
    switchInspector("trace");
  } catch (e) {
    document.getElementById("traceBox").textContent = "Trace load failed: " + e.message;
  }
}

function renderMarkdown(md) {
  const lines = String(md || "").split(/\n/);
  return lines.map(line => {
    if (line.startsWith("### ")) return `<h3>${escapeHtml(line.slice(4))}</h3>`;
    if (line.startsWith("## ")) return `<h2>${escapeHtml(line.slice(3))}</h2>`;
    if (line.startsWith("# ")) return `<h1>${escapeHtml(line.slice(2))}</h1>`;
    if (line.trim().startsWith("- ")) return `<div>• ${escapeHtml(line.trim().slice(2))}</div>`;
    return `<p>${escapeHtml(line)}</p>`;
  }).join("");
}

function renderDiff(diff) {
  return `<pre class="mono diff-view">${String(diff || "").split(/\n/).map(line => {
    const cls = line.startsWith("+") ? "diff-add" : line.startsWith("-") ? "diff-del" : line.startsWith("@@") ? "diff-meta" : "";
    return `<span class="${cls}">${escapeHtml(line)}</span>`;
  }).join("\n")}</pre>`;
}

function setPolicyPanel(policy) {
  const box = document.getElementById("policyBox");
  if (!box) return;
  box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(policy || {}, null, 2))}</pre>`;
}

function setTracePanel(trace) {
  const box = document.getElementById("traceBox");
  if (!box) return;
  box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(trace || {}, null, 2))}</pre>`;
}
