#!/usr/bin/env bash

# P3.14-D7-A Desktop Interaction Regression Acceptance Check
# This script validates D7-A criteria: App startup and service health

set -euo pipefail

echo "========================================="
echo "P3.14-D7-A Acceptance Check"
echo "========================================="
echo

# Check 1: Backend services 13/16 core services healthy
echo "[A.1] Checking 16 backend services..."
cd /Users/mofamaomi/Documents/本地ai/core-platform
bash scripts/check_all_desktop_services.sh > /tmp/d7a_services_check.txt 2>&1
if grep -q "All services healthy" /tmp/d7a_services_check.txt; then
  echo "✅ All 16 backend services healthy"
else
  echo "❌ Some backend services down"
  exit 1
fi

# Check 2: Model Gateway (18080) accessible
echo
echo "[A.2] Checking Model Gateway..."
health=$(curl -s http://127.0.0.1:18080/health)
if echo "$health" | grep -q "ok.*true"; then
  echo "✅ Model Gateway accessible"
else
  echo "❌ Model Gateway not responding"
  exit 1
fi

# Check 3: Enterprise services (18120-18127) have correct versions
echo
echo "[A.3] Checking enterprise service versions..."
enterprise_ports=(18121 18123 18124 18125 18126 18127)
all_enterprise=true
for port in "${enterprise_ports[@]}"; do
  version=$(curl -s http://127.0.0.1:$port/health | grep -o '"version":"[^"]*"' | cut -d'"' -f4)
  if echo "$version" | grep -q "enterprise"; then
    echo "✅ Port $port: $version"
  else
    echo "⚠️  Port $port: $version (not enterprise)"
    all_enterprise=false
  fi
done
if [ "$all_enterprise" = true ]; then
  echo "✅ All enterprise services have enterprise version"
else
  echo "⚠️  Some enterprise services not at enterprise version"
fi

# Check 4: Ollama running
echo
echo "[A.4] Checking Ollama..."
if curl -s http://127.0.0.1:11434/api/tags > /dev/null 2>&1; then
  echo "✅ Ollama running on :11434"
else
  echo "⚠️  Ollama not accessible on :11434"
fi

# Check 5: Desktop app bundle exists
echo
echo "[A.5] Checking Desktop app bundle..."
if [ -d "/Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src-tauri/target/release/bundle/macos/Local AI Platform.app" ]; then
  echo "✅ Desktop app bundle exists"
else
  echo "❌ Desktop app bundle not found"
  exit 1
fi

# Check 6: Verify app is running (check if Tauri process is alive)
echo
echo "[A.6] Checking if Desktop app is running..."
if pgrep -f "Local AI Platform" > /dev/null; then
  echo "✅ Desktop app process found"
else
  echo "⚠️  Desktop app not running (may need manual start)"
fi

echo
echo "========================================="
echo "D7-A Automated Checks Complete"
echo "========================================="
echo
echo "Manual verification required:"
echo "- [ ] App launches without errors"
echo "- [ ] No red error boxes in UI"
echo "- [ ] Right-side service health panel can refresh"
echo "- [ ] Left-side navigation buttons work"
echo "- [ ] Local model returns Chinese responses"
echo "- [ ] Chat session isolation works"
echo
echo "See: /Users/mofamaomi/Documents/本地ai/core-platform/releases/maomiai-desktop-demo/docs/P3_14_D7_DESKTOP_INTERACTION_REGRESSION_CHECKLIST.md"
echo
