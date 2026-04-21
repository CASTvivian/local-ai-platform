from __future__ import annotations

import json
import concurrent.futures
import time
import threading
import uuid
from datetime import datetime
from pathlib import Path

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

ASK_URL = "http://127.0.0.1:18081/ask"
CODE_AGENT_URL = "http://127.0.0.1:18085"
RESEARCH_URL = "http://127.0.0.1:18098"
HYPERFRAMES_URL = "http://127.0.0.1:18099"
TTS_URL = "http://127.0.0.1:18095/tts/speak"

BASE_DIR = Path("/Users/mofamaomi/Documents/本地ai/core-platform")
DOCS_DIR = BASE_DIR / "docs"
PROMPTS_DIR = BASE_DIR / "prompts" / "agent_team"
DATA_DIR = BASE_DIR / "data" / "agent_team"
RUNS_DIR = DATA_DIR / "runs"
PHASE_LOG_DIR = DATA_DIR / "phase_logs"
DATA_DIR.mkdir(parents=True, exist_ok=True)
RUNS_DIR.mkdir(parents=True, exist_ok=True)
PHASE_LOG_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:19000", "http://localhost:19000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ROLES = ["planner", "coder", "reviewer", "researcher", "operator", "synthesizer", "coder_fix"]
DEFAULT_PIPELINE = ["planner", "researcher", "coder", "reviewer", "operator", "synthesizer"]
ROLE_TIMEOUTS = {
    "planner": 180,
    "researcher": 240,
    "coder": 300,
    "reviewer": 180,
    "operator": 300,
    "synthesizer": 180,
    "coder_fix": 240,
    "operator_tools": 600,
    "operator_retry_tools": 600,
    "synthesizer_final": 240,
}
RUN_STATE = {}


def ts():
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def iso_now():
    return datetime.now().isoformat()


def load_prompt(role: str) -> str:
    path = PROMPTS_DIR / f"{role}.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    defaults = {
        "coder_fix": "你是 Coder Fix Agent。根据 reviewer 指出的缺口，输出修正方案与补丁思路。"
    }
    return defaults.get(role, f"你是 {role} agent。")


def ask_general(prompt: str, timeout: int = 600):
    response = requests.post(
        ASK_URL,
        json={"task_type": "general", "prompt": prompt},
        timeout=timeout,
    )
    response.raise_for_status()
    return response.json()


