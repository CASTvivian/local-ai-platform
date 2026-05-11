"""Unit tests for code review gate service."""

import pytest
from app.models import (
    Finding,
    FindingType,
    RiskLevel,
    ReviewRequest,
    ReviewDecision,
)
from app.rules import RuleEngine, SecurityRule
from app.service import review_diff, suggest_tests, _determine_decision


def test_security_rule_dangerous_shell():
    """Test detection of dangerous shell commands."""
    rule = SecurityRule(
        rule_type=FindingType.dangerous_shell,
        patterns=["rm -rf /", "curl | sh"],
        severity=RiskLevel.high,
    )
    
    code = "rm -rf /some/path"
    findings = rule.check(code)
    
    assert len(findings) == 1
    assert findings[0].type == FindingType.dangerous_shell
    assert findings[0].pattern == "rm -rf /"
    assert findings[0].line == 1


def test_security_rule_secret_leak():
    """Test detection of secret leaks."""
    rule = SecurityRule(
        rule_type=FindingType.secret_leak,
        patterns=["api_key", "secret", "token"],
        severity=RiskLevel.critical,
    )
    
    code = "api_key = 'sk-1234567890'"
    findings = rule.check(code)
    
    assert len(findings) == 1
    assert findings[0].type == FindingType.secret_leak
    assert findings[0].severity == RiskLevel.critical


def test_security_rule_dynamic_exec():
    """Test detection of dynamic execution."""
    rule = SecurityRule(
        rule_type=FindingType.dynamic_exec,
        patterns=["eval(", "exec(", "subprocess.Popen"],
        severity=RiskLevel.high,
    )
    
    code = "eval(user_input)"
    findings = rule.check(code)
    
    assert len(findings) == 1
    assert findings[0].type == FindingType.dynamic_exec


def test_rule_engine_no_findings():
    """Test rule engine with safe code."""
    engine = RuleEngine()
    safe_code = "print('Hello, World!')"
    
    findings = engine.review_diff(safe_code)
    assert len(findings) == 0


def test_rule_engine_dangerous_code():
    """Test rule engine with dangerous code."""
    engine = RuleEngine()
    dangerous_code = "rm -rf /some/path && eval(code)"
    
    findings = engine.review_diff(dangerous_code)
    assert len(findings) >= 2  # At least 2 findings


def test_calculate_risk_level_low():
    """Test risk level calculation with no findings."""
    engine = RuleEngine()
    risk_level = engine.calculate_risk_level([])
    
    assert risk_level == RiskLevel.low


def test_calculate_risk_level_high():
    """Test risk level calculation with high-risk findings."""
    engine = RuleEngine()
    findings = [
        Finding(type=FindingType.dangerous_shell, pattern="rm -rf", severity=RiskLevel.high),
    ]
    risk_level = engine.calculate_risk_level(findings)
    
    assert risk_level == RiskLevel.high


def test_calculate_risk_level_critical():
    """Test risk level calculation with critical findings."""
    engine = RuleEngine()
    findings = [
        Finding(type=FindingType.secret_leak, pattern="api_key", severity=RiskLevel.critical),
    ]
    risk_level = engine.calculate_risk_level(findings)
    
    assert risk_level == RiskLevel.critical


def test_determine_decision_critical():
    """Test decision for critical risk."""
    decision = _determine_decision(RiskLevel.critical, [])
    assert decision == ReviewDecision.reject


def test_determine_decision_high():
    """Test decision for high risk."""
    decision = _determine_decision(RiskLevel.high, [])
    assert decision == ReviewDecision.request_changes


def test_determine_decision_low():
    """Test decision for low risk."""
    decision = _determine_decision(RiskLevel.low, [])
    assert decision == ReviewDecision.approve


def test_suggest_tests_python():
    """Test test suggestions for Python code."""
    req = {
        "code": "def my_function():\n    pass",
        "language": "python",
        "coverage_threshold": 0.8,
    }
    
    suggestions = suggest_tests(req)
    assert len(suggestions) > 0
    assert any(s.type == "unit" for s in suggestions)


def test_review_diff_endpoint():
    """Test review diff endpoint."""
    req = ReviewRequest(
        diff="print('hello')",
        files=["test.py"],
    )
    
    result = review_diff(req)
    assert result.review_id.startswith("review_")
    assert result.risk_level in [RiskLevel.low, RiskLevel.medium, RiskLevel.high, RiskLevel.critical]
    assert result.decision in [ReviewDecision.approve, ReviewDecision.reject, ReviewDecision.request_changes, ReviewDecision.needs_review]
