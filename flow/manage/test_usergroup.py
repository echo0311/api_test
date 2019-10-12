# -*- coding: utf-8 -*-
import unittest
import os
from apis.account_apis import GetUserGroup
from util.operation_header import OperationHeader
from log.Log import log


class UserGroupFlows(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        oper_header = OperationHeader()
        oper_header.is_cookie()

    def setUp(self):
        self.g = globals()

    def test_get_usergroup(self):
        """
            测试获取用户组信息接口
            :return: None
        """
        log.info("开始测试获取用户组信息接口")
        get_usergroup = GetUserGroup()
        get_usergroup_res = get_usergroup.run()
        self.assertEqual(get_usergroup_res.status_code, 200, '获取用户组信息接口失败')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
