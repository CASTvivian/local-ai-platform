from __future__ import annotations

import ast
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


CONFIG = Path("core-platform/data/agent_policy/hardcode_guard.json")


def load_config() -> Dict[str, Any]:
    return json.loads(CONFIG.read_text(encoding="utf-8"))


def is_allowed_file(path: Path, allowed_files: List[str]) -> bool:
    normalized = str(path).replace("\\", "/")
    for item in allowed_files:
        allowed = item.replace("\\", "/").rstrip("/")
        if normalized == allowed or normalized.startswith(allowed + "/"):
            return True
    return False


def iter_runtime_files(scopes: List[str], allowed_files: List[str]) -> Iterable[Path]:
    for scope in scopes:
        root = Path(scope)
        if not root.exists():
            continue
        candidates = [root] if root.is_file() else root.rglob("*")
        for path in candidates:
            if not path.is_file():
                continue
            if is_allowed_file(path, allowed_files):
                continue
            if any(part in str(path) for part in ("__pycache__", ".git", "node_modules", "target")):
                continue
            if path.suffix.lower() in {".py", ".js", ".ts", ".rs"}:
                yield path


def string_constants(node: ast.AST) -> List[str]:
    values = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Constant) and isinstance(sub.value, str):
            values.append(sub.value)
    return values


def names_in(node: ast.AST) -> set[str]:
    names: set[str] = set()
    for sub in ast.walk(node):
        if isinstance(sub, ast.Name):
            names.add(sub.id)
        elif isinstance(sub, ast.Attribute):
            names.add(sub.attr)
    return names


def is_allowed_literal(value: str, cfg: Dict[str, Any]) -> bool:
    if value in set(cfg.get("allowed_literal_exact") or []):
        return True
    for prefix in cfg.get("allowed_literal_prefixes") or []:
        if value.startswith(prefix):
            return True
    if value.isidentifier() and len(value) <= 32:
        return True
    parts = value.split(".")
    if len(parts) == 2 and all(part.replace("_", "").isalnum() for part in parts):
        return True
    return False


class PythonHardcodeVisitor(ast.NodeVisitor):
    def __init__(self, path: Path, cfg: Dict[str, Any]):
        self.path = path
        self.cfg = cfg
        self.query_names = set(cfg.get("query_variable_names") or [])
        self.routing_name_fragments = tuple(cfg.get("routing_assignment_name_fragments") or [])
        self.violations: List[Dict[str, Any]] = []

    def add(self, node: ast.AST, rule: str, value: str) -> None:
        if is_allowed_literal(value, self.cfg):
            return
        self.violations.append(
            {
                "file": str(self.path),
                "line": getattr(node, "lineno", 0),
                "rule": rule,
                "literal": value[:240],
            }
        )

    def visit_If(self, node: ast.If) -> None:
        if names_in(node.test) & self.query_names:
            for value in string_constants(node.test):
                self.add(node, "string_literal_in_user_query_condition", value)
        self.generic_visit(node)

    def visit_IfExp(self, node: ast.IfExp) -> None:
        if names_in(node.test) & self.query_names:
            for value in string_constants(node.test):
                self.add(node, "string_literal_in_user_query_conditional_expression", value)
        self.generic_visit(node)

    def visit_Compare(self, node: ast.Compare) -> None:
        if names_in(node) & self.query_names:
            for op in node.ops:
                if isinstance(op, (ast.In, ast.NotIn, ast.Eq, ast.NotEq)):
                    for value in string_constants(node):
                        self.add(node, "user_query_literal_compare_or_membership", value)
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign) -> None:
        target_names = {
            target.id
            for target in node.targets
            if isinstance(target, ast.Name)
        }
        lower_names = " ".join(target_names).lower()
        if any(fragment in lower_names for fragment in self.routing_name_fragments):
            for value in string_constants(node.value):
                self.add(node, "runtime_routing_literal_assignment", value)
        self.generic_visit(node)


def scan_blocked_literals(path: Path, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    violations = []
    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#") or stripped.startswith("//"):
            continue
        for literal in cfg.get("blocked_literals") or []:
            if literal in stripped:
                violations.append(
                    {
                        "file": str(path),
                        "line": index,
                        "rule": "blocked_runtime_literal",
                        "literal": literal,
                        "text": stripped[:240],
                    }
                )
    return violations


def scan_python(path: Path, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    source = path.read_text(encoding="utf-8", errors="ignore")
    try:
        tree = ast.parse(source)
    except Exception as exc:
        return [{"file": str(path), "line": 0, "rule": "python_parse_error", "literal": str(exc)}]
    visitor = PythonHardcodeVisitor(path, cfg)
    visitor.visit(tree)
    return scan_blocked_literals(path, cfg) + visitor.violations


def scan_text_runtime(path: Path, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    violations = scan_blocked_literals(path, cfg)
    query_tokens = (".includes(", "text.includes", "query.includes", "userText.includes", "message.includes")
    for index, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("//") or stripped.startswith("/*") or stripped.startswith("*"):
            continue
        for token in query_tokens:
            if token in stripped:
                violations.append(
                    {
                        "file": str(path),
                        "line": index,
                        "rule": "text_runtime_possible_query_routing",
                        "literal": stripped[:240],
                    }
                )
    return violations


def main() -> int:
    cfg = load_config()
    violations: List[Dict[str, Any]] = []
    for path in iter_runtime_files(cfg.get("runtime_scopes") or [], cfg.get("allowed_files") or []):
        if path.suffix == ".py":
            violations.extend(scan_python(path, cfg))
        else:
            violations.extend(scan_text_runtime(path, cfg))
    if violations:
        print("RUNTIME STRUCTURAL HARDCODE GUARD FAILED")
        print(json.dumps(violations, ensure_ascii=False, indent=2))
        return 1
    print("OK: structural runtime hardcode guard passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
