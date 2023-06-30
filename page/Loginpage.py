import time


import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 导包等待的对象
from selenium.webdriver.support import expected_conditions as EC, expected_conditions  # 导包等待的条件的集合包，并设置别名
from base.LoginBase import LoginBase
from base.ObjectMap import ObjectMap
from common.yaml_config import GetConf
from config.driver_config import DriverConfig
from logs.log import  log


class LoginPage(ObjectMap,LoginBase):

    def login_input_value(self, driver, input_placeholder, input_value):
        """
        登录页输入值
        :param driver:
        :param input_placeholder:
        :param input_value:
        :return:
        """

        input_xpath = self.login_input(input_placeholder)
        # return driver.find_element_by_xpath(input_xpath).send_keys(input_value)
        return self.element_fill_value(driver, By.XPATH, input_xpath, input_value)

    def click_login(self, driver, button_name):
        """
        点击登录
        :param driver:
        :param button_name:
        :return:
        """
        log.info("点击登录")
        button_xpath = self.login_button(button_name)
        # return driver.find_element_by_xpath(button_xpath).click()
        return self.element_click(driver, By.XPATH, button_xpath)

    def login(self, driver):
        """
        登录
        :param driver:
        :param user:
        :param need_captcha:
        :return:
        """
        data=GetConf().load_file("D:\web\config\environment.yaml")
        url=data["url"]
        self.element_to_url(driver,url)
        username=data["username"]
        password=data["password"]
        self.login_input_value(driver,"用户名",username)
        self.login_input_value(driver, "密码", password)
        self.click_login(driver,"登录")

        # self.assert_login_success(driver)

    def login_fail(self, driver):
        """
        登录
        :param driver:
        :param user:
        :param need_captcha:
        :return:
        """
        data=GetConf().load_file("D:\web\config\environment.yaml")
        url=data["url"]
        self.element_to_url(driver,url)
        username=data["username"]
        password=data["password1"]
        self.login_input_value(driver,"用户名",username)
        self.login_input_value(driver, "密码", "2")
        self.click_login(driver,"登录")



    def login_assert(self, driver, img_name):
        """
        登录后判断头像
        :param driver:
        :param img_name:
        :return:
        """

        return self.find_img_in_source(driver, img_name)

    def assert_login_success(self, driver):
        """
        验证是否登录成功
        :param driver:
        :return:
        """
        # driver.switch_to_alert()
        print("----")
        success_xpath=self.login_success()




        # locator =("xpath",success_xpath)

        # login_element=self.get_element(driver,By.XPATH,success_xpath)
        # login_element=WebDriverWait(driver, 10, 0.5).until(EC.presence_of_element_located(locator))
        login_element = WebDriverWait(driver, 10, 0.5).until(
            lambda el: driver.find_element("xpath",success_xpath ), message="显示等待查找失败"
        )
        print(login_element)
        login_text=login_element.text
        assert login_text=="登录成功"



    def select_need_captcha(self, driver):
        """
        点击勾选是否需要验证码
        :param driver:
        :return:
        """
        log.info("点击勾选是否需要验证码")
        select_xpath = self.need_captcha()
        return self.element_click(driver, By.XPATH, select_xpath)