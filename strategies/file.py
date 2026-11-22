from pathlib import Path
from .base import OutputStrategy

class FileStrategy(OutputStrategy):
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def write(self, formatted_message: str) -> None:
        # Логика работы с файлом переехала сюда
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("a", encoding="utf-8") as stream:
            stream.write(formatted_message + "\n")


class UpperFileStrategy(OutputStrategy):
    def __init__(self, file_path: str | Path) -> None:
        self.file_path = Path(file_path)

    def write(self, formatted_message: str) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        with self.file_path.open("a", encoding="utf-8") as stream:
            stream.write(formatted_message.upper() + "\n")