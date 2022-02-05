import logging 
import os
from colored_formatter import ColoredFormatter


class RationalLogger(object):
    def __init__(self, logger_name, log_level = logging.DEBUG, show_logger_name = False, show_time = False):
        self._logger = logging.getLogger(logger_name)
        self._logger.setLevel(log_level)
        console = logging.StreamHandler()
        console.setLevel(log_level)

        messageFormat = self.setFormatter(show_logger_name, show_time)

        if os.name != 'nt':
            console.setFormatter(ColoredFormatter(messageFormat))
        if os.name == 'nt':
            console.setFormatter(messageFormat)

        self._logger.addHandler(console)


    def debug(self, msg):
        self._logger.debug(msg)

    def warn(self, msg):
        self._logger.warn(msg)

    def info(self, msg):
        self._logger.info(msg)

    def error(self, msg):
        self._logger.error(msg)

    def critical(self, msg):
        self._logger.critical(msg)

    def setFormatter(self, show_logger_name, show_time):
        format = ''

        if show_logger_name:
            format = '%(name)s'

        if show_time:
            if len(format) > 0:
                format = format + ' | '
            
            format = format + '%(asctime)s'

        if len(format) > 0:
            format = format + ' | '

        format = format + '%(filename)s | %(lineno)d | %(message)s'

        return format
        

        

    






