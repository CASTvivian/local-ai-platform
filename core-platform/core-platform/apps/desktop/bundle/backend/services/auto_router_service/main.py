from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import requests
import json
import hashlib
from datetime import datetime

MODEL_GATEWAY_URL = "http://127.0.0.1:18080/generate"
DATA_DIR = Path("/Users/mofamaomi/Documents/本地ai/core-platform/data/router")
CACHE_PATH = DATA_DIR / "route_cache.json"
STATS_PATH = DATA_DIR / "route_stats.json"
LOG_PATH = DATA_DIR / "route_log.jsonl"

DATA_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

RULES = [
    ("stock_research", ["A股", "股票", "大盘", "k线", "日线", "涨停", "跌停", "市场", "今天", "最新", "新闻", "个股"]),
    ("web_research", ["联网", "搜索", "查询", "查一下", "搜一下", "最新消息", "实时", "帮我找资料"]),
    ("browser_use_task", ["打开网页", "访问网站", "去这个网站", "网页登录", "在网页上操作", "帮我去网站上做事", "打开这个页面", "浏览这个网站"]),
    ("stagehand_task", ["提取网页内容", "从页面提取", "抽取网页", "网页内容抓取", "抓取网页信息", "提取页面信息"]),
    ("skyvern_task", ["自动填写表单", "网页表单", "自动提交", "网站流程自动化", "帮我填表单", "自动走网页流程"]),
    ("rag_impl", ["pdf", "文件", "文档", "表格", "总结这个文件", "分析这个文件", "上传的文件", "帮我读这个文档"]),
    ("vision_impl", ["图片", "图像", "看图", "识别图片", "分析图片", "这张图", "看看图片里有什么"]),
    ("tts_impl", ["语音", "播报", "朗读", "转语音", "念出来", "读出来", "配音", "文字转语音", "把这段话读出来", "生成音频", "做成音频", "合成语音"]),
    ("finance_impl", ["量化", "因子", "回测", "策略研究", "金融研究", "市场分析", "研究报告"]),
    ("hyperframes_render", ["模板视频", "成片渲染", "图文转视频", "字幕视频", "渲染视频模板", "口播视频", "research to video"]),
    ("video_impl", ["生成视频", "做个视频", "视频生成", "视频动画", "文生视频", "短片", "做成动画", "做个动画", "做一段视频"]),
    ("image", ["生成图片", "画一张", "出图", "做图", "海报", "插画", "做一张图"]),
    ("code", ["写代码", "修代码", "报错", "接口", "函数", "脚本", "bug", "改代码"]),
    ("workflow", ["计划", "复盘", "评审", "review", "qa", "retro", "帮我规划"])
]

VALID_TASKS = [
    "general", "code", "image", "video_impl", "hyperframes_render", "vision_impl", "rag_impl",
    "finance_impl", "tts_impl", "stock_research", "web_research",
    "browser_use_task", "stagehand_task", "skyvern_task", "workflow"
]

def now():
    return datetime.now().isoformat()

def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default

def save_json(path: Path, obj):
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def prompt_key(prompt: str):
    return hashlib.sha256(prompt.strip().lower().encode("utf-8")).hexdigest()

