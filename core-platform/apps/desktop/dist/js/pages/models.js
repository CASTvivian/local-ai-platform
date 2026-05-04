// P3.14-D3-G Models / Model Setup / P4 Entry page
let modelCatalogItems = [];
let deviceProfileItems = [];
let selectedDeviceProfile = "mac_standard";
let selectedModelType = "all";

async function renderModelsPage(content) {
  content.innerHTML = pageHero("Models", "P4 入口：设备档位、模型组合、下载策略、模型网关 v2 准备。") + `
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <h2>选择设备档位</h2>
      <div id="deviceProfilesBox" class="card-list">加载中...</div>
    </div>
    <div class="page-card" style="max-width:1080px;margin:0 auto 16px;">
      <div style="display:grid;grid-template-columns:1fr 220px 220px auto;gap:10px;align-items:center;">
        <input class="field" id="model搜索" placeholder="搜索模型名称 / 用途 / 服务 / 类型" oninput="renderModelCards()" />
        <select class="field" id="modelTypeFilter" onchange="selectedModelType=this.value;renderModelCards()">
          <option value="all">全部类型</option>
          <option value="chat">Chat 通用对话</option>
          <option value="code">Code 代码模型</option>
          <option value="embedding">Embedding 向量模型</option>
          <option value="reranker">Reranker 重排模型</option>
          <option value="vision">Vision 多模态</option>
          <option value="tts">TTS 语音</option>
          <option value="video_3d">Video / 3D 高级</option>
        </select>
        <select class="field" id="profileFilter" onchange="selectedDeviceProfile=this.value;renderDeviceProfiles();renderModelCards();renderRecommendedStack()">
          <option value="windows_light">Windows 轻量</option>
          <option value="mac_standard" selected>Mac 标准</option>
          <option value="code">代码 Agent</option>
          <option value="rag">RAG 文档</option>
          <option value="tts">TTS 内容</option>
          <option value="high_performance">高性能服务器</option>
        </select>
        <button class="btn-primary" onclick="loadModelsPage()">刷新</button>
      </div>
    </div>
    <div class="page-grid" style="max-width:1080px;">
      <div class="page-card">
        <h2>推荐模型组合</h2>
        <div id="recommendedStackBox" class="card-list">加载中...</div>
      </div>
      <div class="page-card">
        <h2>模型类型说明</h2>
        <div class="card-list">
          <div class="mini-card"><b>Chat</b><br/>聊天、总结、规划、通用任务。</div>
          <div class="mini-card"><b>Code</b><br/>代码生成、修复、审查、仓库理解。</div>
          <div class="mini-card"><b>Embedding</b><br/>文档向量化，RAG 检索基础。</div>
          <div class="mini-card"><b>Reranker</b><br/>重排检索结果，提高知识库准确度。</div>
          <div class="mini-card"><b>Vision</b><br/>截图、图片、UI、文档图像理解。</div>
          <div class="mini-card"><b>TTS</b><br/>语音合成、日报播报、短视频配音。</div>
        </div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>模型目录</h2>
        <div id="modelCardsBox" class="card-list">加载中...</div>
      </div>
      <div class="page-card" style="grid-column:1 / -1;">
        <h2>P4 接入说明</h2>
        <div class="mono">
          当前页面是 P4 模型底座入口。<br/>
          本阶段不自动下载模型。真实下载将在 P4 接入：model_registry_service、model_downloader_service、model_gateway_v2。<br/>
          大模型、视频/3D 模型、高性能服务器模型必须用户手动确认。
        </div>
      </div>
    </div>`;
  await loadModelsPage();
}

async function loadModelsPage() {
  try {
    const [models, profiles] = await Promise.all([
      fetch("../../manifests/model_registry/models_catalog.json").then(r => r.json()),
      fetch("../../manifests/model_registry/device_profiles.json").then(r => r.json()),
    ]);
    modelCatalogItems = Array.isArray(models) ? models : (models.items || []);
    deviceProfileItems = Array.isArray(profiles) ? profiles : (profiles.items || []);
    renderDeviceProfiles();
    renderRecommendedStack();
    renderModelCards();
  } catch (e) {
    const box = document.getElementById("modelCardsBox");
    if (box) box.textContent = "load models failed: " + e.message;
  }
}

function renderDeviceProfiles() {
  const box = document.getElementById("deviceProfilesBox");
  if (!box) return;
  box.innerHTML = deviceProfileItems.map(p => {
    const active = p.id === selectedDeviceProfile ? "border-color:#174ea6;background:#f6f9ff;" : "";
    return `
      <div class="mini-card" style="${active}">
        <b>${escapeHtml(p.name)}</b>
        <span class="badge">${escapeHtml(p.ram || "")}</span>
        <span class="badge">${escapeHtml(p.gpu || "")}</span><br/>
        <div>${escapeHtml(p.description || "")}</div>
        ${(p.use_cases || []).map(x => `<span class="badge">${escapeHtml(x)}</span>`).join("")}
        <div style="margin-top:10px;">
          <button class="btn-soft" onclick="selectDeviceProfile('${p.id}')">选择</button>
        </div>
      </div>
    `;
  }).join("");
}

