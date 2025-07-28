import logging
import logging.handlers
import os
import time


def cleanup_log_files(base_name: str):
    for file_name in os.listdir("./logs"):
        if file_name.startswith(base_name):
            os.remove(file_name)


def basic_handler():
    """Basic logging with FileHandler"""

    print("Basic logging with FileHandler")
    print("-------\n")

    # Create logger
    basic_logger = logging.getLogger("file.basic")
    basic_logger.setLevel(logging.DEBUG)

    # Create handler and attach it to logger
    basic_fh = logging.FileHandler("logs/basicfile.log", delay=True, encoding="utf-8")
    basic_fh.setLevel(logging.INFO)
    basic_logger.addHandler(basic_fh)

    # Log message
    basic_logger.info("INFO: will be written to file")


def rotation_filehandler():
    """Size-based log rotation with RotatingFileHandler"""

    print("Size-based log rotation with RotatingFileHandler")
    print("-------\n")

    rotating_logs_filename = "logs/rotatingfile.log"

    # Start with fresh files when we run this script
    cleanup_log_files(rotating_logs_filename)

    # Create logger
    rotating_logger = logging.getLogger("file.rotating")
    rotating_logger.setLevel(logging.DEBUG)

    # Create handler, attach formatter to it and attach it to the logger
    rotating_fh = logging.handlers.RotatingFileHandler(
        rotating_logs_filename,
        maxBytes=500,
        backupCount=2,
        encoding="utf-8",
    )
    rotating_fh.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
    rotating_logger.addHandler(rotating_fh)

    # Log messages
    for i in range(30):
        rotating_logger.info(f"Entry {i}: {'Z' * 50}")
        time.sleep(0.05)


def timerotatinghandler():
    """Time-based log rotation with TimedRotatingFileHandler"""

    print("Time-based log rotation with TimedRotatingFileHandler")
    print("-------\n")

    timed_rotating_logs_filename = "logs/timedrotatingfile.log"

    # Start with fresh files when we run this script
    cleanup_log_files(timed_rotating_logs_filename)

    # Create logger
    timed_rotating_logger = logging.getLogger("file.timed")
    timed_rotating_logger.setLevel(logging.DEBUG)

    # Create handler, attach formatter to it and attach it to the logger
    timed_rotating_fh = logging.handlers.TimedRotatingFileHandler(
        timed_rotating_logs_filename,
        when="S",  # second
        interval=3,  # every 3sec
        backupCount=2,
        encoding="utf-8",
    )
    timed_rotating_fh.setFormatter(logging.Formatter("%(levelname)-8s %(message)s"))
    timed_rotating_logger.addHandler(timed_rotating_fh)

    # Log messages
    for i in range(30):
        timed_rotating_logger.info(f"Entry {i}: {'Z' * 50}")
        time.sleep(0.5)


if __name__ == "__main__":
    basic_handler()
    # rotation_filehandler()
    # timerotatinghandler()
