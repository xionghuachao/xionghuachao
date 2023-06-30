import unittest
from config.HTMLTestReportCN import HTMLTestRunner

from testcases.test_login import Testlogin

#suite=unittest.TestSuite()
suite=unittest.TestLoader().loadTestsFromTestCase(Testlogin)
f=open("result.html","wb")
HTMLTestRunner(stream=f,title="登录测试报告",description="太棒了").run(suite)
f.close()