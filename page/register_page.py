from base.find_element import FindElement


class RegisterPage(object):
    def __init__(self, driver) -> None:
        self.get_ele = FindElement(driver)

    def get_email_element(self):
        return self.get_ele.get_element('user_email')

    def get_username_element(self):
        return self.get_ele.get_element('user_name')

    def get_password_element(self):
        return self.get_ele.get_element('user_password')

    def get_vcode_element(self):
        return self.get_ele.get_element('verification_code')

    def get_click_button_element(self):
        return self.get_ele.get_element('regbtn')

    def get_email_error_element(self):
        return self.get_ele.get_element('user_email_error')

    def get_name_error_element(self):
        return self.get_ele.get_element('user_name_error')

    def get_password_error_element(self):
        return self.get_ele.get_element('user_password_error')

    def get_vcode_error_element(self):
        return self.get_ele.get_element('vcode_error')
