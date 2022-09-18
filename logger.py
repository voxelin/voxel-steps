import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='debug.log', filemode='a', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('Start of program')
logging.info('Doing something')
logging.warning('Dying now')
logging.error('Error')
logging.critical('Critical error')