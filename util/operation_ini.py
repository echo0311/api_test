# -*- coding: utf-8 -*-
import configparser


class OperationIni(object):

    def __init__(self, file_name=None):
        if file_name is None:
            self.file_name = "../config/base.ini"
        else:
            self.file_name = file_name
        self.cf = self.load_ini()

    def load_ini(self):
        cf = configparser.ConfigParser()
        cf.read(self.file_name)
        return cf

    # 获取section下的options
    def get_options(self,section):
        data = self.cf.options(section)
        return data

    # 根据section，option获取数值
    def get_value(self, section, option):
        data = self.cf.get(section, option)
        return data

    # 根据section值获取所有键值对,返回一个字典
    def get_items(self, section):
        data = self.cf.items(section)
        return dict(data)

    # 写数据
    def write_value(self, section, option, value):
        self.cf.set(section, option, value)
        self.cf.write(open(self.file_name, "w"))


if __name__ == '__main__':
    read_ini = OperationIni()
    # read_ini.write_value('header', 'Cookie',"'ESGSESSIONID=8153807793856758611; auth=YXV0bzoxNTU3Mzk1NzQ2Mjc2OmEwMDE0MDA2NjE5OTM1NjUyNzIwODE4NTI4N2VkMjM4OkVTQUdF'")
    print(read_ini.get_items('header'))
