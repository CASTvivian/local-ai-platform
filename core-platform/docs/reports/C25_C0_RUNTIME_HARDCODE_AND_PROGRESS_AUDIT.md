# C25-C0 Runtime Hardcode + Progress Audit

Generated at: 2026-05-14T14:23:08.481282

## 1. Progress

- agent_runtime_service: ✅
- run_store: ✅
- session_store: ✅
- approval_security: ✅
- runtime_execution: ✅
- mcp_registry: ✅
- capability_registry: ✅
- filesystem_sandbox: ✅
- browser_runtime: ✅
- web_search_runtime: ✅
- weather_runtime: ✅

## 2. Hardcode Risk Summary

### business_entity_hardcode

- files: 1

#### `core-platform/services/agent_runtime_service/app/planner.py`
- L31 `原神`: `"元神": "原神",`
- L32 `原神`: `"猿神": "原神",`
- L33 `原神`: `"源神": "原神",`
- L31 `元神`: `"元神": "原神",`

### if_else_query_routing

- files: 7

#### `core-platform/services/agent_runtime_service/app/planner.py`
- L50 `if "`: `if "后天" in query:`
- L52 `if "`: `if "明天" in query:`
- L54 `if "`: `if "昨天" in query:`
- L56 `if "`: `if "前天" in query:`
- L44 `has_any(`: `def has_any(query: str, keywords: list[str]) -> bool:`
- L111 `has_any(`: `if has_any(`
- L131 `has_any(`: `if has_any(normalized, ["天气", "气温", "下雨", "台风", "空气质量"]):`
- L140 `has_any(`: `if has_any(normalized, ["执行命令", "运行命令", "shell", "终端命令", "删除文件", "写入文件"]):`
- L149 `has_any(`: `if has_any(`
- L175 `has_any(`: `if has_any(`
- L203 `has_any(`: `if has_any(`
- L241 `has_any(`: `if has_any(`

#### `core-platform/services/agent_runtime_service/app/capability/registry.py`
- L236 `if "`: `if "code" in capability.tags:`
- L239 `if "`: `if "reasoning" in capability.tags:`
- L242 `if "`: `if "memory" in capability.tags or "repo" in capability.tags:`
- L245 `if "`: `if "video" in capability.tags:`
- L248 `if "`: `if "browser" in capability.tags or "fetch" in capability.tags:`

#### `core-platform/services/agent_runtime_service/app/runtime/web_search_runtime.py`
- L39 `if "`: `if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):`

#### `core-platform/services/agent_runtime_service/app/runtime/browser_runtime.py`
- L167 `if "`: `if "html" in content_type.lower() or "<html" in body.lower():`

#### `core-platform/apps/desktop/src/js/windows-click-model-setup.js`
- L168 `.includes(`: `if (msg.includes("bootstrap_runtime.ps1") || msg.includes("运行时脚本")) {`
- L171 `.includes(`: `if (msg.includes("ExecutionPolicy") || msg.includes("PowerShell")) {`
- L206 `.includes(`: `return raw.includes(modelName);`
- L210 `.includes(`: `if (raw.includes(modelName)) return "已安装";`
- L168 `includes("`: `if (msg.includes("bootstrap_runtime.ps1") || msg.includes("运行时脚本")) {`
- L171 `includes("`: `if (msg.includes("ExecutionPolicy") || msg.includes("PowerShell")) {`

