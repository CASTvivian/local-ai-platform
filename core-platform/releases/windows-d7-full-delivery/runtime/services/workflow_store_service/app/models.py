"""Pydantic data models for workflow store service."""

from enum import Enum
from typing import Any, Dict, List, Optional, Set
from datetime import datetime
from pydantic import BaseModel, Field, field_validator


class WorkflowNodeType(str, Enum):
    start = "start"
    end = "end"
    agent = "agent"
    tool = "tool"
    condition = "condition"
    parallel = "parallel"
    document_retrieval = "document_retrieval"
    model_invocation = "model_invocation"
    code_execution = "code_execution"
    web_scraping = "web_scraping"
    file_operation = "file_operation"


class WorkflowNode(BaseModel):
    id: str = Field(..., min_length=1)
    type: WorkflowNodeType
    name: str = Field(..., min_length=1)
    config: Dict[str, Any] = Field(default_factory=dict)
    position: Optional[Dict[str, float]] = None


class WorkflowEdge(BaseModel):
    id: str = Field(..., min_length=1)
    source: str = Field(..., min_length=1)
    target: str = Field(..., min_length=1)
    condition: Optional[Dict[str, Any]] = None


class RuntimeRequirements(BaseModel):
    services: List[str] = Field(default_factory=list)
    models: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)
    permissions: List[str] = Field(default_factory=list)
    estimated_timeout_sec: int = 300

    @field_validator("estimated_timeout_sec")
    @classmethod
    def validate_timeout(cls, v: int) -> int:
        if v < 1:
            return 300
        if v > 24 * 3600:
            raise ValueError("estimated_timeout_sec is too large")
        return v


class WorkflowDefinition(BaseModel):
    nodes: List[WorkflowNode] = Field(default_factory=list)
    edges: List[WorkflowEdge] = Field(default_factory=list)
    runtime_requirements: Optional[RuntimeRequirements] = None

    @field_validator("nodes")
    @classmethod
    def validate_unique_node_ids(cls, v: List[WorkflowNode]) -> List[WorkflowNode]:
        ids = [n.id for n in v]
        if len(ids) != len(set(ids)):
            duplicates = [x for x in ids if ids.count(x) > 1]
            raise ValueError(f"duplicate node ids: {set(duplicates)}")
        return v


class WorkflowRecord(BaseModel):
    id: str
    name: str = Field(..., min_length=1)
    version: str = "1.0.0"
    description: str = ""
    source: str = "manual"
    enabled: bool = True
    definition: WorkflowDefinition
    created_at: float
    updated_at: float


class StoreFile(BaseModel):
    store_version: str = "1.0.0"
    items: List[WorkflowRecord] = Field(default_factory=list)


# Request models
class RegisterWorkflowRequest(WorkflowDefinition):
    name: str = Field(..., min_length=1)
    version: str = "1.0.0"
    description: str = ""
    source: str = "manual"


class ImportWorkflowRequest(BaseModel):
    workflow_json: Dict[str, Any]


class DryRunRequest(BaseModel):
    workflow_id: str = Field(..., min_length=1)
    input_context: Dict[str, Any] = Field(default_factory=dict)


# Validation models
class ValidationIssue(BaseModel):
    level: str = Field(..., pattern="^(error|warning|info)$")
    code: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
    node_id: Optional[str] = None
    edge_id: Optional[str] = None


class ValidationResult(BaseModel):
    ok: bool
    issues: List[ValidationIssue] = Field(default_factory=list)
