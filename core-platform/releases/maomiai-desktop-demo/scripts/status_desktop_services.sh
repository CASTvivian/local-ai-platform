#!/usr/bin/env bash
set -euo pipefail
ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
ENV_FILE="$ROOT/scripts/desktop/desktop_services.env"

cd "$ROOT" || exit 1

echo "===== MAOMIAI Desktop Services Status ====="
PASS=0
FAIL=0

while IFS='|' read -r port name module log_name; do
  [[ -z "${port:-}" ]] && continue
  [[ "$port" =~ ^# ]] && continue
  
  if curl -fsS --max-time 2 "http://127.0.0.1:$port/health" >/tmp/maomiai_health_$port.json 2>/dev/null; then
    version="$(python3 - <<PY
import json
try:
    with open('/tmp/maomiai_health_$port.json') as f:
        j=json.load(f)
    print(j.get('version','unknown'))
except Exception:
    print('unknown')
PY
)"
    echo "✅ $port $name healthy version=$version"
    PASS=$((PASS+1))
  else
    if lsof -ti tcp:"$port" >/dev/null 2>&1; then
      pid="$(lsof -ti tcp:"$port" | head -1)"
      echo "⚠️  $port $name port-used-but-unhealthy pid=$pid"
    else
      echo "❌ $port $name down"
    fi
    FAIL=$((FAIL+1))
  fi
done < "$ENV_FILE"

echo
echo "PASS=$PASS"
echo "FAIL=$FAIL"

if [ "$FAIL" -ne 0 ]; then
  exit 1
fi
