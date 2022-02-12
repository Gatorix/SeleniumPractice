from xml.sax.handler import DTDHandler
from pydoc import classname
import sys
import time
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
sys.path.append(r'\\mac\Home\Documents\SeleniumPractice')
from HtmlTestRunner import HTMLTestRunner
import unittest
from business.register_business import RegisterBusiness
from log.user_log import UserLog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


import ddt
import unittest


@ddt.ddt
class DdtTest(unittest.TestCase):
    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')
    @ddt.data(
        [1,2],
        [3,4],
        [5,6]
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__=='__main__':
    unittest.main()
