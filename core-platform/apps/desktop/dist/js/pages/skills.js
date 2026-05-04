// P3.14-D3-X4-A extracted Skill Store page

function renderSkillsPage(content) {
  content.innerHTML = pageHero("Skill Store", "18121：技能安装、搜索、Agent 标签、启用/禁用、SKILL.md 预览。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr auto;gap:10px;align-items:center;">
        <input class="field" id="skill搜索" placeholder="搜索技能名称 / ID / source / tags / agents" oninput="renderSkillPageList()" />
        <select class="field" id="skill启用dFilter" onchange="renderSkillPageList()">
          <option value="">全部状态</option>
          <option value="enabled">enabled</option>
          <option value="disabled">disabled</option>
        </select>
        <input class="field" id="skillAgentFilter" placeholder="Agent 标签，例如 codex" oninput="renderSkillPageList()" />
        <button class="btn-primary" onclick="loadSkillsPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>安装 SKILL.md</h2>
        <textarea class="field" id="skillMdText" style="min-height:220px;" placeholder="# code-review-basic
version: 0.2.0
description: 代码审查基础技能
agents: codex,aider,claude-code
tags: code,review,safety

## Instructions
检查 diff 中的危险命令、secret 泄漏和测试建议。"></textarea>
        <button class="btn-soft" onclick="parseSkillMd()">解析</button>
        <button class="btn-primary" onclick="installSkillMd()">安装技能</button>
        <div id="skillParseResult" class="mono" style="margin-top:12px;"></div>
      </div>
      <div class="page-card">
        <h2>技能详情</h2>
        <div id="skillPage详情" class="mono">请选择一个技能。</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>技能列表</h2>
        <div id="skillsList" class="card-list">加载中...</div>
      </div>
    </div>`;
  loadSkillsPage();
}

function loadSkills() {
  return loadSkillsPage();
}

async function loadSkillsPage() {
  const box = document.getElementById("skillsList");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.skill}/list`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    skillPageItems = json.items || json.skills || [];
    renderSkillPageList();
  } catch (e) {
    if (box) box.textContent = "load skills failed: " + e.message;
  }
}

function getSkillDisplayFields(x) {
  const payload = x.payload || {};
  const agents = payload.agents || payload.agent_tags || x.agents || [];
  const tags = payload.tags || x.tags || [];
  const signature = payload.signature_status || x.signature_status || "unsigned";
  return {
    id: x.id || "",
    name: x.name || payload.name || x.id || "Untitled Skill",
    version: x.version || payload.version || "0.1.0",
    source: x.source || payload.source || "unknown",
    enabled: x.enabled !== false,
    description: payload.description || x.description || "",
    agents,
    tags,
    signature_status: signature,
    raw: payload.raw || x.raw || JSON.stringify(x, null, 2),
    created_at: x.created_at || "",
    updated_at: x.updated_at || "",
  };
}

