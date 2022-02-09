import msvcrt
import os
import random
import time
import analyze
from PIL import Image

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

global driver

# 使用webdriver_manager,但是似乎不行
# 使用Service+Options参数可以避免出现 DeprecationWarning: executable_path has been deprecated, please pass in a Service object
# from webdriver_manager.chrome import ChromeDriverManager


def gen_random_str(len=8, prefix='', suffix=''):
    return prefix+''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyz", len))+suffix


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

    driver.maximize_window()  # 最大化窗口
    # driver.implicitly_wait(3)
    driver.get("http://www.5itest.cn/register")

    driver.save_screenshot(r'.\tmp\test.png')
    code_element = driver.find_element(By.ID, "getcode_num")

    left = code_element.location['x']+202
    top = code_element.location['y']+132
    right = code_element.size['width']+left+20
    bottom = code_element.size['height']+top+10
    # print(code_element.location)
    # print(left, top, right, bottom)
    saved_img = Image.open(r'.\tmp\test.png')
    verification_img = saved_img.crop((left, top, right, bottom))
    verification_img.save(r'.\tmp\verification_img.png')

    # time.sleep(5)
    # print(ec.title_contains("注册"))
    # 使用WebDriverWait在1s内查找class name=controls的元素是否存在
    # locater = (By.CLASS_NAME, "controls")
    # WebDriverWait(driver, 1).until(
    #     ec.visibility_of_element_located(locater))
    email_element = driver.find_element(By.ID, "register_email")
    # 获取placeholder的默认值
    # defemail = email_element.get_attribute("placeholder")
    email_element.send_keys(gen_random_str(len=16, suffix="@outlook.com"))
    # 获取当前输入的值
    # curremail = email_element.get_attribute("value")
    # print(defemail, curremail)

    # driver.find_element(By.ID, "register_email").send_keys("test@163.com")

    # 父级div的class_name=controls定位,有两个,取第二个
    user_name_element_node = driver.find_elements(By.CLASS_NAME, "controls")[1]
    # 子级div的class_name=form-control定位
    user_element = user_name_element_node.find_element(By.CLASS_NAME,
                                                       "form-control")
    # print("长度:%s" % (len(user_element)))
    # 输入值
    user_element.send_keys(gen_random_str())

    driver.find_element(By.NAME, "password").send_keys(gen_random_str())

    # 调用api解析验证码，次数有限
    # driver.find_element(
    #     By.XPATH, '//*[@id="captcha_code"]').send_keys(analyze.analyze(r'tmp\verification_img.png'))

    # 先随机传一个进去
    driver.find_element(
        By.XPATH, '//*[@id="captcha_code"]').send_keys(gen_random_str(len=5))

    # ec.title_is()  # 完全匹配

    exit_with_anykey()
    # driver.close()


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
    # chrome()
    edge()
    # firefox()
