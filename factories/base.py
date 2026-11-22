from abc import ABC, abstractmethod
from strategies import OutputStrategy

class LoggerCreator(ABC):
    """Абстрактная фабрика (Создатель)."""
    
    @abstractmethod
    def create_strategy(self) -> OutputStrategy:
        """Фабричный метод, который должны реализовать наследники."""
        pass