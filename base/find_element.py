import sys
sys.path.append(r'C:\Users\Gatorix\Documents\SeleniumPractice')
from util.read_config import ReadConfig
from selenium.webdriver.common.by import By


class FindElement(object):
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_element(self, key):
        readconf = ReadConfig()
        data = readconf.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]

        try:
            if by == "id":
                return self.driver.find_element(By.ID, value)
            elif by == "name":
                return self.driver.find_element(By.NAME, value)
            elif by == "class_name":
                return self.driver.find_element(By.CLASS_NAME, value)
            elif by == "xpath":
                return self.driver.find_element(By.XPATH, value)
            else:
                return None
        except:
            return None
