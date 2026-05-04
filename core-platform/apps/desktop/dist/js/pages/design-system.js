// P3.14-D3-X4-B extracted Design System page

function renderDesignSystemPage(content) {
  content.innerHTML = pageHero("Design System", "18127：DESIGN.md 解析、UI Tokens、组件规范、品牌风格、AI 前端生成约束。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1.4fr 0.8fr 0.8fr auto;gap:10px;align-items:center;">
        <input class="field" id="designSystem搜索" placeholder="搜索设计系统名称 / brand / component / token" oninput="renderDesignSystemList()" />
        <input class="field" id="designSystemComponentFilter" placeholder="组件过滤，例如 button" oninput="renderDesignSystemList()" />
        <input class="field" id="designSystemTokenFilter" placeholder="Token过滤，例如 primary" oninput="renderDesignSystemList()" />
        <button class="btn-primary" onclick="loadDesignSystemsPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>解析 / 注册 DESIGN.md</h2>
        <textarea class="field" id="designMdText" style="min-height:360px;" placeholder="---
name: MAOMIAI Desktop
version: 0.3.1
brand: MAOMIAI
style: clean-enterprise
---
# MAOMIAI Desktop Design System
## Brand
primary: #2563eb
accent: #7c3aed
font: Inter, system-ui
radius: 16px
shadow: soft
## Colors
primary: #2563eb
surface: #ffffff
muted: #f8fafc
danger: #dc2626
success: #16a34a
## Spacing
xs: 4px
sm: 8px
md: 16px
lg: 24px
xl: 32px
## Components
### Button
Use rounded corners, clear hover state, visible disabled state.
### Card
Use soft shadow, 16px radius, 20px padding.
### Input
Use clear border, focus ring, consistent height.
### Modal
Use backdrop, centered content, explicit cancel/confirm actions.
### Table
Use sticky header, compact rows, visible empty state.
"></textarea>
        <div style="display:flex;gap:8px;flex-wrap:wrap;">
          <button class="btn-soft" onclick="parseDesignMd()">解析 DESIGN.md</button>
          <button class="btn-primary" onclick="registerDesignSystem()">注册 Design System</button>
          <button class="btn-soft" onclick="clearDesignMd()">清空</button>
        </div>
        <div id="designActionResult" class="mono" style="margin-top:12px;"></div>
      </div>
      <div class="page-card">
        <h2>Design System 详情</h2>
        <div id="designSystem详情" class="mono">请选择一个设计系统。</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>Design Systems</h2>
        <div id="designSystemList" class="card-list">加载中...</div>
      </div>
      <div class="page-card">
        <h2>Suggest UI</h2>
        <input class="field" id="suggestComponent" placeholder="组件类型，例如 button / card / modal / table" />
        <textarea class="field" id="suggestContext" placeholder="使用场景，例如：为模型下载页面生成主按钮和状态卡片"></textarea>
        <button class="btn-primary" onclick="suggestDesignUi()">生成 UI 建议</button>
      </div>
      <div class="page-card">
        <h2>UI 建议结果</h2>
        <div id="designSuggestionResult" class="mono">暂无建议。</div>
      </div>
    </div>`;
  loadDesignSystemsPage();
}

async function loadDesignSystemsPage() {
  const box = document.getElementById("designSystemList");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.designSystem}/list`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    designSystemPageItems = json.items || json.design_systems || json.systems || [];
    renderDesignSystemList();
  } catch (e) {
    if (box) box.textContent = "load design systems failed: " + e.message;
  }
}

function getDesignSystemDisplayFields(x) {
  const payload = x.payload || {};
  const tokens = x.tokens || payload.tokens || {};
  const components = x.components || payload.components || [];
  const brand = x.brand || payload.brand || {};
  const meta = x.metadata || payload.metadata || {};
  const componentNames = Array.isArray(components)
    ? components.map(c => c.name || c.type || c.id || "").filter(Boolean)
    : Object.keys(components || {});
  const tokenText = JSON.stringify(tokens || {});
  return {
    id: x.id || payload.id || "",
    name: x.name || payload.name || meta.name || x.id || "Untitled Design System",
    version: x.version || payload.version || meta.version || "0.1.0",
    brand_name: brand.name || meta.brand || x.brand_name || "unknown",
    style: x.style || meta.style || "",
    tokens,
    components,
    componentNames,
    tokenText,
    raw: x.raw || payload.raw || JSON.stringify(x, null,2),
    created_at: x.created_at || "",
    updated_at: x.updated_at || "",
  };
}

