from time import sleep

import allure

from common.report_add_img import add_img_2_report
from common.yaml_config import GetConf
from config.driver_config import DriverConfig
from page.ExteralPage import ExteralPage
from page.Loginpage import LoginPage


class TestWindowHandle:
    @allure.description("窗口句柄")
    @allure.epic("登录")
    @allure.feature("登录失败")
    # @allure.story("story")
    # @allure.tag("tag")
    def test_switch_window(self,driver):
       # driver=DriverConfig().get_driver("chrome")
       driver.maximize_window()
       LoginPage().login(driver)
       sleep(3)
       with allure.step("断言title"):
          title = ExteralPage().goto_imooc(driver)
          print(title)
          assert title == "慕课网-程序员的梦工厂"

    @allure.description("登录")
    @allure.epic("登录")
    @allure.feature("登录成功")

    # @allure.tag("tag2")
    def test_switch_window1(self, driver):
        # driver=DriverConfig().get_driver("chrome")
        driver.maximize_window()
        LoginPage().login(driver)
        sleep(3)
        with allure.step("断言title"):
            title = ExteralPage().goto_imooc(driver)
            print(title)
            assert title == "慕课网-程序员的梦工厂"





