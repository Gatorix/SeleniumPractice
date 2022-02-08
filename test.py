from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
import msvcrt
import os
import time

global driver

# 使用webdriver_manager,但是似乎不行
# 使用Service+Options参数可以避免出现 DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# from webdriver_manager.chrome import ChromeDriverManager


def exit_with_anykey():
    print("press any key to exit")
    ord(msvcrt.getch())
    os._exit(1)


def chrome():
    service = Service(r"venv\Scripts\chromedriver.exe")
    options = webdriver.ChromeOptions()
    # 剔除无用日志
    options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    # 打开页面
    # driverpath = r'venv\Scripts\chromedriver.exe'
    driver = webdriver.Chrome(service=service, options=options)

    # driver.maximize_window()  # 最大化窗口
    # driver.implicitly_wait(3)
    driver.get("http://www.5itest.cn/register")

    # time.sleep(5)
    print(ec.title_contains("注册"))

    driver.find_element_by_id("register_email").send_keys("test@163.com")

    # 父级div的class_name=controls定位,有两个,取第二个
    user_name_element_node = driver.find_elements_by_class_name("controls")[1]
    # 子级div的class_name=form-control定位
    user_element = user_name_element_node.find_element_by_class_name(
        "form-control")
    # print("长度:%s" % (len(user_element)))
    # 输入值
    user_element.send_keys("asdfasdf")

    driver.find_element_by_name("password").send_keys("111111")

    driver.find_element_by_xpath('//*[@id="captcha_code"]').send_keys("111111")
    # ec.title_is()#完全匹配
    exit_with_anykey()


def edge():
    # service = Service(r"venv\Scripts\msedgedriver.exe")
    # options = webdriver.ChromeOptions()
    # 打开页面
    driver = webdriver.Edge(r"venv\Scripts\msedgedriver.exe")

    # driver.maximize_window()  # 最大化窗口
    # driver.implicitly_wait(3)
    driver.get("http://www.5itest.cn/register")
    # exit_with_anykey()


def firefox():
    # service = Service(r"venv\Scripts\msedgedriver.exe")
    # options = webdriver.ChromeOptions()
    # 打开页面
    driver = webdriver.Firefox(
        executable_path=r"venv\Scripts\geckodriver.exe", service_log_path=r"venv\watchlog.log")

    # driver.maximize_window()  # 最大化窗口
    # driver.implicitly_wait(3)
    driver.get("http://www.5itest.cn/register")
    # exit_with_anykey()


if __name__ == "__main__":
    chrome()
    # edge()
    # firefox()