#### `core-platform/apps/desktop/src/js/windows-demo-stable-router.js`
- L36 `.includes(`: `const installed = getCatalog().filter((item) => raw.includes(item.model));`
- L328 `.includes(`: `if (["chat", "new-chat", "new"].includes(target)) return renderChat();`
- L329 `.includes(`: `if (["models", "model", "local-model", "local-models"].includes(target)) return renderLocalModels();`
- L330 `.includes(`: `if (["artifacts", "files", "documents"].includes(target)) return renderFiles();`
- L331 `.includes(`: `if (["code-review", "code"].includes(target)) return renderCodeReview();`
- L332 `.includes(`: `if (["settings", "setting"].includes(target)) return renderSettings();`
- L338 `.includes(`: `if (value.includes("新对话") || value.includes("新建会话")) return "chat";`
- L339 `.includes(`: `if (value.includes("本地模型") || value.includes("模型")) return "models";`
- L340 `.includes(`: `if (value.includes("文件") || value.includes("结果") || value.includes("产物")) return "artifacts";`
- L341 `.includes(`: `if (value.includes("代码")) return "code-review";`
- L342 `.includes(`: `if (value.includes("设置")) return "settings";`
- L420 `.includes(`: `if (text === "发送" || text.includes("发送")) {`
- L338 `includes("`: `if (value.includes("新对话") || value.includes("新建会话")) return "chat";`
- L339 `includes("`: `if (value.includes("本地模型") || value.includes("模型")) return "models";`
- L340 `includes("`: `if (value.includes("文件") || value.includes("结果") || value.includes("产物")) return "artifacts";`
- L341 `includes("`: `if (value.includes("代码")) return "code-review";`
- L342 `includes("`: `if (value.includes("设置")) return "settings";`
- L420 `includes("`: `if (text === "发送" || text.includes("发送")) {`
- L420 `text.includes`: `if (text === "发送" || text.includes("发送")) {`

#### `core-platform/apps/desktop/src/js/chatgpt-like-ui.js`
- L78 `.includes(`: `if (meta && (!meta.textContent || meta.textContent.includes("view:"))) {`
- L78 `includes("`: `if (meta && (!meta.textContent || meta.textContent.includes("view:"))) {`

### weather_city_or_code_maps

- files: 0

### direct_model_bypass

- files: 3

#### `core-platform/services/agent_runtime_service/app/planner.py`
- L243 `ollama`: `["模型", "大模型", "视频生成", "comfyui", "wan", "hunyuan", "cogvideo", "ollama"],`

#### `core-platform/apps/desktop/src/js/windows-click-model-setup.js`
- L307 `local_ai_status_direct`: `const out = await invoke("local_ai_status_direct");`
- L171 `PowerShell`: `if (msg.includes("ExecutionPolicy") || msg.includes("PowerShell")) {`
- L172 `PowerShell`: `return "Windows PowerShell 执行受限，请以管理员身份或允许脚本执行后重试。";`
- L168 `bootstrap_runtime`: `if (msg.includes("bootstrap_runtime.ps1") || msg.includes("运行时脚本")) {`

#### `core-platform/apps/desktop/src-tauri/src/lib.rs`
- L287 `generate_local_ai_response`: `fn generate_local_ai_response(profile: String, prompt: String) -> Result<String, String> {`
- L303 `generate_local_ai_response`: `generate_local_ai_response`
- L272 `download_local_model_capability`: `fn download_local_model_capability(profile: String) -> Result<String, String> {`
- L300 `download_local_model_capability`: `download_local_model_capability,`
- L262 `local_ai_status_direct`: `fn local_ai_status_direct() -> Result<String, String> {`
- L298 `local_ai_status_direct`: `local_ai_status_direct,`
- L268 `ollama`: `run_windows_bootstrap("install_ollama", None)`
- L146 `bootstrap_runtime`: `let script_content = include_str!("../../../../scripts/windows/bootstrap_runtime.ps1");`
- L152 `bootstrap_runtime`: `let script_path = runtime_dir.join("bootstrap_runtime.ps1");`
- L154 `bootstrap_runtime`: `.map_err(|e| format!("无法写入 bootstrap_runtime.ps1: {}", e))?;`
- L156 `bootstrap_runtime`: `.map_err(|e| format!("写入 bootstrap_runtime.ps1 失败: {}", e))?;`

### tool_runtime_positive

