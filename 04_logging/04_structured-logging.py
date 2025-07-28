import logging
import sys
from pythonjsonlogger.json import JsonFormatter


def structured_logging():
    print("Configuring python-json-logger")
    print("---------\n")

    # Create logger
    json_logger = logging.getLogger("demo.json")
    json_logger.setLevel(logging.INFO)

    # Create handler
    handler = logging.StreamHandler(sys.stdout)

    # Create json formatter
    json_formatter = JsonFormatter(
        "{asctime}{levelname}{message}",
        style="{",
        json_indent=4,
        rename_fields={"asctime": "timestamp", "levelname": "level"},
    )

    # Attach formatter to the handler
    handler.setFormatter(json_formatter)

    # Attach handler to the logger
    json_logger.addHandler(handler)

    # Log message
    json_logger.info("Structured logging initialized")

    # Logging with extra context
    print("Logging with extra context")
    print("---------\n")

    extra_context = {
        "user_id": "devops1",
        "request_id": "request-12345abc",
        "source_ip": "10.0.0.5",
    }

    json_logger.warning(
        "Request took longer than 5s to complete",
        extra=extra_context,
    )

    # Logging exceptions as JSON
    print("Logging exceptions as JSON")
    print("---------\n")

    try:
        result = 1 / 0
    except ZeroDivisionError:
        json_logger.exception(
            "Unexpected calculation error",
            extra={"operation": "division"},
        )


def log_info():
    # Create logger
    logger = logging.getLogger("demo.worker_pool")
    logger.setLevel(logging.INFO)

    # Create handler, attach JSON formatter to it and attach it to the logger
    handler = logging.StreamHandler(sys.stdout)
    formatter = JsonFormatter("%(levelname)s %(name)s %(message)s", json_indent=4)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Context data
    context_data = {"task_id": "t-456", "worker_id": "w-03"}

    # Log message
    logger.info("Task completed successfully", extra=context_data)


if __name__ == "__main__":
    # structured_logging()
    log_info()
