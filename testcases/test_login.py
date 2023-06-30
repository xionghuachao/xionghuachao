from time import sleep

import allure
import pytest

from common.yaml_config import GetConf
from page.ExteralPage import ExteralPage
from page.Loginpage import LoginPage
from common.report_add_img import add_img_2_report

from config.driver_config import DriverConfig


class Testlogin:

    @allure.epic("登录")
    @allure.feature("输入正确账号密码，测试登录是否成功")
    @allure.description("测试登录成功")
    def test_login(self,driver):
        """
        使用正确的账号登录
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login(driver)



        with allure.step("断言登录后文本为登录成功"):
            login_text=LoginPage().assert_login_success(driver)
    @allure.epic("登录")
    @allure.feature("用户名为空时，测试是否登录失败")
    @allure.description("用户名为空，密码正确输入，测试是否登录失败")
    def test_login_fail(self, driver):
        """
        使用正确的账号登录
        :param driver:
        :return:
        """
        with allure.step("登录"):
            LoginPage().login_fail(driver)
        with allure.step("断言登录后文本为登录成功"):
            login_text = LoginPage().assert_login_success(driver)



if __name__ == "__main__":
    pytest.main(['-s', '-v'])
