from legacy import LogLevel
from logger import Logger
from strategies import ConsoleStrategy, FileStrategy, UpperFileStrategy

def main() -> None:
    # 1. Работаем с консолью
    console_logger = Logger(ConsoleStrategy())
    console_logger.log(LogLevel.INFO, "Application started")

    # 2. Работаем с файлом
    file_logger = Logger(FileStrategy("logs/app.log"))
    file_logger.log(LogLevel.WARN, "Low disk space")

    # 3. Работаем с файлом в верхнем регистре
    upper_logger = Logger(UpperFileStrategy("logs/app.log"))
    upper_logger.log(LogLevel.ERROR, "Example error")

if __name__ == "__main__":
    main()