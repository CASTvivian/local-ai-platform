// P3.14-D4-B Enhanced services module with launcher-aligned metadata
const CORE_SERVICES = [
  {
    port: 18093,
    key: "auto_router",
    name: "Auto Router",
    module: "services.auto_router_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/auto-router.log",
    required: true,
    tier: "owned",
    role: "任务路由 / 能力选择",
  },
  {
    port: 18101,
    key: "reference_skill",
    name: "Reference Skill",
    module: "services.reference_skill_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/reference-skill.log",
    required: false,
    tier: "owned",
    role: "技能参考 / 示例",
    note: "可选",
  },
  {
    port: 18102,
    key: "capability_learning",
    name: "Capability Learning",
    module: "services.capability_learning_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/capability-learning.log",
    required: false,
    tier: "owned",
    role: "能力学习 / 迁移",
    note: "可选",
  },
  {
    port: 18104,
    key: "runtime_execution",
    name: "Runtime Execution",
    module: "services.runtime_execution_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/runtime-execution.log",
    required: true,
    tier: "owned",
    role: "代码执行 / 沙箱",
  },
  {
    port: 18110,
    key: "policy_engine",
    name: "Policy Engine",
    module: "services.policy_engine_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/policy-engine.log",
    required: true,
    tier: "owned",
    role: "策略评估 / 权限",
  },
  {
    port: 18111,
    key: "trace_observability",
    name: "Trace Observability",
    module: "services.trace_observability_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/trace-observability.log",
    required: true,
    tier: "owned",
    role: "可观测性 / 审计",
  },
  {
    port: 18112,
    key: "eval_gateway",
    name: "Eval Gateway",
    module: "services.eval_gateway_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/eval-gateway.log",
    required: true,
    tier: "owned",
    role: "评估入口 / 指标",
  },
  {
    port: 18120,
    key: "document_ingestion",
    name: "Document Ingestion",
    module: "services.document_ingestion_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/document-ingestion.log",
    required: false,
    tier: "partial",
    role: "文档处理 / 向量化",
    note: "部分企业化",
  },
  {
    port: 18121,
    key: "skill_store",
    name: "Skill Store",
    module: "services.skill_store_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/skill-store.log",
    required: true,
    tier: "enterprise",
    role: "技能仓库 / 安装",
  },
  {
    port: 18122,
    key: "job_orchestrator",
    name: "Job Orchestrator",
    module: "services.job_orchestrator_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/job-orchestrator.log",
    required: false,
    tier: "owned",
    role: "任务编排 / 调度",
    note: "可选",
  },
  {
    port: 18123,
    key: "artifact_registry",
    name: "Artifact Registry",
    module: "services.artifact_registry_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/artifact-registry.log",
    required: true,
    tier: "enterprise",
    role: "产物注册 / 生命周期",
  },
  {
    port: 18124,
    key: "code_review_gate",
    name: "Code Review Gate",
    module: "services.code_review_gate_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/code-review-gate.log",
    required: true,
    tier: "enterprise",
    role: "代码审查 / 安全检查",
  },
  {
    port: 18125,
    key: "repo_memory",
    name: "Repo Memory",
    module: "services.repo_memory_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/repo-memory.log",
    required: true,
    tier: "enterprise",
    role: "仓库记忆 / 共享学习",
  },
  {
    port: 18126,
    key: "workflow_store",
    name: "Workflow Store",
    module: "services.workflow_store_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/workflow-store.log",
    required: true,
    tier: "enterprise",
    role: "工作流仓库 / 模板",
  },
  {
    port: 18127,
    key: "design_system",
    name: "Design System",
    module: "services.design_system_service.main:app",
    log: "/Users/mofamaomi/Documents/本地ai/logs/design-system.log",
    required: true,
    tier: "enterprise",
    role: "设计系统 / UI 约束",
  },
];

// Health checking functions
async function checkServiceHealth(service) {
  const url = `http://127.0.0.1:${service.port}/health`;
  try {
    const res = await fetch(url, { signal: AbortSignal.timeout(1800) });
    const json = await res.json();
    return {
      ...service,
      ok: !!json.ok,
      detail: json,
      version: json.version || "unknown",
    };
  } catch (e) {
    return {
      ...service,
      ok: false,
      error: e.message,
      version: "unknown",
    };
  }
}

async function refreshHealth() {
  const box = document.getElementById("serviceGrid") || document.getElementById("healthGrid") || document.getElementById("services");
  if (box) box.innerHTML = `<div class="mono">正在检查服务...</div>`;
  const list = typeof CORE_SERVICES !== "undefined" ? CORE_SERVICES : (typeof SERVICES !== "undefined" ? SERVICES : []);
  const results = await Promise.all(list.map(checkServiceHealth));
  renderServiceHealth(results);
  return results;
}

function renderServiceHealth(results) {
  const box = document.getElementById("serviceGrid") || document.getElementById("healthGrid") || document.getElementById("services");
  if (!box) return;

  const enterpriseCount = results.filter(x => x.tier === "enterprise" && x.ok).length;
  const enterpriseTotal = results.filter(x => x.tier === "enterprise").length;
  const totalCount = results.length;
  const okCount = results.filter(x => x.ok).length;

  box.innerHTML = `
    <div style="margin-bottom: 12px; padding: 8px; background: rgba(255,255,255,0.05); border-radius: 6px;">
      <div style="display: flex; justify-content: space-between; font-size: 13px; margin-bottom: 6px;">
        <span>总服务: <b>${totalCount}</b></span>
        <span>运行中: <b>${okCount}</b></span>
      </div>
      <div style="display: flex; justify-content: space-between; font-size: 13px;">
        <span>企业服务: <b>${enterpriseCount}/${enterpriseTotal}</b></span>
        <span>必需服务: <b>${results.filter(x => x.required && x.ok).length}/${results.filter(x => x.required).length}</b></span>
      </div>
    </div>
    <div class="service-grid">
      ${results.map(s => renderServiceCard(s)).join("")}
    </div>
  `;

  const top = document.getElementById("service状态");
  if (top) {
    top.textContent = `${okCount}/${totalCount} services (${enterpriseCount}/${enterpriseTotal} enterprise)`;
  }
}

function renderServiceCard(service) {
  const tierBadge = service.tier === "enterprise" ? 
    `<span class="badge badge-enterprise">ENT</span>` : 
    service.tier === "partial" ? 
    `<span class="badge badge-partial">PART</span>` : "";
  
  const requiredBadge = service.required ? 
    `<span class="badge badge-required">REQ</span>` : "";
  
  const versionDisplay = service.ok && service.version && service.version !== "unknown" ?
    `<div class="service-version mono">${escapeHtml(service.version)}</div>` : "";

  return `
    <div class="service-card ${service.ok ? 'ok' : 'bad'}">
      <div class="service-header">
        <div class="service-info">
          <div class="service-name">
            <span class="dot ${service.ok ? 'ok' : 'bad'}"></span>
            <b>${escapeHtml(service.name)}</b>
          </div>
          <div class="service-port mono">${service.port}</div>
        </div>
        <div class="service-badges">
          ${tierBadge}
          ${requiredBadge}
        </div>
      </div>
      ${versionDisplay}
      <div class="service-role">${escapeHtml(service.role)}</div>
      ${service.note ? `<div class="service-note">${escapeHtml(service.note)}</div>` : ""}
      ${!service.ok && service.error ? 
        `<div class="service-error mono">${escapeHtml(service.error)}</div>` : ""}
    </div>
  `;
}

async function loadServiceHealth() {
  return refreshHealth();
}

// Utility function
function escapeHtml(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
