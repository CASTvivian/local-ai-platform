#!/usr/bin/env bash
set -euo pipefail

ROOT="/Users/mofamaomi/Documents/本地ai/core-platform"
cd "$ROOT" || exit 1

pkill -f "Local AI Platform" || true
pkill -f "desktop_lib" || true

bash scripts/desktop/stop_desktop_services.sh || true

echo "Desktop demo stopped."
