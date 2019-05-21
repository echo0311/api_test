# -*- coding: utf-8 -*-
from base.api_requests import RunMethod
from util.operation_ini import OperationIni
from util.operation_header import OperationHeader
from data.get_data import GetData
from util.operation_vdc import OperationVDC


class ApiBase(object):

    def __init__(self, file_name=None, sheet_id=None):

        self.oper_ini = OperationIni()
        self.oper_h = OperationHeader()
        self.run = RunMethod()
        self.data = GetData(file_name, sheet_id)
        self.vdc = OperationVDC()
        self.accept = None

    def get_host(self):
        ip = self.oper_ini.get_value('host', 'url')
        return ip

    def get_flag(self, rowx):
        return self.data.get_flag(rowx)

    def get_path_xls(self, rowx):
        return self.data.get_url(rowx)

    def get_url(self, rowx, vapp_id=None):
        ip = self.get_host()
        path_xls = self.get_path_xls(rowx)
        vdc_id = self.get_vdc_id()
        flag = self.get_flag(rowx)
        url = None
        # 根据flag判断是否需要修改url信息：0为不需要，1是需要替换vdc_id ,2是需要替换vdc_id,vapp_id
        if flag == 0:
            url = ip + path_xls
        elif flag == 1:
            path = path_xls % vdc_id
            url = ip + path
        elif flag == 2:
            path = path_xls % (vdc_id, vapp_id)
            url = ip + path
        return url

    def get_vdc_id(self):
        return self.vdc.get_vdc_id()

    def get_headers(self, accept=None, content_type=None):
        headers = self.oper_h.get_headers(accept, content_type)
        return headers

    def get_request_data(self, rowx):
        return self.data.get_request_for_json(rowx)

    def request_get(self, path, headers):
        url = self.get_url(path)
        res = self.run.run_main(url, 'GET', headers=headers)
        print(res)


if __name__ == '__main__':
    path = '/api/cloud/virtualdatacenters'
    accept = 'application/vnd.esage.virtualdatacenters+json;version=3.0'
    api_base = ApiBase()
    headers = api_base.get_headers(accept=accept)
    api_base.request_get(path, headers=headers)
