# -*- coding: utf-8 -*-
import unittest
import os
import HTMLTestRunnerCN
from apis.account_apis import AddAccount
from apis.account_apis import EditAccount
from apis.account_apis import DeleteAccount
from util.operation_header import OperationHeader
from log.Log import log
from utx import *


class AccountFlows(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        oper_header = OperationHeader()
        oper_header.is_cookie()

    def setUp(self):
        self.g = globals()

    def test_add_account(self):
        """
        测试新增用户接口
        :return: None
        """
        log.info("开始测试新增用户接口")
        add_account = AddAccount()
        add_res = add_account.run()
        add_res_code = add_res.status_code
        log.info("新增用户接口的返回码为%d" % add_res_code)
        self.assertEqual(add_res_code, 201, '新增用户接口测试失败')
        # 设置全局变量，作为接口依赖参数
        self.g['add_account'] = add_res.json()

    def test_edit_account(self):
        """
            测试编辑用户接口
            :return: None
        """
        log.info("开始测试编辑用户接口")
        add_res = self.g['add_account']
        # 获取添加用户的响应信息
        edit_account = EditAccount(add_res)
        edit_res = edit_account.run()
        log.info("编辑用户接口的返回码为%d" % edit_res.status_code)
        self.assertEqual(edit_res.status_code, 201, '编辑用户接口测试失败')

    # @unittest.skip("I don't want to run this case.")
    def test_del_account(self):
        """
             测试删除用户接口
            :return: None
        """
        log.info("开始删除用户接口")
        # 获取添加用户的响应信息
        add_res = self.g['add_account']
        del_account = DeleteAccount(add_res)
        del_res = del_account.run()
        log.info("删除用户接口的返回码为%d" % del_res.status_code)
        self.assertEqual(del_res.status_code, 204, '删除用户接口测试失败')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(map(AccountFlows, ['test_add_account', 'test_edit_account', 'test_del_account']))
    path = os.path.abspath(os.path.join(os.getcwd(), "../.."))
    report_path = os.path.join(path, 'report\接口自动化测试报告.html')
    fp = open(report_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='ESage接口自动化测试报告',
        description='报告中描述部分',
        tester='test'
    )
    runner.run(suite)
    fp.close()