function renderSkillPageList() {
  const box = document.getElementById("skillsList");
  if (!box) return;
  const q = (document.getElementById("skill搜索")?.value || "").toLowerCase().trim();
  const enabledFilter = document.getElementById("skill启用dFilter")?.value || "";
  const agentFilter = (document.getElementById("skillAgentFilter")?.value || "").toLowerCase().trim();
  let items = skillPageItems || [];
  items = items.filter(x => {
    const f = getSkillDisplayFields(x);
    const text = JSON.stringify(f).toLowerCase();
    if (q && !text.includes(q)) return false;
    if (enabledFilter === "enabled" && !f.enabled) return false;
    if (enabledFilter === "disabled" && f.enabled) return false;
    if (agentFilter) {
      const agentsText = (f.agents || []).join(",").toLowerCase();
      if (!agentsText.includes(agentFilter)) return false;
    }
    return true;
  });
  if (!items.length) {
    box.textContent = "暂无匹配技能";
    return;
  }
  box.innerHTML = items.map(x => {
    const f = getSkillDisplayFields(x);
    const active = selectedSkillId === f.id ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(f.name)}</b><br/>
        <span class="mono">${escapeHtml(f.id)}</span><br/>
        ${f.description ? `<div style="margin-top:6px;">${escapeHtml(f.description)}</div>` : ""}
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">${f.enabled ? "enabled" : "disabled"}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        <span class="badge">signature:${escapeHtml(f.signature_status)}</span>
        ${(f.agents || []).map(a => `<span class="badge">agent:${escapeHtml(a)}</span>`).join("")}
        ${(f.tags || []).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join("")}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectSkill('${f.id}')">详情</button>
          <button class="btn-soft" onclick="enableSkill('${f.id}')">启用</button>
          <button class="btn-soft" onclick="disableSkill('${f.id}')">禁用</button>
          <button class="btn-soft" onclick='previewText(${JSON.stringify("SKILL.md: " + f.name)}, ${JSON.stringify(f.raw)}, "markdown")'>预览</button>
        </div>
      </div>
    `;
  }).join("");
}

async function selectSkill(id) {
  selectedSkillId = id;
  renderSkillPageList();
  const box = document.getElementById("skillPage详情");
  if (box) box.textContent = "加载中...";
  try {
    let json = null;
    try {
      const res = await fetch(`${API.skill}/skill/${id}`, { signal: AbortSignal.timeout(8000) });
      json = await res.json();
    } catch (_) {
      json = { ok: false };
    }
    let item = json.item || json.skill || null;
    if (!item) {
      item = (skillPageItems || []).find(x => (x.id || "") === id);
    }
    if (!item) {
      if (box) box.textContent = "skill not found: " + id;
      return;
    }
    const f = getSkillDisplayFields(item);
    if (box) {
      box.innerHTML = `
        <div><b>${escapeHtml(f.name)}</b></div>
        <div class="mono" style="margin:8px 0;">${escapeHtml(f.id)}</div>
        ${f.description ? `<div>${escapeHtml(f.description)}</div>` : ""}
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">${f.enabled ? "enabled" : "disabled"}</span>
        <span class="badge">${escapeHtml(f.source)}</span>
        <span class="badge">signature:${escapeHtml(f.signature_status)}</span>
        ${(f.agents || []).map(a => `<span class="badge">agent:${escapeHtml(a)}</span>`).join("")}
        ${(f.tags || []).map(t => `<span class="badge">${escapeHtml(t)}</span>`).join("")}
        <div style="margin-top:12px;">
          <button class="btn-soft" onclick="enableSkill('${f.id}')">启用</button>
          <button class="btn-soft" onclick="disableSkill('${f.id}')">禁用</button>
          <button class="btn-soft" onclick='previewText(${JSON.stringify("SKILL.md: " + f.name)}, ${JSON.stringify(f.raw)}, "markdown")'>发送到 预览</button>
        </div>
        <h3 style="margin-top:16px;">SKILL.md / Raw</h3>
        <pre class="mono">${escapeHtml(f.raw)}</pre>
        <h3 style="margin-top:16px;">元数据</h3>
        <pre class="mono">${escapeHtml(JSON.stringify(item, null, 2))}</pre>
      `;
    }
  } catch (e) {
    if (box) box.textContent = "load skill detail failed: " + e.message;
  }
}

async function parseSkillMd() {
  const text = document.getElementById("skillMdText").value || "";
  const box = document.getElementById("skillParseResult");
  box.textContent = "parsing...";
  try {
    const json = await postJson(`${API.skill}/parse_skill_md`, { text });
    box.textContent = JSON.stringify(json, null, 2);
  } catch (e) {
    box.textContent = "parse failed: " + e.message;
  }
}

async function installSkillMd() {
  const text = document.getElementById("skillMdText").value || "";
  const box = document.getElementById("skillParseResult");
  box.textContent = "installing...";
  try {
    const json = await postJson(`${API.skill}/install_skill_md`, { text, source: "desktop_ui" });
    box.textContent = JSON.stringify(json, null, 2);
    await loadSkillsPage();
    if (json.item?.id) await selectSkill(json.item.id);
    systemMessage("Skill 已安装：" + (json.item?.name || ""));
  } catch (e) {
    box.textContent = "install failed: " + e.message;
  }
}

async function disableSkill(id) {
  await postJson(`${API.skill}/disable/${id}`, {});
  await loadSkillsPage();
  await selectSkill(id);
}

async function enableSkill(id) {
  await postJson(`${API.skill}/enable/${id}`, {});
  await loadSkillsPage();
  await selectSkill(id);
}