def log_route(item: dict):
    with LOG_PATH.open("a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

def update_stats(task: str, source: str):
    stats = load_json(STATS_PATH, {"total": 0, "by_task": {}, "by_source": {}})
    stats["total"] += 1
    stats["by_task"][task] = stats["by_task"].get(task, 0) + 1
    stats["by_source"][source] = stats["by_source"].get(source, 0) + 1
    save_json(STATS_PATH, stats)

def rule_route(prompt: str):
    text = (prompt or "").lower()
    for target, keywords in RULES:
        if any(k.lower() in text for k in keywords):
            return target, f"keyword_match:{target}"
    return "general", "fallback_general"

def llm_route(prompt: str):
    route_prompt = f"""你是一个任务路由分类器。
请只返回一个任务类型，不要解释，不要输出其他内容。

可选任务类型：
{", ".join(VALID_TASKS)}

分类规则：
- 涉及代码编写、修复、接口、脚本、报错 => code
- 涉及图片生成、画图、海报、插画 => image
- 涉及视频生成、动画、短片、文生视频 => video_impl
- 涉及图片理解、看图、识图、图像分析 => vision_impl
- 涉及文件总结、PDF、文档问答、表格分析 => rag_impl
- 涉及金融研究、量化、因子、市场分析 => finance_impl
- 涉及股票、A股、大盘、日线、K线、个股分析 => stock_research
- 涉及联网搜索、查资料、最新消息 => web_research
- 涉及打开网站、网页导航、网页操作 => browser_use_task
- 涉及提取网页内容、页面信息抽取 => stagehand_task
- 涉及自动填写网页表单、自动提交网页流程 => skyvern_task
- 涉及朗读、转语音、播报、配音、生成音频 => tts_impl
- 涉及计划、复盘、评审 => workflow
- 其他 => general

用户输入：
{prompt}
""".strip()

    try:
        r = requests.post(
            MODEL_GATEWAY_URL,
            json={"model": "qwen2.5:7b", "prompt": route_prompt},
            timeout=60
        )
        r.raise_for_status()
        text = r.json().get("response", "").strip()
        text = text.splitlines()[0].strip().replace("`", "").replace('"', "").replace("'", "")
        if text in VALID_TASKS:
            return text, f"llm_route:{text}"
        return None, f"llm_invalid:{text}"
    except Exception as e:
        return None, f"llm_error:{e}"

@app.get("/health")
def health():
    return {"ok": True}

@app.get("/health/details")
def health_details():
    stats = load_json(STATS_PATH, {"total": 0, "by_task": {}, "by_source": {}})
    cache = load_json(CACHE_PATH, {})
    return {
        "ok": True,
        "rule_count": len(RULES),
        "valid_tasks": VALID_TASKS,
        "cache_entries": len(cache),
        "stats": stats,
        "rules": [{"target": target, "keywords": keywords} for target, keywords in RULES]
    }

@app.get("/stats")
def stats():
    return load_json(STATS_PATH, {"total": 0, "by_task": {}, "by_source": {}})

@app.post("/route")
def route(payload: dict):
    prompt = payload.get("prompt", "") or ""
    task_type = payload.get("task_type", "auto")

    if task_type and task_type != "auto":
        update_stats(task_type, "manual")
        log_route({"ts": now(), "prompt": prompt, "task_type": task_type, "reason": "manual_task_type"})
        return {"ok": True, "task_type": task_type, "reason": "manual_task_type"}

    cache = load_json(CACHE_PATH, {})
    key = prompt_key(prompt)
    if key in cache:
        hit = cache[key]
        update_stats(hit["task_type"], "cache")
        log_route({"ts": now(), "prompt": prompt, "task_type": hit["task_type"], "reason": f'cache:{hit["reason"]}'})
        return {"ok": True, "task_type": hit["task_type"], "reason": f'cache:{hit["reason"]}'}

    llm_task, llm_reason = llm_route(prompt)
    if llm_task:
        cache[key] = {"task_type": llm_task, "reason": llm_reason}
        save_json(CACHE_PATH, cache)
        update_stats(llm_task, "llm")
        log_route({"ts": now(), "prompt": prompt, "task_type": llm_task, "reason": llm_reason})
        return {"ok": True, "task_type": llm_task, "reason": llm_reason}

    rule_task, rule_reason = rule_route(prompt)
    cache[key] = {"task_type": rule_task, "reason": f"{llm_reason};{rule_reason}"}
    save_json(CACHE_PATH, cache)
    update_stats(rule_task, "rule")
    log_route({"ts": now(), "prompt": prompt, "task_type": rule_task, "reason": f"{llm_reason};{rule_reason}"})
    return {"ok": True, "task_type": rule_task, "reason": f"{llm_reason};{rule_reason}"}
