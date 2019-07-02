import logging
import logging.config


class LoggerConsole():

    def testLog(self):

        # create logger
        logging.config.fileConfig('logging.conf')
        logger = logging.getLogger(LoggerConf.__name__)

        # logging messages
        logger.debug("debug msg")
        logger.info("info msg")
        logger.warning("warning msg")
        logger.error("error msg")
        logger.critical("critical msg")


ff = LoggerConsole()
ff.testLog()
