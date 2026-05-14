# C25-C5 Desktop Agent Replay UI

## Implementation Summary

Desktop Agent Replay UI 功能已完成，允许用户查看智能体执行过程的时间线回放。

## Changes Made

### 1. JavaScript Core Functions (`core-platform/apps/desktop/src/js/windows-demo-stable-router.js`)

#### Agent Replay UI Helpers
- `window.__MAOMIAI_LAST_RUN_ID__` - 全局存储最后一次运行的 run_id
- `maomiaiEscapeHtml(value)` - HTML 转义函数
- `maomiaiShortJson(value, maxLen)` - JSON 截断显示（最大 900 字符）

#### Timeline Fetch & Render
- `fetchAgentTimeline(runId)` - 从 18131 服务获取 timeline
  - 调用 `GET /agent/replay/timeline/{run_id}`
- `renderAgentTimeline(timeline)` - 渲染 timeline UI
  - 显示 run_id 和 status
  - 显示最终答案（如果有）
  - 显示事件列表（run.created / plan / tool_result / observation / validation / run.completed 等）
  - 每个事件可展开查看详情

#### Page Navigation
- `openAgentReplay(runId)` - 打开 Agent 回放页面
  - 如果没有 run_id，显示提示页面
  - 如果加载失败，显示错误信息
  - 支持"返回对话"和"刷新回放"操作

#### Button Injection
- `injectAgentReplayButton()` - 在聊天头部自动注入"Agent 回放"按钮
  - 每 1.2 秒检查一次，确保按钮存在

#### Run ID Capture
- `maomiaiCaptureRunIdFromResult(result)` - 从 Agent Runtime 响应中提取 run_id
  - 支持多种字段路径（result.run_id / result.raw.run_id / result.data.run_id 等）
  - 自动存储到 `window.__MAOMIAI_LAST_RUN_ID__` 和 localStorage

#### Integration
- 在 `routeUserMessage(query)` 中添加 `maomiaiCaptureRunIdFromResult(result)` 调用
- 添加事件监听器处理按钮点击（open-agent-replay, refresh-agent-replay）

### 2. CSS Styles (`core-platform/apps/desktop/src/styles/main.css`)

新增 Agent Replay UI 样式：

- `.agent-replay-page` - 回放页面容器
- `.agent-replay-actions` - 操作按钮区域
- `.agent-replay-panel` - 主面板，深色背景
- `.agent-replay-header` - 头部，显示标题、run_id、状态
- `.agent-replay-status` - 状态标签（pill 样式）
- `.agent-replay-answer` - 最终答案区域
- `.agent-timeline-list` - 时间线事件列表
- `.agent-timeline-event` - 单个事件卡片
- `.agent-timeline-head` - 事件头部（序号、类型）
- `.agent-timeline-type` - 事件类型标签
- `.agent-timeline-title` - 事件标题
- `.agent-timeline-detail` - 可展开的事件详情
- `.agent-replay-empty` / `.agent-replay-loading` - 空状态和加载状态
- `.agent-replay-open-btn` - 回放按钮样式

设计特点：
- 深色主题（适合开发者调试）
- 渐变头部背景
- 可折叠的事件详情
- 响应式布局

## API Used

**GET `/agent/replay/timeline/{run_id}`**

返回结构：
```json
{
  "ok": true,
  "run_id": "...",
  "status": "completed|failed|running",
  "final_answer": "...",
  "events": [
    {
      "index": 0,
      "type": "run.created",
      "title": "...",
      "detail": {...}
    },
    {
      "index": 1,
      "type": "plan",
      "title": "...",
      "detail": {...}
    },
    {
      "index": 2,
      "type": "tool_result",
      "title": "...",
      "detail": {...}
    },
    {
      "index": 3,
      "type": "observation",
      "title": "...",
      "detail": {...}
    },
    {
      "index": 4,
      "type": "validation",
      "title": "...",
      "detail": {...}
    },
    {
      "index": 5,
      "type": "run.completed",
      "title": "...",
      "detail": {...}
    }
  ]
}
```

## Purpose

暴露 Agent Runtime 的推理和执行轨迹到桌面 UI，让用户可以看到：

1. **用户问题** → **plan**（计划）
2. **tool_result**（工具执行结果）
3. **observation**（观察）
4. **validation**（验证）
5. **replan**（重新规划，如果需要）
6. **execution**（执行）
7. **final**（最终答案）

## User Workflow

1. 用户在聊天中发送消息
2. Agent Runtime 处理并返回响应
3. run_id 被自动捕获并存储
4. 聊天头部自动出现"Agent 回放"按钮
5. 用户点击按钮，查看完整执行时间线
6. 可以展开每个事件查看详细数据
7. 可以点击"刷新回放"更新数据
8. 可以点击"返回对话"回到聊天

## Testing Checklist

- [x] JS 语法检查（通过 node -c）
- [x] Hardcode guard 检查（通过）
- [x] 发送聊天后是否捕获 last run_id
- [ ] 点击 Agent 回放是否能打开页面
- [ ] 页面是否显示 run.created / plan / tool_result / observation / validation / run.completed
- [ ] 如果有 execution audit，是否显示 execution event

## Next Steps

完成验收后，继续 C25-C6: Planner Gateway Health/Self-Healing。

## Related Tasks

- C25-C4: Runtime Hardcode Guard ✅
- C25-C4: LLM Planner Scaffold ✅
- C25-C4: Observation / Replan Loop ✅
- C25-C4: run_store / session_store ✅
- C25-C4: approval / sandbox ✅
- C25-C4: execution audit / replay ✅
- C25-C4: MCP runtime ✅
- C25-C4: capability registry ✅
- C25-C4: filesystem / browser / web / weather tools ✅
- C25-C4: run timeline API ✅
- C25-C5: Desktop Replay UI (当前任务)
- [ ] C25-C6: planner gateway health/self-healing
- [ ] C25-C7: stronger sandbox
- [ ] C25-C8: multi-agent runtime
- [ ] C25-C9: Windows final rebuild / full验收