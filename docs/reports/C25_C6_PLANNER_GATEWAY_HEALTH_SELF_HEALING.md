# C25-C6 Planner Gateway Health + Self-Healing

**状态**: ✅ 已完成

## 概述

实现了 Planner Gateway 健康检查和熔断器机制，使得 LLM planner 在 model_gateway 503 错误时不再静默 fallback，而是可观测、可记录、可短路。

## 实现内容

### 1. 健康检查数据模型 (`app/health/models.py`)

- `ComponentHealth`: 通用组件健康状态模型
- `PlannerRuntimeState`: Planner 运行时状态模型，包含：
  - `ok`: 整体健康状态
  - `planner_mode`: Planner 模式 (llm_first)
  - `model_gateway_ok`: Model gateway 健康状态
  - `circuit_open`: 熔断器是否打开
  - `last_error`: 最后一次错误信息
  - `fallback_active`: 是否处于 fallback 模式
  - `detail`: 详细信息

### 2. 熔断器实现 (`app/health/planner_health.py`)

**核心功能**:
- 状态持久化到 `core-platform/data/planner_runtime/planner_health.json`
- 熔断器 TTL 可配置（默认 60 秒）
- Model gateway 健康检查（默认 `http://127.0.0.1:18080/health`）
- 自动记录和清除 planner 错误

**关键函数**:
- `record_planner_error(error)`: 记录 planner 错误，打开熔断器
- `clear_planner_error()`: 清除 planner 错误，关闭熔断器
- `is_circuit_open()`: 检查熔断器是否打开（考虑 TTL）
- `check_model_gateway(timeout=3)`: 检查 model gateway 健康状态
- `planner_runtime_state(check_live=False)`: 获取 planner 运行时状态

### 3. 健康检查聚合服务 (`app/health/service.py`)

- `agent_health(check_live=False)`: 聚合所有组件健康状态
  - 当 `check_live=True` 时执行实时健康检查
  - 返回 planner 和 model_gateway 的健康状态

### 4. LLM Planner 集成 (`app/planning/llm_planner.py`)

**修改点**:
- 导入健康检查模块
- 在 `call_planner_model()` 中添加熔断器检查
- 如果熔断器打开，直接抛出 `RuntimeError("planner circuit is open; model gateway recently failed")`
- 成功调用后调用 `clear_planner_error()`
- 失败时调用 `record_planner_error(str(exc))` 并设置 `LAST_PLANNER_ERROR`

### 5. Planner Fallback 增强 (`app/planner.py`)

**修改点**:
- 在 `_fallback_local_chat()` 中获取 planner 运行时状态
- 在 `AgentPlan.args` 中添加：
  - `fallback_reason`: "llm_planner_unavailable"
  - `planner_health`: 完整的 planner 健康状态

### 6. API 端点 (`main.py`)

新增两个健康检查端点：

**GET `/agent/health`**:
- 参数: `check_live` (bool, default=False)
- 返回: agent 整体健康状态，包含 components.planner 和 components.model_gateway
- 示例:
  ```json
  {
    "ok": true,
    "checked_at": "2026-05-15T00:00:00.000000",
    "components": {
      "planner": { ... },
      "model_gateway": { ... }
    }
  }
  ```

**GET `/agent/health/planner`**:
- 参数: `check_live` (bool, default=False)
- 返回: planner 运行时状态详情
- 示例:
  ```json
  {
    "ok": true,
    "planner_mode": "llm_first",
    "model_gateway_ok": true,
    "circuit_open": false,
    "last_error": null,
    "fallback_active": false,
    "checked_at": "2026-05-15T00:00:00.000000",
    "detail": { ... }
  }
  ```

## 运行效果

### 正常情况
1. Planner 调用 model_gateway 成功 → `model_gateway_ok=True`, `circuit_open=False`
2. Fallback plan 的 `planner_health` 显示健康状态

### 异常情况（model_gateway 503）
1. Planner 调用失败 → `record_planner_error()` 被调用
2. 状态文件更新: `model_gateway_ok=False`, `circuit_open=True`, `last_error=...`
3. 熔断器打开，持续 60 秒（可配置）
4. 在 TTL 期间，所有 planner 调用直接短路（`is_circuit_open()` 返回 True）
5. Fallback plan 的 `planner_health` 显示错误原因

### 自动恢复
1. TTL 过期后，熔断器自动关闭
2. 下一次 planner 调用会尝试连接 model_gateway
3. 如果成功，调用 `clear_planner_error()` 清除错误状态

## 环境变量

- `MAOMIAI_MODEL_GATEWAY_HEALTH_URL`: model_gateway 健康检查 URL（默认: `http://127.0.0.1:18080/health`）
- `MAOMIAI_PLANNER_CIRCUIT_TTL_SECONDS`: 熔断器 TTL 秒数（默认: `60`）

## 验证清单

- [x] 健康检查数据模型定义
- [x] 熔断器实现（记录错误、清除错误、检查状态）
- [x] Model gateway 健康检查
- [x] Planner 运行时状态查询
- [x] LLM planner 集成熔断器检查
- [x] Fallback plan 包含 planner_health
- [x] `/agent/health` API 端点
- [x] `/agent/health/planner` API 端点
- [x] 状态文件持久化
- [x] 环境变量配置支持

## 下一步

- 桌面/报告页面集成 planner 健康状态展示
- 增强健康状态可观测性
- 考虑添加健康告警机制