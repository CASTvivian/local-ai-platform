#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../.."
python3 core-platform/scripts/quality/check_runtime_no_hardcode.py