def write_memory_snapshot(
    task: str,
    pipeline: list[str],
    outputs: dict,
    tool_runs: dict | None = None,
    final_status: str = "unknown",
    run_id: str | None = None,
):
    snapshot = {
        "task": task,
        "pipeline": pipeline,
        "outputs": outputs,
        "tool_runs": tool_runs or {},
        "final_status": final_status,
        "run_id": run_id,
        "ts": ts(),
    }
    path = DATA_DIR / f"task_memory_{snapshot['ts']}.json"
    path.write_text(json.dumps(snapshot, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)


def write_debug_log(name: str, payload: dict):
    debug_dir = DATA_DIR / "debug"
    debug_dir.mkdir(parents=True, exist_ok=True)
    path = debug_dir / f"{ts()}_{name}.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)


def safe_post(url: str, payload: dict, timeout: int = 600):
    try:
        response = requests.post(url, json=payload, timeout=timeout)
        response.raise_for_status()
        return {"ok": True, "data": response.json()}
    except Exception as exc:
        return {"ok": False, "error": str(exc), "url": url, "payload": payload}


def run_research_bridge(task: str):
    return safe_post(
        f"{RESEARCH_URL}/search",
        {"query": task, "source": "web", "max_results": 5},
        timeout=120,
    )


def run_code_agent_bridge(task: str):
    return safe_post(
        f"{CODE_AGENT_URL}/tasks/run-loop",
        {"task": task, "problem": task, "test_command": "echo agent_team_operator_validation"},
        timeout=1200,
    )


def run_hyperframes_bridge(task: str):
    return safe_post(
        f"{HYPERFRAMES_URL}/render",
        {
            "prompt": task,
            "title": "Agent Team Video Render",
            "subtitle": task[:80],
            "bullets": [
                "由 Agent Team Operator 触发",
                "调用 HyperFrames 渲染模板",
                "后续可接 research / tts / charts",
            ],
        },
        timeout=1200,
    )


def run_tts_bridge(text: str, preset: str = "default_cn"):
    return safe_post(
        TTS_URL,
        {"prompt": text, "preset": preset, "voice": ""},
        timeout=600,
    )


def run_workflow_bundle(task: str):
    bundle = {
        "research": None,
        "summary_text": None,
        "tts": None,
        "video": None,
        "debug_logs": [],
    }

    research = safe_post(
        f"{RESEARCH_URL}/news_summary",
        {"topic": task, "notes": "", "max_results": 5},
        timeout=180,
    )
    bundle["research"] = research
    bundle["debug_logs"].append(
        write_debug_log(
            "workflow_bundle_research",
            {"task": task, "step": "research", "result": research},
        )
    )

    if research.get("ok"):
        data = research.get("data", {})
        summary_text = data.get("summary", "") or task
    else:
        summary_text = task

    bundle["summary_text"] = summary_text
    bundle["debug_logs"].append(
        write_debug_log(
            "workflow_bundle_summary",
            {"task": task, "step": "summary", "summary_text": summary_text},
        )
    )

    try:
        tts = run_tts_bridge(summary_text, preset="default_cn")
    except Exception as exc:
        tts = {"ok": False, "error": str(exc)}
    bundle["tts"] = tts
    bundle["debug_logs"].append(
        write_debug_log(
            "workflow_bundle_tts",
            {"task": task, "step": "tts", "result": tts},
        )
    )

    try:
        video = safe_post(
            f"{HYPERFRAMES_URL}/research_to_video",
            {
                "topic": "Agent Team Workflow Video",
                "summary": summary_text,
                "tts_preset": "default_cn",
            },
            timeout=1800,
        )
    except Exception as exc:
        video = {"ok": False, "error": str(exc)}
    bundle["video"] = video
    bundle["debug_logs"].append(
        write_debug_log(
            "workflow_bundle_video",
            {"task": task, "step": "video", "result": video},
        )
    )
    bundle["debug_logs"].append(
        write_debug_log("workflow_bundle_final", {"task": task, "bundle": bundle})
    )
    return bundle


def run_workflow_bundle_steps(task: str):
    result = {
        "research": None,
        "summary_text": None,
        "tts": None,
        "video": None,
        "debug_logs": [],
    }

    research = safe_post(
        f"{RESEARCH_URL}/news_summary",
        {"topic": task, "notes": "", "max_results": 5},
        timeout=180,
    )
    result["research"] = research
    result["debug_logs"].append(
        write_debug_log("workflow_step_research", {"task": task, "result": research})
    )

    summary_text = task
    if research.get("ok"):
        data = research.get("data", {})
        summary_text = data.get("summary", "") or task
    result["summary_text"] = summary_text
    result["debug_logs"].append(
        write_debug_log(
            "workflow_step_summary",
            {"task": task, "summary_text": summary_text},
        )
    )

    try:
        tts = run_tts_bridge(summary_text, preset="default_cn")
    except Exception as exc:
        tts = {"ok": False, "error": str(exc)}
    result["tts"] = tts
    result["debug_logs"].append(
        write_debug_log("workflow_step_tts", {"task": task, "result": tts})
    )

    try:
        video = safe_post(
            f"{HYPERFRAMES_URL}/research_to_video",
            {
                "topic": "Agent Team Workflow Video",
                "summary": summary_text,
                "tts_preset": "default_cn",
            },
            timeout=1800,
        )
    except Exception as exc:
        video = {"ok": False, "error": str(exc)}
    result["video"] = video
    result["debug_logs"].append(
        write_debug_log("workflow_step_video", {"task": task, "result": video})
    )
    result["debug_logs"].append(
        write_debug_log("workflow_step_final", {"task": task, "result": result})
    )
    return result


def run_research_fast_summary(task: str):
    result = {
        "ok": False,
        "mode": "degraded",
        "summary_text": task,
        "raw": None,
    }

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            future = executor.submit(
                lambda: safe_post(
                    f"{RESEARCH_URL}/news_summary",
                    {"topic": task, "notes": "", "max_results": 3},
                    timeout=45,
                )
            )
            response = future.result(timeout=50)

        result["raw"] = response
        if response.get("ok"):
            data = response.get("data", {})
            result["ok"] = True
            result["mode"] = "news_summary"
            result["summary_text"] = data.get("summary", "") or task
        return result
    except Exception as exc:
        result["error"] = str(exc)
        return result


def poll_video_run(video_run_id: str, max_rounds: int = 60, interval_sec: int = 5):
    last = None
    for _ in range(max_rounds):
        try:
            response = requests.get(f"{HYPERFRAMES_URL}/video_run/{video_run_id}", timeout=30)
            response.raise_for_status()
            last = response.json()
            if last.get("status") in ["completed", "failed"]:
                return last
        except Exception as exc:
            last = {"ok": False, "error": str(exc), "run_id": video_run_id}
        time.sleep(interval_sec)
    return last or {"ok": False, "error": "video polling timeout", "run_id": video_run_id}


def poll_video_run_brief(video_run_id: str, max_rounds: int = 3, interval_sec: int = 3):
    last = None
    for _ in range(max_rounds):
        try:
            response = requests.get(f"{HYPERFRAMES_URL}/video_run/{video_run_id}", timeout=20)
            response.raise_for_status()
            last = response.json()
            if last.get("status") in ["running", "completed", "failed"]:
                return last
        except Exception as exc:
            last = {"ok": False, "error": str(exc), "run_id": video_run_id}
        time.sleep(interval_sec)
    return last or {"ok": False, "error": "video brief polling timeout", "run_id": video_run_id}


def infer_tools(task: str):
    text = task.lower()
    tools = []
    if any(keyword in text for keyword in ["日报视频", "研究转视频", "一键视频", "research to video", "研报视频", "总结成视频"]):
        tools.append("workflow_bundle")
    if any(keyword in text for keyword in ["搜索", "研究", "资料", "新闻", "动态", "日报"]):
        tools.append("research")
    if any(keyword in text for keyword in ["代码", "修复", "报错", "接口", "脚本", "实现"]):
        tools.append("code_agent")
    if any(keyword in text for keyword in ["视频", "成片", "渲染", "模板视频"]):
        tools.append("hyperframes")
    return tools


def run_tools_for_task(task: str):
    tools = infer_tools(task)
    tool_runs = {}
    for tool in tools:
        if tool == "workflow_bundle":
            try:
                workflow_bundle = run_workflow_bundle(task)
                tool_runs["workflow_bundle"] = {"ok": True, "data": workflow_bundle}
            except Exception as exc:
                tool_runs["workflow_bundle"] = {"ok": False, "error": str(exc)}
                write_debug_log(
                    "workflow_bundle_exception",
                    {"task": task, "error": str(exc)},
                )
        elif tool == "research":
            tool_runs["research"] = run_research_bridge(task)
        elif tool == "code_agent":
            tool_runs["code_agent"] = run_code_agent_bridge(task)
        elif tool == "hyperframes":
            tool_runs["hyperframes"] = run_hyperframes_bridge(task)
    write_debug_log(
        "run_tools_for_task",
        {"task": task, "tools": tools, "tool_runs": tool_runs},
    )
    return tool_runs


def summarize_tool_status(tool_runs: dict):
    if not tool_runs:
        return "no_tools"
    oks = []
    fails = []
    for key, value in tool_runs.items():
        if value.get("ok"):
            oks.append(key)
        else:
            fails.append(key)
    if fails and oks:
        return "partial_success"
    if fails and not oks:
        return "failed"
    return "success"


def is_workflow_bundle_fastpath(task: str) -> bool:
    text = task.lower()
    keywords = [
        "日报视频",
        "研究转视频",
        "一键视频",
        "research to video",
        "研报视频",
        "总结成视频",
        "输出研究摘要、语音和成片",
        "生成一份a股市场日报视频",
        "市场日报视频",
    ]
    return any(keyword in text for keyword in keywords)


def run_file(run_id: str) -> Path:
    return RUNS_DIR / f"{run_id}.json"


def phase_log_file(run_id: str, phase: str) -> Path:
    safe_phase = phase.replace("/", "_").replace(" ", "_")
    return PHASE_LOG_DIR / f"{run_id}_{safe_phase}.json"


def persist_run(run_id: str):
    run_file(run_id).write_text(json.dumps(RUN_STATE[run_id], ensure_ascii=False, indent=2), encoding="utf-8")


def write_phase_log(run_id: str, phase: str, payload: dict):
    path = phase_log_file(run_id, phase)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(path)


def begin_phase(run_id: str, phase: str):
    item = {
        "phase": phase,
        "started_at": iso_now(),
        "finished_at": None,
        "duration_ms": None,
        "status": "running",
        "timeout_sec": ROLE_TIMEOUTS.get(phase, 300),
        "log_path": None,
    }
    RUN_STATE[run_id]["phases"].append(item)
    RUN_STATE[run_id]["current_phase"] = phase
    persist_run(run_id)
    return item


def end_phase(run_id: str, item: dict, status: str, log_path: str | None = None):
    item["finished_at"] = iso_now()
    start_dt = datetime.fromisoformat(item["started_at"])
    end_dt = datetime.fromisoformat(item["finished_at"])
    item["duration_ms"] = int((end_dt - start_dt).total_seconds() * 1000)
    item["status"] = status
    item["log_path"] = log_path
    RUN_STATE[run_id]["current_phase"] = None
    persist_run(run_id)


def run_with_timeout(fn, timeout_sec: int):
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    future = executor.submit(fn)
    try:
        return {"ok": True, "value": future.result(timeout=timeout_sec)}
    except concurrent.futures.TimeoutError:
        future.cancel()
        return {"ok": False, "error": f"timeout after {timeout_sec}s"}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}
    finally:
        executor.shutdown(wait=False, cancel_futures=True)


