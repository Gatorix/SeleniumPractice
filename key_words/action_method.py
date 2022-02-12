import sys
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
sys.path.append(r'\\mac\Home\Documents\SeleniumPractice')

import time
from base.find_element import FindElement
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


class ActionMethod:
    def __init__(self) -> None:
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            service = Service(r"venv\Scripts\chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option(
                "excludeSwitches", ['enable-automation', 'enable-logging'])
            self.driver = webdriver.Chrome(service=service, options=options)

        elif browser == 'firefox':
            self.driver = webdriver.Firefox(
                executable_path=r"venv\Scripts\geckodriver.exe", service_log_path=r"venv\watchlog.log")

        elif browser == 'edge':
            self.driver = webdriver.Edge(r"venv\Scripts\msedgedriver.exe")
    
    # 打开url
    def open_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        find_element = FindElement(self.driver)
        return find_element.get_element(key)

    # 输入元素
    def element_send_keys(self, value, key):
        element = self.get_element(key)
        element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.get_element(key).click()

    # 等待
    def sleep_time(self, t=3):
        time.sleep(t)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()
