#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="/Users/mofamaomi/Documents/本地ai/core-platform"
APP_DIR="$ROOT_DIR/apps/web"
LOG_DIR="/Users/mofamaomi/Documents/本地ai/logs"

mkdir -p "$LOG_DIR"

cd "$ROOT_DIR"

if [ ! -d ".venv" ]; then
  echo "missing virtualenv: $ROOT_DIR/.venv"
  exit 1
fi

source .venv/bin/activate

pkill -f "uvicorn services.model_gateway.main:app" || true
pkill -f "uvicorn services.agent_orchestrator.main:app" || true
pkill -f "uvicorn services.plugin_manager.main:app" || true
pkill -f "uvicorn services.eval_engine.main:app" || true
pkill -f "python3 -m http.server 19000" || true

nohup .venv/bin/uvicorn services.model_gateway.main:app \
  --host 0.0.0.0 --port 18080 \
  > "$LOG_DIR/model-gateway.log" 2>&1 &

sleep 1

nohup .venv/bin/uvicorn services.plugin_manager.main:app \
  --host 0.0.0.0 --port 18082 \
  > "$LOG_DIR/plugin-manager.log" 2>&1 &

sleep 1

nohup .venv/bin/uvicorn services.eval_engine.main:app \
  --host 0.0.0.0 --port 18083 \
  > "$LOG_DIR/eval-engine.log" 2>&1 &

sleep 1

nohup .venv/bin/uvicorn services.agent_orchestrator.main:app \
  --host 0.0.0.0 --port 18081 \
  > "$LOG_DIR/agent-orchestrator.log" 2>&1 &

sleep 1

cd "$APP_DIR"
nohup python3 -m http.server 19000 \
  > "$LOG_DIR/web-ui.log" 2>&1 &
