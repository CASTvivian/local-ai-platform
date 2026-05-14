"""MCP-style runtime tool invoker."""

from __future__ import annotations

import json
import urllib.parse
import urllib.request
from typing import Any, Dict

from ..runtime.browser_models import BrowserFetchRequest
from ..runtime.browser_runtime import fetch_url
from ..runtime.filesystem_sandbox import list_files, read_file
from ..runtime.web_search_models import WebSearchRequest
from ..runtime.web_search_runtime import search_web
from ..runtime.weather_models import WeatherQueryRequest
from ..runtime.weather_runtime import query_weather
from ..security.guard import guard_tool
from .models import MCPInvokeRequest, MCPInvokeResult
from .registry import get_tool


def _http_invoke(endpoint: str, method: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    """Invoke an HTTP-backed tool and normalize JSON or text output."""

    upper_method = method.upper()
    url = endpoint
    data = None
    headers = {}
    if upper_method == "GET":
        if arguments:
            url = url + "?" + urllib.parse.urlencode(arguments)
    else:
        data = json.dumps(arguments, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    request = urllib.request.Request(url, data=data, headers=headers, method=upper_method)
    with urllib.request.urlopen(request, timeout=20) as response:
        raw = response.read().decode("utf-8", errors="ignore")
    try:
        parsed = json.loads(raw)
        if isinstance(parsed, dict):
            return parsed
        return {"items": parsed}
    except Exception:
        return {"raw": raw}


def invoke_mcp(request: MCPInvokeRequest) -> MCPInvokeResult:
    """Invoke a registered tool through the unified runtime registry."""

    tool = get_tool(request.tool)
    if not tool:
        return MCPInvokeResult(ok=False, tool=request.tool, error="tool not found")

    if not tool.enabled or tool.method.upper() == "DISABLED":
        return MCPInvokeResult(ok=False, tool=request.tool, error="tool disabled")

    arguments = {
        **request.arguments,
        "run_id": request.run_id,
        "session_id": request.session_id,
    }

    if tool.requires_approval:
        blocked = guard_tool(tool.name, arguments)
        if blocked:
            return MCPInvokeResult(
                ok=False,
                tool=request.tool,
                error="approval required",
                approval_required=True,
                approval_id=blocked.data.get("approval_id"),
                result=blocked.data,
            )

    if tool.method.upper() == "LOCAL":
        if tool.name == "filesystem.read":
            result = read_file(
                sandbox_id=str(request.arguments.get("sandbox_id") or ""),
                path=str(request.arguments.get("path") or ""),
            )
            return MCPInvokeResult(ok=bool(result.get("ok")), tool=request.tool, result=result, error=result.get("message"))
        if tool.name == "filesystem.list":
            result = list_files(
                sandbox_id=str(request.arguments.get("sandbox_id") or ""),
                path=str(request.arguments.get("path") or "."),
            )
            return MCPInvokeResult(ok=bool(result.get("ok")), tool=request.tool, result=result, error=result.get("message"))
        if tool.name == "browser.fetch":
            result = fetch_url(
                BrowserFetchRequest(
                    url=str(request.arguments.get("url") or ""),
                    run_id=request.run_id,
                    session_id=request.session_id,
                    timeout=int(request.arguments.get("timeout") or 20),
                    max_bytes=int(request.arguments.get("max_bytes") or 300000),
                )
            )
            return MCPInvokeResult(ok=bool(result.get("ok")), tool=request.tool, result=result, error=result.get("error"))
        if tool.name == "web.search":
            result = search_web(
                WebSearchRequest(
                    query=str(request.arguments.get("query") or ""),
                    run_id=request.run_id,
                    session_id=request.session_id,
                    limit=int(request.arguments.get("limit") or 5),
                    fetch_top=bool(request.arguments.get("fetch_top", True)),
                )
            )
            return MCPInvokeResult(ok=bool(result.get("ok")), tool=request.tool, result=result, error=result.get("error"))
        if tool.name == "weather.query":
            result = query_weather(
                WeatherQueryRequest(
                    location=str(request.arguments.get("location") or ""),
                    run_id=request.run_id,
                    session_id=request.session_id,
                    days=int(request.arguments.get("days") or 1),
                )
            )
            return MCPInvokeResult(ok=bool(result.get("ok")), tool=request.tool, result=result, error=result.get("error"))
        return MCPInvokeResult(
            ok=False,
            tool=request.tool,
            error="local tool requires approval execution path",
        )

    if not tool.endpoint:
        return MCPInvokeResult(ok=False, tool=request.tool, error="tool endpoint missing")

    try:
        result = _http_invoke(tool.endpoint, tool.method, request.arguments)
        return MCPInvokeResult(ok=True, tool=request.tool, result=result)
    except Exception as exc:
        return MCPInvokeResult(ok=False, tool=request.tool, error=str(exc))