- files: 30

#### `core-platform/services/agent_runtime_service/app/validator.py`
- L35 `run_store`: `"""Build a normalized validation payload for run_store persistence."""`

#### `core-platform/services/agent_runtime_service/app/planner.py`
- L145 `approval`: `reason="restricted local execution requires explicit approval",`

#### `core-platform/services/agent_runtime_service/app/service.py`
- L7 `execute_plan`: `from .executor import execute_plan`
- L106 `execute_plan`: `results = execute_plan(plan, request, run_id=run_state.run_id, session_id=session_id)`
- L74 `run_agent`: `async def run_agent_loop(request: AgentRunRequest) -> AgentRunResponse:`
- L176 `run_agent`: `def run_agent(request: AgentRunRequest) -> AgentRunResponse:`
- L181 `run_agent`: `return asyncio.run(run_agent_loop(request))`
- L79 `approval`: `lands after approval, sandbox, and run_store are available.`
- L79 `sandbox`: `lands after approval, sandbox, and run_store are available.`
- L11 `run_store`: `from .run_store.models import AgentRunStep`
- L12 `run_store`: `from .run_store.store import create_run, save_run`
- L79 `run_store`: `lands after approval, sandbox, and run_store are available.`
- L13 `session_store`: `from .session_store.store import append_run`
- L14 `validator`: `from .validator import build_validation, should_block_hallucination, should_retry`

#### `core-platform/services/agent_runtime_service/app/run_store/store.py`
- L14 `run_store`: `RUN_ROOT = CORE_PLATFORM_ROOT / "data" / "run_store"`

#### `core-platform/services/agent_runtime_service/app/run_store/models.py`
- L12 `validator`: `"""A single persisted planner/executor/validator step."""`

#### `core-platform/services/agent_runtime_service/app/security/approval_store.py`
- L1 `approval`: `"""JSON-file approval store for Agent Runtime."""`
- L9 `approval`: `from .approval_models import ApprovalDecision, ApprovalRecord`
- L13 `approval`: `APPROVAL_ROOT = CORE_PLATFORM_ROOT / "data" / "approval_store"`
- L17 `approval`: `def approval_file(approval_id: str) -> Path:`
- L18 `approval`: `return APPROVAL_ROOT / f"{approval_id}.json"`
- L21 `approval`: `def save_approval(record: ApprovalRecord) -> None:`
- L22 `approval`: `approval_file(record.approval_id).write_text(record.model_dump_json(indent=2), encoding="utf-8")`
- L25 `approval`: `def load_approval(approval_id: str) -> Optional[ApprovalRecord]:`
- L26 `approval`: `path = approval_file(approval_id)`
- L32 `approval`: `def list_approvals() -> List[ApprovalRecord]:`
- L42 `approval`: `def resolve_approval(decision: ApprovalDecision) -> Optional[ApprovalRecord]:`
- L43 `approval`: `record = load_approval(decision.approval_id)`
- L50 `approval`: `save_approval(record)`

#### `core-platform/services/agent_runtime_service/app/security/approval_models.py`
- L22 `approval`: `"""Local reviewer decision for a pending approval."""`
- L24 `approval`: `approval_id: str`
- L31 `approval`: `"""Persisted approval record."""`
- L33 `approval`: `approval_id: str`
- L46 `approval`: `"""Build a new pending approval record."""`
- L49 `approval`: `approval_id=str(uuid.uuid4()),`

#### `core-platform/services/agent_runtime_service/app/security/sandbox.py`
- L40 `approval`: `"requires_approval": False,`
- L47 `approval`: `"requires_approval": True,`
- L53 `approval`: `"requires_approval": True,`
- L1 `sandbox`: `"""Tool sandbox policy for Agent Runtime execution."""`

