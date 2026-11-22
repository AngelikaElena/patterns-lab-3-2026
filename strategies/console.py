from .base import OutputStrategy

class ConsoleStrategy(OutputStrategy):
    def write(self, formatted_message: str) -> None:
        print(formatted_message)