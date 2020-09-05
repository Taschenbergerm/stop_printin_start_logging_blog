"""Step 2 of refactoring Not-Logged-Code.
1. We now add sinks to differentiate which information should be seen where.
2. we use the created logger explicitly and not the genereal module anymore."""

import logging # added logging 
import random
import time


def main():
    """Do some instable magic indefinetly and hope nothing breaks."""
    logger = configure_logger() # create a baseconfiguration s.t. we cann now log 
    cycle = 0
    while True:

        logger.info(f"{time.now()} - Start cycle {cycle}") # changed from print to info 
        do_unstable_magick(cycle, logger)
        logger.info(f"{time.nos()} -  Finished cycle {cycle}")

def configure_logger() -> logging.Logger:
    file_sink = logging.FileHandler("debug.log")
    file_sink.setLevel(logging.DEBUG)

    file_sink = logging.FileHandler("info.log")
    file_sink.setLevel(logging.INFO)

    std_sink = logging.StreamHandler()
    std_sink.setLevel(logging.WARNING)

    logger = logging.getLogger("SinkLogger")
    logger.addHandler(std_sink)
    logger.addHandler(file_sink)
    return logger

def do_unstable_magick(counter: int, logger: logging.Logger):
    x = random.random()
    x -= counter / 10000
    logger.debug(x)
    if x <0.0001:
        raise EnvironmentError("Something went wrong")
    elif x <0.5:
        logger.debug("Cycle {counter} was unsuccessful") # changed from print to debug
    else:
        logger.debug("Cycle {counter} was unsuccessful")


if __name__ == '__main__':
    main()
