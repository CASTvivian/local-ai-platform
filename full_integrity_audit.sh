#!/bin/bash
ROOT="$(git rev-parse --show-toplevel)"
cd "$ROOT" || exit 1
mkdir -p docs/reports
REPORT="docs/reports/P3_14_D7_FULL_LOCAL_PROJECT_INTEGRITY_AUDIT.md"
rm -rf /tmp/p3_14_d7_full_integrity
mkdir -p /tmp/p3_14_d7_full_integrity
echo "# P3.14-D7 Full Local Project Integrity Audit" > "$REPORT"
echo >> "$REPORT"
echo "Generated at: $(date)" >> "$REPORT"
echo >> "$REPORT"
echo "===== 1. Basic Git / root info ====="
{
  echo "## 1. Git / Root"
  echo
  echo '```text'
  pwd
  git rev-parse --show-toplevel
  git branch --show-current
  git log --oneline -20
  echo
  echo "---- git status ----"
  git status --short
  echo '```'
  echo
} >> "$REPORT"
echo "===== 2. Top-level directory inventory ====="
{
  echo "## 2. Top-level Directory Inventory"
  echo
  echo '```text'
  find . -maxdepth 2 -type d | sort
  echo '```'
  echo
} >> "$REPORT"
echo "===== 3. Detect duplicate project roots ====="
{
  echo "## 3. Duplicate / Nested Project Roots"
  echo
  echo '```text'
  echo "Potential desktop roots:"
  find . -path "*/apps/desktop" -type d -print | sort
  echo
  echo "Potential services roots:"
  find . -path "*/services" -type d -print | sort
  echo
  echo "Potential scripts roots:"
  find . -path "*/scripts" -type d -print | sort
  echo
  echo "Potential nested core-platform dirs:"
  find . -path "*/core-platform" -type d -print | sort
  echo '```'
  echo
} >> "$REPORT"
echo "===== 4. Desktop source candidates ====="
{
  echo "## 4. Desktop Source Candidates"
  echo
  for d in \
    "apps/desktop" \
    "core-platform/apps/desktop" \
    "core-platform/core-platform/apps/desktop" \
    "apps/desktop/bundle/backend/apps/desktop"
  do
    echo "### $d"
    echo
    if [ -d "$d" ]; then
      echo '```text'
      echo "EXISTS"
      find "$d" -maxdepth 3 -type f \( -name "index\.html" -o -name "package\.json" -o -name "tauri\.conf\.json" -o -name "*.js" \) | sort | head -200
      echo
      if [ -f "$d/src/index.html" ]; then
        echo "--- src/index.html markers ---"
        grep -n "MAOMIAI\|P3 大脑工作台\|Windows 一体化测试版\|本地 AI\|hidden-internal\|windows-click-model-setup" "$d/src/index.html" | head -100 || true
        wc -l "$d/src/index.html"
      fi
      if [ -f "$d/dist/index.html" ]; then
        echo "--- dist/index.html markers ---"
        grep -n "MAOMIAI\|P3 大脑工作台\|Windows 一体化测试版\|本地 AI\|hidden-internal\|windows-click-model-setup" "$d/dist/index.html" | head -100 || true
        wc -l "$d/dist/index.html"
      fi
      echo '```'
    else
      echo "MISSING"
    fi
    echo
  done
} >> "$REPORT"
echo "===== 5. Service inventory across all service roots ====="
{
  echo "## 5. Service Inventory"
  echo
  for root in "services" "core-platform/services" "core-platform/core-platform/services" "apps/desktop/bundle/backend/services"
  do
    echo "### $root"
    echo
    if [ -d "$root" ]; then
      echo '```text'
      find "$root" -maxdepth 2 -type f \( -name "main\.py" -o -name "*.py" \) | sort
      echo
      echo "--- service summary ---"
      for svc in "$root"/*; do
        [ -d "$svc" ] || continue
        name="$(basename "$svc")"
        py_count="$(find "$svc" -type f -name "*.py" | wc -l | tr -d ' ')"
        main="NO"
        [ -f "$svc/main.py" ] && main="YES"
        marker=""
        [ -f "$svc/main.py" ] && marker="$(grep -E "enterprise|0\.3\.1|0\.2\.0|version" "$svc/main.py" | head -3 | tr '\n' ' ')"
        echo "$name | py_files=$py_count | main.py=$main | $marker"
      done
      echo '```'
    else
      echo "MISSING"
    fi
    echo
  done
} >> "$REPORT"
echo "===== 6. Required core services check ====="
CORE_SERVICES=(
  model_gateway
  model_bootstrap_service
  skill_store_service
  artifact_registry_service
  code_review_gate_service
  repo_memory_service
  workflow_store_service
  design_system_service
  auto_router_service
  runtime_execution_service
  policy_engine_service
  trace_observability_service
  eval_gateway_service
  document_ingestion_service
)
{
  echo "## 6. Required Core Services Check"
  echo
  echo '```text'
  for svc in "${CORE_SERVICES[@]}"; do
    echo "--- $svc ---"
    found=0
    for root in services core-platform/services; do
      if [ -d "$root/$svc" ]; then
        found=1
        echo "FOUND: $root/$svc"
        find "$root/$svc" -maxdepth 2 -type f -name "*.py" | sort
        if [ -f "$root/$svc/main.py" ]; then
          python3 -m py_compile "$root/$svc/main.py" && echo "PY_COMPILE_OK: $root/$svc/main.py" || echo "PY_COMPILE_FAIL: $root/$svc/main.py"
          grep -n "enterprise\|0.3.1\|version\|APP_VERSION" "$root/$svc/main.py" | head -10 || true
        else
          echo "NO_MAIN_PY"
        fi
      fi
    done
    if [ "$found" = "0" ]; then
      echo "MISSING_BOTH_ROOTS: $svc"
    fi
    echo
  done
  echo '```'
  echo
} >> "$REPORT"
echo "===== 7. Empty / suspicious directories ====="
{
  echo "## 7. Empty / Suspicious Directories"
  echo
  echo '```text'
  echo "--- empty dirs under core-platform/services and services ---"
  find services core-platform/services -type d -empty 2>/dev/null | sort || true
  echo
  echo "--- dirs with only __init__.py ---"
  for d in $(find services core-platform/services -maxdepth 2 -type d 2>/dev/null | sort); do
    count="$(find "$d" -maxdepth 1 -type f | wc -l | tr -d ' ')"
    if [ "$count" = "1" ] && [ -f "$d/__init__.py" ]; then
      echo "$d"
    fi
  done
  echo '```'
  echo
} >> "$REPORT"
echo "===== 8. Windows runtime scripts inventory ====="
{
  echo "## 8. Windows Runtime Scripts"
  echo
  for root in scripts/windows core-platform/scripts/windows; do
    echo "### $root"
    echo
    if [ -d "$root" ]; then
      echo '```text'
      find "$root" -maxdepth 1 -type f | sort
      echo
      for f in "$root"/*.ps1; do
        [ -f "$f" ] || continue
        echo "--- $f ---"
        wc -l "$f"
        grep -n "ensure_runtime\|bootstrap_runtime\|ollama\|uvicorn\|python" "$f" | head -30 || true
      done
      echo '```'
    else
      echo "MISSING"
    fi
    echo
  done
} >> "$REPORT"
echo "===== 9. Tauri configs and resource paths ====="
{
  echo "## 9. Tauri Configs"
  echo
  echo '```text'
  find . -name "tauri.conf.json" -print | sort
  echo '```'
  echo
  for f in $(find . -name "tauri.conf.json" -print | sort); do
    echo "### $f"
    echo
    echo '```json'
    cat "$f"
    echo '```'
    echo
    echo '```text'
    echo "--- resource path verification from $(dirname "$f") ---"
    dir="$(dirname "$f")"
    python3 - "$f" <<'PY'
import json, sys, pathlib
p = pathlib.Path(sys.argv[1])
data = json.loads(p.read_text(encoding="utf-8"))
resources = data.get("bundle", {}).get("resources", [])
base = p.parent
for r in resources:
    if r.startswith("http"):
        continue
    target = (base / r).resolve()
    print(("OK " if target.exists() else "MISS ") + r + " -> " + str(target))
PY
    echo '```'
    echo
  done
} >> "$REPORT"
echo "===== 10. GitHub workflow audit ====="
{
  echo "## 10. GitHub Workflow Audit"
  echo
  for f in .github/workflows/*.yml .github/workflows/*.yaml; do
    [ -f "$f" ] || continue
    echo "### $f"
    echo
    echo '```yaml'
    grep -n "name:\|working-directory:\|apps/desktop\|core-platform/apps/desktop\|scripts.windows\|scripts\\\\windows\|services" "$f" || true
    echo '```'
    echo
  done
} >> "$REPORT"
echo "===== 11. Build/release artifacts inventory ====="
{
  echo "## 11. Build and Release Artifacts"
  echo
  echo '```text'
  echo "--- release dirs ---"
  find . -path "*/releases/*" -maxdepth 5 -type f 2>/dev/null | sort | head -300
  echo
  echo "--- tauri bundle dirs ---"
  find . -path "*/src-tauri/target/release/bundle/*" -type f 2>/dev/null | sort | head -300
  echo
  echo "--- package sizes ---"
  find . -type f \( -name "*.dmg" -o -name "*.msi" -o -name "*setup.exe" -o -name "*.tar.gz" \) -exec ls -lh {} \; 2>/dev/null | sort
  echo '```'
  echo
} >> "$REPORT"
echo "===== 12. Large files / ignored risk audit ====="
{
  echo "## 12. Large Files / Git Ignore Risk"
  echo
  echo '```text'
  echo "--- largest files under repo excluding .git/node_modules/target ---"
  find . \
    -path "./.git" -prune -o \
    -path "*/node_modules" -prune -o \
    -path "*/target" -prune -o \
    -type f -size +20M -exec ls -lh {} \; | sort -k5 -h || true
  echo
  echo "--- git ignored files sample ---"
  git status --ignored --short | head -300 || true
  echo '```'
  echo
} >> "$REPORT"
echo "===== 13. Python syntax check for all tracked service main.py ====="
{
  echo "## 13. Python Syntax Check"
  echo
  echo '```text'
  fail=0
  while read -r f; do
    echo "--- $f ---"
    if python3 -m py_compile "$f"; then
      echo "OK"
    else
      echo "FAIL"
      fail=1
    fi
  done < <(find services core-platform/services -type f -name "main.py" 2>/dev/null | sort)
  echo "PY_SYNTAX_FAIL=$fail"
  echo '```'
  echo
} >> "$REPORT"
echo "===== 14. JS syntax check for desktop JS ====="
{
  echo "## 14. JavaScript Syntax Check"
  echo
  echo '```text'
  fail=0
  while read -r f; do
    echo "--- $f ---"
    if node --check "$f"; then
      echo "OK"
    else
      echo "FAIL"
      fail=1
    fi
  done < <(find core-platform/apps/desktop/src/js apps/desktop/src/js -type f -name "*.js" 2>/dev/null | sort)
  echo "JS_SYNTAX_FAIL=$fail"
  echo '```'
  echo
} >> "$REPORT"
echo "===== 15. Summary markers ====="
{
  echo "## 15. Summary"
  echo
  echo "- Full local project audit completed."
  echo "- This report audits the whole local Git repository, not just one packaging path."
  echo "- Review sections for duplicate roots, empty service directories, stale desktop copies, and packaging resources."
  echo
} >> "$REPORT"
echo
echo "===== Report created ====="
echo "$REPORT"
echo
echo "===== Quick suspicious summary ====="
echo "--- empty dirs ---"
find services core-platform/services -type d -empty 2>/dev/null | sort | head -80 || true
echo
echo "--- duplicate desktop roots ---"
find . -path "*/apps/desktop" -type d -print | sort
echo
echo "--- service roots ---"
find . -path "*/services" -type d -print | sort
echo
echo "--- git status ---"
git status --short | head -200
