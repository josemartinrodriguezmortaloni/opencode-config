---
name: designing-systems
description: Designs software architecture using GoF patterns, GRASP principles, and SOLID. Produces class diagrams, sequence diagrams, and design decisions. Use when user asks to design modules, choose patterns, structure systems, or needs architectural guidance before implementation. Triggers on "design", "architecture", "which pattern", "class diagram", "how should I structure", "before coding".
---

# Designing Systems

## Workflow

```
1. ASSESS COMPLEXITY → Determine required artifacts
2. ANSWER DESIGN QUESTIONS → 5 mandatory questions
3. SELECT PATTERNS → Use decision tree
4. DRAW DIAGRAMS → Class + Sequence (if needed)
5. DOCUMENT DECISIONS → Explain why each choice
```

## Step 1: Complexity Assessment

| Complexity | Indicators | Required Output |
|------------|-----------|-----------------|
| **Trivial** | Single function, no state | Code only |
| **Low** | Single class, simple state | Class diagram + Code |
| **Medium** | Multi-class, integrations | Class + Sequence + Design notes |
| **High** | New module, architectural | Full design doc + Risk analysis |
| **Critical** | Core system, security | All above + Scalability assessment |

## Step 2: Mandatory Design Questions

Before ANY diagram, answer explicitly:

```
1. RESPONSIBILITY: Which class owns this behavior? (Information Expert)
2. CREATION: Who creates these objects? (Creator/Factory)
3. COUPLING: What dependencies exist? How to minimize? (DIP)
4. EXTENSION: What will change? How to isolate it? (OCP)
5. SECURITY: What can go wrong? Attack surface?
```

## Step 3: Pattern Selection

For detailed decision tree → See [reference/pattern-decision-tree.md](reference/pattern-decision-tree.md)

### Quick Reference

| Situation | Pattern |
|-----------|---------|
| Object creation varies by context | Factory Method |
| Multiple algorithms, same interface | Strategy |
| Behavior changes by state | State |
| Add behavior without modifying | Decorator |
| Complex object construction | Builder |
| Incompatible interfaces | Adapter |
| Simplify complex subsystem | Facade |
| Notify on changes | Observer |
| `if/switch` on type | **STOP → Polymorphism** |

## Step 4: Diagrams

For Mermaid templates → See [reference/diagram-templates.md](reference/diagram-templates.md)

### Class Diagram Checklist
- [ ] No cycles (A→B→A)
- [ ] No God Class (>7 public methods)
- [ ] Interfaces explicit (DIP visible)
- [ ] Value Objects for primitives (Money, Email)

### Sequence Diagram Checklist
- [ ] Error paths shown
- [ ] Idempotency handled
- [ ] Not too chatty (<5 hops for single operation)

## Step 5: Output Format

```markdown
## Design Decision
Using **[Pattern]** because [justification].

## Class Diagram
[Mermaid diagram]

## Sequence Diagram (if Medium+)
[Mermaid diagram]

## Risk Notes (if High+)
[Identified risks and mitigations]
```

## Related Skills
- After design approved → Use `generating-python-code` for implementation
- Before delivery → Use `securing-code` for validation