def execute_run(run_id: str, task: str, pipeline: list[str], enable_tools: bool, enable_review_loop: bool):
    outputs = {}
    tool_runs = {}
    context = task

    try:
        if enable_tools and is_workflow_bundle_fastpath(task):
            outputs["fastpath"] = "workflow_bundle_fastpath_executed"
            workflow_data = {
                "research": None,
                "summary_text": None,
                "tts": None,
                "video": None,
                "debug_logs": [],
            }

            phase_item = begin_phase(run_id, "workflow_bundle_research")
            try:
                research_fast = run_research_fast_summary(task)
                workflow_data["research"] = research_fast.get("raw") or {
                    "ok": research_fast.get("ok", False),
                    "mode": research_fast.get("mode", "degraded"),
                }
                workflow_data["summary_text"] = research_fast.get("summary_text", task)
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_research",
                    {
                        "task": task,
                        "status": "success",
                        "mode": research_fast.get("mode", "degraded"),
                        "result": workflow_data["research"],
                        "summary_text": workflow_data["summary_text"],
                        "ts": iso_now(),
                    },
                )
                end_phase(run_id, phase_item, "success", log_path=log_path)
            except Exception as exc:
                workflow_data["research"] = {"ok": False, "error": str(exc), "mode": "exception"}
                workflow_data["summary_text"] = task
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_research",
                    {
                        "task": task,
                        "status": "error",
                        "error": str(exc),
                        "summary_text": task,
                        "ts": iso_now(),
                    },
                )
                end_phase(run_id, phase_item, "error", log_path=log_path)

            phase_item = begin_phase(run_id, "workflow_bundle_tts")
            try:
                tts = run_tts_bridge(workflow_data["summary_text"], preset="default_cn")
                workflow_data["tts"] = tts
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_tts",
                    {
                        "task": task,
                        "status": "success" if tts.get("ok") else "error",
                        "result": tts,
                        "ts": iso_now(),
                    },
                )
                end_phase(
                    run_id,
                    phase_item,
                    "success" if tts.get("ok") else "error",
                    log_path=log_path,
                )
            except Exception as exc:
                workflow_data["tts"] = {"ok": False, "error": str(exc)}
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_tts",
                    {"task": task, "status": "error", "error": str(exc), "ts": iso_now()},
                )
                end_phase(run_id, phase_item, "error", log_path=log_path)

            phase_item = begin_phase(run_id, "workflow_bundle_video")
            try:
                submit = safe_post(
                    f"{HYPERFRAMES_URL}/research_to_video_async",
                    {
                        "topic": "Agent Team Workflow Video",
                        "summary": workflow_data["summary_text"],
                        "tts_preset": "default_cn",
                    },
                    timeout=60,
                )

                if submit.get("ok"):
                    submit_data = submit.get("data", {})
                    video_run_id = submit_data.get("run_id", "")
                    polled = poll_video_run_brief(video_run_id, max_rounds=3, interval_sec=3)
                    video_status = polled.get("status", "unknown")
                    workflow_data["video"] = {
                        "ok": video_status in ["running", "completed"],
                        "pending": video_status == "running",
                        "video_run_id": video_run_id,
                        "submit": submit,
                        "poll": polled,
                    }
                else:
                    workflow_data["video"] = {"ok": False, "pending": False, "submit": submit}

                video_ok = bool(workflow_data["video"].get("ok"))
                phase_status = "success" if video_ok else "error"
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_video",
                    {
                        "task": task,
                        "status": phase_status,
                        "result": workflow_data["video"],
                        "ts": iso_now(),
                    },
                )
                end_phase(
                    run_id,
                    phase_item,
                    phase_status,
                    log_path=log_path,
                )
            except Exception as exc:
                workflow_data["video"] = {"ok": False, "pending": False, "error": str(exc)}
                log_path = write_phase_log(
                    run_id,
                    "workflow_bundle_video",
                    {"task": task, "status": "error", "error": str(exc), "ts": iso_now()},
                )
                end_phase(run_id, phase_item, "error", log_path=log_path)

            tool_runs["workflow_bundle"] = {"ok": True, "data": workflow_data}
            research_ok = True
            tts_ok = bool((workflow_data.get("tts") or {}).get("ok"))
            video_ok = bool((workflow_data.get("video") or {}).get("ok"))
            video_pending = bool((workflow_data.get("video") or {}).get("pending"))
            if research_ok and tts_ok and video_ok and not video_pending:
                final_status = "pass"
            elif research_ok and tts_ok and video_pending:
                final_status = "completed_with_pending_video"
            elif tts_ok or video_ok:
                final_status = "partial"
            else:
                final_status = "fail"

            memory_path = write_memory_snapshot(
                task,
                ["workflow_bundle_research", "workflow_bundle_tts", "workflow_bundle_video"],
                outputs,
                tool_runs=tool_runs,
                final_status=final_status,
                run_id=run_id,
            )

            RUN_STATE[run_id]["status"] = "completed"
            RUN_STATE[run_id]["outputs"] = outputs
            RUN_STATE[run_id]["tool_runs"] = tool_runs
            RUN_STATE[run_id]["final_status"] = final_status
            RUN_STATE[run_id]["memory_snapshot"] = memory_path
            RUN_STATE[run_id]["finished_at"] = iso_now()
            persist_run(run_id)
            return

        for role in pipeline:
            phase_item = begin_phase(run_id, role)
            timeout_sec = ROLE_TIMEOUTS.get(role, 300)

            def phase_fn():
                prompt = f"""{load_prompt(role)}

当前总任务：
{task}

当前上下文：
{context}

请输出你这一阶段最重要的结果。"""
                return ask_general(prompt, timeout=timeout_sec)

            result = run_with_timeout(phase_fn, timeout_sec)
            if result["ok"]:
                content = result["value"].get("response", "")
                outputs[role] = content
                context += f"\n\n[{role} 输出]\n{content}"
                log_path = write_phase_log(
                    run_id,
                    role,
                    {
                        "role": role,
                        "task": task,
                        "status": "success",
                        "content": content[:20000],
                        "ts": iso_now(),
                    },
                )
                end_phase(run_id, phase_item, "success", log_path=log_path)

                if enable_tools and role == "operator":
                    tool_phase = begin_phase(run_id, "operator_tools")
                    tool_result = run_with_timeout(lambda: run_tools_for_task(task), ROLE_TIMEOUTS.get("operator_tools", 600))
                    if tool_result["ok"]:
                        tool_runs = tool_result["value"]
                        context += f"\n\n[operator 工具结果]\n{json.dumps(tool_runs, ensure_ascii=False)[:12000]}"
                        log_path = write_phase_log(
                            run_id,
                            "operator_tools",
                            {"status": "success", "tool_runs": tool_runs, "ts": iso_now()},
                        )
                        end_phase(run_id, tool_phase, "success", log_path=log_path)
                    else:
                        tool_runs = {"operator_tools_error": tool_result["error"]}
                        log_path = write_phase_log(
                            run_id,
                            "operator_tools",
                            {"status": "error", "error": tool_result["error"], "ts": iso_now()},
                        )
                        end_phase(run_id, tool_phase, "error", log_path=log_path)
            else:
                outputs[role] = f"agent_error: {result['error']}"
                context += f"\n\n[{role} 输出]\nagent_error: {result['error']}"
                log_path = write_phase_log(
                    run_id,
                    role,
                    {
                        "role": role,
                        "task": task,
                        "status": "error",
                        "error": result["error"],
                        "ts": iso_now(),
                    },
                )
                end_phase(run_id, phase_item, "error", log_path=log_path)
                continue

        review_result = outputs.get("reviewer", "")
        review_fail = any(keyword in review_result.lower() for keyword in ["fail", "不通过", "缺口", "问题", "风险"])

        if enable_review_loop and review_fail:
            fix_phase = begin_phase(run_id, "coder_fix")
            timeout_sec = ROLE_TIMEOUTS.get("coder_fix", 240)

            def fix_fn():
                prompt = f"""{load_prompt("coder_fix")}

原任务：
{task}

reviewer 输出：
{review_result}

请给出修正后的实现方案、补丁思路和下一步验证建议。"""
                return ask_general(prompt, timeout=timeout_sec)

            result = run_with_timeout(fix_fn, timeout_sec)
            if result["ok"]:
                outputs["coder_fix"] = result["value"].get("response", "")
                context += f"\n\n[coder_fix 输出]\n{outputs['coder_fix']}"
                log_path = write_phase_log(
                    run_id,
                    "coder_fix",
                    {"status": "success", "content": outputs["coder_fix"][:20000], "ts": iso_now()},
                )
                end_phase(run_id, fix_phase, "success", log_path=log_path)
            else:
                outputs["coder_fix"] = f"agent_error: {result['error']}"
                log_path = write_phase_log(
                    run_id,
                    "coder_fix",
                    {"status": "error", "error": result["error"], "ts": iso_now()},
                )
                end_phase(run_id, fix_phase, "error", log_path=log_path)

            if enable_tools:
                retry_phase = begin_phase(run_id, "operator_retry_tools")
                retry_result = run_with_timeout(
                    lambda: run_tools_for_task(task + "\n\n根据 reviewer 缺口重新验证"),
                    ROLE_TIMEOUTS.get("operator_retry_tools", 600),
                )
                if retry_result["ok"]:
                    retry_tool_runs = retry_result["value"]
                    tool_runs["retry"] = retry_tool_runs
                    context += f"\n\n[operator 二次工具结果]\n{json.dumps(retry_tool_runs, ensure_ascii=False)[:12000]}"
                    log_path = write_phase_log(
                        run_id,
                        "operator_retry_tools",
                        {"status": "success", "tool_runs": retry_tool_runs, "ts": iso_now()},
                    )
                    end_phase(run_id, retry_phase, "success", log_path=log_path)
                else:
                    tool_runs["retry"] = {"error": retry_result["error"]}
                    log_path = write_phase_log(
                        run_id,
                        "operator_retry_tools",
                        {"status": "error", "error": retry_result["error"], "ts": iso_now()},
                    )
                    end_phase(run_id, retry_phase, "error", log_path=log_path)

            synth_phase = begin_phase(run_id, "synthesizer_final")
            timeout_sec = ROLE_TIMEOUTS.get("synthesizer_final", 240)

            def synth_fn():
                synth_prompt = f"""{load_prompt("synthesizer")}

原任务：
{task}

已有输出：
{context}

请给出最终结构化结论，包含：
1. 完成项
2. 未完成项
3. 工具执行情况
4. 下一步建议
5. 最终状态(pass / partial / fail)
"""
                return ask_general(synth_prompt, timeout=timeout_sec)

            result = run_with_timeout(synth_fn, timeout_sec)
            if result["ok"]:
                outputs["synthesizer_final"] = result["value"].get("response", "")
                log_path = write_phase_log(
                    run_id,
                    "synthesizer_final",
                    {"status": "success", "content": outputs["synthesizer_final"][:20000], "ts": iso_now()},
                )
                end_phase(run_id, synth_phase, "success", log_path=log_path)
            else:
                outputs["synthesizer_final"] = f"agent_error: {result['error']}"
                log_path = write_phase_log(
                    run_id,
                    "synthesizer_final",
                    {"status": "error", "error": result["error"], "ts": iso_now()},
                )
                end_phase(run_id, synth_phase, "error", log_path=log_path)

        tool_status = summarize_tool_status(tool_runs)
        final_status = "pass"
        if review_fail and tool_status == "failed":
            final_status = "fail"
        elif review_fail or tool_status == "partial_success":
            final_status = "partial"

        memory_path = write_memory_snapshot(
            task,
            pipeline,
            outputs,
            tool_runs=tool_runs,
            final_status=final_status,
            run_id=run_id,
        )

        RUN_STATE[run_id]["status"] = "completed"
        RUN_STATE[run_id]["outputs"] = outputs
        RUN_STATE[run_id]["tool_runs"] = tool_runs
        RUN_STATE[run_id]["final_status"] = final_status
        RUN_STATE[run_id]["memory_snapshot"] = memory_path
        RUN_STATE[run_id]["finished_at"] = iso_now()
        persist_run(run_id)
    except Exception as exc:
        RUN_STATE[run_id]["status"] = "failed"
        RUN_STATE[run_id]["error"] = str(exc)
        RUN_STATE[run_id]["finished_at"] = iso_now()
        persist_run(run_id)


