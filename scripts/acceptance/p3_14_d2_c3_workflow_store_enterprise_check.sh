#!/usr/bin/env bash
# P3.14-D2-C3: Workflow Store Enterprise Acceptance Test

set -euo pipefail

echo "=== P3.14-D2-C3 Workflow Store Enterprise Acceptance ==="
echo

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Test counters
TOTAL=0
PASSED=0
FAILED=0

# Base URL
BASE_URL="http://localhost:18126"

# Helper functions
check_json() {
    local test_name="$1"
    local json_str="$2"
    
    TOTAL=$((TOTAL + 1))
    
    # Check for ok: true in JSON
    if echo "$json_str" | grep -q '"ok":\s*true'; then
        echo -e "${GREEN}✓${NC} $test_name"
        PASSED=$((PASSED + 1))
        return 0
    else
        echo -e "${RED}✗${NC} $test_name - ok: false or missing"
        FAILED=$((FAILED + 1))
        echo "  Response: $json_str"
        return 1
    fi
}

echo "Step 1: Health check"
echo "---------------------------------------"

HEALTH_JSON=$(curl -s "${BASE_URL}/health" | tr -d '\r')
check_json "Health check" "$HEALTH_JSON"

echo
echo "Step 2: Debug storage paths"
echo "---------------------------------------"

DEBUG_JSON=$(curl -s "${BASE_URL}/debug/storage" | tr -d '\r')
check_json "Debug storage" "$DEBUG_JSON"
echo "Storage debug:"
echo "$DEBUG_JSON" | head -10

echo
echo "Step 3: List workflows (should be empty initially)"
echo "---------------------------------------"