#### `core-platform/services/agent_runtime_service/app/security/guard.py`
- L8 `approval`: `from .approval_models import ApprovalRequest, build_record`
- L9 `approval`: `from .approval_store import save_approval`
- L14 `approval`: `"""Return a blocking ToolResult when approval is required."""`
- L17 `approval`: `if not policy["requires_approval"]:`
- L28 `approval`: `save_approval(record)`
- L34 `approval`: `"requires_approval": True,`
- L35 `approval`: `"approval_id": record.approval_id,`
- L38 `approval`: `error="Tool execution requires approval.",`
- L10 `sandbox`: `from .sandbox import evaluate_tool`

#### `core-platform/services/agent_runtime_service/app/renderer.py`
- L77 `approval`: `blocked = next((item for item in results if item.data.get("requires_approval")), None)`
- L81 `approval`: `f"approval_id: {blocked.data.get('approval_id')}\n"`
- L176 `approval`: `"核心主链路已经收敛到 /agent/run；下一步需要补 approval、sandbox、run_store 增强和真正多步工具执行。",`
- L176 `sandbox`: `"核心主链路已经收敛到 /agent/run；下一步需要补 approval、sandbox、run_store 增强和真正多步工具执行。",`
- L176 `run_store`: `"核心主链路已经收敛到 /agent/run；下一步需要补 approval、sandbox、run_store 增强和真正多步工具执行。",`

#### `core-platform/services/agent_runtime_service/app/capability/service.py`
- L1 `Capability`: `"""Capability matching service helpers."""`
- L5 `Capability`: `from .models import CapabilityMatchRequest, CapabilityMatchResult`
- L9 `Capability`: `def match_capability(request: CapabilityMatchRequest) -> CapabilityMatchResult:`
- L18 `Capability`: `return CapabilityMatchResult(ok=True, query=request.query, matches=items)`

#### `core-platform/services/agent_runtime_service/app/capability/models.py`
- L1 `Capability`: `"""Capability registry models."""`
- L10 `Capability`: `class Capability(BaseModel):`
- L26 `Capability`: `class CapabilityMatchRequest(BaseModel):`
- L35 `Capability`: `class CapabilityMatchResult(BaseModel):`
- L36 `Capability`: `"""Capability matching response."""`
- L40 `Capability`: `matches: List[Capability] = Field(default_factory=list)`

#### `core-platform/services/agent_runtime_service/app/capability/registry.py`
- L9 `Capability`: `from .models import Capability`
- L17 `Capability`: `Capability(`
- L27 `Capability`: `Capability(`
- L37 `Capability`: `Capability(`
- L47 `Capability`: `Capability(`
- L57 `Capability`: `Capability(`
- L67 `Capability`: `Capability(`
- L77 `Capability`: `Capability(`
- L87 `Capability`: `Capability(`
- L98 `Capability`: `Capability(`
- L108 `Capability`: `Capability(`
- L119 `Capability`: `Capability(`
- L130 `Capability`: `Capability(`
- L151 `Capability`: `def load_capabilities() -> List[Capability]:`
- L156 `Capability`: `return [Capability.model_validate(item) for item in data]`
- L168 `Capability`: `def get_capability(capability_id: str) -> Optional[Capability]:`
- L177 `Capability`: `def save_capabilities(items: List[Capability]) -> None:`
- L187 `Capability`: `def upsert_capability(capability: Capability) -> Capability:`
- L206 `Capability`: `) -> List[Capability]:`
- L211 `Capability`: `scored: list[tuple[float, Capability]] = []`

#### `core-platform/services/agent_runtime_service/app/capability/__init__.py`
- L1 `Capability`: `"""Capability registry for MAOMIAI Agent Runtime."""`

#### `core-platform/services/agent_runtime_service/app/runtime/weather_runtime.py`
- L15 `execution_store`: `from .execution_store import save_execution`

#### `core-platform/services/agent_runtime_service/app/runtime/web_search_runtime.py`
- L18 `execution_store`: `from .execution_store import save_execution`

