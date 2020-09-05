"""Step 4 of refactoring Not-Logged-Code.
0. We realized that this is to much boilerplate code that noone wants to read. .
1. Import the loguru model ( after pip-installing it).
2. We finish this by adding a retention and rotation """

import random
import time

from loguru import logger
from loguru._logger import Logger

def main():
    """Do some instable magic indefinetly and hope nothing breaks."""
    logger.add("debug.log", level="DEBUG", retention="2 weeks", rotation="1 day")
    logger.add("info.log", level="INFO", retention="2 month", rotation="1 week")
    cycle = 0
    while True:

        logger.info(f"{time.now()} - Start cycle {cycle}") # changed from print to info 
        do_unstable_magick(cycle, logger)
        logger.info(f"{time.nos()} -  Finished cycle {cycle}")


def do_unstable_magick(counter: int, logger: Logger):
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
