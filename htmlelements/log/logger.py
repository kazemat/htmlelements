import logging
import sys

logger = logging.getLogger('htmlelements')


def _add_default_handler(logger):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter('%(message)s'))
    logger.addHandler(handler)


def class_logger(cls):
    global logger
    if not getattr(cls, 'logger', None):
        cls.logger = logger
        logger.setLevel(logging.INFO)
        _add_default_handler(cls.logger)
    return cls.logger