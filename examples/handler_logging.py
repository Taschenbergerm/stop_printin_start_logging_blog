import logging 

file_sink = logging.FileHandler("filehandler.log")
file_sink.setLevel(logging.DEBUG)

std_sink = logging.StreamHandler()
std_sink.setLevel(logging.WARNING)

logger = logging.getLogger("SinkLogger")
logger.addHandler(std_sink)
logger.addHandler(file_sink)


logging.debug('This message will neither be visble nor in the file ')
logging.info('This messgae written to the file ')
logging.warning('This message will be printed and written')
logging.error('this as well')