function renderDesignSystemList() {
  const box = document.getElementById("designSystemList");
  if (!box) return;
  const q = (document.getElementById("designSystem搜索")?.value || "").toLowerCase().trim();
  const componentFilter = (document.getElementById("designSystemComponentFilter")?.value || "").toLowerCase().trim();
  const tokenFilter = (document.getElementById("designSystemTokenFilter")?.value || "").toLowerCase().trim();
  let items = designSystemPageItems || [];
  items = items.filter(x => {
    const f = getDesignSystemDisplayFields(x);
    const text = JSON.stringify(f).toLowerCase();
    if (q && !text.includes(q)) return false;
    if (componentFilter) {
      const compText = (f.componentNames || []).join(",").toLowerCase();
      if (!compText.includes(componentFilter)) return false;
    }
    if (tokenFilter) {
      if (!String(f.tokenText || "").toLowerCase().includes(tokenFilter)) return false;
    }
    return true;
  });
  if (!items.length) {
    box.textContent = "暂无匹配设计系统";
    return;
  }
  box.innerHTML = items.map(x => {
    const f = getDesignSystemDisplayFields(x);
    const active = selectedDesignSystemId === f.id ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(f.name)}</b><br/>
        <span class="mono">${escapeHtml(f.id)}</span><br/>
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">brand:${escapeHtml(f.brand_name)}</span>
        ${f.style ? `<span class="badge">${escapeHtml(f.style)}</span>` : ""}
        ${(f.componentNames || []).slice(0, 8).map(c => `<span class="badge">cmp:${escapeHtml(c)}</span>`).join("")}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectDesignSystem('${f.id}')">详情</button>
          <button class="btn-soft" onclick="exportDesignSystem('${f.id}')">导出</button>
          <button class="btn-soft" onclick='previewText("Design System: ${f.name}", ${JSON.stringify(JSON.stringify(f, null, 2))}, "json")'>预览</button>
        </div>
      </div>
    `;
  }).join("");
}

async function parseDesignMd() {
  const box = document.getElementById("designActionResult");
  if (box) box.textContent = "parsing...";
  try {
    const text = document.getElementById("designMdText")?.value || "";
    if (!text.trim()) throw new Error("请输入 DESIGN.md 内容");
    const json = await postJson(`${API.designSystem}/parse_design_md`, {
      text,
      source: "desktop_ui",
    }, 12000);
    if (box) box.textContent = JSON.stringify(json, null, 2);
    previewText("Parsed DESIGN.md", JSON.stringify(json, null, 2), "json");
  } catch (e) {
    if (box) box.textContent = "parse failed: " + e.message;
  }
}

async function registerDesignSystem() {
  const box = document.getElementById("designActionResult");
  if (box) box.textContent = "registering...";
  try {
    const text = document.getElementById("designMdText")?.value || "";
    if (!text.trim()) throw new Error("请输入 DESIGN.md 内容");
    // 先解析
    const parseRes = await postJson(`${API.designSystem}/parse_design_md`, {
      text,
      source: "desktop_ui",
    }, 12000);
    // 然后注册（适配 0.2.0-owned 格式）
    const name = parseRes.name || "Desktop Design System";
    const version = parseRes.version || "0.3.1";
    const json = await postJson(`${API.designSystem}/register`, {
      name,
      version,
      source: "desktop_ui",
      enabled: true,
      payload: {
        name,
        brand: parseRes.brand || "unknown",
        style: parseRes.style || "",
        colors: parseRes.colors || {},
        fonts: parseRes.fonts || {},
        spacing: parseRes.spacing || {},
        border_radius: parseRes.border_radius || {},
        components: parseRes.components || [],
        ui_constraints: parseRes.ui_constraints || {},
        raw: text,
      }
    }, 12000);
    if (box) box.textContent = JSON.stringify(json, null, 2);
    await loadDesignSystemsPage();
    const id = json.item?.id || json.id;
    if (id) await selectDesignSystem(id);
    systemMessage("Design System 已注册：" + name);
  } catch (e) {
    if (box) box.textContent = "register failed: " + e.message;
  }
}

async function selectDesignSystem(id) {
  selectedDesignSystemId = id;
  renderDesignSystemList();
  const box = document.getElementById("designSystem详情");
  if (box) box.textContent = "加载中...";
  try {
    const res = await fetch(`${API.designSystem}/design/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    const item = json.item || json.design || json;
    const payload = item.payload || {};
    const f = {
      id: item.id,
      name: item.name || payload.name || "Untitled Design System",
      version: item.version || payload.version || "0.1.0",
      brand_name: payload.brand || item.brand_name || "unknown",
      style: payload.style || item.style || "",
      tokens: {
        colors: payload.colors || {},
        fonts: payload.fonts || {},
        spacing: payload.spacing || {},
        border_radius: payload.border_radius || {},
      },
      components: payload.components || [],
      ui_constraints: payload.ui_constraints || {},
    };
    const tokens = f.tokens || {};
    const components = Array.isArray(f.components) ? f.components : [];
    if (box) {
      box.innerHTML = `
        <div><b>${escapeHtml(f.name)}</b></div>
        <div class="mono" style="margin:8px 0;">${escapeHtml(f.id)}</div>
        <span class="badge">${escapeHtml(f.version)}</span>
        <span class="badge">brand:${escapeHtml(f.brand_name)}</span>
        ${f.style ? `<span class="badge">${escapeHtml(f.style)}</span>` : ""}
        <h3 style="margin-top:16px;">Tokens</h3>
        ${renderDesignTokens(tokens)}
        <h3 style="margin-top:16px;">Components</h3>
        <div class="card-list">
          ${components.length ? components.map((c, i) => `
            <div class="mini-card">
              <b>${escapeHtml(c.name || c.type || "component_" + i)}</b><br/>
              <pre class="mono">${escapeHtml(JSON.stringify(c, null, 2))}</pre>
            </div>
          `).join("") : "暂无组件规范"}
        </div>
        <div style="margin-top:12px;">
          <button class="btn-soft" onclick="exportDesignSystem('${f.id}')">导出 to 预览</button>
          <button class="btn-soft" onclick='previewText("Design System Raw: ${f.name}", ${JSON.stringify(JSON.stringify(item, null, 2))}, "json")'>Raw 预览</button>
        </div>
      `;
    }
  } catch (e) {
    if (box) box.textContent = "load design system detail failed: " + e.message;
  }
}

