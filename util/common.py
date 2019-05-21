# -*- coding: utf-8 -*-
import json
from filecmp import cmp


class Common:

    def contrast(self, expected, actual):
        '''
        判断一个字符串是否在另一个字符串中
        expected:预期结果
        actual：返回结果
        :return: boolean 值
        '''
        flag = None
        if expected in actual:
            flag = True
        else:
            flag = False
        return flag

    def is_equal_dict(self,dict_one,dict_two):
        '''
        判断两个字典是否相等
        '''
        if isinstance(dict_one,str):
            dict_one = json.loads(dict_one)
        if isinstance(dict_two,str):
            dict_two = json.loads(dict_two)
        return cmp(dict_one,dict_two)