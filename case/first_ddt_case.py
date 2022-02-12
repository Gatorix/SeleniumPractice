from dataclasses import dataclass
import ddt
import sys
import time
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
sys.path.append(r'\\mac\Home\Documents\SeleniumPractice')
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from log.user_log import UserLog
from business.register_business import RegisterBusiness
import unittest
from HtmlTestRunner import HTMLTestRunner
import os
from pydoc import classname
from util.excel_util import ExcelUtil

ex=ExcelUtil()
data=ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls) -> None:
    #     cls.log = UserLog()
    #     cls.logger = cls.log.get_log()
    #     cls.file_name = r'.\tmp\verification_img.png'

    #     cls.service = Service(r"venv\Scripts\chromedriver.exe")
    #     cls.options = webdriver.ChromeOptions()
    #     cls.options.add_experimental_option(
    #         "excludeSwitches", ['enable-automation', 'enable-logging'])
    #     cls.driver = webdriver.Chrome(
    #         service=cls.service, options=cls.options)
    #     cls.driver.maximize_window()
    #     cls.driver.get("http://www.5itest.cn/register")

    def setUp(self) -> None:
        self.file_name = r'.\tmp\verification_img.png'

        self.service = Service(r"venv\Scripts\chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(
            service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.get("http://www.5itest.cn/register")

        # self.driver.refresh()
        # self.logger.info('this is chrome.')
        self.reg = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        time.sleep(2)
        for error in self._outcome.errors:
            if error:
                case_name = self._testMethodName
                img_path = os.path.join(
                    os.getcwd()+'/reports/'+case_name+'.png')
                self.driver.save_screenshot(img_path)
        self.driver.close()

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.log.close_handle()
    #     # cls.driver.close()

    # @ddt.data(
    #     ['11xcvcxqq.com', 'asdfasxczv', '3354354', 'vcode', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['.com', 'asdfasxczv', '3354354', 'vcode', 'user_email_error', '请输入有效的电子邮件地址'],
    #     ['11xcvcx@qq.com', 'asdfasxczv', '3354354', 'vcode', 'user_email_error', '请输入有效的电子邮件地址']
    
    # )

        
    # @ddt.unpack
    @ddt.data(*data)
    def test_reg_case(self, data):
        email, username, password, vcode, assertCode, assertText=data
        
        email_error = self.reg.register_func(
            email, username, password, vcode, assertCode, assertText)
        self.assertFalse(email_error, 'no error')


if __name__ == '__main__':
    # unittest.main()
    suite=unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    # suite.addTest(FirstDdtCase('test_reg_vcode_error'))
    # unittest.main(testRunner=HTMLTestRunner())

    HTMLTestRunner(report_title='first report').run(suite)
