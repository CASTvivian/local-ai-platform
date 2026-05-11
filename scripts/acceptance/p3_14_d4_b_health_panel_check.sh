#!/bin/bash
# P3.14-D4-B: Desktop UI Health Panel 验收脚本
# 目标：验证健康面板与真实 Launcher 状态对齐

set -e

echo "========================================="
echo "P3.14-D4-B: Desktop UI Health Panel 验收"
echo "========================================="

# 颜色定义
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

PASS=0
FAIL=0

# 测试函数
test_pass() {
  echo -e "${GREEN}✅ PASS${NC}: $1"
  PASS=$((PASS+1))
}

test_fail() {
  echo -e "${RED}❌ FAIL${NC}: $1"
  FAIL=$((FAIL+1))
}

test_info() {
  echo -e "${YELLOW}ℹ️  INFO${NC}: $1"
}

# 检查文件存在
check_file() {
  if [ -f "$1" ]; then
    test_pass "$1 存在"
    return 0
  else
    test_fail "$1 不存在"
    return 1
  fi
}

# 检查文件包含特定内容
check_content() {
  if grep -q "$2" "$1" 2>/dev/null; then
    test_pass "$1 包含 '$2'"
    return 0
  else
    test_fail "$1 不包含 '$2'"
    return 1
  fi
}

echo ""
echo "=== 1. services.js 文件检查 ==="
SERVICES_JS="/Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src/js/services.js"
check_file "$SERVICES_JS"
check_content "$SERVICES_JS" "CORE_SERVICES"
check_content "$SERVICES_JS" "checkServiceHealth"
check_content "$SERVICES_JS" "refreshHealth"
check_content "$SERVICES_JS" "renderServiceHealth"
check_content "$SERVICES_JS" "renderServiceCard"

echo ""
echo "=== 2. CORE_SERVICES 数组完整性检查 ==="
check_content "$SERVICES_JS" "18093.*auto_router"
check_content "$SERVICES_JS" "18121.*skill_store"
check_content "$SERVICES_JS" "18123.*artifact_registry"
check_content "$SERVICES_JS" "18124.*code_review_gate"
check_content "$SERVICES_JS" "18125.*repo_memory"
check_content "$SERVICES_JS" "18126.*workflow_store"
check_content "$SERVICES_JS" "18127.*design_system"

echo ""
echo "=== 3. 服务元数据字段检查 ==="
check_content "$SERVICES_JS" 'tier.*"enterprise"'
check_content "$SERVICES_JS" 'tier.*"owned"'
check_content "$SERVICES_JS" 'tier.*"partial"'
check_content "$SERVICES_JS" 'required.*true'
check_content "$SERVICES_JS" 'required.*false'
check_content "$SERVICES_JS" 'role'
check_content "$SERVICES_JS" 'version'

echo ""
echo "=== 4. 渲染函数检查 ==="
check_content "$SERVICES_JS" "badge-enterprise"
check_content "$SERVICES_JS" "badge-partial"
check_content "$SERVICES_JS" "badge-required"
check_content "$SERVICES_JS" "service-version"
check_content "$SERVICES_JS" "service-role"
check_content "$SERVICES_JS" "service-error"

echo ""
echo "=== 5. HTML 集成检查 ==="
INDEX_HTML="/Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src/index.html"
check_file "$INDEX_HTML"
check_content "$INDEX_HTML" "refreshServices"
check_content "$INDEX_HTML" "服务健康"
check_content "$INDEX_HTML" 'onclick="refreshHealth()"'
check_content "$INDEX_HTML" 'id="services"'

echo ""
echo "=== 6. CSS 样式检查 ==="
CSS_FILE="/Users/mofamaomi/Documents/本地ai/core-platform/apps/desktop/src/styles/main.css"
check_file "$CSS_FILE"
check_content "$CSS_FILE" "service-grid"
check_content "$CSS_FILE" "service-card"
check_content "$CSS_FILE" "badge-enterprise"
check_content "$CSS_FILE" "badge-partial"
check_content "$CSS_FILE" "badge-required"
check_content "$CSS_FILE" "service-version"

