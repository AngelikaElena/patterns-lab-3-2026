from legacy import LogLevel
from logger import Logger
from factories import ConsoleLoggerCreator, FileLoggerCreator, UpperFileLoggerCreator

def main() -> None:
    # 1. Работаем с консолью (создаем фабрику, затем через нее - логгер)
    console_factory = ConsoleLoggerCreator()
    console_logger = Logger(console_factory.create_strategy())
    console_logger.log(LogLevel.INFO, "Application started")

    # 2. Работаем с файлом
    file_factory = FileLoggerCreator("logs/app.log")
    file_logger = Logger(file_factory.create_strategy())
    file_logger.log(LogLevel.WARN, "Low disk space")

    # 3. Работаем с файлом в верхнем регистре
    upper_factory = UpperFileLoggerCreator("logs/app.log")
    upper_logger = Logger(upper_factory.create_strategy())
    upper_logger.log(LogLevel.ERROR, "Example error")

if __name__ == "__main__":
    main()