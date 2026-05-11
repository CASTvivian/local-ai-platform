#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
LOG_DIR="/Users/mofamaomi/Documents/本地ai/logs"
ENV_FILE="$ROOT/scripts/desktop/desktop_services.env"

cd "$ROOT" || exit 1

echo "===== MAOMIAI Desktop Services Stop ====="

stop_one() {
  local port="$1"
  local name="$2"
  
  if lsof -ti tcp:"$port" >/dev/null 2>&1; then
    echo "[$name] stopping port $port"
    lsof -ti tcp:"$port" | xargs kill || true
  else
    echo "[$name] port $port not running"
  fi
  
  rm -f "$LOG_DIR/$name.pid" 2>/dev/null || true
}

while IFS='|' read -r port name module log_name; do
  [[ -z "${port:-}" ]] && continue
  [[ "$port" =~ ^# ]] && continue
  stop_one "$port" "$name"
done < "$ENV_FILE"

sleep 2
echo "Stop completed."
