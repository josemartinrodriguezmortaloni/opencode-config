# Pattern Decision Tree

## Creation Patterns

```
Need to create objects?
├── Creation varies by context?
│   ├── Single product family → Factory Method
│   └── Multiple product families → Abstract Factory
├── Complex construction (many params)?
│   └── Builder
├── Expensive to create, need copies?
│   └── Prototype
└── Single global instance?
    └── Singleton (use sparingly)
```

## Behavioral Patterns

```
Need to vary behavior?
├── Algorithm varies at runtime?
│   └── Strategy
├── Behavior depends on object state?
│   └── State
├── Need to add responsibilities dynamically?
│   └── Decorator
├── Process requests through chain?
│   └── Chain of Responsibility
├── Encapsulate request as object (undo/queue)?
│   └── Command
└── Define algorithm skeleton, vary steps?
    └── Template Method
```

## Structural Patterns

```
Need to structure objects?
├── Incompatible interface?
│   └── Adapter
├── Simplify complex subsystem?
│   └── Facade
├── Control access to object?
│   └── Proxy
├── Tree structure with uniform treatment?
│   └── Composite
└── Too many similar objects (memory)?
    └── Flyweight
```

## Communication Patterns

```
Need objects to communicate?
├── Many-to-many dependencies?
│   └── Mediator
├── One-to-many notifications?
│   └── Observer
└── Decouple sender from receiver?
    └── Command
```

## GRASP Quick Guide

| Principle | Question | Action |
|-----------|----------|--------|
| Information Expert | Who has the data? | Put method where data lives |
| Creator | Who creates X? | Class that contains/uses/initializes X |
| Low Coupling | Too many dependencies? | Use interfaces, inject abstractions |
| High Cohesion | Class does too much? | Split responsibilities |
| Polymorphism | if/switch on type? | Replace with interface |
