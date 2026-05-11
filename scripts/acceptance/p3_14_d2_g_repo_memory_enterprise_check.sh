#!/usr/bin/env bash
# P3.14-D2-G: Repo Memory Enterprise Acceptance Test

set -euo pipefail

echo "=== P3.14-D2-G Repo Memory Enterprise Acceptance ==="
echo

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test counters
TOTAL=0
PASSED=0
FAILED=0

# Base URL
BASE_URL="http://localhost:18125"

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
echo "Step 3: Register repo"
echo "---------------------------------------"

cat > /tmp/repo_register.json << 'EOF'
{
  "name": "test-repo",
  "path": "/Users/test/repo",
  "description": "Test repository",
  "tags": ["python", "api"],
  "services": ["service1", "service2"]
}
EOF

REGISTER_JSON=$(curl -s -X POST "${BASE_URL}/repo/register" \
    -H "Content-Type: application/json" \
    -d @/tmp/repo_register.json | tr -d '\r')

check_json "Register repo" "$REGISTER_JSON"

# Extract repo ID
REPO_ID=$(echo "$REGISTER_JSON" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
echo "  Registered repo ID: ${REPO_ID:-}"

if [ -z "$REPO_ID" ]; then
    echo -e "${RED}✗${NC} Failed to extract repo ID"
    exit 1
fi

echo
echo "Step 4: Get repo by ID"
echo "---------------------------------------"

GET_JSON=$(curl -s "${BASE_URL}/repo/${REPO_ID}" | tr -d '\r')
check_json "Get repo" "$GET_JSON"
GET_NAME=$(echo "$GET_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Retrieved repo name: ${GET_NAME:-}"

if [ "$GET_NAME" != "test-repo" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected 'test-repo', got '${GET_NAME:-}'"
    exit 1
fi

echo
echo "Step 5: List repos"
echo "---------------------------------------"

LIST_JSON=$(curl -s "${BASE_URL}/repo/list" | tr -d '\r')
check_json "List repos" "$LIST_JSON"
LIST_COUNT=$(echo "$LIST_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Repos count: ${LIST_COUNT:-0}"

if [ "${LIST_COUNT:-0}" -ne 1 ]; then
    echo -e "${RED}✗${NC} Expected count 1, got ${LIST_COUNT:-0}"
    exit 1
fi

echo
echo "Step 6: Record fix"
echo "---------------------------------------"

cat > /tmp/fix_record.json << EOF
{
  "repo_id": "$REPO_ID",
  "title": "Fix import error",
  "problem": "Module not found error",
  "solution": "Added missing import statement",
  "files_changed": ["app/models.py"],
  "commands_run": ["pytest", "mypy"],
  "tests_run": ["test_import"],
  "result": "success",
  "commit_hash": "abc123"
}
EOF

FIX_JSON=$(curl -s -X POST "${BASE_URL}/fix/record" \
    -H "Content-Type: application/json" \
    -d @/tmp/fix_record.json | tr -d '\r')

check_json "Record fix" "$FIX_JSON"

echo
echo "Step 7: List fixes"
echo "---------------------------------------"

FIXES_JSON=$(curl -s "${BASE_URL}/fix/list?repo_id=${REPO_ID}" | tr -d '\r')
check_json "List fixes" "$FIXES_JSON"
FIXES_COUNT=$(echo "$FIXES_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Fixes count: ${FIXES_COUNT:-0}"

if [ "${FIXES_COUNT:-0}" -ne 1 ]; then
    echo -e "${RED}✗${NC} Expected count 1, got ${FIXES_COUNT:-0}"
    exit 1
fi

echo
echo "Step 8: Snapshot context"
echo "---------------------------------------"

cat > /tmp/snapshot.json << EOF
{
  "repo_id": "$REPO_ID",
  "title": "Initial state",
  "summary": "Fresh repository state",
  "files": ["app/models.py", "app/service.py"],
  "services": ["service1"],
  "tokens_estimate": 1500
}
EOF

SNAPSHOT_JSON=$(curl -s -X POST "${BASE_URL}/context/snapshot" \
    -H "Content-Type: application/json" \
    -d @/tmp/snapshot.json | tr -d '\r')

check_json "Snapshot context" "$SNAPSHOT_JSON"

echo
echo "Step 9: Compress context"
echo "---------------------------------------"

COMPRESS_JSON=$(curl -s "${BASE_URL}/context/compress/${REPO_ID}" | tr -d '\r')
check_json "Compress context" "$COMPRESS_JSON"
COMPRESS_REPO_NAME=$(echo "$COMPRESS_JSON" | grep -o '"repo_name":"[^"]*"' | cut -d'"' -f4)
echo "  Compressed repo name: ${COMPRESS_REPO_NAME:-}"

if [ "$COMPRESS_REPO_NAME" != "test-repo" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected 'test-repo', got '${COMPRESS_REPO_NAME:-}'"
    exit 1
fi

echo
echo "Step 10: Add knowledge"
echo "---------------------------------------"

cat > /tmp/knowledge.json << EOF
{
  "repo_id": "$REPO_ID",
  "category": "troubleshooting",
  "title": "Import error fix",
  "content": "Always check imports first",
  "tags": ["import", "python"]
}
EOF

KNOWLEDGE_JSON=$(curl -s -X POST "${BASE_URL}/knowledge/add" \
    -H "Content-Type: application/json" \
    -d @/tmp/knowledge.json | tr -d '\r')

check_json "Add knowledge" "$KNOWLEDGE_JSON"

echo
echo "Step 11: Search knowledge"
echo "---------------------------------------"

cat > /tmp/search.json << 'EOF'
{
  "query": "import",
  "limit": 10
}
EOF

SEARCH_JSON=$(curl -s -X POST "${BASE_URL}/knowledge/search" \
    -H "Content-Type: application/json" \
    -d @/tmp/search.json | tr -d '\r')

check_json "Search knowledge" "$SEARCH_JSON"
SEARCH_COUNT=$(echo "$SEARCH_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Search results count: ${SEARCH_COUNT:-0}"

if [ "${SEARCH_COUNT:-0}" -lt 1 ]; then
    echo -e "${RED}✗${NC} Expected at least 1 result, got ${SEARCH_COUNT:-0}"
    exit 1
fi

echo
echo "Step 12: Recent events"
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
echo "Step 13: Verify store.json persistence"
echo "---------------------------------------"

# Resolve data directory path
BASE_DIR=$(cd /Users/mofamaomi/Documents/本地ai && pwd)
DATA_DIR="${BASE_DIR}/data/repo_memory"
STORE_PATH="${DATA_DIR}/store.json"

if [ -f "$STORE_PATH" ]; then
    echo -e "${GREEN}✓${NC} store.json exists at: $STORE_PATH"
    STORE_SIZE=$(stat -f%z "$STORE_PATH" 2>/dev/null || stat -c%s "$STORE_PATH" 2>/dev/null)
    echo "  Size: $STORE_SIZE bytes"
    
    # Check for repo ID in store.json
    if grep -q "$REPO_ID" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Repo ID found in store.json"
    else
        echo -e "${RED}✗${NC} Repo ID NOT found in store.json"
        exit 1
    fi
    
    # Check for repo name in store.json
    if grep -q "test-repo" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Repo name found in store.json"
    else
        echo -e "${RED}✗${NC} Repo name NOT found in store.json"
        exit 1
    fi
else
    echo -e "${RED}✗${NC} store.json not found at: $STORE_PATH"
    echo "  Listing data directory:"
    ls -la "$DATA_DIR" 2>/dev/null || echo "  Directory does not exist"
    exit 1
fi

echo
echo "Step 14: Verify events.jsonl persistence"
echo "---------------------------------------"

EVENTS_PATH="${DATA_DIR}/events.jsonl"

if [ -f "$EVENTS_PATH" ]; then
    echo -e "${GREEN}✓${NC} events.jsonl exists at: $EVENTS_PATH"
    EVENT_LINES=$(wc -l < "$EVENTS_PATH" 2>/dev/null || echo "0")
    echo "  Event count: $EVENT_LINES"
else
    echo -e "${RED}✗${NC} events.jsonl not found at: $EVENTS_PATH"
    exit 1
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
