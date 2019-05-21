# -*- coding: utf-8 -*-
from util.operation_excel import OperationExcel
from base.api_requests import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse


class DependData:
    def __init__(self, case_id):
        self.case_id = case_id
        self.oper_excel = OperationExcel()
        self.data = GetData()

    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.oper_excel.get_row_values(self.case_id)

    # 执行所依赖接口，获得结果
    def run_dependent(self):
        run_method = RunMethod()
        rowx = self.oper_excel.get_row_num(self.case_id)
        url = self.data.get_url(rowx)
        # header = self.data.get_header(rowx)
        request_data = self.data.get_request_for_json(rowx)
        method = self.data.get_method_type(rowx)
        res = run_method.run_main(url, method, request_data)
        return res

    # 根据excel中“依赖的返回数据”，查找前置接口运行结果的字段
    def get_data_for_key(self, rowx):
        depend_data = self.data.get_depend_respons(rowx)  # excel中依赖的返回字段
        response_data = self.run_dependent()  # 前置接口运行后的返回结果
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        return [math.value for math in madle]  # 返回匹配的字段值
