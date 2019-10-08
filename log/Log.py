# coding=utf-8
import logging
import os
import datetime
import sys


class Log(object):

    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        # 文件名字
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(base_dir, "logs")
        log_file = datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
        log_name = log_dir + "/" + log_file

        # 文件输出日志
        self.file_handle = logging.FileHandler(log_name, 'a', encoding='utf-8')
        self.file_handle.setLevel(logging.DEBUG)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s--> %(funcName)s %(levelno)s: %(levelname)s ----->%(message)s')
        self.file_handle.setFormatter(formatter)

        # 控制台输出日志
        self.ch = logging.StreamHandler(stream=sys.stdout)
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)
        self.logger.addHandler(self.ch)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == '__main__':
    user = Log()
    log = user.get_log()
    log.debug('test')
    user.close_handle()