#### `core-platform/services/agent_runtime_service/app/runtime/sandbox_executor.py`
- L15 `sandbox`: `RUNTIME_ROOT = CORE_PLATFORM_ROOT / "data" / "sandbox_runtime"`
- L27 `sandbox`: `def _write_execution_record(sandbox_id: str, record: Dict[str, Any]) -> None:`
- L28 `sandbox`: `path = RUNTIME_ROOT / sandbox_id / "execution.json"`
- L32 `sandbox`: `def execute_sandboxed(command: str) -> Dict[str, Any]:`
- L35 `sandbox`: `This is a local sandbox boundary, not a container or VM. It prevents`
- L37 `sandbox`: `C25-B4 should replace this with a stronger OS/container sandbox.`
- L40 `sandbox`: `sandbox_id = str(uuid.uuid4())`
- L41 `sandbox`: `workdir = RUNTIME_ROOT / sandbox_id`
- L49 `sandbox`: `"sandbox_id": sandbox_id,`
- L52 `sandbox`: `_write_execution_record(sandbox_id, result)`
- L58 `sandbox`: `"sandbox_id": sandbox_id,`
- L61 `sandbox`: `_write_execution_record(sandbox_id, result)`
- L68 `sandbox`: `"sandbox_id": sandbox_id,`
- L71 `sandbox`: `_write_execution_record(sandbox_id, result)`
- L86 `sandbox`: `"sandbox_id": sandbox_id,`
- L96 `sandbox`: `_write_execution_record(sandbox_id, result)`
- L101 `sandbox`: `"sandbox_id": sandbox_id,`
- L108 `sandbox`: `_write_execution_record(sandbox_id, result)`

#### `core-platform/services/agent_runtime_service/app/runtime/browser_runtime.py`
- L117 `approval`: `approval_id=None,`
- L134 `sandbox`: `sandbox_id=result.get("snapshot_id"),`
- L18 `execution_store`: `from .execution_store import save_execution`

#### `core-platform/services/agent_runtime_service/app/runtime/execution_store.py`
- L35 `approval`: `approval_id: Optional[str] = None,`
- L46 `approval`: `if approval_id and data.get("approval_id") != approval_id:`
- L13 `execution_store`: `EXECUTION_ROOT = CORE_PLATFORM_ROOT / "data" / "execution_store"`

#### `core-platform/services/agent_runtime_service/app/runtime/approval_executor.py`
- L8 `approval`: `from ..security.approval_store import load_approval`
- L15 `approval`: `def execute_approved_action(approval_id: str) -> Dict[str, Any]:`
- L18 `approval`: `record = load_approval(approval_id)`
- L22 `approval`: `approval_id=approval_id,`
- L26 `approval`: `error="approval not found",`
- L27 `approval`: `metadata={"source": "approval_executor"},`
- L33 `approval`: `"message": "approval not found",`
- L34 `approval`: `"approval_id": approval_id,`
- L43 `approval`: `approval_id=approval_id,`
- L50 `approval`: `error="approval not granted",`
- L51 `approval`: `metadata={"source": "approval_executor"},`
- L57 `approval`: `"message": "approval not granted",`
- L58 `approval`: `"approval_id": approval_id,`
- L66 `approval`: `approval_id=approval_id,`
- L74 `approval`: `metadata={"source": "approval_executor"},`
- L81 `approval`: `"approval_id": approval_id,`
- L86 `approval`: `approval_id=approval_id,`
- L99 `approval`: `"source": "approval_executor",`
- L106 `approval`: `result["approval_id"] = approval_id`
- L118 `approval`: `approval_id=approval_id,`

#### `core-platform/services/agent_runtime_service/app/runtime/execution_models.py`
- L16 `approval`: `approval_id: Optional[str] = None`
- L36 `approval`: `approval_id: Optional[str] = None,`
- L51 `approval`: `approval_id=approval_id,`
- L27 `sandbox`: `sandbox_id: Optional[str] = None`
- L44 `sandbox`: `sandbox_id: Optional[str] = None,`
- L62 `sandbox`: `sandbox_id=sandbox_id,`

