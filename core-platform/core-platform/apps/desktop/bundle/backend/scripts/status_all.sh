#!/usr/bin/env bash
set -euo pipefail

echo "== 18080 =="
curl -s http://127.0.0.1:18080/health || true
echo
echo "== 18081 =="
curl -s http://127.0.0.1:18081/health || true
echo
echo "== 18082 =="
curl -s http://127.0.0.1:18082/health || true
echo
echo "== 18083 =="
curl -s http://127.0.0.1:18083/health || true
echo
