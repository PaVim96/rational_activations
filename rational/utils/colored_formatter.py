import logging



#https://alexandra-zaharia.github.io/posts/make-your-own-custom-color-formatter-with-python-logging/
class ColoredFormatter(logging.Formatter):
    reset = '\x1b[0m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    white = '\x1b[38;5;231m'

    def __init__(self, format):
        logging.Formatter.__init__(self, format)
        self.fmt = format

        self.FORMATS = {
            logging.DEBUG: self.blue + self.fmt + self.reset, 
            logging.INFO: self.white + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset, 
            logging.ERROR: self.red + self.fmt + self.reset, 
            logging.WARNING: self.yellow + self.fmt + self.reset
        }



    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)