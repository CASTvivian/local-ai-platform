#!/usr/bin/env bash
set -euo pipefail
FAIL=0
echo "===== P3.14-D2-C Workflow Store Deepen Check ====="

check() {
  name="$1"
  shift
  echo
  echo "===== $name ====="
  if "$@"; then
    echo "OK $name"
  else
    echo "FAIL $name"
    FAIL=$((FAIL+1))
  fi
}

# 1. Health check
check "workflow_store health" bash -c 'curl -fsS --max-time 8 http://127.0.0.1:18080/health | python3 -m json.tool'

# 2. Register workflow
WORKFLOW_NAME="Test RAG Workflow"
REGISTER_RESP=$(curl -fsS --max-time 10 -X POST http://127.0.0.1:18080/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "'$WORKFLOW_NAME'",
    "description": "A simple RAG workflow for testing",
    "version": "1.0.0",
    "enabled": true,
    "nodes": [
      {
        "id": "node_start",
        "type": "start",
        "name": "Start",
        "config": {},
        "position": {"x": 0, "y": 0}
      },
      {
        "id": "node_retrieve",
        "type": "document_retrieval",
        "name": "Retrieve Documents",
        "config": {"max_docs": 10, "similarity_threshold": 0.7},
        "position": {"x": 200, "y": 100}
      },
      {
        "id": "node_model",
        "type": "model_invocation",
        "name": "Generate Response",
        "config": {"model": "claude-3"},
        "position": {"x": 400, "y": 100}
      },
      {
        "id": "node_end",
        "type": "end",
        "name": "End",
        "config": {},
        "position": {"x": 600, "y": 100}
      }
    ],
    "edges": [
      {
        "id": "edge_1",
        "source": "node_start",
        "target": "node_retrieve",
        "label": "trigger"
      },
      {
        "id": "edge_2",
        "source": "node_retrieve",
        "target": "node_model",
        "label": "documents"
      },
      {
        "id": "edge_3",
        "source": "node_model",
        "target": "node_end",
        "label": "response"
      }
    ],
    "metadata": {
      "author": "test_user",
      "tags": ["rag", "test"],
      "category": "research",
      "runtime_requirements": {
        "min_agents": 1,
        "supported_modes": ["async"],
        "required_services": ["document_ingestion", "model_gateway"],
        "estimated_duration": "2-5min",
        "max_parallel_tasks": 3
      }
    }
  }' || echo "REGISTER_FAILED")

echo "$REGISTER_RESP" | python3 -m json.tool || echo "$REGISTER_RESP"
if echo "$REGISTER_RESP" | python3 -c "import json,sys; sys.exit(0 if json.load(sys.stdin).get('ok') == True else 1)"; then
  echo "OK register workflow"
else
  echo "FAIL register workflow"
  FAIL=$((FAIL+1))
fi

# Extract workflow_id
WORKFLOW_ID=$(echo "$REGISTER_RESP" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("workflow_id",""))' || echo "")
if [ -n "$WORKFLOW_ID" ]; then
  echo "Workflow ID: $WORKFLOW_ID"
else
  echo "FAIL no workflow_id"
  FAIL=$((FAIL+1))
  WORKFLOW_ID="workflow_test"
fi

# 3. List workflows
if [ -n "$WORKFLOW_ID" ]; then
  check "list workflows" bash -c "curl -fsS --max-time 8 http://127.0.0.1:18080/list | python3 -m json.tool"
fi

# 4. Get workflow details
if [ -n "$WORKFLOW_ID" ]; then
  check "get workflow details" bash -c "curl -fsS --max-time 8 http://127.0.0.1:18080/get/$WORKFLOW_ID | python3 -m json.tool"
fi

# 5. Dry run workflow
if [ -n "$WORKFLOW_ID" ]; then
  check "dry run workflow" bash -c "curl -fsS --max-time 10 -X POST http://127.0.0.1:18080/dry_run/$WORKFLOW_ID | python3 -m json.tool"
fi

# 6. Export workflow
if [ -n "$WORKFLOW_ID" ]; then
  check "export workflow" bash -c "curl -fsS --max-time 8 http://127.0.0.1:18080/export/$WORKFLOW_ID | python3 -m json.tool"
fi

# 7. Import workflow
IMPORT_RESP=$(curl -fsS --max-time 10 -X POST http://127.0.0.1:18080/import \
  -H "Content-Type: application/json" \
  -d '{
    "format": "json",
    "content": {
      "name": "Imported Workflow",
      "description": "A workflow imported from JSON",
      "version": "2.0.0",
      "nodes": [
        {
          "id": "node_1",
          "type": "agent",
          "name": "Agent Task",
          "config": {}
        }
      ],
      "edges": []
    }
  }' || echo "IMPORT_FAILED")

echo "$IMPORT_RESP" | python3 -m json.tool || echo "$IMPORT_RESP"
if echo "$IMPORT_RESP" | python3 -c "import json,sys; sys.exit(0 if json.load(sys.stdin).get('ok') == True else 1)"; then
  echo "OK import workflow"
else
  echo "FAIL import workflow"
  FAIL=$((FAIL+1))
fi

# 8. Validate workflow
check "validate workflow" bash -c 'curl -fsS --max-time 8 -X POST http://127.0.0.1:18080/validate \
  -H "Content-Type: application/json" \
  -d '"{\"name\":\"Test\",\"nodes\":[],\"edges\":[]}" | python3 -m json.tool'

# 9. Recent events
check "recent events" bash -c "curl -fsS --max-time 8 http://127.0.0.1:18080/recent | python3 -m json.tool"

echo
echo "===== Result ====="
if [ "$FAIL" -eq 0 ]; then
  echo "P3.14-D2-C WORKFLOW STORE DEEPEN CHECK PASS"
  exit 0
else
  echo "P3.14-D2-C WORKFLOW STORE DEEPEN CHECK FAIL: $FAIL checks failed"
  exit 1
fi
