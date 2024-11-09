import logging

logging.basicConfig(filename = 'basicConfig.log',level = logging.DEBUG,format='%(asctimes)s - %(levelnames)s')

logging.debug("this is debug msg")
logging.info("this is info msg")
logging.warning("this is warning msg")
logging.error("this is error msg")
logging.critical("this is critical msg")

#
# logger = logging.getLogger("Get logger")
# handler = logging.FileHandler("file handler")
# formatter = logging.formatter("Formatter")
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)
#
#
# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')