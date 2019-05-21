# -*- coding: utf-8 -*-
from base.api_requests import RunMethod
from util.operation_header import OperationHeader
from apis.vapp_apis import VirtualAppliances


class VirtualDatacenters(object):
    def __init__(self,file_name, sheet_id):
        self.run = RunMethod()
        self.oper_header = OperationHeader()
        self.vapps = VirtualAppliances(file_name, sheet_id)

    def run_api(self):
        url = self.vapps.get_url(3)
        headers = self.vapps.get_headers()
        res = self.run.run_main(url, 'GET', headers=headers)
        print(res)


if __name__ == '__main__':
    file_name = '../dataconfig/managerment_api.xls'
    sheet_id = 0
    vcd = VirtualDatacenters(file_name, sheet_id)
    vcd.run_api()
