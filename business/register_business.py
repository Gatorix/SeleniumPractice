from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver) -> None:

        self.register_hd = RegisterHandle(driver)

    def register_base(self, email, name, password, vcode):
        self.register_hd.send_user_email(email)
        self.register_hd.send_user_name(name)
        self.register_hd.send_password(password)
        self.register_hd.send_verification_code(vcode)
        self.register_hd.click_register_button()

    def register_success(self):
        if self.register_hd.get_register_text() == None:
            return True
        else:
            return False

    def register_email_error(self, email, name, password, vcode):
        self.register_base(email, name, password, vcode)
        if self.register_hd.get_ver_text('user_email_error', '请输入有效的电子邮件地址') == None:
            return True
        else:
            return False

    def register_name_error(self, email, name, password, vcode):
        self.register_base(email, name, password, vcode)
        if self.register_hd.get_ver_text('user_name_error', '字符长度必须大于等于4，一个中文字算2个字符') == None:
            return True
        else:
            return False

    def register_password_error(self, email, name, password, vcode):
        self.register_base(email, name, password, vcode)
        if self.register_hd.get_ver_text('user_password_error', '最少需要输入 5 个字符') == None:
            return True
        else:
            return False

    def register_vcode_error(self, email, name, password, vcode):
        self.register_base(email, name, password, vcode)
        if self.register_hd.get_ver_text('vcode_error', '验证码错误') == None:
            return True
        else:
            return False
