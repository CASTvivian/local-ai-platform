#!/usr/bin/env bash
# P3.14-D2-E: Skill Store Enterprise Acceptance Test

set -euo pipefail

echo "=== P3.14-D2-E Skill Store Enterprise Acceptance ==="
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
BASE_URL="http://localhost:18121"

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
echo "Step 3: Parse SKILL.md"
echo "---------------------------------------"

PARSE_JSON=$(curl -s -X POST "${BASE_URL}/parse_skill_md" \
    -H "Content-Type: application/json" \
    -d '{
        "text": "# Test Skill\nName: test-skill\nVersion: 1.0.0\nDescription: A test skill"
    }' | tr -d '\r')

check_json "Parse SKILL.md" "$PARSE_JSON"
PARSED_NAME=$(echo "$PARSE_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Parsed name: ${PARSED_NAME:-}"

if [ "$PARSED_NAME" != "test-skill" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected 'test-skill', got '${PARSED_NAME:-}'"
    exit 1
fi

echo
echo "Step 4: Install skill from SKILL.md"
echo "---------------------------------------"

INSTALL_JSON=$(curl -s -X POST "${BASE_URL}/install_skill_md" \
    -H "Content-Type: application/json" \
    -d '{
        "text": "# My Test Skill\nName: my-test-skill\nVersion: 1.0.0\nDescription: My test skill\nAgents: coder, tester\nTags: automation, testing",
        "source": "desktop_skill_md"
    }' | tr -d '\r')

check_json "Install skill" "$INSTALL_JSON"

# Extract skill ID
SKILL_ID=$(echo "$INSTALL_JSON" | grep -o '"id":"[^"]*"' | cut -d'"' -f4)
echo "  Installed skill ID: ${SKILL_ID:-}"

if [ -z "$SKILL_ID" ]; then
    echo -e "${RED}✗${NC} Failed to extract skill ID"
    echo "  Response: $INSTALL_JSON"
    exit 1
fi

echo
echo "Step 5: List skills (should contain 1)"
echo "---------------------------------------"

LIST_JSON=$(curl -s "${BASE_URL}/list" | tr -d '\r')
check_json "List skills" "$LIST_JSON"
LIST_COUNT=$(echo "$LIST_JSON" | grep -o '"count":[0-9]*' | cut -d: -f2)
echo "  Skills count: ${LIST_COUNT:-0}"

if [ "${LIST_COUNT:-0}" -ne 1 ]; then
    echo -e "${RED}✗${NC} Expected count 1, got ${LIST_COUNT:-0}"
    exit 1
fi

echo
echo "Step 6: Get skill by ID"
echo "---------------------------------------"

GET_JSON=$(curl -s "${BASE_URL}/skill/${SKILL_ID}" | tr -d '\r')
check_json "Get skill" "$GET_JSON"
GET_NAME=$(echo "$GET_JSON" | grep -o '"name":"[^"]*"' | cut -d'"' -f4)
echo "  Retrieved skill name: ${GET_NAME:-}"

if [ "$GET_NAME" != "my-test-skill" ]; then
    echo -e "${RED}✗${NC} Name mismatch: expected 'my-test-skill', got '${GET_NAME:-}'"
    exit 1
fi

echo
echo "Step 7: Disable skill"
echo "---------------------------------------"

DISABLE_JSON=$(curl -s -X POST "${BASE_URL}/disable/${SKILL_ID}" | tr -d '\r')
check_json "Disable skill" "$DISABLE_JSON"
DISABLED_ENABLED=$(echo "$DISABLE_JSON" | grep -o '"enabled":[^,}]*' | cut -d: -f2)
echo "  Skill enabled: ${DISABLED_ENABLED:-true}"

if [ "$DISABLED_ENABLED" != "false" ]; then
    echo -e "${RED}✗${NC} Skill should be disabled, but enabled=${DISABLED_ENABLED:-true}"
    exit 1
fi

echo
echo "Step 8: Enable skill"
echo "---------------------------------------"

ENABLE_JSON=$(curl -s -X POST "${BASE_URL}/enable/${SKILL_ID}" | tr -d '\r')
check_json "Enable skill" "$ENABLE_JSON"
ENABLED_ENABLED=$(echo "$ENABLE_JSON" | grep -o '"enabled":[^,}]*' | cut -d: -f2)
echo "  Skill enabled: ${ENABLED_ENABLED:-false}"

if [ "$ENABLED_ENABLED" != "true" ]; then
    echo -e "${RED}✗${NC} Skill should be enabled, but enabled=${ENABLED_ENABLED:-false}"
    exit 1
fi

echo
echo "Step 9: Recent events"
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
DATA_DIR="${BASE_DIR}/data/skill_store"
STORE_PATH="${DATA_DIR}/store.json"

if [ -f "$STORE_PATH" ]; then
    echo -e "${GREEN}✓${NC} store.json exists at: $STORE_PATH"
    STORE_SIZE=$(stat -f%z "$STORE_PATH" 2>/dev/null || stat -c%s "$STORE_PATH" 2>/dev/null)
    echo "  Size: $STORE_SIZE bytes"
    
    # Check for skill ID in store.json
    if grep -q "$SKILL_ID" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Skill ID found in store.json"
    else
        echo -e "${RED}✗${NC} Skill ID NOT found in store.json"
        exit 1
    fi
    
    # Check for skill name in store.json
    if grep -q "my-test-skill" "$STORE_PATH"; then
        echo -e "${GREEN}✓${NC} Skill name found in store.json"
    else
        echo -e "${RED}✗${NC} Skill name NOT found in store.json"
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
