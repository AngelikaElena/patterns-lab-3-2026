from legacy import LegacyLogger, LogLevel


def main() -> None:
    logger = LegacyLogger("logs/app.log")
    logger.log(LogLevel.INFO, "Application started", output="console")
    logger.log(LogLevel.WARN, "Low disk space", output="file")
    logger.log(LogLevel.ERROR, "Example error", output="upper_file")


if __name__ == "__main__":
    main()
