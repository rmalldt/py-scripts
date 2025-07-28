import logging
import sys


def log_levels():
    print("Log levels in practice")
    print("------\n")

    for lvl in (
        logging.DEBUG,
        logging.INFO,
        logging.WARNING,
        logging.ERROR,
        logging.CRITICAL,
    ):
        print(f"{logging.getLevelName(lvl):<8} = {lvl}")


def two_stage_filtering():
    print("Two stage filtering")
    print("------\n")

    filter_logger = logging.getLogger("demo.filter")
    filter_logger.setLevel(logging.INFO)  # level below INFO are discarded (i.e. DEBUG)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.ERROR)  # level below ERROR are discarded
    filter_logger.addHandler(stream_handler)  # attach handler to logger

    filter_logger.info("INFO: will not be shown")
    filter_logger.error("ERROR: will be shown")
    filter_logger.critical("CRITICAL: will be shown")


def configure_multiple_handlers():
    print("Configuring logs and handlers")
    print("------\n")

    # Create logger
    data_logger = logging.getLogger("demo.data")
    data_logger.setLevel(logging.DEBUG)  # all levels

    # Handler 1: StreamHandler
    data_sh = logging.StreamHandler(sys.stdout)
    data_sh.setLevel(logging.ERROR)  # from ERROR and above only

    # Handler 2: FileHandler
    data_fh = logging.FileHandler("logs/process.log", "w")
    data_fh.setLevel(logging.INFO)  # from INFO and above only

    # Attach handlers to logger
    data_logger.addHandler(data_sh)
    data_logger.addHandler(data_fh)

    data_logger.debug("DEBUG: will be dropped")
    data_logger.info("INFO: file only")
    data_logger.warning("WARNING: file only")
    data_logger.error("ERROR: file and console")
    data_logger.critical("CRITICAL: file and console")


if __name__ == "__main__":
    log_levels()
    two_stage_filtering()
    configure_multiple_handlers()
