from __future__ import annotations
from pathlib import Path
from datetime import datetime, timedelta
import concurrent.futures
import hashlib
import json

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

GEN_DIR = Path("/Users/mofamaomi/Documents/本地ai/generated/research")
CACHE_DIR = Path("/Users/mofamaomi/Documents/本地ai/core-platform/data/research_cache")
GATEWAY_URL = "http://127.0.0.1:18080/generate"

SEARCH_TIMEOUT = 12
AK_TIMEOUT = 12
LLM_TIMEOUT = 120
CACHE_TTL_MINUTES = 20

GEN_DIR.mkdir(parents=True, exist_ok=True)
CACHE_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def now_iso():
    return datetime.now().isoformat()


def write_json(payload: dict):
    out = GEN_DIR / f"research_{ts()}.json"
    out.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(out)


def cache_key(prefix: str, text: str) -> Path:
    digest = hashlib.sha256(f"{prefix}:{text}".encode("utf-8")).hexdigest()
    return CACHE_DIR / f"{prefix}_{digest}.json"


def load_cache(prefix: str, text: str):
    path = cache_key(prefix, text)
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        ts_raw = data.get("_cached_at")
        if not ts_raw:
            return None
        cached_at = datetime.fromisoformat(ts_raw)
        if datetime.now() - cached_at > timedelta(minutes=CACHE_TTL_MINUTES):
            return None
        return data.get("payload")
    except Exception:
        return None


