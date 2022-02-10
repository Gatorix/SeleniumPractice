import sys
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
sys.path.append(r'\\mac\Home\Documents\SeleniumPractice')

# from TestRunner import HTMLTestRunner
# import HtmlTestRunner
from HtmlTestRunner import HTMLTestRunner
import unittest
import msvcrt
import os
from business.register_business import RegisterBusiness
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RegisterCase(unittest.TestCase):
    def setUp(self) -> None:
        self.service = Service(r"venv\Scripts\chromedriver.exe")
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        self.driver = webdriver.Chrome(
            service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.get("http://www.5itest.cn/register")
        self.reg = RegisterBusiness(self.driver)

    def tearDown(self) -> None:
        self.driver.close()

    def test_reg_email_error(self):
        email_error = self.reg.register_email_error(
            '111', 'adsfasdfa', '12312311', 'ccccc')
        # if email_error == True:
        #     print('注册成功，用例执行失败')
        self.assertFalse(email_error, '注册成功，用例执行失败')

    def test_reg_name_error(self):
        name_error = self.reg.register_name_error(
            '111@163.com', '11', '12312311', 'ccccc')
        # if name_error == True:
        #     print('注册成功，用例执行失败')
        # else:
        #     print('用例执行通过')
        self.assertFalse(name_error, '注册成功，用例执行失败')

    def test_reg_password_error(self):
        password_error = self.reg.register_password_error(
            '111@163.com', 'adsfasdfa', '11', 'ccccc')
        # if password_error == True:
        #     print('注册成功，用例执行失败')
        # else:
        #     print('用例执行通过')
        self.assertFalse(password_error, '注册成功，用例执行失败')

    def test_reg_vcode_error(self):
        vcode_error = self.reg.register_vcode_error(
            '111@163.com', 'adsfasdfa', '12312311', 'c1')
        # if vcode_error == True:
        #     print('注册成功，用例执行失败')
        # else:
        #     print('用例执行通过')
        self.assertFalse(vcode_error, '注册成功，用例执行失败')

    def test_reg_success(self):
        success = self.reg.register_base(
            '111@163.com', 'adsfasdfa', '12312311', 'c1')
        # if self.reg.register_success() == True:
        #     print('注册成功，用例通过')
        # else:
        #     print('用例执行失败')
        self.assertTrue(success, '注册成功，用例执行失败')


if __name__ == "__main__":
    # report_path = os.path.join(os.getcwd()+"/report/report.html")
    # f=open(report_path,'wb')
    # print(type(f))
    suite=unittest.TestSuite()
    suite.addTest(RegisterCase('test_reg_vcode_error'))
    # unittest.main(testRunner=HTMLTestRunner())

    HTMLTestRunner(report_title='first report').run(suite)
