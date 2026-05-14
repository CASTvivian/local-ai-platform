"""Public web search connector with optional browser snapshot capture."""

from __future__ import annotations

import hashlib
import html
import json
import re
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Callable, List

from .browser_models import BrowserFetchRequest
from .browser_runtime import fetch_url
from .execution_models import new_execution_record
from .execution_store import save_execution
from .web_search_models import WebSearchRequest, WebSearchResponse, WebSearchResultItem


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
WEB_SEARCH_ROOT = CORE_PLATFORM_ROOT / "data" / "web_search_runtime"
WEB_SEARCH_ROOT.mkdir(parents=True, exist_ok=True)


def _runtime_file(search_id: str) -> Path:
    return WEB_SEARCH_ROOT / f"{search_id}.json"


def _clean_text(value: str) -> str:
    text = html.unescape(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _unwrap_duckduckgo_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
        params = urllib.parse.parse_qs(parsed.query)
        if params.get("uddg"):
            return params["uddg"][0]
    return url


def _extract_duckduckgo_results(raw: str, limit: int) -> List[WebSearchResultItem]:
    items: List[WebSearchResultItem] = []
    patterns = [
        re.compile(r'<a[^>]+class="[^"]*result__a[^"]*"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.I | re.S),
        re.compile(r'<a[^>]+class="[^"]*result-link[^"]*"[^>]+href="([^"]+)"[^>]*>(.*?)</a>', re.I | re.S),
    ]
    for pattern in patterns:
        for match in pattern.finditer(raw):
            url = _unwrap_duckduckgo_url(html.unescape(match.group(1)))
            title = _clean_text(match.group(2))
            if not url or not title:
                continue
            items.append(WebSearchResultItem(title=title[:240], url=url, snippet=""))
            if len(items) >= limit:
                return items
    generic = re.compile(r'<a[^>]+href="(https?://[^"]+)"[^>]*>(.*?)</a>', re.I | re.S)
    seen: set[str] = set()
    for match in generic.finditer(raw):
        url = _unwrap_duckduckgo_url(html.unescape(match.group(1)))
        title = _clean_text(match.group(2))
        if not url or not title or url in seen or "duckduckgo.com" in urllib.parse.urlparse(url).netloc:
            continue
        seen.add(url)
        items.append(WebSearchResultItem(title=title[:240], url=url, snippet=""))
        if len(items) >= limit:
            break
    return items


def _extract_bing_results(raw: str, limit: int) -> List[WebSearchResultItem]:
    items: List[WebSearchResultItem] = []
    pattern = re.compile(r'<li class="b_algo"[\s\S]*?<a href="(https?://[^"]+)"[^>]*>(.*?)</a>', re.I)
    for match in pattern.finditer(raw):
        url = html.unescape(match.group(1))
        title = _clean_text(match.group(2))
        if not url or not title:
            continue
        items.append(WebSearchResultItem(title=title[:240], url=url, snippet=""))
        if len(items) >= limit:
            break
    return items


def _fetch_search_page(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MAOMIAI-AgentRuntime/0.1",
            "Accept": "text/html,application/xhtml+xml,text/plain,*/*",
        },
        method="GET",
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read(900000).decode("utf-8", errors="replace")


def _duckduckgo_html(query: str, limit: int) -> List[WebSearchResultItem]:
    url = "https://duckduckgo.com/html/?" + urllib.parse.urlencode({"q": query})
    return _extract_duckduckgo_results(_fetch_search_page(url), limit)


def _duckduckgo_lite(query: str, limit: int) -> List[WebSearchResultItem]:
    url = "https://lite.duckduckgo.com/lite/?" + urllib.parse.urlencode({"q": query})
    return _extract_duckduckgo_results(_fetch_search_page(url), limit)


def _bing_html(query: str, limit: int) -> List[WebSearchResultItem]:
    url = "https://www.bing.com/search?" + urllib.parse.urlencode({"q": query})
    return _extract_bing_results(_fetch_search_page(url), limit)


def _search_with_fallbacks(query: str, limit: int) -> tuple[List[WebSearchResultItem], str, list[str]]:
    providers: list[tuple[str, Callable[[str, int], List[WebSearchResultItem]]]] = [
        ("duckduckgo_html", _duckduckgo_html),
        ("duckduckgo_lite", _duckduckgo_lite),
        ("bing_html", _bing_html),
    ]
    errors: list[str] = []
    for name, provider in providers:
        try:
            items = provider(query, limit)
            if items:
                return items, name, errors
            errors.append(f"{name}: no results parsed")
        except Exception as exc:
            errors.append(f"{name}: {exc}")
    return [], "none", errors


def _save_search_audit(request: WebSearchRequest, payload: dict) -> None:
    save_execution(
        new_execution_record(
            run_id=request.run_id,
            session_id=request.session_id,
            tool="web.search",
            command=request.query,
            status="completed" if payload.get("ok") else "failed",
            ok=bool(payload.get("ok")),
            stdout=json.dumps(
                {
                    "query": payload.get("query"),
                    "items": [
                        {"title": item.get("title"), "url": item.get("url"), "snapshot_id": item.get("snapshot_id")}
                        for item in payload.get("items", [])[:5]
                    ],
                    "metadata": payload.get("metadata"),
                },
                ensure_ascii=False,
            ),
            error=payload.get("error"),
            metadata={"source": "web_search_runtime", **(payload.get("metadata") or {})},
        )
    )


def search_web(request: WebSearchRequest) -> dict:
    """Search public web and optionally fetch the top result."""

    search_id = hashlib.sha256(f"{request.query}:{datetime.utcnow().isoformat()}".encode("utf-8")).hexdigest()[:24]
    try:
        limit = max(1, min(int(request.limit or 5), 10))
        items, provider, provider_errors = _search_with_fallbacks(request.query, limit)
        if request.fetch_top and items:
            top = items[0]
            fetched = fetch_url(
                BrowserFetchRequest(
                    url=top.url,
                    run_id=request.run_id,
                    session_id=request.session_id,
                    timeout=20,
                    max_bytes=300000,
                )
            )
            if fetched.get("ok"):
                top.snapshot_id = fetched.get("snapshot_id")
                top.snippet = (fetched.get("text") or "")[:500]
            else:
                top.snippet = fetched.get("error") or ""
        response = WebSearchResponse(
            ok=bool(items),
            query=request.query,
            items=items,
            error=None if items else "; ".join(provider_errors) or "no search results",
            metadata={
                "search_id": search_id,
                "provider": provider,
                "provider_errors": provider_errors,
                "created_at": datetime.utcnow().isoformat(),
                "run_id": request.run_id,
                "session_id": request.session_id,
            },
        )
        payload = response.model_dump()
        _runtime_file(search_id).write_text(response.model_dump_json(indent=2), encoding="utf-8")
        _save_search_audit(request, payload)
        return payload
    except Exception as exc:
        response = WebSearchResponse(
            ok=False,
            query=request.query,
            error=str(exc),
            metadata={
                "search_id": search_id,
                "provider": "none",
                "created_at": datetime.utcnow().isoformat(),
                "run_id": request.run_id,
                "session_id": request.session_id,
            },
        )
        payload = response.model_dump()
        _save_search_audit(request, payload)
        return payload


def list_web_searches(limit: int = 100) -> dict:
    """List persisted web searches without loading full snippets."""

    items = []
    for path in sorted(WEB_SEARCH_ROOT.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        items.append(
            {
                "search_id": data.get("metadata", {}).get("search_id"),
                "query": data.get("query"),
                "ok": data.get("ok"),
                "item_count": len(data.get("items") or []),
                "provider": data.get("metadata", {}).get("provider"),
                "created_at": data.get("metadata", {}).get("created_at"),
                "run_id": data.get("metadata", {}).get("run_id"),
                "session_id": data.get("metadata", {}).get("session_id"),
            }
        )
        if len(items) >= limit:
            break
    return {"ok": True, "items": items}