#### `core-platform/services/agent_runtime_service/app/runtime/filesystem_models.py`
- L6 `sandbox`: `sandbox_id: Optional[str] = None`
- L12 `sandbox`: `sandbox_id: str`
- L17 `sandbox`: `sandbox_id: str`
- L22 `sandbox`: `sandbox_id: str`

#### `core-platform/services/agent_runtime_service/app/runtime/filesystem_sandbox.py`
- L1 `sandbox`: `"""Filesystem sandbox restricted to a runtime-owned working directory."""`
- L12 `sandbox`: `SANDBOX_ROOT = CORE_PLATFORM_ROOT / "data" / "filesystem_sandbox"`
- L16 `sandbox`: `def _sandbox_dir(sandbox_id: str | None = None) -> Path:`
- L17 `sandbox`: `sid = sandbox_id or str(uuid.uuid4())`
- L32 `sandbox`: `raise ValueError("path escapes sandbox") from exc`
- L34 `sandbox`: `raise ValueError("path escapes sandbox")`
- L38 `sandbox`: `def _error(sandbox_id: str | None, path: str, error: Exception) -> Dict[str, Any]:`
- L41 `sandbox`: `"sandbox_id": sandbox_id,`
- L47 `sandbox`: `def create_sandbox() -> Dict[str, Any]:`
- L48 `sandbox`: `root = _sandbox_dir()`
- L51 `sandbox`: `"sandbox_id": root.name,`
- L56 `sandbox`: `def write_file(sandbox_id: str | None, path: str, content: str) -> Dict[str, Any]:`
- L57 `sandbox`: `root = _sandbox_dir(sandbox_id)`
- L66 `sandbox`: `"sandbox_id": root.name,`
- L72 `sandbox`: `def read_file(sandbox_id: str, path: str) -> Dict[str, Any]:`
- L73 `sandbox`: `root = _sandbox_dir(sandbox_id)`
- L81 `sandbox`: `"sandbox_id": root.name,`
- L88 `sandbox`: `"sandbox_id": root.name,`
- L94 `sandbox`: `def list_files(sandbox_id: str, path: str = ".") -> Dict[str, Any]:`
- L95 `sandbox`: `root = _sandbox_dir(sandbox_id)`

#### `core-platform/services/agent_runtime_service/app/mcp/models.py`
- L10 `MCPTool`: `class MCPTool(BaseModel):`
- L20 `approval`: `requires_approval: bool = False`
- L40 `approval`: `approval_required: bool = False`
- L41 `approval`: `approval_id: Optional[str] = None`

#### `core-platform/services/agent_runtime_service/app/mcp/registry.py`
- L9 `MCPTool`: `from .models import MCPTool`
- L17 `MCPTool`: `MCPTool(`
- L28 `MCPTool`: `MCPTool(`
- L38 `MCPTool`: `MCPTool(`
- L48 `MCPTool`: `MCPTool(`
- L59 `MCPTool`: `MCPTool(`
- L70 `MCPTool`: `MCPTool(`
- L81 `MCPTool`: `MCPTool(`
- L92 `MCPTool`: `MCPTool(`
- L103 `MCPTool`: `MCPTool(`
- L114 `MCPTool`: `MCPTool(`
- L125 `MCPTool`: `MCPTool(`
- L136 `MCPTool`: `MCPTool(`
- L158 `MCPTool`: `def load_tools() -> List[MCPTool]:`
- L163 `MCPTool`: `return [MCPTool.model_validate(item) for item in data]`
- L172 `MCPTool`: `def get_tool(name: str) -> Optional[MCPTool]:`
- L181 `MCPTool`: `def save_tools(tools: List[MCPTool]) -> None:`
- L191 `MCPTool`: `def upsert_tool(tool: MCPTool) -> MCPTool:`
- L25 `approval`: `requires_approval=False,`
- L35 `approval`: `requires_approval=False,`

