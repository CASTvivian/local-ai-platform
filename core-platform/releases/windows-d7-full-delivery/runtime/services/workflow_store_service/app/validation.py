"""Validation logic for workflow definitions."""

from typing import List, Set

from .models import (
    WorkflowDefinition,
    WorkflowNodeType,
    ValidationIssue,
    ValidationResult,
)


def validate_workflow(defn: WorkflowDefinition) -> ValidationResult:
    """Validate workflow definition and return any issues."""
    issues: list[ValidationIssue] = []
    node_ids: Set[str] = {n.id for n in defn.nodes}

    # Check for nodes
    if not defn.nodes:
        issues.append(
            ValidationIssue(
                level="error",
                code="no_nodes",
                message="workflow must contain at least one node",
            )
        )

    # Check start and end nodes
    start_nodes = [n for n in defn.nodes if n.type == WorkflowNodeType.start]
    end_nodes = [n for n in defn.nodes if n.type == WorkflowNodeType.end]

    if len(start_nodes) != 1:
        issues.append(
            ValidationIssue(
                level="error",
                code="invalid_start_count",
                message=f"workflow must contain exactly one start node, found {len(start_nodes)}",
            )
        )

    if len(end_nodes) < 1:
        issues.append(
            ValidationIssue(
                level="warning",
                code="missing_end_node",
                message="workflow should contain at least one end node",
            )
        )

    # Check edge references
    for edge in defn.edges:
        if edge.source not in node_ids:
            issues.append(
                ValidationIssue(
                    level="error",
                    code="edge_source_missing",
                    message=f"edge source node not found: {edge.source}",
                    edge_id=edge.id,
                )
            )

        if edge.target not in node_ids:
            issues.append(
                ValidationIssue(
                    level="error",
                    code="edge_target_missing",
                    message=f"edge target node not found: {edge.target}",
                    edge_id=edge.id,
                )
            )

    # Check for isolated nodes (not start/end, but not connected)
    connected: Set[str] = set()
    for edge in defn.edges:
        connected.add(edge.source)
        connected.add(edge.target)

    for node in defn.nodes:
        if node.type not in {WorkflowNodeType.start, WorkflowNodeType.end} and node.id not in connected:
            issues.append(
                ValidationIssue(
                    level="warning",
                    code="isolated_node",
                    message=f"node is isolated (no edges): {node.id}",
                    node_id=node.id,
                )
            )

    ok = not any(i.level == "error" for i in issues)
    return ValidationResult(ok=ok, issues=issues)
