"""User-facing answer rendering for agent runtime results."""

from __future__ import annotations

from .models import AgentPlan, ToolResult


def _format_local_time(data: dict) -> str:
    return (
        f"{data.get('year')}年{data.get('month')}月{data.get('day')}日，"
        f"{data.get('weekday')}，{int(data.get('hour') or 0):02d}:{int(data.get('minute') or 0):02d}"
    )


def _extract_items(data: dict) -> list[dict]:
    return (
        data.get("results")
        or data.get("items")
        or data.get("matches")
        or data.get("data", {}).get("results")
        or data.get("data", {}).get("items")
        or []
    )


def render_answer(plan: AgentPlan, results: list[ToolResult]) -> str:
    """Render a grounded answer for the current plan."""

    if plan.intent == "time_now":
        current = next((item for item in results if item.tool == "time.now" and item.ok), None)
        if current:
            return "现在是本机时间：" + _format_local_time(current.data) + "。"

    if plan.intent == "date_math":
        current = next((item for item in results if item.tool == "time.now" and item.ok), None)
        target = next((item for item in results if item.tool == "time.date_math" and item.ok), None)
        if target:
            prefix = ""
            if current:
                prefix = "现在是本机时间：" + _format_local_time(current.data) + "。\n"
            return (
                prefix
                + f"{target.data.get('offset_days')} 天后的日期是："
                + f"{target.data.get('target_cn')}，{target.data.get('weekday')}。"
            )

    if plan.intent == "weather":
        return (
            "这是实时天气问题，当前天气工具尚未启用，所以我不能凭空编天气。\n"
            "后续接入 Weather Tool 后，这类问题会自动调用天气接口。"
        )

    if plan.intent == "web_fact":
        corrections = plan.args.get("corrections") or []
        prefix = ""
        if corrections:
            prefix = f"我检测到你可能想问的是：{plan.normalized_query}\n\n"
        return (
            prefix
            + "这是需要事实来源或联网查询的问题，当前 Web Search 工具尚未启用。\n"
            + "因此我不能用本地模型直接编答案。接入联网搜索后，会先查询来源再回答。"
        )

    if plan.intent in ("project_knowledge", "catalog_knowledge"):
        repo_result = next(
            (item for item in results if item.tool == "repo_memory.search" and item.ok),
            None,
        )
        if not repo_result:
            return "我应该查询本地 Repo Memory，但当前没有拿到可用结果。请确认 repo_memory_service 已启动。"

        items = _extract_items(repo_result.data)
        if not items:
            return "我查询了本地 Repo Memory，但没有找到明确匹配资产。"

        lines = ["我已查询本地 Repo Memory，相关资产包括："]
        for item in items[:8]:
            name = (
                item.get("full_name")
                or item.get("repo")
                or item.get("name")
                or item.get("title")
                or item.get("source")
                or "unknown"
            )
            description = (
                item.get("description")
                or item.get("summary")
                or item.get("content")
                or item.get("text")
                or ""
            )
            clean_description = str(description).replace("\n", " ")[:180]
            lines.append(f"- {name}" + (f"：{clean_description}" if clean_description else ""))
        return "\n".join(lines)

    if plan.intent == "capability_status":
        return "\n".join(
            [
                "当前 MAOMIAI 是本地智能体平台 Demo Kernel，已经开始具备 Agent Runtime 能力。",
                "",
                "已具备：",
                "1. 桌面端与 Windows 打包；",
                "2. 本地模型下载、选择和推理；",
                "3. Repo Memory 资产库；",
                "4. GitHub Stars 与参考仓摘要；",
                "5. Agent Runtime Planner / Tool Router / Executor / Validator 雏形。",
                "",
                "待补齐：",
                "1. Web Search；",
                "2. Weather Tool；",
                "3. MCP Gateway；",
                "4. Graph Memory / Codebase Graph；",
                "5. 视频生成后端。",
            ]
        )

    if plan.intent == "local_chat":
        model_result = next(
            (item for item in results if item.tool == "model.generate" and item.ok),
            None,
        )
        if model_result:
            data = model_result.data
            return (
                data.get("response")
                or data.get("output")
                or data.get("text")
                or data.get("message")
                or str(data)
            )
        return "Agent Runtime 已接管该请求，但当前模型生成后端没有返回可用结果。"

    return ""
