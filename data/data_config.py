# -*- coding: utf-8 -*-
class GlobalConstant:
    ID = 0
    MODULE = 1
    URL = 2
    FLAG = 3  # 是否需要修改url信息 0为不需要，1是需要替换vdc_id ,2是需要替换vdc_id,vapp_id
    IS_RUN = 4
    METHOD_TYPE = 5
    IS_COOKIE = 6
    DEPEND_CASE = 7  # 依赖的case编号
    DEPEND_RES = 8  # 依赖的结果返回
    DEPEND_REQ = 9  # 需要替换掉请求字段
    REQUEST_DATA = 10
    FIX_REQUEST_DATA = 11  # 需要修改的请求字段
    EXPECTED_RESULT = 12
    ACTUAL_RESULT = 13


def get_id():
    return GlobalConstant.ID


def get_module():
    return GlobalConstant.MODULE


def get_url():
    return GlobalConstant.URL


def get_flag():
    return GlobalConstant.FLAG


def get_is_run():
    return GlobalConstant.IS_RUN


def get_method_type():
    return GlobalConstant.METHOD_TYPE


# 是否携带header
def get_is_header():
    return GlobalConstant.IS_COOKIE


# 依赖的case编号
def get_depend_case():
    return GlobalConstant.DEPEND_CASE


# 依赖的结果返回   8
def get_depend_res():
    return GlobalConstant.DEPEND_RES


# 需要替换掉请求字段   9
def get_depend_req():
    return GlobalConstant.DEPEND_REQ


# 获取请求数据 10
def get_request_data():
    return GlobalConstant.REQUEST_DATA


# 获取修改的请求字段
def get_fix_request_data():
    return GlobalConstant.FIX_REQUEST_DATA


# 获取期望结果  12
def get_expected_result():
    return GlobalConstant.EXPECTED_RESULT


# 获取实际结果  13
def get_actual_result():
    return GlobalConstant.ACTUAL_RESULT

# # 获取header的值
# def get_header():
#     header = {
#         "header": "123456"
#     }
#     return header
