from pathlib import Path
from strategies import OutputStrategy, ConsoleStrategy, FileStrategy, UpperFileStrategy
from .base import LoggerCreator

class ConsoleLoggerCreator(LoggerCreator):
    """Создает стратегию для консоли."""
    def create_strategy(self) -> OutputStrategy:
        return ConsoleStrategy()

class FileLoggerCreator(LoggerCreator):
    """Создает стратегию для файла."""
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = file_path

    def create_strategy(self) -> OutputStrategy:
        return FileStrategy(self.file_path)

class UpperFileLoggerCreator(LoggerCreator):
    """Создает стратегию для файла с верхним регистром."""
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = file_path

    def create_strategy(self) -> OutputStrategy:
        return UpperFileStrategy(self.file_path)