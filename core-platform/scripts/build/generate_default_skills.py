#!/usr/bin/env python3
"""
C26-SKILL-BRAIN-DEFAULT-A: Generate default_skills.json from brain assets.

Sources:
  - data/brain_assets/manifests/brain_asset_index.json  (147 indexed repos)
  - data/github_stars/CASTvivian_starred_repos.json     (all starred repos)
  - data/repo_memory/brain_asset_seed.json               (cross-reference)

Each generated skill includes:
  - id, title, source_path, source_type, enabled_by_default
  - tags (mapped from brain buckets + original tags → skill categories)
  - description, tools, risk, created_at
"""

import json
import re
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent.parent.parent  # core-platform/

# ── Sources ──────────────────────────────────────────────────────────
ASSET_INDEX = ROOT / "data/brain_assets/manifests/brain_asset_index.json"
STARS_JSON = ROOT / "data/github_stars/CASTvivian_starred_repos.json"
SEED_JSON = ROOT / "data/repo_memory/brain_asset_seed.json"
MODEL_CATALOG = ROOT / "data/brain_assets/model_catalog"

# ── Outputs ──────────────────────────────────────────────────────────
OUT_JSON = ROOT / "data/skill_brain/default_skills.json"
AUDIT_JSON = ROOT / "data/agent_core_audit/c26/skill_brain/c26_skill_brain_default_audit.json"


# ── Tag mapping: brain bucket / original tag → skill category ────────
BUCKET_MAP = {
    "agent": "agent_runtime",
    "rag": "memory",
    "mcp": "mcp_tool",
    "llm_runtime": "local_model",
    "ui": "ui_component",
    "video": "browser_agent",
    "security": "security",
    "code": "code_agent",
}

KEYWORD_MAP = [
    ("code_agent", ["coding-agent", "code-generation", "code-editor", "copilot", "ide", "lsp", "code-review"]),
    ("mcp_tool", ["mcp", "tool-server", "stdio-transport"]),
    ("browser_agent", ["browser-automation", "web-crawler", "web-scraping", "playwright", "puppeteer", "headless-browser"]),
    ("workflow", ["workflow", "automation", "pipeline", "orchestration", "langgraph", "langchain"]),
    ("local_model", ["llm", "ollama", "qwen", "embedding-model", "inference-engine", "transformer"]),
    ("memory", ["memory", "rag", "vector-db", "knowledge-graph", "retrieval-augmented"]),
    ("ui_component", ["react", "vue", "tauri", "desktop-app", "frontend", "design-system", "component-lib"]),
    ("evaluation", ["eval", "benchmark", "metric"]),
    ("security", ["sandbox", "approval", "policy", "guard", "cybersecurity"]),
    ("agent_runtime", ["agent", "autonomous", "planner", "executor", "harness", "agentic"]),
    ("prompt_framework", ["prompt-engineering", "skill-framework", "claude-code", "codex-cli", "instinct"]),
]


def _word_match(keyword: str, corpus: str) -> bool:
    """Match keyword as a whole word or hyphenated compound in corpus."""
    # For multi-word keywords like "coding-agent", split and check each part
    parts = keyword.split("-")
    return all(re.search(rf"\b{re.escape(p)}\b", corpus) for p in parts)


def classify(buckets: list[str], tags: list[str], text: str) -> list[str]:
    """Classify a repo into skill categories using buckets, tags, and text."""
    result = set()

    # 1) Bucket-based classification (highest priority)
    for b in buckets:
        if b in BUCKET_MAP:
            result.add(BUCKET_MAP[b])

    # 2) Tag + text keyword matching with word-boundary
    corpus = " ".join(tags).lower() + " " + text.lower()
    for cat, keywords in KEYWORD_MAP:
        if any(_word_match(kw, corpus) for kw in keywords):
            result.add(cat)

    # 3) Fallback: check original tags for specific domains
    tag_set = set(t.lower() for t in tags)
    if tag_set & {"mcp", "mcp-server"}:
        result.add("mcp_tool")
    if tag_set & {"agent", "multi-agent", "ai-agent", "autonomous-agent"}:
        result.add("agent_runtime")
    if tag_set & {"llm", "large-language-model", "llms"}:
        result.add("local_model")
    if tag_set & {"rag", "vector", "knowledge-graph", "retrieval"}:
        result.add("memory")
    if tag_set & {"browser", "web-scraping", "crawler", "playwright"}:
        result.add("browser_agent")
    if tag_set & {"security", "cybersecurity", "sandbox", "vulnerability"}:
        result.add("security")

    return sorted(result) if result else ["general_skill"]


