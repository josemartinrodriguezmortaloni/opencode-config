#!/usr/bin/env python3
"""Basic security scanner for Python code.

Usage: python security_scan.py <file_or_directory>

Detects:
- SQL injection patterns
- Hardcoded secrets
- Unsafe deserialization
- Command injection
- Path traversal risks
"""
import ast
import re
import sys
from pathlib import Path
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


@dataclass
class Finding:
    severity: Severity
    category: str
    file: str
    line: int
    message: str
    code_snippet: str


SECRET_PATTERNS = [
    (r'(?i)(api[_-]?key|apikey)\s*=\s*["\'][^"\']{10,}["\']', "API key"),
    (r'(?i)(secret|password|passwd|pwd)\s*=\s*["\'][^"\']+["\']', "Secret/Password"),
    (r'(?i)(token)\s*=\s*["\'][^"\']{10,}["\']', "Token"),
    (r'sk-[a-zA-Z0-9]{20,}', "OpenAI API key"),
    (r'ghp_[a-zA-Z0-9]{36}', "GitHub token"),
]

SQL_INJECTION_PATTERNS = [
    r'f["\'].*SELECT.*\{',
    r'f["\'].*INSERT.*\{',
    r'f["\'].*UPDATE.*\{',
    r'f["\'].*DELETE.*\{',
    r'\.format\(.*\).*(?:SELECT|INSERT|UPDATE|DELETE)',
]


class SecurityVisitor(ast.NodeVisitor):
    def __init__(self, filepath: str, source_lines: list[str]):
        self.filepath = filepath
        self.source_lines = source_lines
        self.findings: list[Finding] = []

    def visit_Call(self, node: ast.Call) -> None:
        self._check_dangerous_calls(node)
        self._check_pickle(node)
        self._check_eval_exec(node)
        self.generic_visit(node)

    def _check_dangerous_calls(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ('system', 'popen'):
                self.findings.append(Finding(
                    severity=Severity.HIGH,
                    category="Command Injection",
                    file=self.filepath,
                    line=node.lineno,
                    message="Potential command injection via os.system/popen",
                    code_snippet=self.source_lines[node.lineno - 1].strip()
                ))

    def _check_pickle(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Attribute):
            if node.func.attr in ('loads', 'load') and hasattr(node.func.value, 'id'):
                if getattr(node.func.value, 'id', '') == 'pickle':
                    self.findings.append(Finding(
                        severity=Severity.CRITICAL,
                        category="Unsafe Deserialization",
                        file=self.filepath,
                        line=node.lineno,
                        message="pickle.loads() can execute arbitrary code",
                        code_snippet=self.source_lines[node.lineno - 1].strip()
                    ))

    def _check_eval_exec(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name):
            if node.func.id in ('eval', 'exec'):
                self.findings.append(Finding(
                    severity=Severity.CRITICAL,
                    category="Code Injection",
                    file=self.filepath,
                    line=node.lineno,
                    message=f"{node.func.id}() can execute arbitrary code",
                    code_snippet=self.source_lines[node.lineno - 1].strip()
                ))


def scan_file(filepath: Path) -> list[Finding]:
    findings: list[Finding] = []
    source = filepath.read_text()
    lines = source.splitlines()

    for i, line in enumerate(lines, 1):
        for pattern, secret_type in SECRET_PATTERNS:
            if re.search(pattern, line):
                findings.append(Finding(
                    severity=Severity.HIGH,
                    category="Hardcoded Secret",
                    file=str(filepath),
                    line=i,
                    message=f"Potential hardcoded {secret_type}",
                    code_snippet=line.strip()[:80]
                ))

        for pattern in SQL_INJECTION_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                findings.append(Finding(
                    severity=Severity.CRITICAL,
                    category="SQL Injection",
                    file=str(filepath),
                    line=i,
                    message="String formatting in SQL query",
                    code_snippet=line.strip()[:80]
                ))

    try:
        tree = ast.parse(source)
        visitor = SecurityVisitor(str(filepath), lines)
        visitor.visit(tree)
        findings.extend(visitor.findings)
    except SyntaxError:
        pass

    return findings


def scan_directory(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    for pyfile in path.rglob("*.py"):
        findings.extend(scan_file(pyfile))
    return findings


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python security_scan.py <file_or_directory>")
        return 1

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"ERROR: Path not found: {target}")
        return 1

    if target.is_file():
        findings = scan_file(target)
    else:
        findings = scan_directory(target)

    if not findings:
        print("✓ No security issues found")
        return 0

    by_severity = {s: [] for s in Severity}
    for f in findings:
        by_severity[f.severity].append(f)

    print(f"\nSECURITY SCAN RESULTS")
    print(f"{'='*50}")
    print(f"Critical: {len(by_severity[Severity.CRITICAL])} | "
          f"High: {len(by_severity[Severity.HIGH])} | "
          f"Medium: {len(by_severity[Severity.MEDIUM])} | "
          f"Low: {len(by_severity[Severity.LOW])}")
    print(f"{'='*50}\n")

    for severity in Severity:
        for f in by_severity[severity]:
            print(f"[{f.severity.value}] {f.category}")
            print(f"  File: {f.file}:{f.line}")
            print(f"  {f.message}")
            print(f"  Code: {f.code_snippet}")
            print()

    return 1 if by_severity[Severity.CRITICAL] else 0


if __name__ == "__main__":
    sys.exit(main())
