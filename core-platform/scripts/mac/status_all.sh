#!/usr/bin/env bash
set -u

check() {
  local name="$1"
  local url="$2"
  if curl -fsS --max-time 3 "$url" >/tmp/maomiai-status-$name.json 2>/dev/null; then
    echo "\"$name\":{\"ok\":true,\"url\":\"$url\"}"
  else
    echo "\"$name\":{\"ok\":false,\"url\":\"$url\"}"
  fi
}

echo "{"
check "ollama" "http://127.0.0.1:11434/api/tags"
echo ","
check "model_gateway" "http://127.0.0.1:18080/health"
echo ","
check "agent_runtime" "http://127.0.0.1:18131/health"
echo ","
check "repo_memory" "http://127.0.0.1:18125/health"
echo ","
check "skill_store" "http://127.0.0.1:18121/health"
echo ","
check "workflow_store" "http://127.0.0.1:18126/health"
echo ","
check "model_bootstrap" "http://127.0.0.1:18100/health"
echo "}"
