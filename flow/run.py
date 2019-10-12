# coding=utf-8
import unittest
import os
import HTMLTestRunnerCN

# 测试用例存放路径
# case_path = os.path.join(os.getcwd(), "manage")
case_path = os.getcwd()

# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite


if __name__ == '__main__':
    path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    report_path = os.path.join(path, 'report\接口自动化测试报告.html')
    fp = open(report_path, 'wb')
    runner = HTMLTestRunnerCN.HTMLTestReportCN(
        stream=fp,
        title='ESage接口自动化测试报告',
        description='报告中描述部分',
        tester='test'
    )
    runner.run(get_allcase())
    fp.close()
