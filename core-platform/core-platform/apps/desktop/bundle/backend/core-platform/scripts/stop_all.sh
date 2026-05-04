#!/usr/bin/env bash
set -euo pipefail

pkill -f "uvicorn services.model_gateway.main:app" || true
pkill -f "uvicorn services.agent_orchestrator.main:app" || true
pkill -f "uvicorn services.plugin_manager.main:app" || true
pkill -f "uvicorn services.eval_engine.main:app" || true
pkill -f "python3 -m http.server 19000" || true