function renderDesignTokens(tokens) {
  if (!tokens || !Object.keys(tokens).length) {
    return `<div class="mono">暂无 tokens</div>`;
  }
  const sections = Object.entries(tokens).map(([group, value]) => {
    if (typeof value === "object" && value !== null) {
      return `
        <div class="mini-card">
          <b>${escapeHtml(group)}</b>
          <div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px;">
            ${Object.entries(value).map(([k, v]) => {
              const val = String(v);
              const isColor = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i.test(val);
              return `
                <span class="badge" title="${escapeHtml(k + ': ' + val)}">
                  ${isColor ? `<span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:${escapeHtml(val)};margin-right:4px;border:1px solid #ddd;"></span>` : ""}
                  ${escapeHtml(k)}:${escapeHtml(val)}
                </span>
              `;
            }).join("")}
          </div>
        </div>
      `;
    }
    return `
      <div class="mini-card">
        <b>${escapeHtml(group)}</b>
        <span class="badge">${escapeHtml(String(value))}</span>
      </div>
    `;
  }).join("");
  return `<div class="card-list">${sections}</div>`;
}

async function exportDesignSystem(id) {
  try {
    const res = await fetch(`${API.designSystem}/export/${id}`, { signal: AbortSignal.timeout(8000) });
    const json = await res.json();
    previewText("Design System 导出: " + id, JSON.stringify(json.item || json.design || json, null, 2), "json");
  } catch (e) {
    systemMessage("Design System export failed: " + e.message);
  }
}

async function suggestDesignUi() {
  const box = document.getElementById("designSuggestionResult");
  if (box) box.textContent = "suggesting...";
  try {
    const component = document.getElementById("suggestComponent")?.value.trim() || "card";
    const context = document.getElementById("suggestContext")?.value.trim() || "";
    const json = await postJson(`${API.designSystem}/suggest_ui`, {
      design_id: selectedDesignSystemId || "",
      component,
      context,
      source: "desktop_ui",
    }, 12000);
    designSystemLastSuggestion = json;
    if (box) {
      box.innerHTML = `<pre class="mono">${escapeHtml(JSON.stringify(json, null, 2))}</pre>
      <div style="margin-top:12px;">
        <button class="btn-soft" onclick="sendDesignSuggestionTo预览()">发送到 预览</button>
      </div>`;
    }
  } catch (e) {
    if (box) box.textContent = "suggest failed: " + e.message;
  }
}

function sendDesignSuggestionTo预览() {
  if (!designSystemLastSuggestion) {
    systemMessage("暂无 UI 建议结果");
    return;
  }
  previewText("Design UI Suggestion", JSON.stringify(designSystemLastSuggestion, null, 2), "json");
}

function clearDesignMd() {
  const box = document.getElementById("designMdText");
  if (box) box.value = "";
}

