import sys
import logging
import datetime

from functools import wraps


logger = logging.getLogger()
logger.addHandler(logging.FileHandler('/tmp/sensys_error.log'))


def error():
    logger.exception('SenSys Exception at {}'.format(datetime.datetime.now()))
    sys.exit(1)


def plugin_error(func):
    # noinspection PyBroadException
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except BaseException:
            error()
    return wrapper
