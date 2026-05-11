"""Business logic layer for code review gate service."""

from datetime import datetime
from typing import List, Optional, Dict, Any

from .models import (
    ReviewResult,
    ReviewRequest,
    ReviewDecision,
    RiskLevel,
    SuggestTestsRequest,
    TestSuggestion,
    ReviewSummary,
)
from .storage import (
    load_store,
    save_store,
    append_event,
    append_error,
    recent_events,
    make_review_id,
    BASE_DIR,
)
from .rules import rule_engine, get_default_rules


def now_ts() -> float:
    """Get current timestamp."""
    return datetime.utcnow().timestamp()


def review_diff(req: ReviewRequest) -> ReviewResult:
    """
    Review code diff and return assessment.
    
    Args:
        req: Review request with diff and metadata
    
    Returns:
        ReviewResult with findings and decision
    """
    # Run security rules
    findings = rule_engine.review_diff(req.diff, req.files)
    
    # Calculate risk level
    risk_level = rule_engine.calculate_risk_level(findings)
    
    # Determine decision based on risk level
    decision = _determine_decision(risk_level, findings)
    
    # Generate summary
    summary = _generate_summary(risk_level, len(findings))
    
    # Generate test suggestions
    test_suggestions = _suggest_tests(req.diff, req.files)
    
    # Create review result
    review_id = make_review_id()
    ts = now_ts()
    
    result = ReviewResult(
        review_id=review_id,
        risk_level=risk_level,
        decision=decision,
        findings=findings,
        test_suggestions=test_suggestions,
        summary=summary,
        created_at=ts,
    )
    
    # Store result
    store = load_store()
    store.items.append(result)
    save_store(store)
    
    append_event(
        "review_diff",
        {
            "review_id": review_id,
            "risk_level": str(risk_level),
            "decision": str(decision),
            "findings_count": len(findings),
            "files": req.files,
        }
    )
    
    return result


def suggest_tests(req: SuggestTestsRequest) -> List[TestSuggestion]:
    """
    Generate test suggestions for code.
    
    Args:
        req: Test suggestion request
    
    Returns:
        List of test suggestions
    """
    suggestions = []
    
    # Check code patterns and suggest appropriate tests
    code_lower = req.code.lower()
    
    # Function definitions suggest unit tests
    if "def " in code_lower:
        suggestions.append(TestSuggestion(
            type="unit",
            description="Write unit tests for each function",
            code="def test_<function_name>():\n    # Arrange\n    # Act\n    # Assert",
            priority="high",
        ))
    
    # Class definitions suggest integration tests
    if "class " in code_lower:
        suggestions.append(TestSuggestion(
            type="integration",
            description="Write integration tests for class interactions",
            code="def test_<class_name>_integration():\n    # Test class with dependencies",
            priority="medium",
        ))
    
    # API calls suggest API tests
    if any(keyword in code_lower for keyword in ["requests.", "http.", "fetch", "axios"]):
        suggestions.append(TestSuggestion(
            type="integration",
            description="Write API endpoint tests",
            code="def test_api_endpoint():\n    # Test HTTP requests",
            priority="high",
        ))
    
    # Database operations suggest DB tests
    if any(keyword in code_lower for keyword in ["db.", "database", "sql", "query"]):
        suggestions.append(TestSuggestion(
            type="integration",
            description="Write database query tests",
            code="def test_database_query():\n    # Test SQL queries",
            priority="high",
        ))
    
    # File operations suggest file tests
    if any(keyword in code_lower for keyword in ["open(", "Path(", "file"]):
        suggestions.append(TestSuggestion(
            type="unit",
            description="Write file I/O tests",
            code="def test_file_operations():\n    # Test read/write operations",
            priority="medium",
        ))
    
    # Add general suggestions if none specific
    if not suggestions:
        suggestions.append(TestSuggestion(
            type="unit",
            description="Write unit tests to verify core functionality",
            priority="high",
        ))
        suggestions.append(TestSuggestion(
            type="integration",
            description="Write integration tests for component interactions",
            priority="medium",
        ))
    
    # Add coverage goal suggestion
    if req.coverage_threshold > 0:
        suggestions.append(TestSuggestion(
            type="e2e",
            description=f"Achieve {req.coverage_threshold * 100}% code coverage",
            code=f"# Run coverage: pytest --cov=. --cov-fail-under={req.coverage_threshold * 100}",
            priority="medium",
        ))
    
    return suggestions


