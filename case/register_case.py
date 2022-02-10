import sys
import msvcrt
import os
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
from business.register_business import RegisterBusiness
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class RegisterCase(object):
    def __init__(self) -> None:
        service = Service(r"venv\Scripts\chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "excludeSwitches", ['enable-automation', 'enable-logging'])
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()
        driver.get("http://www.5itest.cn/register")
        self.reg = RegisterBusiness(driver)

    def test_reg_email_error(self):
        email_error = self.reg.register_email_error(
            '111', 'adsfasdfa', '12312311', 'ccccc')
        if email_error == True:
            print('注册成功，用例执行失败')

    def test_reg_name_error(self):
        name_error = self.reg.register_name_error(
            '111@163.com', '11', '12312311', 'ccccc')
        if name_error == True:
            print('注册成功，用例执行失败')
        else:
            print('用例执行通过')

    def test_reg_password_error(self):
        password_error = self.reg.register_password_error(
            '111@163.com', 'adsfasdfa', '11', 'ccccc')
        if password_error == True:
            print('注册成功，用例执行失败')
        else:
            print('用例执行通过')

    def test_reg_vcode_error(self):
        vcode_error = self.reg.register_vcode_error(
            '111@163.com', 'adsfasdfa', '12312311', 'c1')
        if vcode_error == True:
            print('注册成功，用例执行失败')
        else:
            print('用例执行通过')

    def test_reg_success(self):
        self.reg.register_base(
            '111@163.com', 'adsfasdfa', '12312311', 'c1')
        if self.reg.register_success() == True:
            print('注册成功，用例通过')
        else:
            print('用例执行失败')


if __name__ == "__main__":
    regi = RegisterCase()
    regi.test_reg_email_error()
    regi.test_reg_name_error
    regi.test_reg_password_error()
    regi.test_reg_vcode_error()
    regi.test_reg_success()
    ord(msvcrt.getch())
    os._exit(1)