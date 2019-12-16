# -*- coding: UTF-8 -*-
import os
import sys

path = os.path.split(os.path.realpath(__file__))[0]  # 定位类目录
print(path)
sys.path.append(path)
from utlis.file.FileUtil import file_utils
from BeautifulReport.BeautifulReport import BeautifulReport
from webdriver.SeleniumDriver import SeleniumDriver
from initialize.busines.MkLogin import MkLogin
from utlis.read_res.Read_exec import read_exec
import unittest
import ddt

data = read_exec.get_data()


@ddt.ddt
class Test_ddt_case(unittest.TestCase):

    def setUp(self):
        self.web_tools = SeleniumDriver(SeleniumDriver.Chrome)
        self.mlgoin = MkLogin(self.web_tools)
        self.web_tools.open_url_is_true("https://www.imooc.com/","慕课网")




    @ddt.data(*data)
    def test_register_case(self,data):
        phone,passwrod,error_cod,assert_text = data
        rest = self.mlgoin.register_function(phone, passwrod, error_cod, assert_text)
        self.assertTrue(rest,"预期结果错误")



    def tearDown(self):
        self.web_tools.close()
# 如果不能打开这个文件，可能是now的格式，不支持：和空格
# 报告地址&名称
report_title = "我的测试报告"

# 报告描述
desc = '用于展示修改样式后的HTMLTestRunner'

if __name__ == '__main__':
    # unittest.main()
    report_path = file_utils.location_file("report")
    # file = open(report_path,"wb")
    # suite = unittest.TestLoader().loadTestsFromTestCase(Test_ddt_case)
    # runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="This is first report1",description=u"这个是我们第一次测试报告1",verbosity=2)
    # runner.run(suite)

    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(Test_ddt_case))
    run = BeautifulReport(testsuite)
    run.report(description=desc, filename="我的报告", log_path=report_path)