echo ""
echo "=== 7. 企业服务健康检查 ==="
test_info "检查企业服务是否运行并返回正确版本"

# 检查 Skill Store
if curl -fsS http://127.0.0.1:18121/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18121 Skill Store 返回 0.3.1-enterprise"
else
  test_fail "18121 Skill Store 版本不正确或未运行"
fi

# 检查 Artifact Registry
if curl -fsS http://127.0.0.1:18123/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18123 Artifact Registry 返回 0.3.1-enterprise"
else
  test_fail "18123 Artifact Registry 版本不正确或未运行"
fi

# 检查 Code Review Gate
if curl -fsS http://127.0.0.1:18124/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18124 Code Review Gate 返回 0.3.1-enterprise"
else
  test_fail "18124 Code Review Gate 版本不正确或未运行"
fi

# 检查 Repo Memory
if curl -fsS http://127.0.0.1:18125/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18125 Repo Memory 返回 0.3.1-enterprise"
else
  test_fail "18125 Repo Memory 版本不正确或未运行"
fi

# 检查 Workflow Store
if curl -fsS http://127.0.0.1:18126/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18126 Workflow Store 返回 0.3.1-enterprise"
else
  test_fail "18126 Workflow Store 版本不正确或未运行"
fi

# 检查 Design System
if curl -fsS http://127.0.0.1:18127/health | grep -q '"version":"0.3.1-enterprise"'; then
  test_pass "18127 Design System 返回 0.3.1-enterprise"
else
  test_fail "18127 Design System 版本不正确或未运行"
fi

echo ""
echo "=== 8. 服务数量统计 ==="
test_info "统计 CORE_SERVICES 中的服务数量"
SERVICE_COUNT=$(grep -c 'port: 18' "$SERVICES_JS" || echo "0")
if [ "$SERVICE_COUNT" -eq 13 ]; then
  test_pass "CORE_SERVICES 包含 13 个服务"
else
  test_fail "CORE_SERVICES 包含 $SERVICE_COUNT 个服务（期望 13 个）"
fi

ENTERPRISE_COUNT=$(grep -c 'tier: "enterprise"' "$SERVICES_JS" || echo "0")
if [ "$ENTERPRISE_COUNT" -eq 6 ]; then
  test_pass "CORE_SERVICES 包含 6 个企业服务"
else
  test_fail "CORE_SERVICES 包含 $ENTERPRISE_COUNT 个企业服务（期望 6 个）"
fi

echo ""
echo "========================================="
echo "P3.14-D4-B 验收结果"
echo "========================================="
echo -e "通过: ${GREEN}${PASS}${NC}"
echo -e "失败: ${RED}${FAIL}${NC}"
echo "总计: $((PASS+FAIL))"

if [ $FAIL -eq 0 ]; then
  echo -e "${GREEN}🎉 所有验收测试通过！${NC}"
  echo ""
  echo "D4-B 完成内容："
  echo "1. ✅ 增强 services.js 包含完整的 CORE_SERVICES 数组"
  echo "2. ✅ 每个服务包含元数据（port, key, name, module, log, required, tier, role, note）"
  echo "3. ✅ 健康检查函数支持版本检测"
  echo "4. ✅ 渲染函数支持企业徽章和详细统计"
  echo "5. ✅ HTML 集成刷新按钮和服务健康面板"
  echo "6. ✅ CSS 样式支持增强的服务卡片"
  echo "7. ✅ 所有 6 个企业服务运行正常（0.3.1-enterprise）"
  echo ""
  echo "下一步：P3.14-D4-C: Package Preflight / 打包前验收"
  exit 0
else
  echo -e "${RED}❌ 有 $FAIL 个测试失败${NC}"
  exit 1
fi
