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

source .venv/bin/activate

echo "[1/4] starting model gateway on :18080"
nohup .venv/bin/uvicorn services.model_gateway.main:app \
  --host 0.0.0.0 --port 18080 \
  > "$LOG_DIR/model-gateway.log" 2>&1 &

sleep 1

echo "[2/4] starting plugin manager on :18082"
nohup .venv/bin/uvicorn services.plugin_manager.main:app \
  --host 0.0.0.0 --port 18082 \
  > "$LOG_DIR/plugin-manager.log" 2>&1 &

sleep 1

echo "[3/4] starting eval engine on :18083"
nohup .venv/bin/uvicorn services.eval_engine.main:app \
  --host 0.0.0.0 --port 18083 \
  > "$LOG_DIR/eval-engine.log" 2>&1 &

sleep 1

echo "[4/4] starting agent orchestrator on :18081"
nohup .venv/bin/uvicorn services.agent_orchestrator.main:app \
  --host 0.0.0.0 --port 18081 \
  > "$LOG_DIR/agent-orchestrator.log" 2>&1 &

sleep 2

echo
echo "health checks:"
curl -s http://127.0.0.1:18080/health || true
echo
curl -s http://127.0.0.1:18081/health || true
echo
curl -s http://127.0.0.1:18082/health || true
echo
curl -s http://127.0.0.1:18083/health || true
echo
echo "done"
