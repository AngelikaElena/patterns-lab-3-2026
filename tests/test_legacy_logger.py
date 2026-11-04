from pathlib import Path

import pytest

from legacy import LegacyLogger, LogLevel


def test_console_output(capsys: pytest.CaptureFixture[str]) -> None:
    logger = LegacyLogger()
    result = logger.log(LogLevel.INFO, "hello", output="console")

    captured = capsys.readouterr()
    assert "[INFO] hello" in result
    assert result in captured.out


def test_file_output(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    logger = LegacyLogger(path)

    logger.log(LogLevel.WARN, "careful", output="file")

    assert "[WARN] careful" in path.read_text(encoding="utf-8")


def test_upper_file_output(tmp_path: Path) -> None:
    path = tmp_path / "app.log"
    logger = LegacyLogger(path)

    logger.log(LogLevel.ERROR, "Something happened", output="upper_file")

    text = path.read_text(encoding="utf-8")
    assert "[ERROR] SOMETHING HAPPENED" in text


def test_unknown_output_is_rejected() -> None:
    logger = LegacyLogger()

    with pytest.raises(ValueError):
        logger.log(LogLevel.INFO, "hello", output="network")
