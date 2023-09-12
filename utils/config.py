from .logger import get_logger
import logging
config_logger=logging.getLogger(__name__)

def config_test():
    #print(__name__)
    config_logger.critical(__name__)