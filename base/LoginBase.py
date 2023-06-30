class LoginBase:

    def login_input(self, input_placeholder):
        """
        登录用户名、密码输入框
        :param input_placeholder:
        :return:
        """
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        """
        登录按钮
        :param button_name:
        :return:
        """
        return "//span[text()='" + button_name + "']/parent::button"

    def login_success(self):
        """
        登录成功
        :return:
        """
        return '//p[text()="登录成功"]'

    def need_captcha(self):
        """
        是否需要验证码的单选框
        :return:
        """
        return "//span[contains(text(),'是否需要验证码')]/preceding-sibling::span/span"

    def captcha(self):
        """
        验证码
        :return:
        """
        return "//div[@class='el-image']"

    def input_captcha(self):
        print(1)
        """
        输入验证码的输入框
        :return:
        """
        return ""

    # def login_success(self):
    #     """
    #     登录成功
    #     :return:
    #     """
if __name__ == "__main__":
    # input_captcha();
    print("111111111")
    print(LoginBase().login_success())
    print("22222222222222")

