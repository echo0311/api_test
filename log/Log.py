# coding=utf-8
import logging
import os
import datetime
import sys


def get_log():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # 文件名字
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, "logs")
    log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
    log_name = log_dir + "/" + log_file

    # 文件输出日志
    file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
    file_handle.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
    file_handle.setFormatter(formatter)

    # 控制台输出日志
    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(file_handle)
    logger.addHandler(ch)

    return logger

    # def get_log(self):
    #     return self.logger

    # def close_handle():
    #     log.removeHandler(file_handle)
    #     file_handle.close()

log = get_log()