function selectDeviceProfile(id) {
  selectedDeviceProfile = id;
  const select = document.getElementById("profileFilter");
  if (select) select.value = id;
  renderDeviceProfiles();
  renderRecommendedStack();
  renderModelCards();
}

function renderRecommendedStack() {
  const box = document.getElementById("recommendedStackBox");
  if (!box) return;
  const profile = deviceProfileItems.find(x => x.id === selectedDeviceProfile);
  if (!profile) {
    box.textContent = "请选择设备档位";
    return;
  }
  const ids = profile.recommended_models || [];
  const models = ids.map(id => modelCatalogItems.find(m => m.id === id)).filter(Boolean);
  box.innerHTML = `
    <div class="mini-card">
      <b>${escapeHtml(profile.name)}</b><br/>
      <div>${escapeHtml(profile.description || "")}</div>
      <span class="badge">${escapeHtml(profile.ram || "")}</span>
      <span class="badge">${escapeHtml(profile.gpu || "")}</span>
    </div>
    ${models.map(renderModelMiniCard).join("")}
  `;
}

function renderModelCards() {
  const box = document.getElementById("modelCardsBox");
  if (!box) return;
  const q = (document.getElementById("model搜索")?.value || "").toLowerCase().trim();
  const type = selectedModelType || "all";
  const profile = selectedDeviceProfile || "mac_standard";
  let items = modelCatalogItems || [];
  items = items.filter(m => {
    const text = JSON.stringify(m).toLowerCase();
    if (type !== "all" && m.type !== type) return false;
    if (q && !text.includes(q)) return false;
    return true;
  });
  items.sort((a, b) => {
    const aa = (a.profile_tags || []).includes(profile) ? 0 : 1;
    const bb = (b.profile_tags || []).includes(profile) ? 0 : 1;
    return aa - bb;
  });
  if (!items.length) {
    box.textContent = "暂无匹配";
    return;
  }
  box.innerHTML = items.map(renderModelCard).join("");
}

function renderModelMiniCard(m) {
  return `
    <div class="mini-card">
      <b>${escapeHtml(m.name)}</b>
      <span class="badge">${escapeHtml(m.type)}</span>
      <span class="badge">${escapeHtml(m.size)}</span><br/>
      <div>${escapeHtml(m.description || "")}</div>
      <div style="margin-top:6px;">
        ${(m.connected_services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
      </div>
    </div>
  `;
}

function renderModelCard(m) {
  const recommended = (m.profile_tags || []).includes(selectedDeviceProfile);
  const advanced = ["video_3d"].includes(m.type) || (m.profile_tags || []).includes("advanced");
  return `
    <div class="mini-card" style="${recommended ? "border-color:#174ea6;background:#f6f9ff;" : ""}">
      <div style="display:flex;justify-content:space-between;gap:12px;align-items:flex-start;">
        <div>
          <b>${escapeHtml(m.name)}</b>
          ${recommended ? `<span class="badge" style="background:#dcfce7;color:#166534;">推荐</span>` : ""}
          ${advanced ? `<span class="badge" style="background:#ffedd5;color:#9a3412;">高级/需确认</span>` : ""}
          <span class="badge">${escapeHtml(m.type)}</span>
          <span class="badge">${escapeHtml(m.provider || "")}</span>
        </div>
        <button class="btn-soft" onclick="requestModelDownload('${escapeJs(m.id)}')">下载 / 配置</button>
      </div>
      <div style="margin-top:8px;">${escapeHtml(m.description || "")}</div>
      <div style="margin-top:8px;"><b>推荐理由：</b>${escapeHtml(m.recommended_reason || "")}</div>
      <div style="margin-top:8px;">
        <span class="badge">大小:${escapeHtml(m.size || "")}</span>
        <span class="badge">内存:${escapeHtml(m.ram || "")}</span>
        <span class="badge">GPU:${escapeHtml(m.gpu || "")}</span>
        <span class="badge">上下文:${escapeHtml(m.context || "")}</span>
      </div>
      <div style="margin-top:8px;">
        ${(m.use_cases || []).map(x => `<span class="badge">${escapeHtml(x)}</span>`).join("")}
      </div>
      <div style="margin-top:8px;">
        ${(m.connected_services || []).map(s => `<span class="badge">svc:${escapeHtml(s)}</span>`).join("")}
      </div>
    </div>
  `;
}

function requestModelDownload(modelId) {
  const m = modelCatalogItems.find(x => x.id === modelId);
  if (!m) return;
  const advanced = ["video_3d"].includes(m.type) || (m.profile_tags || []).includes("advanced");
  const message = advanced
    ? `高级模型 ${m.name} 通常体积较大，需要强 GPU。P4 下载器接入后必须二次确认。`
    : `${m.name} 将在 P4 model_downloader_service 接入后支持下载、校验、注册到 model_gateway_v2。`;
  previewText("Model Setup: " + m.name, JSON.stringify({
    status: "p4_downloader_pending",
    model: m,
    message,
    next_services: [
      "model_registry_service",
      "model_downloader_service",
      "model_gateway_v2"
    ]
  }, null, 2), "json");
  systemMessage("模型下载功能将在 P4 接入：" + m.name);
}
