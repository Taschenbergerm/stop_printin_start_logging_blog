import logging

logging.basicConfig(filename='simple_logging.log',level=logging.INFO)
logging.debug('This message will neither be visble nor in the file ')
logging.info('This messgae will printed and written to the file ')
logging.warning('And this, too')
logging.error('this as well')