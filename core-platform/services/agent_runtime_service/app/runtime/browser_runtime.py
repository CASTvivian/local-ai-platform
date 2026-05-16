"""Read-only browser fetch runtime with SSRF protections.

Provides crawl and scrape capabilities for public web pages.
Supports playwright-style page snapshotting via urllib fetch
(no headless browser dependency required).
"""

from __future__ import annotations

import hashlib
import ipaddress
import json
import re
import socket
import ssl
import urllib.request
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

from .browser_models import BrowserFetchRequest
from .execution_models import new_execution_record
from .execution_store import save_execution


CORE_PLATFORM_ROOT = Path(__file__).resolve().parents[4]
BROWSER_ROOT = CORE_PLATFORM_ROOT / "data" / "browser_runtime"
BROWSER_ROOT.mkdir(parents=True, exist_ok=True)

BLOCKED_HOSTS = {
    "localhost",
    "localhost.localdomain",
    "127.0.0.1",
    "0.0.0.0",
    "::1",
}


def _snapshot_file(snapshot_id: str) -> Path:
    return BROWSER_ROOT / f"{snapshot_id}.json"


def _is_blocked_ip(ip: str) -> bool:
    try:
        address = ipaddress.ip_address(ip)
    except Exception:
        return True
    return (
        address.is_private
        or address.is_loopback
        or address.is_link_local
        or address.is_multicast
        or address.is_unspecified
    )


def _is_benchmark_proxy_ip(ip: str) -> bool:
    """Allow DNS-proxy benchmark net only when reached via a hostname.

    Some local networks map public domains to 198.18.0.0/15 proxy addresses.
    Direct requests to those IPs are still blocked below.
    """

    try:
        return ipaddress.ip_address(ip) in ipaddress.ip_network("198.18.0.0/15")
    except Exception:
        return False


def _validate_url(url: str):
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError("only http/https urls are allowed")
    if not parsed.hostname:
        raise ValueError("missing hostname")
    host = parsed.hostname.lower()
    if host in BLOCKED_HOSTS:
        raise ValueError("blocked localhost/private host")
    host_is_ip = False
    try:
        ipaddress.ip_address(host)
        host_is_ip = True
    except Exception:
        host_is_ip = False
    try:
        infos = socket.getaddrinfo(host, parsed.port or (443 if parsed.scheme == "https" else 80))
    except Exception as exc:
        raise ValueError(f"dns resolve failed: {exc}") from exc
    for info in infos:
        ip = info[4][0]
        if _is_benchmark_proxy_ip(ip) and not host_is_ip:
            continue
        if _is_blocked_ip(ip):
            raise ValueError(f"blocked private/local ip: {ip}")
    return parsed


def _extract_title(html: str) -> str | None:
    match = re.search(r"<title[^>]*>(.*?)</title>", html, flags=re.I | re.S)
    if not match:
        return None
    return re.sub(r"\s+", " ", match.group(1)).strip()[:300]


def _html_to_text(html: str) -> str:
    text = re.sub(r"<script[\s\S]*?</script>", " ", html, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = (
        text.replace("&nbsp;", " ")
        .replace("&amp;", "&")
        .replace("&lt;", "<")
        .replace("&gt;", ">")
        .replace("&quot;", '"')
    )
    return re.sub(r"\s+", " ", text).strip()


def _save_browser_audit(request: BrowserFetchRequest, result: dict) -> None:
    save_execution(
        new_execution_record(
            approval_id=None,
            run_id=request.run_id,
            session_id=request.session_id,
            tool="browser.fetch",
            command=request.url,
            status="completed" if result.get("ok") else "failed",
            ok=bool(result.get("ok")),
            stdout=json.dumps(
                {
                    "snapshot_id": result.get("snapshot_id"),
                    "url": result.get("url"),
                    "status_code": result.get("status_code"),
                    "title": result.get("title"),
                },
                ensure_ascii=False,
            ),
            error=result.get("error"),
            sandbox_id=result.get("snapshot_id"),
            metadata={
                "source": "browser_runtime",
                "snapshot_id": result.get("snapshot_id"),
                **(result.get("metadata") or {}),
            },
        )
    )


def fetch_url(request: BrowserFetchRequest) -> dict:
    """Fetch a public webpage into a local snapshot."""

    try:
        parsed = _validate_url(request.url)
        http_request = urllib.request.Request(
            request.url,
            headers={
                "User-Agent": "MAOMIAI-AgentRuntime/0.1",
                "Accept": "text/html,application/xhtml+xml,text/plain,application/json;q=0.9,*/*;q=0.8",
            },
            method="GET",
        )
        context = ssl.create_default_context()
        with urllib.request.urlopen(http_request, timeout=request.timeout, context=context) as response:
            status_code = getattr(response, "status", None)
            content_type = response.headers.get("content-type", "")
            raw = response.read(request.max_bytes + 1)
        truncated = len(raw) > request.max_bytes
        raw = raw[: request.max_bytes]
        body = raw.decode("utf-8", errors="replace")
        title = None
        readable_text = body
        if "html" in content_type.lower() or "<html" in body.lower():
            title = _extract_title(body)
            readable_text = _html_to_text(body)
        snapshot_id = hashlib.sha256(
            f"{request.url}:{datetime.utcnow().isoformat()}".encode("utf-8")
        ).hexdigest()[:24]
        snapshot = {
            "snapshot_id": snapshot_id,
            "url": request.url,
            "host": parsed.hostname,
            "status_code": status_code,
            "content_type": content_type,
            "title": title,
            "text": readable_text[:50000],
            "truncated": truncated,
            "created_at": datetime.utcnow().isoformat(),
            "run_id": request.run_id,
            "session_id": request.session_id,
            "metadata": {
                "runtime": "browser.fetch",
                "max_bytes": request.max_bytes,
            },
        }
        _snapshot_file(snapshot_id).write_text(
            json.dumps(snapshot, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        result = {
            "ok": True,
            "snapshot_id": snapshot_id,
            "url": request.url,
            "status_code": status_code,
            "title": title,
            "text": readable_text[:12000],
            "metadata": {
                "content_type": content_type,
                "truncated": truncated,
                "snapshot_file": str(_snapshot_file(snapshot_id)),
            },
        }
        _save_browser_audit(request, result)
        return result
    except Exception as exc:
        result = {
            "ok": False,
            "url": request.url,
            "error": str(exc),
            "metadata": {"runtime": "browser.fetch"},
        }
        _save_browser_audit(request, result)
        return result


def load_snapshot(snapshot_id: str) -> dict:
    """Load one browser snapshot."""

    path = _snapshot_file(snapshot_id)
    if not path.exists():
        return {"ok": False, "snapshot_id": snapshot_id, "error": "snapshot not found"}
    return {"ok": True, "snapshot": json.loads(path.read_text(encoding="utf-8"))}


def list_snapshots(limit: int = 100) -> dict:
    """List browser snapshots without loading full page text."""

    items = []
    for path in sorted(BROWSER_ROOT.glob("*.json"), key=lambda item: item.stat().st_mtime, reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        items.append(
            {
                "snapshot_id": data.get("snapshot_id"),
                "url": data.get("url"),
                "title": data.get("title"),
                "status_code": data.get("status_code"),
                "created_at": data.get("created_at"),
                "run_id": data.get("run_id"),
                "session_id": data.get("session_id"),
            }
        )
        if len(items) >= limit:
            break
    return {"ok": True, "items": items}