def get_review_summary() -> ReviewSummary:
    """
    Generate summary of all reviews.
    
    Returns:
        ReviewSummary with statistics
    """
    store = load_store()
    items = store.items
    
    if not items:
        return ReviewSummary(
            total_reviews=0,
            high_risk_count=0,
            medium_risk_count=0,
            low_risk_count=0,
            approval_rate=0.0,
            average_findings=0.0,
        )
    
    # Count by risk level
    high_risk = sum(1 for r in items if r.risk_level == RiskLevel.high)
    medium_risk = sum(1 for r in items if r.risk_level == RiskLevel.medium)
    low_risk = sum(1 for r in items if r.risk_level == RiskLevel.low)
    critical_risk = sum(1 for r in items if r.risk_level == RiskLevel.critical)
    
    # Calculate approval rate
    approved = sum(1 for r in items if r.decision == ReviewDecision.approve)
    approval_rate = approved / len(items) if items else 0.0
    
    # Calculate average findings
    total_findings = sum(len(r.findings) for r in items)
    avg_findings = total_findings / len(items) if items else 0.0
    
    return ReviewSummary(
        total_reviews=len(items),
        high_risk_count=high_risk + critical_risk,
        medium_risk_count=medium_risk,
        low_risk_count=low_risk,
        approval_rate=approval_rate,
        average_findings=avg_findings,
    )


def _determine_decision(risk_level: RiskLevel, findings: List) -> ReviewDecision:
    """Determine review decision based on risk level and findings."""
    if risk_level == RiskLevel.critical:
        return ReviewDecision.reject
    elif risk_level == RiskLevel.high:
        return ReviewDecision.request_changes
    elif risk_level == RiskLevel.medium:
        return ReviewDecision.needs_review
    else:
        return ReviewDecision.approve


def _generate_summary(risk_level: RiskLevel, findings_count: int) -> str:
    """Generate review summary."""
    if risk_level == RiskLevel.critical:
        return f"CRITICAL: {findings_count} security findings detected. Immediate action required."
    elif risk_level == RiskLevel.high:
        return f"HIGH: {findings_count} findings detected. Review and fix before merge."
    elif risk_level == RiskLevel.medium:
        return f"MEDIUM: {findings_count} findings detected. Review recommended."
    else:
        return f"LOW: Code passed security checks. {findings_count} minor findings."


def _suggest_tests(diff: str, files: List[str]) -> List[str]:
    """Generate test suggestions based on code diff."""
    suggestions = [
        "Run unit tests",
        "Run integration tests",
        "Run source integrity check",
        "Run eval gateway regression",
        "Run security scan",
    ]
    
    # Add language-specific suggestions
    if any(f.endswith(('.py', '.pyx', '.pyi')) for f in files):
        suggestions.append("Run pytest with coverage")
        suggestions.append("Run mypy type checking")
        suggestions.append("Run black formatting check")
    
    if any(f.endswith(('.ts', '.tsx', '.js', '.jsx')) for f in files):
        suggestions.append("Run ESLint")
        suggestions.append("Run TypeScript type checking")
        suggestions.append("Run Jest tests")
    
    return suggestions


def get_recent_events(limit: int = 50) -> List[Dict[str, Any]]:
    """Get recent events."""
    return recent_events(limit)


def get_health_info() -> Dict[str, Any]:
    """Get health information."""
    store = load_store()
    return {
        "service": "code_review_gate_service",
        "version": "0.3.1-enterprise",
        "kind": "code_review_gate",
        "description": "diff 审查、危险代码检测、测试建议、变更风险评分。",
        "store_version": store.store_version,
        "count": len(store.items),
    }
