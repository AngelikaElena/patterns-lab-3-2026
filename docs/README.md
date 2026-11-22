# Диаграмма

Поместите сюда структурную диаграмму итогового решения.

Допустимые форматы:

- `architecture.puml`;
- `architecture.mmd`;
- изображение, экспортированное из diagrams.net;
- другой согласованный с преподавателем формат.

На диаграмме должны быть различимы участники шаблонов Strategy и Factory Method.

# Структурная диаграмма решения

Ниже представлена UML-диаграмма классов, демонстрирующая применение паттернов **Strategy** и **Factory Method**.

```mermaid
classDiagram
    direction TB

    %% Контекст (Logger)
    class Logger {
        -_strategy: OutputStrategy
        +log(level: LogLevel, message: str) str
        -_format(level: LogLevel, message: str) str
    }

    %% Интерфейс стратегии
    class OutputStrategy {
        <<interface>>
        +write(formatted_message: str)
    }

    %% Конкретные стратегии
    class ConsoleStrategy {
        +write(formatted_message: str)
    }
    class FileStrategy {
        -file_path: Path
        +write(formatted_message: str)
    }
    class UpperFileStrategy {
        -file_path: Path
        +write(formatted_message: str)
    }

    %% Базовый создатель (Фабрика)
    class LoggerCreator {
        <<interface>>
        +create_strategy() OutputStrategy
    }

    %% Конкретные создатели
    class ConsoleLoggerCreator {
        +create_strategy() OutputStrategy
    }
    class FileLoggerCreator {
        -file_path: Path
        +create_strategy() OutputStrategy
    }
    class UpperFileLoggerCreator {
        -file_path: Path
        +create_strategy() OutputStrategy
    }

    %% Связи Strategy
    Logger o--> OutputStrategy : uses (context)
    OutputStrategy <|.. ConsoleStrategy : implements
    OutputStrategy <|.. FileStrategy : implements
    OutputStrategy <|.. UpperFileStrategy : implements

    %% Связи Factory Method
    LoggerCreator <|-- ConsoleLoggerCreator : implements
    LoggerCreator <|-- FileLoggerCreator : implements
    LoggerCreator <|-- UpperFileLoggerCreator : implements

    %% Связи создания (Factory Method создает стратегии)
    ConsoleLoggerCreator ..> ConsoleStrategy : creates
    FileLoggerCreator ..> FileStrategy : creates
    UpperFileLoggerCreator ..> UpperFileStrategy : creates