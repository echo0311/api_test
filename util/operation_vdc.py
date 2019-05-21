# -*- coding: utf-8 -*-
from util.operation_ini import OperationIni
from util.operation_header import OperationHeader
from base.api_requests import RunMethod


class OperationVDC(object):

    def __init__(self):
        self.oper_ini = OperationIni()
        self.oper_h = OperationHeader()
        self.run = RunMethod()

    def request_virtualdatacenters(self):
        url = self.oper_ini.get_value('host', 'url') + '/api/cloud/virtualdatacenters'
        accept = 'application/vnd.esage.virtualdatacenters+json;version=3.0'
        headers = self.oper_h.get_headers(accept=accept)
        res = self.run.run_main(url, 'GET', headers=headers)
        id = res['collection'][0]['id']
        return id

    def write_vdc_id(self):
        vdc_id = self.request_virtualdatacenters()
        self.oper_ini.write_value('global', 'virtualdatacenters', str(vdc_id))

    def get_vdc_id(self):
        vdc_id = self.oper_ini.get_value('global', 'virtualdatacenters')
        return vdc_id


if __name__ == '__main__':
    oper_vdc = OperationVDC()
    oper_vdc.write_vdc_id()
    print(oper_vdc.get_vdc_id())
