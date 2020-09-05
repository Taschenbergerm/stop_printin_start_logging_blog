import time
from loguru import logger

logger.add("debug.log",rotation="10MB", retention=5, level="DEBUG")
logger.add("error.log",rotation="100MB", retention="100 days", level="ERROR")


while True: 
    logger.debug(""" This log will only show up in the debug log which has a shorter retention time
        As such we do not need to worry that this script will create too many log file and the hard drive might get to crowded 
        Even if we print this  way to often """)
    logger.info(""" Same goes for this - so we do not need to worry too much about the filesize - even with the loop 
     As we only keep five files with this much data we can log to our hearts content without worry """)
    logger.warning("Moreover we could also fill the compress argument which then  compresses all files rotations (or after close) in e.g. gzip or lzma ( or many more) ")
    logger.error("This message will pop up in the error log and as such be available for way longer - so we can see long passt error ")
    time.sleep(1)
