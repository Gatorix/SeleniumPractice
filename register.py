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


def get_verification_img():
    driver.save_screenshot(r'.\tmp\test.png')
    code_element = driver.find_element(By.ID, "getcode_num")
    left = code_element.location['x']+202
    top = code_element.location['y']+132
    right = code_element.size['width']+left+20
    bottom = code_element.size['height']+top+10
    saved_img = Image.open(r'.\tmp\test.png')
    verification_img = saved_img.crop((left, top, right, bottom))
    verification_img.save(r'.\tmp\verification_img.png')


def gen_random_str(len=8, prefix='', suffix=''):
    return prefix+''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyz", len))+suffix


def exit_with_anykey():
    print("press any key to exit")
    ord(msvcrt.getch())
    os._exit(1)


def find_element_by_xpath(xpath):
    return driver.find_element(By.XPATH, xpath)


def send_element(element, key):
    element.send_keys(key)


def main():
    user_email = gen_random_str(len=10, suffix='@outlook.com')
    user_name = gen_random_str(len=12)
    user_password = gen_random_str()
    verification_code = gen_random_str(len=5)

    find_element_by_xpath('//*[@id="register_email"]').send_keys(user_email)

    find_element_by_xpath('//*[@id="register_nickname"]').send_keys(user_name)

    find_element_by_xpath(
        '//*[@id="register_password"]').send_keys(user_password)

    get_verification_img()

    # 随机填充验证码
    find_element_by_xpath(
        '//*[@id="captcha_code"]').send_keys(verification_code)

    # API解析验证码
    # find_element_by_xpath(
    #     '//*[@id="captcha_code"]').send_keys(analyze.analyze(r'tmp\verification_img.png'))

    find_element_by_xpath('//*[@id="register-btn"]').click()

    exit_with_anykey()


if __name__ == "__main__":
    main()
