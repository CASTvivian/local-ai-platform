#!/usr/bin/env bash

echo "========================================="
echo "MAOMIAI Desktop Services Health Check"
echo "========================================="
echo

# Services to check: 16 ports
declare -a services=(
  "18080|model_gateway"
  "18081|agent_orchestrator"
  "18082|plugin_manager"
  "18083|eval_engine"
  "18093|auto_router"
  "18104|runtime_execution"
  "18110|policy_engine"
  "18111|trace_observability"
  "18112|eval_gateway"
  "18120|document_ingestion"
  "18121|skill_store"
  "18123|artifact_registry"
  "18124|code_review_gate"
  "18125|repo_memory"
  "18126|workflow_store"
  "18127|design_system"
)

total=${#services[@]}
up=0
down=0

for service in "${services[@]}"; do
  IFS='|' read -r port name <<< "$service"
  result=$(curl -s http://127.0.0.1:$port/health 2>/dev/null)
  if [ $? -eq 0 ]; then
    echo "✅ $port $name"
    ((up++))
  else
    echo "❌ $port $name"
    ((down++))
  fi
done

echo
echo "========================================="
echo "Summary: $up/$total services UP, $down/$total services DOWN"
echo "========================================="

if [ $down -eq 0 ]; then
  echo
  echo "✅ All services healthy!"
  exit 0
else
  echo
  echo "⚠️  Some services are down"
  exit 1
fi
