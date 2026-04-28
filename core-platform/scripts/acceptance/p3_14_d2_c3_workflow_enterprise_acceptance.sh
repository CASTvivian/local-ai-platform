#!/usr/bin/env bash
set -euo pipefail
FAIL=0
BASE="http://127.0.0.1:18126"
STORE="data/workflow_store/store.json"

check_json_ok() {
  local name="$1"
  local json="$2"
  echo
  echo "===== $name ====="
  echo "$json" | python3 -m json.tool || echo "$json"
  if echo "$json" | python3 -c "import json,sys; sys.exit(0 if json.load(sys.stdin).get('ok') == True else 1)"; then
    echo "OK $name"
  else
    echo "FAIL $name"
    FAIL=$((FAIL+1))
  fi
}

echo "===== P3.14-D2-C3 Workflow Enterprise Acceptance ====="
echo "===== health ====="
HEALTH="$(curl -fsS --max-time 8 "$BASE/health" || true)"
check_json_ok "health" "$HEALTH"

WF='{
  "name": "enterprise-rag-report-flow-acceptance",
  "version": "0.3.1",
  "description": "企业级RAG报告工作流验收",
  "source": "p3_14_d2_c3_acceptance",
  "nodes": [
    {"id":"start","type":"start","name":"Start"},
    {"id":"retrieve","type":"document_retrieval","name":"Retrieve Documents","config":{"top_k":5}},
    {"id":"model","type":"model_invocation","name":"Generate Report","config":{"model":"qwen2.5:7b"}},
    {"id":"end","type":"end","name":"End"}
  ],
  "edges": [
    {"id":"e1","source":"start","target":"retrieve"},
    {"id":"e2","source":"retrieve","target":"model"},
    {"id":"e3","source":"model","target":"end"}
  ],
  "runtime_requirements": {
    "services": ["18120","18125","18104"],
    "models": ["qwen2.5:7b","nomic-embed-text"],
    "tools": ["document_ingestion","runtime_execution"],
    "permissions": ["read_documents"],
    "estimated_timeout_sec": 600
  }
}'

echo
echo "===== register ====="
REG="$(curl -fsS --max-time 10 -X POST "$BASE/register" \
  -H "Content-Type: application/json" \
  -d "$WF" || true)"
check_json_ok "register" "$REG"

ID="$(python3 <<PY
import json
try:
    d=json.loads('''$REG''')
    print(d.get("item",{}).get("id",""))
except Exception:
    print("")
PY
)"
if [ -z "$ID" ]; then
  echo "FAIL no workflow id"
  FAIL=$((FAIL+1))
else
  echo "workflow_id=$ID"
fi

echo
echo "===== list ====="
LIST="$(curl -fsS --max-time 8 "$BASE/list" || true)"
check_json_ok "list" "$LIST"

if echo "$LIST" | grep -q "$ID"; then
  echo "OK list contains workflow id"
else
  echo "FAIL list does not contain workflow id"
  FAIL=$((FAIL+1))
fi

echo
echo "===== get ====="
GET="$(curl -fsS --max-time 8 "$BASE/get/$ID" || true)"
check_json_ok "get" "$GET"

echo
echo "===== dry_run ====="
DRY="$(curl -fsS --max-time 10 -X POST "$BASE/dry_run" \
  -H "Content-Type: application/json" \
  -d "{\"workflow_id\":\"$ID\",\"input\":{\"topic\":\"项目结构审计\"}}" || true)"
check_json_ok "dry_run" "$DRY"

if echo "$DRY" | grep -q '"plan"'; then
  echo "OK dry_run has plan"
else
  echo "FAIL dry_run no plan"
  FAIL=$((FAIL+1))
fi

echo
echo "===== export ====="
EXPORT="$(curl -fsS --max-time 8 "$BASE/export/$ID" || true)"
check_json_ok "export" "$EXPORT"

echo
echo "===== recent ====="
RECENT="$(curl -fsS --max-time 8 "$BASE/recent" || true)"
check_json_ok "recent" "$RECENT"

echo
echo "===== store file check ====="
if [ -f "$STORE" ]; then
  echo "OK store exists: $STORE"
  python3 <<PY
import json
with open("$STORE", encoding="utf-8") as p:
    d=json.load(p)
    print("store_version=", d.get("store_version"))
    print("items=", len(d.get("items",[])))
    assert any(x.get("id")=="$ID" for x in d.get("items",[])), "workflow id not found in store"
    print("OK workflow id found in store")
PY
else
  echo "FAIL store missing: $STORE"
  FAIL=$((FAIL+1))
fi

echo
echo "===== restart persistence check ====="
pkill -f "uvicorn services.workflow_store_service.main:app" || true
sleep 2

PYBIN=".venv/bin/python3"
if [ ! -x "$PYBIN" ]; then
  PYBIN="python3"
fi

nohup "$PYBIN" -m uvicorn services.workflow_store_service.main:app \
  --host 0.0.0.0 --port 18126 \
  > /Users/mofamaomi/Documents/本地ai/logs/workflow-store.log 2>&1 &
echo "Service restarted, PID: $!"
sleep 6

GET2="$(curl -fsS --max-time 8 "$BASE/get/$ID" || true)"
check_json_ok "get after restart" "$GET2"

if echo "$GET2" | grep -q "$ID"; then
  echo "OK persistence after restart"
else
  echo "FAIL persistence after restart"
  FAIL=$((FAIL+1))
fi

echo
echo "===== Result ====="
if [ "$FAIL" -eq 0 ]; then
  echo "P3.14-D2-C3 WORKFLOW ENTERPRISE ACCEPTANCE PASS"
  exit 0
else
  echo "P3.14-D2-C3 WORKFLOW ENTERPRISE ACCEPTANCE FAIL: $FAIL checks failed"
  exit 1
fi
