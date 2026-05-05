#!/usr/bin/env bash
export PYTHONPATH=/Users/mofamaomi/Documents/本地ai/core-platform:$PYTHONPATH
source .venv/bin/activate
exec .venv/bin/uvicorn "$@"