LIST_JSON=$(curl -s "${BASE_URL}/list" | tr -d '\r')
check_json "List workflows (empty)" "$LIST_JSON"
LIST_COUNT=$(echo "$LIST_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Initial count: ${LIST_COUNT:-0}"

echo
echo "Step 4: Register a workflow"
echo "---------------------------------------"

WORKFLOW_NAME="acceptance_test_$(date +%s)"
REGISTER_JSON=$(curl -s -X POST "${BASE_URL}/register" \
    -H "Content-Type: application/json" \
    -d "{
        \"name\": \"${WORKFLOW_NAME}\",
        \"version\": \"1.0.0\",
        \"description\": \"Acceptance test workflow\",
        \"source\": \"test\",
        \"nodes\": [
            {\"id\": \"start\", \"type\": \"start\", \"name\": \"Start\"},
            {\"id\": \"end\", \"type\": \"end\", \"name\": \"End\"}
        ],
        \"edges\": [
            {\"id\": \"e1\", \"source\": \"start\", \"target\": \"end\"}
        ],
        \"runtime_requirements\": {
            \"services\": [\"18104\"],
            \"models\": [\"qwen2.5:7b\"]
        }
    }" | tr -d '\r')

check_json "Register workflow" "$REGISTER_JSON"

# Extract workflow ID
WORKFLOW_ID=$(echo "$REGISTER_JSON" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
echo "  Registered workflow ID: ${WORKFLOW_ID:-}"

if [ -z "$WORKFLOW_ID" ]; then
    echo -e "${RED}✗${NC} Failed to extract workflow ID"
    echo "  Response: $REGISTER_JSON"
    exit 1
fi

echo
echo "Step 5: List workflows (should contain 1)"
echo "---------------------------------------"

LIST_JSON2=$(curl -s "${BASE_URL}/list" | tr -d '\r')
check_json "List workflows (1 item)" "$LIST_JSON2"
LIST_COUNT2=$(echo "$LIST_JSON2" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Count after register: ${LIST_COUNT2:-0}"

if [ "${LIST_COUNT2:-0}" -ne 1 ]; then
    echo -e "${RED}✗${NC} Expected count 1, got ${LIST_COUNT2:-0}"
    exit 1
fi

echo
echo "Step 6: Get workflow details"
echo "---------------------------------------"

GET_JSON=$(curl -s "${BASE_URL}/get/${WORKFLOW_ID}" | tr -d '\r')
check_json "Get workflow" "$GET_JSON"
GET_NAME=$(echo "$GET_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Retrieved workflow name: ${GET_NAME:-}"

if [ "$GET_NAME" != "$WORKFLOW_NAME" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected '$WORKFLOW_NAME', got '${GET_NAME:-}'"
    exit 1
fi

echo
echo "Step 7: Dry run workflow"
echo "---------------------------------------"

DRYRUN_JSON=$(curl -s -X POST "${BASE_URL}/dry_run" \
    -H "Content-Type: application/json" \
    -d "{
        \"workflow_id\": \"${WORKFLOW_ID}\",
        \"input_context\": {}
    }" | tr -d '\r')

check_json "Dry run" "$DRYRUN_JSON"
DRYRUN_STEPS=$(echo "$DRYRUN_JSON" | grep -o '"total_steps":[0-9]*' | cut -d: -f2)
echo "  Dry run steps: ${DRYRUN_STEPS:-}"

echo
echo "Step 8: Export workflow"
echo "---------------------------------------"

EXPORT_JSON=$(curl -s "${BASE_URL}/export/${WORKFLOW_ID}" | tr -d '\r')
check_json "Export workflow" "$EXPORT_JSON"
EXPORT_NAME=$(echo "$EXPORT_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Exported workflow name: ${EXPORT_NAME:-}"

echo
echo "Step 9: Check recent events"
echo "---------------------------------------"

EVENTS_JSON=$(curl -s "${BASE_URL}/recent" | tr -d '\r')
check_json "Recent events" "$EVENTS_JSON"
EVENTS_COUNT=$(echo "$EVENTS_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Events count: ${EVENTS_COUNT:-0}"

if [ "${EVENTS_COUNT:-0}" -lt 1 ]; then
    echo -e "${RED}✗${NC} Expected at least 1 event, got ${EVENTS_COUNT:-0}"
    exit 1
fi

echo
echo "Step 10: Verify store.json persistence"
echo "---------------------------------------"

# Resolve data directory path
BASE_DIR=$(cd /Users/mofamaomi/Documents/本地ai && pwd)
DATA_DIR="${BASE_DIR}/data/workflow_store"
STORE_PATH="${DATA_DIR}/store.json"

if [ -f "$STORE_PATH" ]; then
    echo -e "${GREEN}✓${NC} store.json exists at: $STORE_PATH"
    STORE_SIZE=$(stat -f%z "$STORE_PATH" 2>/dev/null || stat -c%s "$STORE_PATH" 2>/dev/null)
    echo "  Size: $STORE_SIZE bytes"
    
    # Check for workflow ID in store.json
    if grep -q "$WORKFLOW_ID" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Workflow ID found in store.json"
    else
        echo -e "${RED}✗${NC} Workflow ID NOT found in store.json"
        exit 1
    fi
    
    # Check for workflow name in store.json
    if grep -q "$WORKFLOW_NAME" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Workflow name found in store.json"
    else
        echo -e "${RED}✗${NC} Workflow name NOT found in store.json"
        exit 1
    fi
else
    echo -e "${RED}✗${NC} store.json not found at: $STORE_PATH"
    echo "  Listing data directory:"
    ls -la "$DATA_DIR" 2>/dev/null || echo "  Directory does not exist"
    exit 1
fi

echo
echo "Step 11: Verify events.jsonl persistence"
echo "---------------------------------------"

EVENTS_PATH="${DATA_DIR}/events.jsonl"

if [ -f "$EVENTS_PATH" ]; then
    echo -e "${GREEN}✓${NC} events.jsonl exists at: $EVENTS_PATH"
    EVENT_LINES=$(wc -l < "$EVENTS_PATH" 2>/dev/null || echo "0")
    echo "  Event count: $EVENT_LINES"
else
    echo -e "${YELLOW}⚠${NC} events.jsonl not found at: $EVENTS_PATH (non-critical)"
fi

echo
echo "=== Test Summary ==="
echo "Total: $TOTAL"
echo -e "${GREEN}Passed: $PASSED${NC}"
echo -e "${RED}Failed: $FAILED${NC}"
echo

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}=== ALL TESTS PASSED ===${NC}"
    echo -e "${GREEN}✓ OK PERSISTED${NC}"
    exit 0
else
    echo -e "${RED}=== TESTS FAILED ===${NC}"
    exit 1
fi
