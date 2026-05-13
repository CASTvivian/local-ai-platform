"""Rule-first planner for the initial MAOMIAI agent runtime."""

from __future__ import annotations

import re

from .models import AgentPlan


def normalize_query(text: str) -> tuple[str, list[dict[str, str]]]:
    """Normalize obvious local demo typos before intent routing."""

    query = (text or "").strip()
    corrections: list[dict[str, str]] = []
    typo_map = {
        "元神": "原神",
        "猿神": "原神",
        "源神": "原神",
    }
    for wrong, right in typo_map.items():
        if wrong in query:
            query = query.replace(wrong, right)
            corrections.append(
                {"from": wrong, "to": right, "reason": "possible_entity_typo"}
            )
    return query, corrections


def has_any(query: str, keywords: list[str]) -> bool:
    lowered = query.lower()
    return any(keyword.lower() in lowered for keyword in keywords)


def parse_date_offset(query: str) -> int | None:
    if "后天" in query:
        return 2
    if "明天" in query:
        return 1
    if "昨天" in query:
        return -1
    if "前天" in query:
        return -2

    after_match = re.search(r"过\s*(\d+)\s*天", query)
    if after_match:
        return int(after_match.group(1))

    future_match = re.search(r"(\d+)\s*天后", query)
    if future_match:
        return int(future_match.group(1))

    past_match = re.search(r"(\d+)\s*天前", query)
    if past_match:
        return -int(past_match.group(1))

    return None


def build_plan(message: str) -> AgentPlan:
    """Build the first deterministic agent plan for a user message."""

    normalized, corrections = normalize_query(message)
    offset = parse_date_offset(normalized)

    if offset is not None:
        return AgentPlan(
            intent="date_math",
            normalized_query=normalized,
            tools=["time.now", "time.date_math"],
            reason="date calculation required",
            args={"offset_days": offset, "corrections": corrections},
        )

    if has_any(
        normalized,
        [
            "今天几号",
            "今天是几号",
            "今天日期",
            "当前时间",
            "现在几点",
            "星期几",
            "几月几号",
        ],
    ):
        return AgentPlan(
            intent="time_now",
            normalized_query=normalized,
            tools=["time.now"],
            reason="current local time required",
            args={"corrections": corrections},
        )

    if has_any(normalized, ["天气", "气温", "下雨", "台风", "空气质量"]):
        return AgentPlan(
            intent="weather",
            normalized_query=normalized,
            tools=["weather.query"],
            reason="weather requires live weather tool",
            args={"corrections": corrections},
        )

    if has_any(
        normalized,
        [
            "上网",
            "联网",
            "搜索",
            "查一下",
            "最新",
            "新闻",
            "官网",
            "发行时间",
            "发布时间",
            "哪个公司",
            "什么公司",
            "哪家公司",
            "成立时间",
        ],
    ):
        return AgentPlan(
            intent="web_fact",
            normalized_query=normalized,
            tools=["web.search"],
            reason="fresh factual question requires web evidence",
            args={"corrections": corrections},
        )

    if has_any(
        normalized,
        [
            "能做什么",
            "你能完成什么",
            "你有什么能力",
            "你现在有什么能力",
            "有什么能力",
            "你的能力",
            "平台能力",
            "现在完成了什么",
        ],
    ):
        return AgentPlan(
            intent="capability_status",
            normalized_query=normalized,
            tools=[
                "capability.status",
                "skill_store.list",
                "workflow_store.list",
                "repo_memory.search",
                "catalog.search",
            ],
            reason="capability question should be grounded",
            args={"corrections": corrections},
        )

    if has_any(
        normalized,
        [
            "我们仓",
            "本地项目",
            "项目里",
            "repo",
            "repository",
            "github",
            "stars",
            "收藏的仓",
            "rag",
            "mcp",
            "agent",
            "智能体",
            "参考仓",
            "资产",
            "repo memory",
            "知识库",
            "模型目录",
            "视频模型",
            "context engine",
            "我们软件",
            "这个软件",
            "大脑",
            "平台",
            "claude code",
            "技能仓",
        ],
    ):
        return AgentPlan(
            intent="project_knowledge",
            normalized_query=normalized,
            tools=["repo_memory.search"],
            reason="project-specific question should query repo memory",
            args={"corrections": corrections},
        )

    if has_any(
        normalized,
        ["模型", "大模型", "视频生成", "comfyui", "wan", "hunyuan", "cogvideo", "ollama"],
    ):
        return AgentPlan(
            intent="catalog_knowledge",
            normalized_query=normalized,
            tools=["catalog.search", "repo_memory.search"],
            reason="model/video catalog question",
            args={"corrections": corrections},
        )

    return AgentPlan(
        intent="local_chat",
        normalized_query=normalized,
        tools=["model.generate"],
        reason="normal chat can delegate to local model",
        must_not_hallucinate=False,
        delegate_to_model=True,
        args={"corrections": corrections},
    )
