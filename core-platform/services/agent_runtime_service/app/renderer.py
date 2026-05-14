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
        weather = next((item for item in results if item.tool == "weather.query" and item.ok), None)
        if not weather:
            error = next((item.error for item in results if item.tool == "weather.query" and item.error), None)
            return f"这是实时天气问题，但天气工具没有返回可用结果：{error or 'unknown error'}"
        current = weather.data.get("current") or {}
        daily = weather.data.get("daily") or []
        metadata = weather.data.get("metadata") or {}
        lines = [
            f"天气查询结果：{weather.data.get('resolved_location') or weather.data.get('location')}",
            f"- 温度：{current.get('temperature_2m')}°C，体感 {current.get('apparent_temperature')}°C",
            f"- 湿度：{current.get('relative_humidity_2m')}%",
            f"- 降水：{current.get('precipitation')} mm",
            f"- 风速：{current.get('wind_speed_10m')} km/h",
            f"- 天气代码：{current.get('weather_code')}",
            f"- 更新时间：{current.get('time')}",
        ]
        if daily:
            today = daily[0]
            lines.append(
                "今日预报："
                f"天气代码 {today.get('weather_code')}，"
                f"{today.get('temperature_min')}°C - {today.get('temperature_max')}°C，"
                f"降水 {today.get('precipitation_sum')} mm。"
            )
        if metadata.get("source_url"):
            lines.append(f"source: {metadata.get('source_url')}")
        return "\n".join(lines)

    if plan.intent == "restricted_action":
        blocked = next((item for item in results if item.data.get("requires_approval")), None)
        if blocked:
            return (
                "该操作属于受限工具调用，已被 Approval Gate 阻断。\n"
                f"approval_id: {blocked.data.get('approval_id')}\n"
                f"risk: {blocked.data.get('risk')}\n"
                "请在审批 API 中确认后再执行。"
            )
        return "该操作属于受限工具调用，但没有生成审批记录。"

    if plan.intent == "web_fact":
        corrections = plan.args.get("corrections") or []
        prefix = ""
        if corrections:
            prefix = f"我检测到你可能想问的是：{plan.normalized_query}\n\n"
        web_result = next((item for item in results if item.tool == "web.search" and item.ok), None)
        if web_result:
            items = _extract_items(web_result.data)
            if items:
                lines = [prefix + "我已联网搜索，相关证据如下："]
                for item in items[:5]:
                    title = item.get("title") or "-"
                    url = item.get("url") or "-"
                    snippet = item.get("snippet") or ""
                    snapshot_id = item.get("snapshot_id")
                    lines.append(f"- {title}\n  {url}")
                    if snapshot_id:
                        lines.append(f"  snapshot: {snapshot_id}")
                    if snippet:
                        lines.append(f"  摘要: {snippet[:180]}")
                return "\n".join(lines)
        error_result = next((item for item in results if item.tool == "web.search"), None)
        error = error_result.error if error_result else "web.search did not run"
        return prefix + f"这是需要事实来源的问题，但联网搜索没有返回可用结果：{error}"

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

    if plan.intent == "project_architecture_services":
        repo_result = next(
            (item for item in results if item.tool == "repo_memory.search" and item.ok),
            None,
        )
        if not repo_result:
            return "架构分析第 1 步：应该查询 Repo Memory，但当前没有拿到可用结果。"
        items = _extract_items(repo_result.data)
        lines = ["架构分析第 1 步：已查询服务与运行时资产。"]
        for item in items[:5]:
            name = item.get("full_name") or item.get("repo") or item.get("name") or item.get("title") or item.get("source") or "unknown"
            lines.append(f"- {name}")
        return "\n".join(lines)

    if plan.intent == "project_architecture_capabilities":
        catalog = next((item for item in results if item.tool == "catalog.search" and item.ok), None)
        skill_store = next((item for item in results if item.tool == "skill_store.list" and item.ok), None)
        workflow_store = next((item for item in results if item.tool == "workflow_store.list" and item.ok), None)
        return "\n".join(
            [
                "架构分析第 2 步：已检查能力目录、技能库和工作流库。",
                f"- catalog.search: {'ok' if catalog else 'unavailable'}",
                f"- skill_store.list: {'ok' if skill_store else 'unavailable'}",
                f"- workflow_store.list: {'ok' if workflow_store else 'unavailable'}",
            ]
        )

    if plan.intent == "project_architecture_summary":
        return "\n".join(
            [
                "架构分析第 3 步：当前 MAOMIAI 运行时由 Desktop、Agent Runtime、Repo Memory、Skill Store、Workflow Store、Model Gateway 组成。",
                "核心主链路已经收敛到 /agent/run；下一步需要补 approval、sandbox、run_store 增强和真正多步工具执行。",
            ]
        )

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