@app.get("/health")
def health():
    return {"ok": True, "roles": ROLES, "default_pipeline": DEFAULT_PIPELINE}


@app.get("/roles")
def roles():
    return {
        "ok": True,
        "roles": ROLES,
        "default_pipeline": DEFAULT_PIPELINE,
        "roles_doc": str(DOCS_DIR / "agent_team" / "roles.md"),
        "memory_rules_doc": str(DOCS_DIR / "memory" / "memory_rules.md"),
    }


@app.get("/memory_rules")
def memory_rules():
    path = DOCS_DIR / "memory" / "memory_rules.md"
    return {"ok": True, "path": str(path), "content": path.read_text(encoding="utf-8") if path.exists() else ""}


@app.get("/last_runs")
def last_runs():
    files = sorted(DATA_DIR.glob("task_memory_*.json"), reverse=True)[:10]
    rows = []
    for file_path in files:
        try:
            data = json.loads(file_path.read_text(encoding="utf-8"))
            rows.append(
                {
                    "file": str(file_path),
                    "task": data.get("task"),
                    "pipeline": data.get("pipeline"),
                    "ts": data.get("ts"),
                    "tools": list((data.get("tool_runs") or {}).keys()),
                    "final_status": data.get("final_status"),
                    "run_id": data.get("run_id"),
                }
            )
        except Exception:
            pass
    return {"ok": True, "runs": rows}


