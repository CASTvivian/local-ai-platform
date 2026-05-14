"""Runtime capability registry and matcher."""

from __future__ import annotations

import json
from pathlib import Path
from typing import List, Optional

from .models import Capability


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
REGISTRY_ROOT = CORE_PLATFORM_ROOT / "data" / "capability_registry"
REGISTRY_FILE = REGISTRY_ROOT / "capabilities.json"

DEFAULT_CAPABILITIES = [
    Capability(
        id="chat.light",
        name="轻量对话能力",
        type="model",
        description="低配电脑快速对话与基础问答。",
        runtime="model",
        target="qwen2.5:1.5b",
        tags=["chat", "local_model", "light"],
        priority=60,
    ),
    Capability(
        id="chat.standard",
        name="标准对话能力",
        type="model",
        description="中文对话、写作、总结与一般问答。",
        runtime="model",
        target="qwen2.5:7b",
        tags=["chat", "local_model", "cn"],
        priority=80,
    ),
    Capability(
        id="code.standard",
        name="代码能力",
        type="model",
        description="代码生成、代码审查、错误分析和项目修复。",
        runtime="model",
        target="qwen2.5-coder:7b",
        tags=["code", "coding", "developer"],
        priority=85,
    ),
    Capability(
        id="reasoning.standard",
        name="推理分析能力",
        type="model",
        description="复杂问题拆解、分析、推理和策略制定。",
        runtime="model",
        target="deepseek-r1:7b",
        tags=["reasoning", "analysis", "planning"],
        priority=85,
    ),
    Capability(
        id="repo.memory",
        name="项目知识能力",
        type="tool",
        description="查询本地仓库、GitHub Stars、参考仓摘要和 Repo Memory。",
        runtime="mcp",
        target="repo_memory.search",
        tags=["repo", "memory", "rag", "knowledge", "agent", "mcp"],
        priority=95,
    ),
    Capability(
        id="skill.store",
        name="技能仓能力",
        type="tool",
        description="列出和管理本地技能仓能力。",
        runtime="mcp",
        target="skill_store.list",
        tags=["skill", "capability", "tools"],
        priority=70,
    ),
    Capability(
        id="workflow.store",
        name="工作流能力",
        type="tool",
        description="列出和管理本地工作流。",
        runtime="mcp",
        target="workflow_store.list",
        tags=["workflow", "automation"],
        priority=70,
    ),
    Capability(
        id="shell.sandbox",
        name="沙箱命令能力",
        type="tool",
        description="审批后在沙箱中执行安全命令。",
        runtime="mcp",
        target="shell.exec",
        tags=["shell", "sandbox", "execution"],
        priority=40,
        metadata={"requires_approval": True},
    ),
    Capability(
        id="browser.fetch",
        name="网页抓取能力",
        type="tool",
        description="安全抓取公开网页并生成本地 snapshot，用于后续联网搜索和资料读取。",
        runtime="mcp",
        target="browser.fetch",
        tags=["browser", "web", "fetch", "snapshot", "网页抓取"],
        priority=75,
    ),
    Capability(
        id="web.search",
        name="联网搜索能力",
        type="tool",
        description="搜索公开网页，并可抓取首个结果形成 browser snapshot。",
        runtime="mcp",
        target="web.search",
        tags=["web", "search", "realtime", "browser"],
        priority=95,
        enabled=True,
    ),
    Capability(
        id="weather.query",
        name="天气查询能力",
        type="tool",
        description="通过 geocoding 和 Open-Meteo 查询实时天气。",
        runtime="mcp",
        target="weather.query",
        tags=["weather", "realtime", "geocoding"],
        priority=95,
        enabled=True,
    ),
    Capability(
        id="video.catalog",
        name="视频生成目录能力",
        type="catalog",
        description="查询视频生成模型目录和后续 ComfyUI/远程视频生成规划。",
        runtime="catalog",
        target="open_video_model_catalog",
        tags=["video", "comfyui", "generation"],
        priority=60,
    ),
]


def ensure_registry() -> None:
    """Create runtime registry file when missing."""

    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    if not REGISTRY_FILE.exists():
        save_capabilities(DEFAULT_CAPABILITIES)


def load_capabilities() -> List[Capability]:
    """Load registered capabilities."""

    ensure_registry()
    data = json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))
    return [Capability.model_validate(item) for item in data]


def list_capabilities(enabled_only: bool = False) -> List[dict]:
    """Return capability dictionaries for API responses."""

    items = load_capabilities()
    if enabled_only:
        items = [item for item in items if item.enabled]
    return [item.model_dump() for item in items]


def get_capability(capability_id: str) -> Optional[Capability]:
    """Return one capability by id."""

    for item in load_capabilities():
        if item.id == capability_id:
            return item
    return None


def save_capabilities(items: List[Capability]) -> None:
    """Persist runtime capability registry."""

    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    REGISTRY_FILE.write_text(
        json.dumps([item.model_dump() for item in items], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def upsert_capability(capability: Capability) -> Capability:
    """Insert or replace one capability."""

    items = load_capabilities()
    for index, item in enumerate(items):
        if item.id == capability.id:
            items[index] = capability
            save_capabilities(items)
            return capability
    items.append(capability)
    save_capabilities(items)
    return capability


def match_capabilities(
    query: str,
    intent: str | None = None,
    tags: list[str] | None = None,
    limit: int = 5,
) -> List[Capability]:
    """Match a query and optional intent to enabled capabilities."""

    tags = tags or []
    normalized_query = (query or "").lower()
    scored: list[tuple[float, Capability]] = []
    for capability in load_capabilities():
        if not capability.enabled:
            continue
        score = 0.0
        haystack = " ".join(
            [
                capability.id,
                capability.name,
                capability.type,
                capability.description,
                " ".join(capability.tags),
                capability.runtime,
                capability.target,
            ]
        ).lower()
        for token in normalized_query.replace("/", " ").replace("_", " ").split():
            if token and token in haystack:
                score += 5
        for tag in tags:
            if tag in capability.tags:
                score += 10
        if intent and (intent in capability.tags or intent in capability.id or intent in capability.type):
            score += 20
        if any(keyword in normalized_query for keyword in ["代码", "编程", "bug", "报错", "开发"]):
            if "code" in capability.tags:
                score += 30
        if any(keyword in normalized_query for keyword in ["推理", "分析", "判断", "策略"]):
            if "reasoning" in capability.tags:
                score += 30
        if any(keyword in normalized_query for keyword in ["仓", "项目", "mcp", "rag", "agent", "知识库"]):
            if "memory" in capability.tags or "repo" in capability.tags:
                score += 35
        if any(keyword in normalized_query for keyword in ["视频", "生成视频", "comfyui"]):
            if "video" in capability.tags:
                score += 35
        if any(keyword in normalized_query for keyword in ["网页", "抓取", "读取网页", "fetch", "url"]):
            if "browser" in capability.tags or "fetch" in capability.tags:
                score += 35
        score += capability.priority / 100
        if score > 0:
            scored.append((score, capability))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in scored[:limit]]
