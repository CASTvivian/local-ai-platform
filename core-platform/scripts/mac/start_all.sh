#!/usr/bin/env bash
set -u

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LOG_DIR="/tmp/maomiai-runtime/logs"
PID_DIR="/tmp/maomiai-runtime/pids"
mkdir -p "$LOG_DIR" "$PID_DIR"

# --- Resolve RUNTIME_ROOT ---
# Priority: MAOMIAI_RUNTIME_ROOT env var (set by Rust launcher)
# Then try SCRIPT_DIR/../../.. (scripts/mac/ -> core-platform/)
# Then search up from SCRIPT_DIR
if [ -n "${MAOMIAI_RUNTIME_ROOT:-}" ] && [ -d "${MAOMIAI_RUNTIME_ROOT}/services" ]; then
  RUNTIME_ROOT="$MAOMIAI_RUNTIME_ROOT"
elif [ -d "$SCRIPT_DIR/../../services" ]; then
  RUNTIME_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
elif [ -d "$SCRIPT_DIR/../../../core-platform/services" ]; then
  RUNTIME_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)/core-platform"
else
  # Walk up from SCRIPT_DIR to find a directory with services/
  RUNTIME_ROOT=""
  dir="$SCRIPT_DIR"
  for _ in $(seq 1 10); do
    if [ -d "$dir/services" ]; then
      RUNTIME_ROOT="$dir"
      break
    fi
    parent="$(dirname "$dir")"
    if [ "$parent" = "$dir" ]; then break; fi
    dir="$parent"
  done
  # Last resort: dev-time path
  if [ -z "$RUNTIME_ROOT" ]; then
    RUNTIME_ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
  fi
fi

echo "[C25-MAC] RUNTIME_ROOT=$RUNTIME_ROOT"
echo "[C25-MAC] services dir exists: $([ -d "$RUNTIME_ROOT/services" ] && echo YES || echo NO)"

find_python() {
  # 1. venv in RUNTIME_ROOT
  if [ -x "$RUNTIME_ROOT/.venv/bin/python3" ]; then
    echo "$RUNTIME_ROOT/.venv/bin/python3"
    return 0
  fi
  # 2. System python3
  if command -v python3 >/dev/null 2>&1; then
    command -v python3
    return 0
  fi
  # 3. System python
  if command -v python >/dev/null 2>&1; then
    command -v python
    return 0
  fi
  # 4. Common macOS Python paths
  for p in /usr/bin/python3 /usr/local/bin/python3 /opt/homebrew/bin/python3; do
    if [ -x "$p" ]; then
      echo "$p"
      return 0
    fi
  done
  return 1
}

http_ok() {
  local url="$1"
  curl -fsS --max-time 3 "$url" >/dev/null 2>&1
}

start_service() {
  local name="$1"
  local module="$2"
  local port="$3"
  local mode="${4:-module}"
  local health="http://127.0.0.1:${port}/health"

  if http_ok "$health"; then
    echo "{\"name\":\"$name\",\"ok\":true,\"already_running\":true,\"port\":$port}"
    return 0
  fi

  local py
  py="$(find_python || true)"
  if [ -z "$py" ]; then
    echo "{\"name\":\"$name\",\"ok\":false,\"error\":\"python_not_found\",\"port\":$port}"
    return 1
  fi

  cd "$RUNTIME_ROOT" || { echo "{\"name\":\"$name\",\"ok\":false,\"error\":\"cd_failed_to_$RUNTIME_ROOT\"}"; return 1; }
  local out="$LOG_DIR/${name}.out.log"
  local err="$LOG_DIR/${name}.err.log"

  echo "[C25-MAC] Starting $name on :$port with $py ($mode mode, cwd=$RUNTIME_ROOT)"

  if [ "$mode" = "uvicorn" ]; then
    nohup "$py" -m uvicorn "$module:app" --host 127.0.0.1 --port "$port" > "$out" 2> "$err" &
  else
    nohup "$py" -m "$module" > "$out" 2> "$err" &
  fi
  local pid="$!"
  echo "$pid" > "$PID_DIR/${name}.pid"

  for i in $(seq 1 35); do
    sleep 0.8
    if http_ok "$health"; then
      echo "{\"name\":\"$name\",\"ok\":true,\"pid\":$pid,\"port\":$port}"
      return 0
    fi
  done

  local tail_err=""
  if [ -f "$err" ]; then
    tail_err="$(tail -20 "$err" 2>/dev/null | head -5)"
  fi
  echo "{\"name\":\"$name\",\"ok\":false,\"pid\":$pid,\"port\":$port,\"error\":\"health_timeout\",\"stderr_sample\":\"$tail_err\"}"
  return 1
}

# Start core services in dependency order
start_service "repo_memory_service" "services.repo_memory_service.main" 18125 "module"
start_service "skill_store_service" "services.skill_store_service.main" 18121 "module"
start_service "workflow_store_service" "services.workflow_store_service.main" 18126 "uvicorn"
start_service "model_bootstrap_service" "services.model_bootstrap_service.main" 18100 "uvicorn"
start_service "model_gateway" "services.model_gateway.main" 18080 "uvicorn"
start_service "agent_runtime_service" "services.agent_runtime_service.main" 18131 "module"

echo "{\"ok\":true,\"runtime_root\":\"$RUNTIME_ROOT\",\"started_at\":\"$(date -u +%Y-%m-%dT%H:%M:%SZ)\"}"
