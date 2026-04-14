#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REFERENCES_DIR="$ROOT_DIR/references"
CORE_DIR="$ROOT_DIR/core-platform"
OLLAMA_BIN="${OLLAMA_BIN:-}"

mkdir -p "$ROOT_DIR/core-platform" "$ROOT_DIR/plugin-lab" "$ROOT_DIR/capability-registry" "$ROOT_DIR/references" "$ROOT_DIR/scripts"

mkdir -p \
  "$CORE_DIR/apps/desktop" \
  "$CORE_DIR/apps/web" \
  "$CORE_DIR/apps/cli" \
  "$CORE_DIR/services/model_gateway" \
  "$CORE_DIR/services/agent-orchestrator" \
  "$CORE_DIR/services/plugin-manager" \
  "$CORE_DIR/services/eval-engine" \
  "$CORE_DIR/services/update-service" \
  "$CORE_DIR/packages/plugin-sdk" \
  "$CORE_DIR/packages/common" \
  "$CORE_DIR/data/sqlite" \
  "$CORE_DIR/prompts" \
  "$CORE_DIR/manifests" \
  "$CORE_DIR/scripts" \
  "$CORE_DIR/docs"

cd "$REFERENCES_DIR"
for repo in \
  "https://github.com/HKUDS/OpenHarness.git" \
  "https://github.com/shareAI-lab/learn-claude-code.git" \
  "https://github.com/NousResearch/hermes-agent.git" \
  "https://github.com/affaan-m/everything-claude-code.git"
do
  name="$(basename "$repo" .git)"
  if [ ! -d "$name/.git" ]; then
    git clone "$repo"
  fi
done

cd "$CORE_DIR"
if [ ! -d .git ]; then
  git init
  git branch -M main
fi

if [ ! -d .venv ]; then
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

if [ -z "$OLLAMA_BIN" ]; then
  if command -v ollama >/dev/null 2>&1; then
    OLLAMA_BIN="$(command -v ollama)"
  elif [ -x /Applications/Ollama.app/Contents/Resources/ollama ]; then
    OLLAMA_BIN="/Applications/Ollama.app/Contents/Resources/ollama"
  fi
fi

if [ -z "$OLLAMA_BIN" ]; then
  curl -fsSL https://ollama.com/install.sh | sh || true
  if [ -x /Applications/Ollama.app/Contents/Resources/ollama ]; then
    OLLAMA_BIN="/Applications/Ollama.app/Contents/Resources/ollama"
  elif command -v ollama >/dev/null 2>&1; then
    OLLAMA_BIN="$(command -v ollama)"
  else
    echo "Ollama binary not found after installation attempt." >&2
    exit 1
  fi
fi

if ! pgrep -f "ollama serve" >/dev/null 2>&1; then
  nohup "$OLLAMA_BIN" serve > "$ROOT_DIR/ollama.log" 2>&1 &
fi

if ! pgrep -f "uvicorn services.model_gateway.main:app" >/dev/null 2>&1; then
  nohup zsh -lc "cd \"$CORE_DIR\" && .venv/bin/uvicorn services.model_gateway.main:app --host 0.0.0.0 --port 18080" > "$ROOT_DIR/model-gateway.log" 2>&1 &
fi

find "$ROOT_DIR" -maxdepth 2 -type d | sort > "$ROOT_DIR/tree.txt"
echo "Bootstrap complete. Snapshot: $ROOT_DIR/tree.txt"
