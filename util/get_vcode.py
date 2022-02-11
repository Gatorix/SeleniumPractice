
from selenium.webdriver.common.by import By
from PIL import Image
from util.analyze import analyze


class GetVcode():
    def __init__(self, driver) -> None:
        self.driver = driver

    def get_verification_img(self, driver):
        driver.save_screenshot(r'.\tmp\test.png')
        code_element = driver.find_element(By.ID, "getcode_num")
        left = code_element.location['x']+202
        top = code_element.location['y']+132
        right = code_element.size['width']+left+20
        bottom = code_element.size['height']+top+10
        saved_img = Image.open(r'.\tmp\test.png')
        verification_img = saved_img.crop((left, top, right, bottom))
        verification_img.save(r'.\tmp\verification_img.png')

    def alze(self, file_name):
        analyze(file_name)
