from utils.logger import get_logger
from utils.config import config_instance

def main():
    root_logger=get_logger(name=None,f_name='main',fh=True,)
    root_logger.critical('start quantgalaxy')
    config_instance.show_config()

if __name__=='__main__':
    main()
