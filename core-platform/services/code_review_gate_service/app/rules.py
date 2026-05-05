"""Security rules and patterns for code review."""

import re
from typing import List, Dict, Tuple

from .models import Finding, FindingType, RiskLevel


class SecurityRule:
    """Security rule definition."""
    
    def __init__(
        self,
        rule_type: FindingType,
        patterns: List[str],
        severity: RiskLevel = RiskLevel.medium,
        description: str = "",
    ):
        self.rule_type = rule_type
        self.patterns = patterns
        self.severity = severity
        self.description = description
    
    def check(self, text: str, file: str = None) -> List[Finding]:
        """Check text for pattern matches."""
        findings = []
        lines = text.splitlines()
        
        for pattern in self.patterns:
            for i, line in enumerate(lines, 1):
                if pattern.lower() in line.lower():
                    findings.append(Finding(
                        type=self.rule_type,
                        pattern=pattern,
                        line=i,
                        file=file,
                        severity=self.severity,
                        description=self.description,
                    ))
        
        return findings


class RuleEngine:
    """Engine for applying security rules."""
    
    def __init__(self):
        self.rules = self._load_default_rules()
    
    def _load_default_rules(self) -> List[SecurityRule]:
        """Load default security rules."""
        return [
            # Dangerous shell commands
            SecurityRule(
                rule_type=FindingType.dangerous_shell,
                patterns=[
                    "rm -rf /",
                    "rm -rf",
                    "rm -rf *",
                    "curl | sh",
                    "curl | bash",
                    "wget | sh",
                    "wget | bash",
                    "chmod -R 777",
                    "chmod 777",
                    "mkfs",
                    "dd if=/",
                ],
                severity=RiskLevel.high,
                description="Dangerous shell command that could cause data loss or security issues",
            ),
            
            # Secret leaks
            SecurityRule(
                rule_type=FindingType.secret_leak,
                patterns=[
                    "api_key",
                    "apikey",
                    "api-key",
                    "secret",
                    "secret_key",
                    "private_key",
                    "private-key",
                    "password",
                    "pwd",
                    "token",
                    "auth_token",
                    "bearer",
                ],
                severity=RiskLevel.critical,
                description="Potential secret or credential leak",
            ),
            
            # Dynamic execution
            SecurityRule(
                rule_type=FindingType.dynamic_exec,
                patterns=[
                    "eval(",
                    "exec(",
                    "subprocess.Popen",
                    "os.system(",
                    "os.popen(",
                    "execfile(",
                    "compile(",
                ],
                severity=RiskLevel.high,
                description="Dynamic code execution vulnerability",
            ),
            
            # File access
            SecurityRule(
                rule_type=FindingType.file_access,
                patterns=[
                    "open(",
                    "Path(",
                    "Path.unlink",
                    "Path.rmdir",
                    "shutil.rmtree",
                ],
                severity=RiskLevel.low,
                description="File system access",
            ),
            
            # Network access
            SecurityRule(
                rule_type=FindingType.network_access,
                patterns=[
                    "requests.get",
                    "requests.post",
                    "urlopen",
                    "socket.connect",
                    "http.client",
                ],
                severity=RiskLevel.low,
                description="Network access",
            ),
            
            # SQL injection
            SecurityRule(
                rule_type=FindingType.injection,
                patterns=[
                    "execute(sql",
                    "exec(query",
                    "query = \"",
                    "f\"SELECT",
                    "f\"INSERT",
                    "f\"UPDATE",
                    "f\"DELETE",
                ],
                severity=RiskLevel.high,
                description="Potential SQL injection",
            ),
            
            # Path traversal
            SecurityRule(
                rule_type=FindingType.path_traversal,
                patterns=[
                    "../",
                    "..\\",
                    "path.replace",
                    "os.path.join(",
                ],
                severity=RiskLevel.medium,
                description="Potential path traversal vulnerability",
            ),
        ]
    
    def review_diff(self, diff: str, files: List[str] = None) -> List[Finding]:
        """
        Review code diff and return findings.
        
        Args:
            diff: Code diff to review
            files: List of affected files
        
        Returns:
            List of findings
        """
        all_findings: List[Finding] = []
        
        # Review each rule
        for rule in self.rules:
            # If files provided, review per file context
            if files:
                for file in files:
                    file_findings = rule.check(diff, file=file)
                    all_findings.extend(file_findings)
            else:
                findings = rule.check(diff)
                all_findings.extend(findings)
        
        return all_findings
    
    def calculate_risk_level(self, findings: List[Finding]) -> RiskLevel:
        """Calculate overall risk level from findings."""
        if not findings:
            return RiskLevel.low
        
        # Count findings by severity
        critical_count = sum(1 for f in findings if f.severity == RiskLevel.critical)
        high_count = sum(1 for f in findings if f.severity == RiskLevel.high)
        medium_count = sum(1 for f in findings if f.severity == RiskLevel.medium)
        
        # Determine risk level
        if critical_count > 0:
            return RiskLevel.critical
        elif high_count >= 2:
            return RiskLevel.critical
        elif high_count == 1:
            return RiskLevel.high
        elif medium_count >= 3:
            return RiskLevel.high
        elif medium_count >= 1:
            return RiskLevel.medium
        
        return RiskLevel.low


# Global rule engine instance
rule_engine = RuleEngine()


def get_default_rules() -> List[Dict[str, any]]:
    """Get default security rules as dict."""
    return [
        {
            "type": "dangerous_shell",
            "patterns": rule_engine.rules[0].patterns,
            "severity": "high",
            "description": "Dangerous shell command that could cause data loss or security issues",
        },
        {
            "type": "secret_leak",
            "patterns": rule_engine.rules[1].patterns,
            "severity": "critical",
            "description": "Potential secret or credential leak",
        },
        {
            "type": "dynamic_exec",
            "patterns": rule_engine.rules[2].patterns,
            "severity": "high",
            "description": "Dynamic code execution vulnerability",
        },
    ]
