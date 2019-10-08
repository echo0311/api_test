# -*- coding: utf-8 -*-

from apis.account_apis import AddAccount
from apis.account_apis import EditAccount
from apis.account_apis import DeleteAccount
from util.operation_header import OperationHeader
from log.Log import Log

def AccountFlows():
    oper_header = OperationHeader()
    log = Log()
    logger =log.get_log()
    oper_header.is_cookie()

    # 测试新增用户接口
    logger.info("开始测试新增用户接口")
    add_account = AddAccount()
    add_res=add_account.run()
    add_res_code = add_res.status_code
    logger.info("新增用户接口的返回码为%d"% add_res_code)
    assert add_res_code == 201, '新增用户接口测试失败'
    add_res=add_res.json()

    # 测试编辑用户接口
    logger.info("开始测试编辑用户接口")
    edit_account = EditAccount(add_res)
    edit_res = edit_account.run()
    logger.info("编辑用户接口的返回码为%d" % edit_res.status_code)
    assert edit_res.status_code == 200, '编辑用户接口测试失败'

    # 测试删除用户接口
    logger.info("开始删除用户接口")
    del_account = DeleteAccount(add_res)
    del_res=del_account.run()
    logger.info("删除用户接口的返回码为%d" % del_res.status_code)
    assert del_res.status_code == 204, '删除用户接口测试失败'
    log.close_handle()


if __name__ == '__main__':
    AccountFlows()
