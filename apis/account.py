# -*- coding: utf-8 -*-
from base.api_base import BaseAPI
import time
import json


# 新增用户
class AddAccount(BaseAPI):
    def __init__(self):
        super().__init__()

    # 依赖接口
    def relation_api(self):
        pass

    def get_path(self):
        path = '/api/admin/enterprises/1/users'
        return path

    def get_header(self):
        accept = 'application/vnd.esage.user+json;version=3.0'
        content_type = 'application/vnd.esage.user+json;version=3.0'
        headers = self.oper_h.get_headers(accept, content_type)
        return headers

    def get_request_data(self):
        data = self.oper_json.get_data('add_user')
        num = str(int(time.time()))
        data['name'] += num
        data['nick'] += num
        return json.dumps(data)

    def run(self):
        url = self.get_url()
        param = self.get_request_data()
        header = self.get_header()
        res = self.run_method.run_main(url, 'POST', param, header)
        return res


# 编辑用户
class EditAccount(BaseAPI):
    def __init__(self):
        self.user = None
        super().__init__()

    # 依赖接口
    def relation_api(self):
        add_account = AddAccount()
        res = add_account.run()
        return json.loads(res)

    def get_path(self):
        self.user = self.relation_api()
        path = '/api/admin/enterprises/1/users/{user_id}'.format(user_id=self.user['id'])
        return path

    def get_header(self):
        accept = 'application/vnd.esage.user+json;version=3.0'
        content_type = 'application/vnd.esage.user+json;version=3.0'
        headers = self.oper_h.get_headers(accept, content_type)
        return headers

    def get_request_data(self):
        data = self.oper_json.get_data('edit_user')
        data['name'] = self.user['name'] + 'edit'
        data['nick'] = self.user['nick']
        data['id'] = self.user['id']
        return json.dumps(data)

    def run(self):
        url = self.get_url()
        param = self.get_request_data()
        header = self.get_header()
        res = self.run_method.run_main(url, 'PUT', param, header)
        return res


class DeleteAccount(BaseAPI):
    def __init__(self):
        self.user = None
        super().__init__()

    # 依赖接口
    def relation_api(self):
        add_account = AddAccount()
        res = add_account.run()
        return json.loads(res)

    def get_path(self):
        self.user = self.relation_api()
        path = '/api/admin/enterprises/1/users/{user_id}'.format(user_id=self.user['id'])
        return path

    def get_header(self):
        accept = 'application/vnd.esage.user+json;version=3.0'
        headers = self.oper_h.get_headers(accept)
        return headers

    def run(self):
        url = self.get_url()
        header = self.get_header()
        res = self.run_method.run_main(url, 'DELETE', header)
        return res


if __name__ == '__main__':
    edit_account = EditAccount()
    print(edit_account.run())
