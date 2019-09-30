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

    # 测试编辑用户接口
    logger.info("开始测试编辑用户接口")
    edit_account =EditAccount(add_res)
    edit_account.run()

    # 测试删除用户接口
    logger.info("开始删除用户接口")
    del_account = DeleteAccount(add_res)
    del_account.run()

    log.close_handle()

if __name__ == '__main__':
    AccountFlows()
