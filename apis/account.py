# -*- coding: utf-8 -*-
from base.api_base import BaseAPI
from base.api_requests import RunMethod
import time
import json


# 新增用户
class AddAccount(BaseAPI):
    def __init__(self):
        self.path = '/api/admin/enterprises/1/users'
        super().__init__()

    def url(self):
        return super().get_url(self.path)

    def header(self):
        accept = 'application/vnd.esage.user+json;version=3.0'
        content_type = 'application/vnd.esage.user+json;version=3.0'
        header = super().get_header(accept, content_type)
        return header

    def request_data(self):
        data = super().get_request_data('add_user')
        num = str(int(time.time()))
        data['name'] += num
        data['nick'] += num
        return json.dumps(data)


if __name__ == '__main__':
    account = AddAccount()
    url = account.url()
    header = account.header()
    request_data = account.request_data()
    print(url)
    print("-------------------------")
    print(header)
    print("-------------------------")
    print(request_data)

    run = RunMethod()
    res = run.run_main(url, 'POST', request_data, header)
    print(res)
