from utils.logger import get_logger
from utils.config import config_test
if __name__=='__main__':
    root_logger=get_logger(name=None,f_name='main',fh=True,)
    print(root_logger)
    root_logger.info('main test')
    config_test()