@app.post("/run")
def run_team(payload: dict):
    task = payload.get("task", "").strip()
    pipeline = payload.get("pipeline") or DEFAULT_PIPELINE
    pipeline = [role for role in pipeline if role in ROLES]
    enable_tools = bool(payload.get("enable_tools", False))
    enable_review_loop = bool(payload.get("enable_review_loop", True))

    if enable_tools and is_workflow_bundle_fastpath(task):
        tool_runs = run_tools_for_task(task)
        outputs = {"fastpath": "workflow_bundle_fastpath_executed"}
        final_status = "pass"
        memory_path = write_memory_snapshot(
            task,
            ["workflow_bundle_fastpath"],
            outputs,
            tool_runs=tool_runs,
            final_status=final_status,
            run_id=None,
        )
        return {
            "ok": True,
            "kind": "agent_team_run_loop",
            "task": task,
            "pipeline": ["workflow_bundle_fastpath"],
            "enable_tools": enable_tools,
            "enable_review_loop": enable_review_loop,
            "tool_runs": tool_runs,
            "outputs": outputs,
            "final_status": final_status,
            "memory_snapshot": memory_path,
        }

    outputs = {}
    tool_runs = {}
    context = task

    for role in pipeline:
        try:
            prompt = f"""{load_prompt(role)}

当前总任务：
{task}

当前上下文：
{context}

请输出你这一阶段最重要的结果。"""
            result = ask_general(prompt, timeout=600)
            content = result.get("response", "")
            outputs[role] = content
            context += f"\n\n[{role} 输出]\n{content}"

            if enable_tools and role == "operator":
                tool_runs = run_tools_for_task(task)
                context += f"\n\n[operator 工具结果]\n{json.dumps(tool_runs, ensure_ascii=False)[:12000]}"
        except Exception as exc:
            outputs[role] = f"agent_error: {exc}"
            context += f"\n\n[{role} 输出]\nagent_error: {exc}"

    review_result = outputs.get("reviewer", "")
    review_fail = any(keyword in review_result.lower() for keyword in ["fail", "不通过", "缺口", "问题", "风险"])
    if enable_review_loop and review_fail:
        try:
            prompt = f"""{load_prompt("coder_fix")}

原任务：
{task}

reviewer 输出：
{review_result}

请给出修正后的实现方案、补丁思路和下一步验证建议。"""
            result = ask_general(prompt, timeout=600)
            outputs["coder_fix"] = result.get("response", "")
            context += f"\n\n[coder_fix 输出]\n{outputs['coder_fix']}"
        except Exception as exc:
            outputs["coder_fix"] = f"agent_error: {exc}"

        if enable_tools:
            retry_tool_runs = run_tools_for_task(task + "\n\n根据 reviewer 缺口重新验证")
            tool_runs["retry"] = retry_tool_runs
            context += f"\n\n[operator 二次工具结果]\n{json.dumps(retry_tool_runs, ensure_ascii=False)[:12000]}"

        try:
            synth_prompt = f"""{load_prompt("synthesizer")}

原任务：
{task}

已有输出：
{context}

请给出最终结构化结论，包含：
1. 完成项
2. 未完成项
3. 工具执行情况
4. 下一步建议
5. 最终状态(pass / partial / fail)
"""
            result = ask_general(synth_prompt, timeout=600)
            outputs["synthesizer_final"] = result.get("response", "")
        except Exception as exc:
            outputs["synthesizer_final"] = f"agent_error: {exc}"

    tool_status = summarize_tool_status(tool_runs)
    final_status = "pass"
    if review_fail and tool_status == "failed":
        final_status = "fail"
    elif review_fail or tool_status == "partial_success":
        final_status = "partial"

    memory_path = write_memory_snapshot(
        task,
        pipeline,
        outputs,
        tool_runs=tool_runs,
        final_status=final_status,
        run_id=None,
    )

    return {
        "ok": True,
        "kind": "agent_team_run_loop",
        "task": task,
        "pipeline": pipeline,
        "enable_tools": enable_tools,
        "enable_review_loop": enable_review_loop,
        "tool_runs": tool_runs,
        "outputs": outputs,
        "final_status": final_status,
        "memory_snapshot": memory_path,
    }


