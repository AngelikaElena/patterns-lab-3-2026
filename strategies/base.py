from abc import ABC, abstractmethod

class OutputStrategy(ABC):
    @abstractmethod
    def write(self, formatted_message: str) -> None:
        """Метод, который реализуют все конкретные стратегии."""
        pass