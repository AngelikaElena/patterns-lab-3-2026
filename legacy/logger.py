from __future__ import annotations

from datetime import datetime
from enum import Enum
from pathlib import Path


class LogLevel(str, Enum):
    TRACE = "TRACE"
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    FATAL = "FATAL"


class LegacyLogger:
    """
    Намеренно упрощённая реализация.

    Класс одновременно:
    - форматирует сообщения;
    - выбирает способ вывода;
    - выполняет вывод;
    - знает детали файловой системы.

    В лабораторной работе этот код необходимо переработать.
    """

    def __init__(self, log_file: str | Path = "application.log") -> None:
        self.log_file = Path(log_file)

    def _format(self, level: LogLevel, message: str) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"{timestamp} [{level.value}] {message}"

    def log(self, level: LogLevel, message: str, output: str = "console") -> str:
        formatted = self._format(level, message)

        if output == "console":
            print(formatted)
        elif output == "file":
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            with self.log_file.open("a", encoding="utf-8") as stream:
                stream.write(formatted + "\n")
        elif output == "upper_file":
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            with self.log_file.open("a", encoding="utf-8") as stream:
                stream.write(formatted.upper() + "\n")
        else:
            raise ValueError(f"Unknown output: {output}")

        return formatted
