import re
from pathlib import Path

import pytest

from legacy import LogLevel
from logger import Logger
from strategies import ConsoleStrategy, FileStrategy, UpperFileStrategy
from factories import ConsoleLoggerCreator, FileLoggerCreator, UpperFileLoggerCreator

# 1. ТЕСТЫ ДЛЯ СТРАТЕГИЙ

def test_console_strategy(capsys: pytest.CaptureFixture[str]) -> None:
    """Проверяет, что консольная стратегия печатает текст."""
    strategy = ConsoleStrategy()
    strategy.write("Test message")
    captured = capsys.readouterr()
    assert captured.out == "Test message\n"


def test_file_strategy(tmp_path: Path) -> None:
    """Проверяет, что файловая стратегия пишет в файл."""
    file_path = tmp_path / "test.log"
    strategy = FileStrategy(file_path)
    strategy.write("Test file message")
    assert file_path.read_text(encoding="utf-8") == "Test file message\n"


def test_upper_file_strategy(tmp_path: Path) -> None:
    """Проверяет, что стратегия с верхним регистром пишет капсом."""
    file_path = tmp_path / "test.log"
    strategy = UpperFileStrategy(file_path)
    strategy.write("test uppercase")
    assert file_path.read_text(encoding="utf-8") == "TEST UPPERCASE\n"


# 2. ТЕСТЫ ДЛЯ ФАБРИЧНОГО МЕТОДА

def test_console_creator() -> None:
    creator = ConsoleLoggerCreator()
    strategy = creator.create_strategy()
    assert isinstance(strategy, ConsoleStrategy)


def test_file_creator(tmp_path: Path) -> None:
    file_path = tmp_path / "test.log"
    creator = FileLoggerCreator(file_path)
    strategy = creator.create_strategy()
    assert isinstance(strategy, FileStrategy)
    assert strategy.file_path == file_path


def test_upper_file_creator(tmp_path: Path) -> None:
    file_path = tmp_path / "test.log"
    creator = UpperFileLoggerCreator(file_path)
    strategy = creator.create_strategy()
    assert isinstance(strategy, UpperFileStrategy)
    assert strategy.file_path == file_path


# 3. ТЕСТЫ ДЛЯ ЛОГГЕРА (ФОРМАТИРОВАНИЕ И ОШИБКИ)

def test_logger_formatting() -> None:
    """Проверяет формат: YYYY-MM-DD HH:mm:ss [LEVEL] Message."""
    logger = Logger(ConsoleStrategy())
    # Используем capsys, чтобы не засорять консоль
    formatted = logger.log(LogLevel.INFO, "Hello world")
    
    # Регулярное выражение для проверки формата
    pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \[INFO\] Hello world$"
    assert re.match(pattern, formatted) is not None


def test_logger_invalid_level() -> None:
    """Проверяет, что при некорректном уровне выбрасывается ValueError."""
    logger = Logger(ConsoleStrategy())
    
    with pytest.raises(ValueError, match="Недопустимый уровень лога"):
        logger.log("INVALID_LEVEL", "This should fail")


def test_logger_with_string_level() -> None:
    """Проверяет, что логгер принимает уровень в виде строки и преобразует его."""
    logger = Logger(ConsoleStrategy())
    # Передаем строку "ERROR" вместо enum LogLevel.ERROR
    formatted = logger.log("ERROR", "String level test")
    assert "[ERROR] String level test" in formatted