from time import sleep

from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap


class ExteralPage(ObjectMap,LeftMenuBase):
    def goto_imooc(self,driver):
        """
        切换窗口为慕课网
        :param driver:
        :return:
        """
        wailian=self.click_wailian()
        self.element_click(driver,By.XPATH,wailian)
        sleep(2)
        self.switch_window_handle(driver)
        return driver.title
    def get_more_cookies(self,driver):
        self.get_cookie(driver)