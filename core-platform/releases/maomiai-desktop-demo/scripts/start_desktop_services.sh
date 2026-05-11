#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
LOG_DIR="/Users/mofamaomi/Documents/本地ai/logs"
ENV_FILE="$ROOT/scripts/desktop/desktop_services.env"

cd "$ROOT" || exit 1
mkdir -p "$LOG_DIR"

PYTHON_BIN="$ROOT/.venv/bin/python3"
if [ ! -x "$PYTHON_BIN" ]; then
  PYTHON_BIN="$(command -v python3)"
fi

echo "===== MAOMIAI Desktop Services Start ====="
echo "ROOT=$ROOT"
echo "PYTHON_BIN=$PYTHON_BIN"
echo "LOG_DIR=$LOG_DIR"

if ! "$PYTHON_BIN" - <<'PY'
import importlib.util
import sys
missing = []
for name in ["uvicorn", "fastapi", "pydantic"]:
    if importlib.util.find_spec(name) is None:
        missing.append(name)
if missing:
    print("MISSING_DEPS=" + ",".join(missing))
    sys.exit(1)
print("deps ok")
PY
then
  echo "ERROR: required python packages missing. Please check virtualenv."
  exit 1
fi

start_one() {
  local port="$1"
  local name="$2"
  local module="$3"
  local log_name="$4"
  local log_path="$LOG_DIR/$log_name"
  
  if lsof -ti tcp:"$port" >/dev/null 2>&1; then
    local pid
    pid="$(lsof -ti tcp:"$port" | head -1)"
    echo "[$name] port $port already in use by PID $pid"
    if curl -fsS --max-time 2 "http://127.0.0.1:$port/health" >/dev/null 2>&1; then
      echo "[$name] already healthy"
      return 0
    fi
    echo "[$name] port occupied but unhealthy, killing PID $pid"
    kill "$pid" || true
    sleep 1
  fi
  
  echo "[$name] starting on $port -> $module"
  MAOMIAI_CORE_PLATFORM_DIR="$ROOT" nohup "$PYTHON_BIN" -m uvicorn "$module" \
    --host 0.0.0.0 \
    --port "$port" \
    > "$log_path" 2>&1 &
  echo $! > "$LOG_DIR/$name.pid"
}

while IFS='|' read -r port name module log_name; do
  [[ -z "${port:-}" ]] && continue
  [[ "$port" =~ ^# ]] && continue
  start_one "$port" "$name" "$module" "$log_name"
done < "$ENV_FILE"

echo
echo "Waiting for services..."
sleep 6

echo
echo "===== Health Check ====="
FAIL=0
while IFS='|' read -r port name module log_name; do
  [[ -z "${port:-}" ]] && continue
  [[ "$port" =~ ^# ]] && continue
  
  if curl -fsS --max-time 3 "http://127.0.0.1:$port/health" >/tmp/maomiai_health_"$port".json 2>/dev/null; then
    echo "✅ $name $port healthy"
  else
    echo "❌ $name $port failed"
    echo "---- log tail: $LOG_DIR/$log_name ----"
    tail -40 "$LOG_DIR/$log_name" || true
    FAIL=$((FAIL+1))
  fi
done < "$ENV_FILE"

if [ "$FAIL" -ne 0 ]; then
  echo "Desktop service start completed with failures: $FAIL"
  exit 1
fi

echo "All desktop services healthy."
