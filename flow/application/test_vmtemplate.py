# -*- coding: utf-8 -*-
import unittest
from log.Log import log


class VMTemplateFlow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_get_vmtemplate(self):
        """
        测试查询模板名称接口
        :return: None
        """
        log.info('开始测试查询模板名称接口')

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
