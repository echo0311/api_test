# -*- coding: utf-8 -*-
import json

from data.get_data import GetData
from base.api_requests import RunMethod
from util.common import Common
from data.depend_data import DependData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import random


class RunTest:
    def __init__(self, file_name=None, sheet_id=0):
        self.data = GetData(file_name, sheet_id)
        self.oper_header = OperationHeader()
        self.run = RunMethod()
        self.comm = Common()
        self.send_mail = SendEmail()

    def go_on_run(self):
        lines = self.data.get_case_lines()
        pass_count = []
        fail_count = []
        for i in range(1, lines):
            is_run = self.data.get_is_run(i)
            if is_run:
                res = None
                url = self.data.get_url(i)
                method = self.data.get_method_type(i)
                fix_request_key = self.data.get_fix_request_key(i)
                request_data = self.data.get_request_for_json(i)
                expected = self.data.get_expected_result(i)
                header = self.data.get_header(i)
                is_depend = self.data.is_depend(i)
                if is_depend is not None:
                    depend_case_id = self.data.get_depend_case_id(i)
                    depend_request = self.data.get_depend_request(i)
                    depend_data = DependData(depend_case_id)
                    depend_response = depend_data.get_data_for_key(i)  # 从依赖接口的返回结果中匹配需要的依赖字段
                    request_data[depend_request] = depend_response
                if header == 'yes':
                    self.oper_header.write_cookie()
                    cookies = self.oper_header.get_cookie()
                    header = {'Cookie': cookies}
                    # json.dump()
                    res = self.run.run_main(url, method, request_data, header)
                else:
                    res = self.run.run_main(url, method, request_data)
                # if self.comm.contrast(expected, res):
                #     print("测试通过")
                #     self.data.write_result(i, 'pass')
                #     pass_count.append(i)
                # else:
                #     print("测试失败")
                #     self.data.write_result(i, res)
                #     fail_count.append(i)
        # self.send_mail.send_main(pass_count,fail_count)

    def run_request_data(self, index, value):
        request_data = self.data.get_request_for_json(index)
        key = self.data.get_fix_request_key(index)
        request_data[key] = value
        return request_data

    def run_expected_data(self, index, value):
        key = self.data.get_expected_result(index)
        expected_data = {}
        expected_data[key] = value
        expected_data = key + ":" + expected_data[key]
        return expected_data


if __name__ == '__main__':
    file_name = '../dataconfig/managerment_api.xls'
    run = RunTest(file_name)
    run.go_on_run()
