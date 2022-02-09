from lib2to3.pgen2 import driver
import random
import base64
import hashlib
import hmac
import ssl
from datetime import datetime as pydatetime
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from find_element import FindElement

try:
    from urllib import urlencode

    # from urllib2 import Request, urlopen
except ImportError:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen


class RegisterFunc(object):
    def __init__(self, url, i) -> None:
        self.driver = self.get_driver(url, i)

    def get_driver(self, url, i):
        service_chrome = Service(r"venv\Scripts\chromedriver.exe")
        options_chrome = webdriver.ChromeOptions()
            # 剔除无用日志
        options_chrome.add_experimental_option(
                "excludeSwitches", ['enable-automation', 'enable-logging'])
        service_edge = Service(r"venv\Scripts\msedgedriver.exe")

        service_firefox = Service(r"venv\Scripts\geckodriver.exe")
        if i == 0:
            driver = webdriver.Chrome(
                service=service_chrome, options=options_chrome)

        elif i == 1:
            driver = webdriver.Edge(service=service_edge)

        else:
            driver = webdriver.Firefox(
                service=service_firefox, service_log_path=r"venv\watchlog.log")
        driver.maximize_window()  # 最大化窗口
        driver.get(url)
        return driver

    def send_user_info(self, key, input_data):
        self.get_user_element(key).send_keys(input_data)

    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_verification_img(self, imgfile):
        self.driver.save_screenshot(imgfile)
        code_element = self.get_user_element('verification_code_img')
        left = code_element.location['x']+202
        top = code_element.location['y']+132
        right = code_element.size['width']+left+20
        bottom = code_element.size['height']+top+10
        saved_img = Image.open(imgfile)
        verification_img = saved_img.crop((left, top, right, bottom))
        verification_img.save(imgfile)

    def gen_random_str(self, len=8, prefix='', suffix=''):
        return prefix+''.join(random.sample("1234567890abcdefghijklmnopqrstuvwxyz", len))+suffix

    def analyze(self, imgfile):
        self.get_verification_img(imgfile)
        # 云市场分配的密钥Id
        secretId = "AKID5Zt5dn9gc1Irrvzuxnk8I5Y8b6K7IIA6mTVd"
        # 云市场分配的密钥Key
        secretKey = "a0VnKOuEky9cl1VjV0HNcx58Q5H2281CuOJ6Sgqd"
        source = "market"

        # 签名
        datetime = pydatetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        signStr = "x-date: %s\nx-source: %s" % (datetime, source)
        sign = base64.b64encode(hmac.new(secretKey.encode(
            'utf-8'), signStr.encode('utf-8'), hashlib.sha1).digest())
        auth = 'hmac id="%s", algorithm="hmac-sha1", headers="x-date x-source", signature="%s"' % (
            secretId, sign.decode('utf-8'))

        # 请求方法
        method = 'POST'
        # 请求头
        headers = {
            'X-Source': source,
            'X-Date': datetime,
            'Authorization': auth,

        }
        # 查询参数
        queryParams = {
        }

        with open(imgfile, 'rb') as fileObj:
            image_data = fileObj.read()
            base64.b64encode(image_data)

        # body参数（POST方法下存在）
        bodyParams = {
            "number": "5",
            "pri_id": "ne",
            "v_pic": base64.b64encode(image_data)}
        # url参数拼接
        url = 'http://service-98wvmcga-1256810135.ap-guangzhou.apigateway.myqcloud.com/release/yzm'
        if len(queryParams.keys()) > 0:
            url = url + '?' + urlencode(queryParams)

        request = Request(url, headers=headers)
        request.get_method = lambda: method
        if method in ('POST', 'PUT', 'PATCH'):
            request.data = urlencode(bodyParams).encode('utf-8')
            request.add_header(
                'Content-Type', 'application/x-www-form-urlencoded')
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        response = urlopen(request, context=ctx)
        content = response.read()
        if content:
            vcode = eval(content.decode('utf-8'))
            # print(vcode['v_code'])
            return vcode['v_code']

    def main(self):
        imgfile = r'tmp\verification_img.png'
        user_name = self.gen_random_str()
        user_email = self.gen_random_str(suffix='@outlook.com')
        user_password = self.gen_random_str()
        vcode = self.analyze(imgfile)

        self.send_user_info('user_email', user_email)
        self.send_user_info('user_name', user_name)
        self.send_user_info('user_password', user_password)
        self.send_user_info('verification_code', vcode)
        self.get_user_element('regbtn').click()

        if self.get_user_element('vcode_error') == None:
            print('注册成功')
        else:
            while self.get_user_element('vcode_error') != None:
                print('注册失败，再次尝试')
                self.get_user_element('verification_code').clear()
                time.sleep(5)
                vcoder = self.analyze(imgfile)
                # self.driver.save_screenshot('tmp/reg_fail%s.png' % (int(time.time())))
                self.send_user_info('verification_code', vcoder)
                self.get_user_element('regbtn').click()
            print('注册成功')

        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    url="http://www.5itest.cn/register"
    for i in range(3):
        regfunc=RegisterFunc(url, i)
        regfunc.main()
