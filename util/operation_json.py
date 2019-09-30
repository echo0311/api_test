# -*- coding: utf-8 -*-
import json
import os

class OperationJson:
    def __init__(self, file_path=None):
        if file_path is None:
            self.base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
            self.file_path = self.base_path+"\\dataconfig\\request_data.json"
        else:
            self.file_path = file_path
        self.data = self.get_json()

    # 获取json文件
    def get_json(self):
        with open(self.file_path, encoding='UTF-8') as fp:
            data = json.load(fp)
            return data

    # 根据关键字获取数据
    def get_data(self, key):
        value = self.data[key]
        return value

    # 写入json文件
    def write_json(self, data):
        with open(self.file_path, 'w') as fp:
            fp.write(json.dumps(data))



# if __name__ == '__main__':
#     oper_json = OperationJson()
#     print(oper_json.get_data('login'))
