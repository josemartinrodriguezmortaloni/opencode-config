---
name: securing-code
description: Reviews and secures code against vulnerabilities. Provides security checklists, validates input handling, and identifies common attack vectors. Use when auditing code, checking for security issues, before deployment, or when user mentions security concerns. Triggers on "review", "security", "vulnerabilities", "audit", "validate", "before deploy", "is this secure".
allowed-tools: Read, Grep, Bash(python:*)
---

# Securing Code

## Security Review Workflow

```
1. RUN SECURITY SCAN → Execute automated checks
2. MANUAL REVIEW → Check against vulnerability list
3. VALIDATE INPUTS → Trace all external data
4. CHECK ERROR HANDLING → Verify no data leakage
5. DOCUMENT FINDINGS → Report with severity
```

## Step 1: Automated Scan

Run security scanner on target files:

```bash
python scripts/security_scan.py <file_or_directory>
```

Scanner checks: SQL injection, hardcoded secrets, unsafe deserialization, command injection, path traversal.

## Step 2: Manual Review Checklist

### Input Validation
- [ ] ALL external input validated (user, API, file, env)
- [ ] Whitelist validation preferred over blacklist
- [ ] Type checking enforced
- [ ] Size limits on all inputs

### Authentication & Authorization
- [ ] No client-side only validation
- [ ] Permissions checked on every request
- [ ] Internal IDs not exposed directly
- [ ] Session handling secure

### Data Protection
- [ ] No sensitive data in logs (passwords, tokens, PII)
- [ ] Parameterized queries (no string concatenation)
- [ ] Encryption for sensitive data at rest
- [ ] HTTPS enforced for data in transit

### Error Handling
- [ ] No stack traces to users
- [ ] Domain exceptions used (not generic)
- [ ] Errors logged with context (not sensitive data)
- [ ] Fail securely (deny by default)

### Secrets
- [ ] No hardcoded secrets
- [ ] Environment variables or secret manager used
- [ ] .env files not committed (check .gitignore)

## Common Vulnerabilities

For detailed vulnerability patterns → See [reference/vulnerabilities.md](reference/vulnerabilities.md)

### Quick Reference

| Vulnerability | Pattern to Find | Fix |
|--------------|-----------------|-----|
| SQL Injection | `f"SELECT...{var}"` | Parameterized queries |
| Command Injection | `os.system(user_input)` | `subprocess` with list args |
| Path Traversal | `open(user_path)` | Validate against base path |
| Hardcoded Secret | `api_key = "sk-..."` | Environment variable |
| Unsafe Pickle | `pickle.loads(data)` | Use JSON or validate source |
| SSRF | `requests.get(user_url)` | Whitelist allowed domains |

## Risk Assessment

| Severity | Criteria | Action |
|----------|----------|--------|
| **Critical** | RCE, auth bypass, data breach | Block release, fix immediately |
| **High** | Privilege escalation, injection | Fix before release |
| **Medium** | Information disclosure | Fix in next sprint |
| **Low** | Best practice violation | Track in backlog |

## Output Format

```markdown
## Security Review: [Component]

### Summary
- Critical: X | High: X | Medium: X | Low: X

### Findings

#### [CRITICAL] SQL Injection in user_repository.py:45
**Description**: User input concatenated into SQL query
**Risk**: Full database compromise
**Fix**: Use parameterized query

### Recommendations
1. [Priority fixes]
2. [Follow-up items]
```

## Related Skills
- Use `designing-systems` for secure architecture from start
- Use `generating-python-code` for secure implementation patterns
