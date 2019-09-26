# -*- coding: utf-8 -*-
import requests
from util.operation_json import OperationJson
from util.operation_ini import OperationIni

requests.packages.urllib3.disable_warnings()


class OperationHeader:
    def __init__(self):
        self.file_path = '../config/base.ini'
        self.oper_json = OperationJson('../dataconfig/cookies.json')
        self.oper_ini = OperationIni(self.file_path)

    def request_cookie(self):
        '''
        获取cookie的jar文件
        '''
        url = self.oper_ini.get_value('host', 'url') + '/api/login'
        # 账号:auto  密码:auto@123
        headers = {
            "Authorization": "Basic YXV0bzphdXRvQDEyMw==",
            "Accept": "application/vnd.esage.login+json;version=3.0"
        }
        res = requests.get(url, headers=headers, verify=False)
        return res.cookies

    # 第一种方式将cookie信息写入json文件中  ../dataconfig/cookies.json
    # 将cookie文件写到json中
    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.request_cookie())
        self.oper_json.write_json(cookie)

    # 从json中读取cookie值
    def get_cookie(self):
        cookie = []
        data = self.oper_json.get_json()
        for key, value in data.items():
            cookie.append('%s=%s' % (key, value))
        return ';'.join(cookie)

    # 第二种方式将cookie信息写入配置文件中 ../config/base.ini   (默认使用这种方式)
    # 将cookie文件写入配置文件中
    def write_cookie_ini(self):
        data = requests.utils.dict_from_cookiejar(self.request_cookie())
        cookie_data = []
        for key, value in data.items():
            cookie_data.append('%s=%s' % (key, value))
        cookie = ';'.join(cookie_data)
        self.oper_ini.write_value('headers', 'Cookie', cookie)

    # 从配置文件中读取cookie信息
    def get_cookie_ini(self):
        cookie = self.oper_ini.get_value('headers', 'Cookie')
        return cookie

    # 从配置文件中读取headers信息
    def get_headers(self, accept=None, content_type=None):
        headers = self.oper_ini.get_items('headers')
        if 'cookie' not in headers:
            self.write_cookie_ini()
            headers = self.oper_ini.get_items('headers')

        if accept is not None:
            headers['Accept'] = accept
        if content_type is not None:
            headers['Content-Type'] = content_type
        return headers


if __name__ == '__main__':
    oper = OperationHeader()
    oper.write_cookie()
    print(oper.get_headers())
