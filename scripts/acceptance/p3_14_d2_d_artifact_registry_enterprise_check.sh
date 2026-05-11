#!/usr/bin/env bash
# P3.14-D2-D: Artifact Registry Enterprise Acceptance Test

set -euo pipefail

echo "=== P3.14-D2-D Artifact Registry Enterprise Acceptance ==="
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
BASE_URL="http://localhost:18123"

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
echo "Step 3: List artifacts (should be empty initially)"
echo "---------------------------------------"

LIST_JSON=$(curl -s "${BASE_URL}/list" | tr -d '\r')
check_json "List artifacts (empty)" "$LIST_JSON"
LIST_COUNT=$(echo "$LIST_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Initial count: ${LIST_COUNT:-0}"

echo
echo "Step 4: Register execution result"
echo "---------------------------------------"

ARTIFACT_NAME="test_artifact_$(date +%s)"
RUN_ID="run_test_$(date +%s)"
REGISTER_JSON=$(curl -s -X POST "${BASE_URL}/register_execution_result" \
    -H "Content-Type: application/json" \
    -d "{
        \"name\": \"${ARTIFACT_NAME}\",
        \"type\": \"execution_result\",
        \"run_id\": \"${RUN_ID}\",
        \"path\": \"/tmp/test_artifact.txt\",
        \"lifecycle\": \"active\",
        \"source\": \"test\",
        \"version\": \"0.1.0\",
        \"payload\": {
            \"title\": \"Test Execution Result\",
            \"status\": \"completed\"
        }
    }" | tr -d '\r')

check_json "Register execution result" "$REGISTER_JSON"

# Extract artifact ID
ARTIFACT_ID=$(echo "$REGISTER_JSON" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
echo "  Registered artifact ID: ${ARTIFACT_ID:-}"

if [ -z "$ARTIFACT_ID" ]; then
    echo -e "${RED}✗${NC} Failed to extract artifact ID"
    echo "  Response: $REGISTER_JSON"
    exit 1
fi

echo
echo "Step 5: List artifacts (should contain 1)"
echo "---------------------------------------"

LIST_JSON2=$(curl -s "${BASE_URL}/list" | tr -d '\r')
check_json "List artifacts (1 item)" "$LIST_JSON2"
LIST_COUNT2=$(echo "$LIST_JSON2" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Count after register: ${LIST_COUNT2:-0}"

if [ "${LIST_COUNT2:-0}" -ne 1 ]; then
    echo -e "${RED}✗${NC} Expected count 1, got ${LIST_COUNT2:-0}"
    exit 1
fi

echo
echo "Step 6: Get artifact by ID"
echo "---------------------------------------"

GET_JSON=$(curl -s "${BASE_URL}/artifact/${ARTIFACT_ID}" | tr -d '\r')
check_json "Get artifact" "$GET_JSON"
GET_NAME=$(echo "$GET_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Retrieved artifact name: ${GET_NAME:-}"

if [ "$GET_NAME" != "$ARTIFACT_NAME" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected '$ARTIFACT_NAME', got '${GET_NAME:-}'"
    exit 1
fi

echo
echo "Step 7: Get file status"
echo "---------------------------------------"

STATUS_JSON=$(curl -s "${BASE_URL}/artifact/${ARTIFACT_ID}/file_status" | tr -d '\r')
check_json "File status" "$STATUS_JSON"
STATUS_EXISTS=$(echo "$STATUS_JSON" | grep -o '"exists":[^,}]*' | cut -d: -f2)
echo "  File exists: ${STATUS_EXISTS:-false}"

echo
echo "Step 8: Get download info"
echo "---------------------------------------"

DOWNLOAD_JSON=$(curl -s "${BASE_URL}/download/${ARTIFACT_ID}" | tr -d '\r')
check_json "Download info" "$DOWNLOAD_JSON"
DOWNLOAD_READY=$(echo "$DOWNLOAD_JSON" | grep -o '"download_ready":[^,}]*' | cut -d: -f2)
echo "  Download ready: ${DOWNLOAD_READY:-false}"

echo
echo "Step 9: Update lifecycle to archived"
echo "---------------------------------------"

UPDATE_JSON=$(curl -s -X POST "${BASE_URL}/artifact/${ARTIFACT_ID}/lifecycle" \
    -H "Content-Type: application/json" \
    -d "{
        \"lifecycle\": \"archived\",
        \"reason\": \"Test archival\"
    }" | tr -d '\r')

check_json "Update lifecycle" "$UPDATE_JSON"
UPDATED_LIFECYCLE=$(echo "$UPDATE_JSON" | grep -o '"lifecycle":"[^"]*"' | cut -d'"' -f4)
echo "  Updated lifecycle: ${UPDATED_LIFECYCLE:-}"

if [ "$UPDATED_LIFECYCLE" != "archived" ]; then
    echo -e "${RED}✗${NC} Lifecycle mismatch: expected 'archived', got '${UPDATED_LIFECYCLE:-}'"
    exit 1
fi

echo
echo "Step 10: Recent events"
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
echo "Step 11: Verify store.json persistence"
echo "---------------------------------------"

# Resolve data directory path
BASE_DIR=$(cd /Users/mofamaomi/Documents/本地ai && pwd)
DATA_DIR="${BASE_DIR}/data/artifact_registry"
STORE_PATH="${DATA_DIR}/store.json"

if [ -f "$STORE_PATH" ]; then
    echo -e "${GREEN}✓${NC} store.json exists at: $STORE_PATH"
    STORE_SIZE=$(stat -f%z "$STORE_PATH" 2>/dev/null || stat -c%s "$STORE_PATH" 2>/dev/null)
    echo "  Size: $STORE_SIZE bytes"
    
    # Check for artifact ID in store.json
    if grep -q "$ARTIFACT_ID" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Artifact ID found in store.json"
    else
        echo -e "${RED}✗${NC} Artifact ID NOT found in store.json"
        exit 1
    fi
    
    # Check for artifact name in store.json
    if grep -q "$ARTIFACT_NAME" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Artifact name found in store.json"
    else
        echo -e "${RED}✗${NC} Artifact name NOT found in store.json"
        exit 1
    fi
else
    echo -e "${RED}✗${NC} store.json not found at: $STORE_PATH"
    echo "  Listing data directory:"
    ls -la "$DATA_DIR" 2>/dev/null || echo "  Directory does not exist"
    exit 1
fi

echo
echo "Step 12: Verify events.jsonl persistence"
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
