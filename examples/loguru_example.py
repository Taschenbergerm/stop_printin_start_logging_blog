import sys
from loguru import logger

logger.debug("This will be printed as the default logger will use std.out:DEBUG as sink")


logger.remove()
logger.debug("all sinks are now gone - no print no write")


logger.add(sys.stdout, level="INFO")
logger.add("loguru_example", level="DEBUG")


logger.debug('This message will neither be visble nor in the file ')
logger.info('This messgae written to the file ')
logger.warning('This message will be printed and written')
logger.error('this as well')
