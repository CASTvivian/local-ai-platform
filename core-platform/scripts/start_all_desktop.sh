#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
LOG_DIR="$ROOT_DIR/../logs"
mkdir -p "$LOG_DIR"

cd "$ROOT_DIR"

if [ ! -d ".venv" ]; then
  echo "missing virtualenv: $ROOT_DIR/.venv"
  exit 1
fi

# 使用包装脚本启动服务（自动设置 PYTHONPATH）
START_SCRIPT="$ROOT_DIR/scripts/start_service.sh"

# Core services from start_all.sh
echo "[1/15] starting model gateway on :18080"
nohup "$START_SCRIPT" services.model_gateway.main:app \
  --host 0.0.0.0 --port 18080 \
  > "$LOG_DIR/model-gateway.log" 2>&1 &
sleep 1

echo "[2/15] starting plugin manager on :18082"
nohup "$START_SCRIPT" services.plugin_manager.main:app \
  --host 0.0.0.0 --port 18082 \
  > "$LOG_DIR/plugin-manager.log" 2>&1 &
sleep 1

echo "[3/15] starting eval engine on :18083"
nohup "$START_SCRIPT" services.eval_engine.main:app \
  --host 0.0.0.0 --port 18083 \
  > "$LOG_DIR/eval-engine.log" 2>&1 &
sleep 1

echo "[4/15] starting agent orchestrator on :18081"
nohup "$START_SCRIPT" services.agent_orchestrator.main:app \
  --host 0.0.0.0 --port 18081 \
  > "$LOG_DIR/orchestrator.log" 2>&1 &
sleep 1

# MAOMIAI Desktop P3 services
echo "[5/15] starting auto_router on :18093"
nohup "$START_SCRIPT" services.auto_router_service.main:app \
  --host 0.0.0.0 --port 18093 \
  > "$LOG_DIR/auto-router.log" 2>&1 &
sleep 1

echo "[6/15] starting runtime_execution on :18104"
nohup "$START_SCRIPT" services.runtime_execution_service.main:app \
  --host 0.0.0.0 --port 18104 \
  > "$LOG_DIR/runtime-execution.log" 2>&1 &
sleep 1

echo "[7/15] starting policy_engine on :18110"
nohup "$START_SCRIPT" services.policy_engine_service.main:app \
  --host 0.0.0.0 --port 18110 \
  > "$LOG_DIR/policy-engine.log" 2>&1 &
sleep 1

echo "[8/15] starting trace_observability on :18111"
nohup "$START_SCRIPT" services.trace_observability_service.main:app \
  --host 0.0.0.0 --port 18111 \
  > "$LOG_DIR/trace-observability.log" 2>&1 &
sleep 1

echo "[9/15] starting eval_gateway on :18112"
nohup "$START_SCRIPT" services.eval_gateway_service.main:app \
  --host 0.0.0.0 --port 18112 \
  > "$LOG_DIR/eval-gateway.log" 2>&1 &
sleep 1

echo "[10/15] starting document_ingestion on :18120"
nohup "$START_SCRIPT" services.document_ingestion_service.main:app \
  --host 0.0.0.0 --port 18120 \
  > "$LOG_DIR/document-ingestion.log" 2>&1 &
sleep 1

echo "[11/15] starting skill_store on :18121"
nohup "$START_SCRIPT" services.skill_store_service.main:app \
  --host 0.0.0.0 --port 18121 \
  > "$LOG_DIR/skill-store.log" 2>&1 &
sleep 1

echo "[12/15] starting artifact_registry on :18123"
nohup "$START_SCRIPT" services.artifact_registry_service.main:app \
  --host 0.0.0.0 --port 18123 \
  > "$LOG_DIR/artifact-registry.log" 2>&1 &
sleep 1

echo "[13/15] starting code_review_gate on :18124"
nohup "$START_SCRIPT" services.code_review_gate_service.main:app \
  --host 0.0.0.0 --port 18124 \
  > "$LOG_DIR/code-review-gate.log" 2>&1 &
sleep 1

echo "[14/15] starting repo_memory on :18125"
nohup "$START_SCRIPT" services.repo_memory_service.main:app \
  --host 0.0.0.0 --port 18125 \
  > "$LOG_DIR/repo-memory.log" 2>&1 &
sleep 1

echo "[15/15] starting workflow_store on :18126"
nohup "$START_SCRIPT" services.workflow_store_service.main:app \
  --host 0.0.0.0 --port 18126 \
  > "$LOG_DIR/workflow-store.log" 2>&1 &
sleep 1

echo "[16/16] starting design_system on :18127"
nohup "$START_SCRIPT" services.design_system_service.main:app \
  --host 0.0.0.0 --port 18127 \
  > "$LOG_DIR/design-system.log" 2>&1 &
sleep 3

echo "[17/17] starting agent_runtime on :18131"
nohup "$START_SCRIPT" services.agent_runtime_service.main:app \
  --host 0.0.0.0 --port 18131 \
  > "$LOG_DIR/agent-runtime.log" 2>&1 &
sleep 1

echo
echo "All services started. Running health checks..."
echo
