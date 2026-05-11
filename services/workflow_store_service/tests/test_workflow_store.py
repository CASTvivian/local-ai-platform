"""Unit tests for workflow store service."""

import pytest
from app.models import (
    WorkflowNodeType,
    WorkflowNode,
    WorkflowEdge,
    RegisterWorkflowRequest,
    ValidationResult,
)
from app.validation import validate_workflow


def test_validate_minimal_workflow():
    """Test validation of minimal valid workflow."""
    req = RegisterWorkflowRequest.model_validate(
        {
            "name": "minimal",
            "nodes": [
                {"id": "start", "type": "start", "name": "Start"},
                {"id": "end", "type": "end", "name": "End"},
            ],
            "edges": [{"id": "e1", "source": "start", "target": "end"}],
            "runtime_requirements": {"services": ["18104"], "models": ["qwen2.5:7b"]},
        }
    )
    result = validate_workflow(req)
    assert result.ok is True
    assert len(result.issues) == 0


def test_validate_missing_start():
    """Test validation with missing start node."""
    req = RegisterWorkflowRequest.model_validate(
        {
            "name": "no_start",
            "nodes": [
                {"id": "agent", "type": "agent", "name": "Agent"},
                {"id": "end", "type": "end", "name": "End"},
            ],
            "edges": [{"id": "e1", "source": "agent", "target": "end"}],
        }
    )
    result = validate_workflow(req)
    assert result.ok is False
    assert any(i.code == "invalid_start_count" for i in result.issues)


def test_validate_duplicate_nodes():
    """Test validation with duplicate node IDs."""
    with pytest.raises(ValueError, match="duplicate node ids"):
        RegisterWorkflowRequest.model_validate(
            {
                "name": "duplicate",
                "nodes": [
                    {"id": "node1", "type": "start", "name": "Start"},
                    {"id": "node1", "type": "end", "name": "End"},
                ],
                "edges": [],
            }
        )


def test_validate_edge_references():
    """Test validation with invalid edge references."""
    req = RegisterWorkflowRequest.model_validate(
        {
            "name": "bad_edges",
            "nodes": [
                {"id": "start", "type": "start", "name": "Start"},
                {"id": "end", "type": "end", "name": "End"},
            ],
            "edges": [
                {"id": "e1", "source": "start", "target": "nonexistent"},
                {"id": "e2", "source": "ghost", "target": "end"},
            ],
        }
    )
    result = validate_workflow(req)
    assert result.ok is False
    assert any(i.code == "edge_target_missing" for i in result.issues)
    assert any(i.code == "edge_source_missing" for i in result.issues)
