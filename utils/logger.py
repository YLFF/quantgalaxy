
from logging.handlers import RotatingFileHandler
import logging
import os
def get_logger(name=__name__,ch_level=logging.DEBUG,fh=True,fh_path=r'E:\wangzhilin\quantgalaxy\logs',f_name=__name__,fh_level=logging.INFO):

    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        fmt='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
        datefmt='%m-%d %H:%M')
    if  fh:
        #name=f_name
        general_fh = RotatingFileHandler(os.path.join(fh_path, f'{f_name}.log'), maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
        general_fh.setLevel(fh_level)
        general_fh.setFormatter(formatter)
        logger.addHandler(general_fh)
        
        # 添加一个错误专用的文件处理器
        error_fh = RotatingFileHandler(os.path.join(fh_path, f'{f_name}_error.log'), maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
        error_fh.setLevel(logging.ERROR)  # 设置为ERROR级别
        error_fh.setFormatter(formatter)
        logger.addHandler(error_fh)
        
    ch = logging.StreamHandler()
    ch.setLevel(ch_level)

    ch.setFormatter(formatter)


    logger.addHandler(ch)
    logger.propagate=True
    return logger
'''test the behavior where run from main.py'''
#loglogger=logging.getLogger(__name__)
#loglogger.setLevel(logging.DEBUG)
#loglogger.propagate=True