def title_from_name(repo_name: str) -> str:
    """Convert repo_name like '666ghj/MiroFish' → 'MiroFish'."""
    name = repo_name.split("/")[-1] if "/" in repo_name else repo_name
    name = re.sub(r"[_\-]+", " ", name).strip()
    return name[:1].upper() + name[1:] if name else repo_name


def make_skill_id(asset_id: str) -> str:
    """Normalize asset_id into a valid skill id."""
    sid = re.sub(r"[^a-zA-Z0-9]+", "_", asset_id).strip("_").lower()
    # Remove brain_ prefix and keep meaningful part
    if sid.startswith("brain_"):
        sid = sid[6:]
    return ("skill_" + sid)[:120]


def load_json(path: Path) -> dict | list:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    items = []
    seen_ids = set()

    # ── Source 1: brain_asset_index.json (primary, 147 repos) ───────
    asset_index = load_json(ASSET_INDEX)
    asset_items = asset_index.get("items", []) if isinstance(asset_index, dict) else []

    for entry in asset_items:
        asset_id = entry.get("asset_id", "")
        skill_id = make_skill_id(asset_id)
        if skill_id in seen_ids:
            continue
        seen_ids.add(skill_id)

        repo = entry.get("repo", entry.get("repo_name", ""))
        buckets = entry.get("buckets", [])
        tags = entry.get("tags", [])
        desc = entry.get("description", "")
        stars = entry.get("stars", 0)
        language = entry.get("language", "")
        html_url = entry.get("html_url", "")
        local_path = entry.get("local_path", "")
        summary_file = entry.get("summary_file", "")

        # Read summary for richer classification
        summary_text = ""
        if summary_file:
            sf = ROOT.parent / summary_file  # path relative to project root
            if not sf.exists():
                sf = ROOT / summary_file  # try relative to core-platform
            if sf.exists():
                try:
                    summary_text = sf.read_text(encoding="utf-8", errors="ignore")[:2000]
                except Exception:
                    pass

        skill_tags = classify(buckets, tags, desc + " " + summary_text)

        item = {
            "id": skill_id,
            "title": title_from_name(repo),
            "source_path": local_path or f"brain_assets/{asset_id}",
            "source_type": "brain_asset",
            "source_repo": repo,
            "html_url": html_url,
            "enabled_by_default": True,
            "tags": skill_tags,
            "buckets": buckets,
            "original_tags": tags[:15],
            "description": (desc or "")[:400],
            "language": language,
            "stars": stars,
            "tools": ["repo_memory.search", "capability.match", "model.generate"],
            "risk": "safe",
            "created_at": now,
        }
        items.append(item)

    # ── Source 2: CASTvivian_starred_repos.json (supplement) ────────
    stars_data = load_json(STARS_JSON)
    if isinstance(stars_data, list):
        for entry in stars_data:
            full_name = entry.get("full_name", "")
            # Generate ID from full_name
            raw_id = re.sub(r"[^a-zA-Z0-9]+", "_", full_name).strip("_").lower()
            skill_id = ("skill_" + raw_id)[:120]
            if skill_id in seen_ids:
                continue
            seen_ids.add(skill_id)

            desc = entry.get("description", "") or ""
            topics = entry.get("topics", [])
            language = entry.get("language", "") or ""
            stars = entry.get("stars", 0)
            html_url = entry.get("html_url", "")
            clone_url = entry.get("clone_url", "")

            skill_tags = classify([], topics, desc + " " + language)

            item = {
                "id": skill_id,
                "title": title_from_name(full_name),
                "source_path": f"github_stars/{raw_id}",
                "source_type": "github_star",
                "source_repo": full_name,
                "html_url": html_url,
                "enabled_by_default": True,
                "tags": skill_tags,
                "buckets": [],
                "original_tags": topics[:15],
                "description": desc[:400],
                "language": language,
                "stars": stars,
                "tools": ["repo_memory.search", "capability.match", "model.generate"],
                "risk": "safe",
                "created_at": now,
            }
            items.append(item)

    # ── Source 3: repo_memory/brain_asset_seed.json (cross-ref) ────
    seed_data = load_json(SEED_JSON)
    seed_entries = seed_data.get("entries", []) if isinstance(seed_data, dict) else []
    for entry in seed_entries:
        asset_id = entry.get("asset_id", "")
        skill_id = make_skill_id(asset_id)
        # Cross-reference: if already exists, enrich; otherwise add
        existing = next((i for i, x in enumerate(items) if x["id"] == skill_id), None)
        if existing is not None:
            # Enrich with repo_memory knowledge
            knowledge = entry.get("knowledge", {})
            if knowledge and not items[existing].get("description"):
                items[existing]["description"] = (knowledge.get("title", "") + ": " + knowledge.get("content", "")[:300]).strip()[:400]
            # Add repo_memory tags
            rm_tags = knowledge.get("tags", [])
            if rm_tags:
                extra = classify([], rm_tags, " ".join(rm_tags))
                current = set(items[existing]["tags"])
                current.update(extra)
                items[existing]["tags"] = sorted(current)
            continue

        # New entry from seed
        if skill_id in seen_ids:
            continue
        seen_ids.add(skill_id)

        repo_name = entry.get("repo_name", "")
        desc = entry.get("description", "")
        tags = entry.get("tags", [])
        knowledge = entry.get("knowledge", {})

        skill_tags = classify([], tags, desc)

        item = {
            "id": skill_id,
            "title": title_from_name(repo_name),
            "source_path": entry.get("repo_path", f"repo_memory/{asset_id}"),
            "source_type": "repo_memory",
            "source_repo": repo_name,
            "html_url": "",
            "enabled_by_default": True,
            "tags": skill_tags,
            "buckets": [],
            "original_tags": tags[:15],
            "description": (desc or knowledge.get("title", ""))[:400],
            "language": "",
            "stars": 0,
            "tools": ["repo_memory.search", "capability.match", "model.generate"],
            "risk": "safe",
            "created_at": now,
        }
        items.append(item)

    # ── Sort by stars descending ────────────────────────────────────
    items.sort(key=lambda x: x.get("stars", 0), reverse=True)

    # ── Generate output ─────────────────────────────────────────────
    result = {
        "version": "c26-skill-brain-default-a",
        "generated_at": now,
        "description": "Default skills generated from local brain assets, GitHub stars, and repository memory.",
        "source_summary": {
            "brain_asset_index": len(asset_items),
            "github_stars": len(stars_data) if isinstance(stars_data, list) else 0,
            "repo_memory_seed": len(seed_entries),
        },
        "skill_count": len(items),
        "skills": items,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    # ── Audit ───────────────────────────────────────────────────────
    tag_summary: dict[str, int] = {}
    source_summary: dict[str, int] = {}
    lang_summary: dict[str, int] = {}
    for item in items:
        for tag in item["tags"]:
            tag_summary[tag] = tag_summary.get(tag, 0) + 1
        src = item.get("source_type", "unknown")
        source_summary[src] = source_summary.get(src, 0) + 1
        lang = item.get("language", "unknown") or "unknown"
        lang_summary[lang] = lang_summary.get(lang, 0) + 1

    audit = {
        "version": "c26-skill-brain-default-a",
        "checked_at": now,
        "sources": {
            "brain_asset_index": str(ASSET_INDEX),
            "github_stars": str(STARS_JSON),
            "repo_memory_seed": str(SEED_JSON),
        },
        "skill_count": len(items),
        "tag_summary": dict(sorted(tag_summary.items(), key=lambda x: -x[1])),
        "source_type_summary": source_summary,
        "language_summary": dict(sorted(lang_summary.items(), key=lambda x: -x[1])),
        "top_stars": [
            {"id": i["id"], "title": i["title"], "stars": i["stars"], "tags": i["tags"]}
            for i in items[:20]
        ],
    }

    AUDIT_JSON.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_JSON.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    # ── Console output ──────────────────────────────────────────────
    print(json.dumps({
        "status": "ok",
        "skill_count": len(items),
        "tag_summary": dict(sorted(tag_summary.items(), key=lambda x: -x[1])),
        "source_type_summary": source_summary,
        "language_top5": dict(sorted(lang_summary.items(), key=lambda x: -x[1])[:5]),
        "sample": [
            {"id": i["id"], "title": i["title"], "stars": i["stars"], "tags": i["tags"]}
            for i in items[:5]
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
