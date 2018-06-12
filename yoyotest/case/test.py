from case.run_all_case import all_case

__author__ = 'zhangqq'
# coding:utf-8
import unittest
import time
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("start")
    @classmethod
    def tearDownClass(cls):
        time.sleep(1)
        print "end"
    def test01(self):
        print u"执行测试用例01"
    def test03(self):
        print u"执行测试用例03"
    def addtest(self):
        print u"add方法"
if __name__=="_main_":
    import HTMLTestRunner
    report_path="D：\\"
    fp=open(report_path,"web")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,
                                         title=u"z这是我的报告",
                                         description=u"用例执行情况")
    runner.run(all_case())
    fp.close()
    unittest.main()