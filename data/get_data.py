# -*- coding: utf-8 -*-
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data import data_config
from util.operation_db import OperationMysql


class GetData:
    def __init__(self, file_name=None, sheet_id=None):
        self.oper_excel = OperationExcel(file_name, sheet_id)

    # 获取excel行数
    def get_case_lines(self):
        lines = self.oper_excel.get_lines()
        return lines

    # 获取url地址
    def get_url(self, rowx):
        colx = data_config.get_url()
        url = self.oper_excel.get_cell_value(rowx, colx)
        return url

    # 获取flag信息
    def get_flag(self,rowx):
        colx = data_config.get_flag()
        flag = self.oper_excel.get_cell_value(rowx, colx)
        return flag

    # 获取是否运行
    def get_is_run(self, rowx):
        flag = None
        colx = data_config.get_is_run()
        is_run = self.oper_excel.get_cell_value(rowx, colx)
        if is_run == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_method_type(self, rowx):
        colx = data_config.get_method_type()
        method_type = self.oper_excel.get_cell_value(rowx, colx)
        if method_type == 'get':
            return 'GET'
        elif method_type == 'post':
            return 'POST'

    def get_header(self, rowx):
        colx = data_config.get_is_header()
        header = self.oper_excel.get_cell_value(rowx, colx)
        if header == 'no':
            return None
        else:
            return header

    # 获取请求数据
    def get_request_key(self, rowx):
        colx = data_config.get_request_data()
        request_key = self.oper_excel.get_cell_value(rowx, colx)
        if request_key == '':
            return None
        else:
            return request_key

    # 获取修改的请求字段
    def get_fix_request_key(self, rowx):
        colx = data_config.get_fix_request_data()
        fix_request_key = self.oper_excel.get_cell_value(rowx, colx)
        if fix_request_key == '':
            return None
        else:
            return fix_request_key

    # 根据关键字，在json文件中获取请求数据
    def get_request_for_json(self, rowx):
        oper_json = OperationJson()
        request_key = self.get_request_key(rowx)
        if request_key is None:
            request_data = None
        else:
            request_data = oper_json.get_data(request_key)
        return request_data

    # 获取实际结果
    def get_actual_result(self, rowx):
        colx = data_config.get_actual_result()
        actual_result = self.oper_excel.get_cell_value(rowx, colx)
        return actual_result

    # 获取预期结果
    def get_expected_result(self, rowx):
        colx = data_config.get_expected_result()
        expected_result = self.oper_excel.get_cell_value(rowx, colx)
        return expected_result

    # 根据sql查询预期结果
    def get_expected_result_by_mysql(self, rowx):
        oper_mysql = OperationMysql()
        sql = self.get_expected_result(rowx)
        res = oper_mysql.search(sql)
        return res.decode('unicode-escape')

    # 将结果写入excel中
    def write_result(self, rowx, value):
        colx = data_config.get_actual_result()
        self.oper_excel.write_value(rowx, colx, value)

    # 获取依赖数据的case_id
    def get_depend_case_id(self, rowx):
        colx = data_config.get_depend_case()
        depend_case_id = self.oper_excel.get_cell_value(rowx, colx)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    # 所依赖的结果返回的字段
    def get_depend_respons(self, rowx):
        colx = data_config.get_depend_res()
        depend_respons = self.oper_excel.get_cell_value(rowx, colx)
        if depend_respons == "":
            return None
        else:
            return depend_respons

    # 需要替换掉请求字段
    def get_depend_request(self, rowx):
        colx = data_config.get_depend_req()
        depend_request = self.oper_excel.get_cell_value(rowx, colx)
        if depend_request == "":
            return None
        else:
            return depend_request

    # 判断是否有case依赖
    def is_depend(self, rowx):
        depend_field = self.get_depend_request(rowx)
        if depend_field == "":
            return None
        else:
            return depend_field
