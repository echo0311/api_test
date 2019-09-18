# -*- coding: utf-8 -*-
from base.api_base import ApiBase


# 查看多个VAPP接口
class virtualAppliances(ApiBase):
    # def __init__(self, file_name=None, sheet_id=None):
    #     super().__init__(file_name, sheet_id)

    # 传入不同的accpet和content_type
    def get_headers(self, content_type=None, **kwargs):
        self.accept = ''
        headers = self.oper_h.get_headers(self.accept)
        return headers

    # 修改request信息
    def get_request_data(self, index):
        request_data = self.data.get_request_for_json(index)

        return request_data

    # def get_headers(self):
    #     accept = 'application/vnd.esage.virtualappliances+json;version=3.0'
    #     headers = self.base.get_headers(accept=accept)
    #     return headers
