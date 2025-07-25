import logging
import logging.config
import json
from typing import Any, Dict


def ini_config():
    print("Declarative configuration using INI files")
    print("---------\n")

    config_path = "05_declarative-config.ini"

    # Reference the file config
    logging.config.fileConfig(
        fname=config_path,
    )

    # Create logger
    app_logger = logging.getLogger("app")
    app_logger.debug("INI-style fileConfig is working!")


def dict_config():
    print("Declarative configuration using dictionary config")
    print("---------\n")

    dict_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {"simple": {"format": "%(levelname)-8s - %(message)s"}},
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "simple",
                "stream": "ext://sys.stdout",
            }
        },
        "loggers": {
            "config.dict": {
                "level": "DEBUG",
                "handlers": ["console"],
            }
        },
    }

    # Reference the dict config
    logging.config.dictConfig(dict_config)

    config_logger = logging.getLogger("config.dict")
    config_logger.debug("dictConfig setup successfully")
    config_logger.info("Info goes to console")


def json_config():
    print("Declarative configuration using JSON config")
    print("---------\n")

    config_path = "05_declarative-config.json"

    with open(config_path, "r") as config_file:
        json_config = json.load(config_file)

    # Reference the dict config
    logging.config.dictConfig(json_config)

    config_logger = logging.getLogger("config.json")
    config_logger.debug("JSON config setup successfully")
    config_logger.info("Info goes to console")


# This value typically comes from environment such as environment variable.
# Here, it is hard-coded for understanding purpose
def is_debug():
    return True


def dynamic_config():
    print("Dynamically building config")
    print("---------\n")

    # Base config
    base_config: Dict[str, Any] = {
        "version": 1,
        "disable_existing_loggers": True,
        "handlers": {},
        "formatters": {},
        "loggers": {},
    }

    # Set formatter
    base_config["formatters"]["simple"] = {"format": "%(levelname)-8s - %(message)s"}

    # Set handler
    base_config["handlers"]["console"] = {
        "class": "logging.StreamHandler",
        "level": "DEBUG",
        "formatter": "simple",
        "stream": "ext://sys.stdout",
    }

    # Set logger
    base_config["loggers"]["config.dynamic"] = {
        "level": "WARNING",
        "handlers": ["console"],
    }

    if is_debug():
        for logger, _config in base_config["loggers"].items():
            base_config["loggers"][logger]["level"] = "DEBUG"  # Set log LEVEL to debug

    # Reference the dict config
    logging.config.dictConfig(base_config)

    config_logger = logging.getLogger("config.dynamic")
    config_logger.debug("Dynamic config setup successfully")
    config_logger.info("Info goes to console")


if __name__ == "__main__":
    # ini_config()
    # dict_config()
    # json_config()
    dynamic_config()
