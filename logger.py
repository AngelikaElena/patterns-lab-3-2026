from datetime import datetime
from legacy.logger import LogLevel
from strategies import OutputStrategy

class Logger:
    """Контекст паттерна Strategy."""

    def __init__(self, strategy: OutputStrategy) -> None:
        # Логгер принимает стратегию через конструктор!
        self._strategy = strategy

    def _format(self, level: LogLevel, message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} [{level.value}] {message}"

    def log(self, level: LogLevel, message: str) -> str:
        formatted = self._format(level, message)
        
        # Никаких if/elif! Просто вызываем метод у стратегии.
        self._strategy.write(formatted)
        
        return formatted