#### `core-platform/services/agent_runtime_service/app/mcp/invoker.py`
- L63 `approval`: `if tool.requires_approval:`
- L69 `approval`: `error="approval required",`
- L70 `approval`: `approval_required=True,`
- L71 `approval`: `approval_id=blocked.data.get("approval_id"),`
- L123 `approval`: `error="local tool requires approval execution path",`
- L12 `sandbox`: `from ..runtime.filesystem_sandbox import list_files, read_file`
- L78 `sandbox`: `sandbox_id=str(request.arguments.get("sandbox_id") or ""),`
- L84 `sandbox`: `sandbox_id=str(request.arguments.get("sandbox_id") or ""),`

#### `core-platform/services/agent_runtime_service/app/session_store/store.py`
- L13 `session_store`: `SESSION_ROOT = CORE_PLATFORM_ROOT / "data" / "session_store"`

#### `core-platform/services/agent_runtime_service/app/executor.py`
- L7 `Capability`: `from .capability.models import CapabilityMatchRequest`
- L107 `Capability`: `CapabilityMatchRequest(`
- L53 `execute_plan`: `def execute_plan(`
- L46 `approval`: `"approval_required": result.approval_required,`
- L47 `approval`: `"approval_id": result.approval_id,`

#### `core-platform/services/agent_runtime_service/main.py`
- L25 `MCPTool`: `from services.agent_runtime_service.app.mcp.models import MCPInvokeRequest, MCPTool`
- L214 `MCPTool`: `def agent_mcp_upsert_tool(tool: MCPTool) -> Dict[str, Any]:`
- L16 `Capability`: `from services.agent_runtime_service.app.capability.models import Capability, CapabilityMatchRequest`
- L238 `Capability`: `def agent_upsert_capability(capability: Capability) -> Dict[str, Any]:`
- L244 `Capability`: `def agent_match_capabilities(request: CapabilityMatchRequest) -> Dict[str, Any]:`
- L65 `run_agent`: `from services.agent_runtime_service.app.service import run_agent_loop`
- L114 `run_agent`: `return (await run_agent_loop(request)).model_dump()`
- L29 `approval`: `from services.agent_runtime_service.app.runtime.approval_executor import execute_approved_action`
- L58 `approval`: `from services.agent_runtime_service.app.security.approval_models import ApprovalDecision`
- L59 `approval`: `from services.agent_runtime_service.app.security.approval_store import (`
- L60 `approval`: `list_approvals,`
- L61 `approval`: `load_approval,`
- L62 `approval`: `resolve_approval,`
- L133 `approval`: `@app.get("/agent/approvals")`
- L134 `approval`: `def agent_approvals() -> Dict[str, Any]:`
- L137 `approval`: `"items": [item.model_dump() for item in list_approvals()],`
- L141 `approval`: `@app.get("/agent/approval/{approval_id}")`
- L142 `approval`: `def agent_approval(approval_id: str) -> Dict[str, Any]:`
- L143 `approval`: `item = load_approval(approval_id)`
- L145 `approval`: `return {"ok": False, "error": "approval_not_found", "approval_id": approval_id}`

#### `core-platform/apps/desktop/src/js/services.js`
- L5 `Capability`: `{ name: "Capability Learning", port: 18102 },`


## 3. Interpretation

Runtime should avoid business/entity hardcoding.
Concrete entities should come from memory, provider APIs, capability registry, or model planner.
Rules may remain only as safety fallback, not primary Agent intelligence.

## 4. Next

C25-C1 should remove or externalize hardcoded business/entity routing.
C25-C2 should replace rule planner with model-driven planner + tool schema.
