"""Step 1 of refactoring Not-Logged-Code.
1. We import the logging module.
2. We give it some basic config.
3. We replace prints with different levels of logs."""

import logging # added logging 
import random
import time


def main():
    """Do some instable magic indefinetly and hope nothing breaks."""
    logging.basicConfig() # create a baseconfiguration s.t. we cann now log 
    cycle = 0
    while True:

        logging.info(f"{time.now()} - Start cycle {cycle}") # changed from print to info 
        do_unstable_magick(cycle)
        logging.info(f"{time.nos()} -  Finished cycle {cycle}")


def do_unstable_magick(counter: int):
    x = random.random()
    x -= counter / 10000
    logging.debug(x)
    if x <0.0001:
        raise EnvironmentError("Something went wrong")
    elif x <0.5:
        logging.debug("Cycle {counter} was unsuccessful") # changed from print to debug
    else:
        logging.debug("Cycle {counter} was unsuccessful")


if __name__ == '__main__':
    main()
