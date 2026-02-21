# Mermaid Diagram Templates

## Class Diagram - Service with Repository

```mermaid
classDiagram
    class IRepository~T~ {
        <<interface>>
        +get(id: str) T
        +save(entity: T) void
    }
    
    class Service {
        -repository: IRepository
        +execute(data: Input) Output
    }
    
    class ConcreteRepository {
        +get(id: str) T
        +save(entity: T) void
    }
    
    Service --> IRepository : uses
    ConcreteRepository ..|> IRepository : implements
```

## Sequence Diagram - Request with Error Handling

```mermaid
sequenceDiagram
    participant C as Client
    participant S as Service
    participant R as Repository
    participant DB as Database
    
    C->>S: request(data)
    S->>S: validate(data)
    alt validation fails
        S-->>C: ValidationError
    else validation passes
        S->>R: save(entity)
        R->>DB: INSERT
        alt db error
            DB-->>R: DatabaseError
            R-->>S: RepositoryError
            S-->>C: ServiceError
        else success
            DB-->>R: OK
            R-->>S: entity
            S-->>C: Success(entity)
        end
    end
```

## Class Diagram - Strategy Pattern

```mermaid
classDiagram
    class Context {
        -strategy: IStrategy
        +set_strategy(s: IStrategy)
        +execute()
    }
    
    class IStrategy {
        <<interface>>
        +algorithm()
    }
    
    class ConcreteStrategyA {
        +algorithm()
    }
    
    class ConcreteStrategyB {
        +algorithm()
    }
    
    Context --> IStrategy
    ConcreteStrategyA ..|> IStrategy
    ConcreteStrategyB ..|> IStrategy
```

## Class Diagram - Factory Method

```mermaid
classDiagram
    class Creator {
        <<abstract>>
        +factory_method()* Product
        +operation()
    }
    
    class ConcreteCreatorA {
        +factory_method() Product
    }
    
    class ConcreteCreatorB {
        +factory_method() Product
    }
    
    class Product {
        <<interface>>
    }
    
    class ConcreteProductA
    class ConcreteProductB
    
    Creator <|-- ConcreteCreatorA
    Creator <|-- ConcreteCreatorB
    Product <|.. ConcreteProductA
    Product <|.. ConcreteProductB
    ConcreteCreatorA ..> ConcreteProductA : creates
    ConcreteCreatorB ..> ConcreteProductB : creates
```

## Class Diagram - Observer Pattern

```mermaid
classDiagram
    class IObserver {
        <<interface>>
        +update(event: Event)
    }
    
    class Subject {
        -observers: list~IObserver~
        +attach(observer: IObserver)
        +detach(observer: IObserver)
        +notify(event: Event)
    }
    
    class ConcreteObserverA {
        +update(event: Event)
    }
    
    class ConcreteObserverB {
        +update(event: Event)
    }
    
    Subject --> IObserver : notifies
    ConcreteObserverA ..|> IObserver
    ConcreteObserverB ..|> IObserver
```
