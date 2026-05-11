#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
APP="$ROOT/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app"

cd "$ROOT" || exit 1

echo "===== MAOMIAI Desktop Demo ====="

echo
echo "1. Starting services..."
bash scripts/desktop/start_desktop_services.sh

echo
echo "2. Service status..."
bash scripts/desktop/status_desktop_services.sh

echo
echo "3. Model gateway smoke..."
python3 - <<'PY'
import json
import urllib.request

payload = {
    "model": "qwen2.5:7b",
    "prompt": "请用一句中文回答：本地模型是否可用？",
    "stream": False,
}
req = urllib.request.Request(
    "http://127.0.0.1:18080/generate",
    data=json.dumps(payload).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urllib.request.urlopen(req, timeout=60) as r:
    print(r.read().decode("utf-8", errors="ignore"))
PY

echo
echo "4. Opening desktop app..."
open "$APP"

echo
echo "Demo app launched."