@app.post("/run_async")
def run_async(payload: dict):
    task = payload.get("task", "").strip()
    pipeline = payload.get("pipeline") or DEFAULT_PIPELINE
    pipeline = [role for role in pipeline if role in ROLES]
    enable_tools = bool(payload.get("enable_tools", False))
    enable_review_loop = bool(payload.get("enable_review_loop", True))

    run_id = uuid.uuid4().hex[:16]
    RUN_STATE[run_id] = {
        "run_id": run_id,
        "task": task,
        "pipeline": pipeline,
        "enable_tools": enable_tools,
        "enable_review_loop": enable_review_loop,
        "status": "running",
        "current_phase": None,
        "phases": [],
        "outputs": {},
        "tool_runs": {},
        "final_status": None,
        "memory_snapshot": None,
        "started_at": iso_now(),
        "finished_at": None,
        "error": None,
    }
    persist_run(run_id)

    worker = threading.Thread(
        target=execute_run,
        args=(run_id, task, pipeline, enable_tools, enable_review_loop),
        daemon=True,
    )
    worker.start()

    return {
        "ok": True,
        "run_id": run_id,
        "status": "running",
        "fastpath_candidate": is_workflow_bundle_fastpath(task),
    }


@app.get("/run_status/{run_id}")
def run_status(run_id: str):
    if run_id in RUN_STATE:
        state = RUN_STATE[run_id]
        return {
            "ok": True,
            "run_id": run_id,
            "status": state.get("status"),
            "current_phase": state.get("current_phase"),
            "phases": state.get("phases"),
            "started_at": state.get("started_at"),
            "finished_at": state.get("finished_at"),
            "final_status": state.get("final_status"),
        }

    path = run_file(run_id)
    if path.exists():
        data = json.loads(path.read_text(encoding="utf-8"))
        return {
            "ok": True,
            "run_id": run_id,
            "status": data.get("status"),
            "current_phase": data.get("current_phase"),
            "phases": data.get("phases"),
            "started_at": data.get("started_at"),
            "finished_at": data.get("finished_at"),
            "final_status": data.get("final_status"),
        }

    return {"ok": False, "error": "run_id not found"}


@app.get("/run_result/{run_id}")
def run_result(run_id: str):
    if run_id in RUN_STATE:
        return {"ok": True, **RUN_STATE[run_id]}
    path = run_file(run_id)
    if path.exists():
        return {"ok": True, **json.loads(path.read_text(encoding="utf-8"))}
    return {"ok": False, "error": "run_id not found"}