def save_cache(prefix: str, text: str, payload: dict):
    path = cache_key(prefix, text)
    path.write_text(
        json.dumps({"_cached_at": now_iso(), "payload": payload}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def ask_model(prompt: str, timeout: int | None = None, model: str = "qwen2.5:7b"):
    """
    内部总结专用：直接打 model gateway，绕过 orchestrator / auto-router，
    避免 stock_report -> /ask -> auto-route -> stock_research -> plugin -> stock_report 递归。
    """
    if timeout is None:
        timeout = LLM_TIMEOUT
    r = requests.post(
        GATEWAY_URL,
        json={"model": model, "prompt": prompt},
        timeout=timeout
    )
    r.raise_for_status()
    data = r.json()
    # 兼容旧调用方仍然使用 .get("response", "")
    return {"response": data.get("response", "")}


def ddg_search(query: str, max_results: int = 5):
    from duckduckgo_search import DDGS

    rows = []
    with DDGS() as ddgs:
        for item in ddgs.text(query, max_results=max_results):
            rows.append(
                {
                    "title": item.get("title", "")[:240],
                    "href": item.get("href", ""),
                    "body": item.get("body", "")[:500],
                }
            )
    return rows


def safe_run(fn, timeout: int, default):
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(fn)
        try:
            return future.result(timeout=timeout)
        except Exception:
            return default


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/search")
def search(payload: dict):
    query = payload.get("query", "").strip()
    source = payload.get("source", "web")
    max_results = int(payload.get("max_results", 5))

    cached = load_cache("search", query)
    if cached:
        cached["cache_hit"] = True
        return cached

    results = []
    if query:
        results = safe_run(
            lambda: ddg_search(query, max_results=max_results),
            timeout=SEARCH_TIMEOUT,
            default=[{"title": "search_timeout_or_error", "href": "", "body": "search stage failed or timed out"}],
        )

    result = {
        "ok": True,
        "kind": "research_search",
        "research_scope": "general_web_research",
        "query": query,
        "source": source,
        "max_results": max_results,
        "results": results,
        "cache_hit": False,
    }
    result["output_path"] = write_json(result)
    save_cache("search", query, result)
    return result


@app.post("/news_summary")
def news_summary(payload: dict):
    topic = payload.get("topic", "").strip()
    notes = payload.get("notes", "")
    max_results = int(payload.get("max_results", 5))

    cache_id = f"{topic}|{notes}"
    cached = load_cache("news_summary", cache_id)
    if cached:
        cached["cache_hit"] = True
        return cached

    sources = []
    if topic:
        sources = safe_run(
            lambda: ddg_search(topic, max_results=max_results),
            timeout=SEARCH_TIMEOUT,
            default=[{"title": "search_timeout_or_error", "href": "", "body": "search stage failed or timed out"}],
        )

    source_text = "\n\n".join(
        [
            f"[{i+1}] 标题: {item.get('title', '')}\n链接: {item.get('href', '')}\n摘要: {item.get('body', '')}"
            for i, item in enumerate(sources[:4])
        ]
    )[:5000]

    summary = ""
    try:
        summary = ask_model(
            f"请基于以下新闻检索结果与附加素材，生成一段结构化新闻摘要，控制在 300 字以内。\n\n主题：{topic}\n\n检索结果：\n{source_text}\n\n附加素材：\n{notes}",
            timeout=LLM_TIMEOUT,
        ).get("response", "")
    except Exception as exc:
        summary = f"summary_error: {exc}"

    result = {
        "ok": True,
        "kind": "news_summary",
        "research_scope": "general_news_research",
        "topic": topic,
        "sources": sources,
        "notes": notes,
        "summary": summary,
        "cache_hit": False,
    }
    result["output_path"] = write_json(result)
    save_cache("news_summary", cache_id, result)
    return result


@app.post("/stock_report")
def stock_report(payload: dict):
    stock = payload.get("stock", "").strip()
    notes = payload.get("notes", "")
    lightweight = bool(payload.get("lightweight", True))

    cache_id = f"{stock}|{notes}|{lightweight}"
    cached = load_cache("stock_report", cache_id)
    if cached:
        cached["cache_hit"] = True
        return cached

    web_sources = []
    quotes = {}
    fundamentals = {}
    stages = {"web_search": "pending", "market_data": "pending", "llm_report": "pending"}

    if stock:
        web_sources = safe_run(
            lambda: ddg_search(stock, max_results=3 if lightweight else 5),
            timeout=SEARCH_TIMEOUT,
            default=[{"title": "search_timeout_or_error", "href": "", "body": "search stage failed or timed out"}],
        )
        stages["web_search"] = "done"

    def load_market():
        import akshare as ak

        output = {"quotes": {}, "fundamentals": {}}
        try:
            df = ak.stock_zh_a_spot_em()
            hit = df[df["名称"].astype(str).str.contains(stock, na=False)].head(2 if lightweight else 3)
            output["quotes"]["spot"] = hit.to_dict(orient="records")
        except Exception as exc:
            output["quotes"]["spot_error"] = str(exc)

        try:
            if stock.isdigit():
                info = ak.stock_individual_info_em(symbol=stock)
                rows = info.to_dict(orient="records")
                output["fundamentals"]["individual_info"] = rows[:6] if lightweight else rows
        except Exception as exc:
            output["fundamentals"]["individual_info_error"] = str(exc)
        return output

    market = safe_run(
        load_market,
        timeout=AK_TIMEOUT,
        default={
            "quotes": {"market_timeout_or_error": True},
            "fundamentals": {"market_timeout_or_error": True},
        },
    )
    quotes = market.get("quotes", {})
    fundamentals = market.get("fundamentals", {})
    stages["market_data"] = "done"

    source_text = "\n\n".join(
        [
            f"[{i+1}] 标题: {item.get('title', '')}\n链接: {item.get('href', '')}\n摘要: {item.get('body', '')}"
            for i, item in enumerate(web_sources[: 3 if lightweight else 5])
        ]
    )[: 4000 if lightweight else 8000]

    report = ""
    try:
        prompt = (
            f"请围绕以下股票主题生成一份{'轻量' if lightweight else '标准'}研究报告。"
            f"包含：概况、市场关注点、风险点、结论。"
            f"{'控制在 350 字以内。' if lightweight else ''}\n\n"
            f"股票/主题：{stock}\n\n"
            f"网页检索结果：\n{source_text}\n\n"
            f"行情/基本面数据：\n"
            f"{json.dumps({'quotes': quotes, 'fundamentals': fundamentals}, ensure_ascii=False)[: 6000 if lightweight else 10000]}\n\n"
            f"附加素材：\n{notes}"
        )
        report = ask_model(prompt, timeout=LLM_TIMEOUT).get("response", "")
        stages["llm_report"] = "done"
    except Exception as exc:
        report = f"report_error: {exc}"
        stages["llm_report"] = "error"

    result = {
        "ok": True,
        "kind": "stock_report",
        "research_scope": "stock_research",
        "stock": stock,
        "lightweight": lightweight,
        "stages": stages,
        "web_sources": web_sources,
        "quotes": quotes,
        "fundamentals": fundamentals,
        "notes": notes,
        "report": report,
        "cache_hit": False,
    }
    result["output_path"] = write_json(result)
    save_cache("stock_report", cache_id, result)
    return result
