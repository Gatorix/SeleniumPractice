from page.register_page import RegisterPage


class RegisterHandle(object):
    def __init__(self, driver) -> None:
        self.register_page = RegisterPage(driver)

    def send_user_email(self, email):
        self.register_page.get_email_element().send_keys(email)

    def send_user_name(self, username):
        self.register_page.get_username_element().send_keys(username)

    def send_password(self, password):
        self.register_page.get_password_element().send_keys(password)

    def send_verification_code(self, vcode):
        self.register_page.get_vcode_element().send_keys(vcode)

    def get_ver_text(self, info, user_info):
        try:
            if info == 'user_email_error':
                text = self.register_page.get_email_error_element().text
            elif info == 'user_name_error':
                text = self.register_page.get_name_error_element().text
            elif info == 'user_password_error':
                text = self.register_page.get_password_error_element().text
            elif info == 'vcode_error':
                text = self.register_page.get_vcode_error_element().text
        except:
            text = None
        return text

    def click_register_button(self):
        self.register_page.get_click_button_element()

    def get_register_text(self):
        return self.register_page.get_click_button_element().text
