from selenium.webdriver.common.by import By

from base.ObjectMap import ObjectMap
from base.OrderBase import OrderBase


class OrderPage(ObjectMap,OrderBase):
    def click_tab(self,driver,tab_name):
        """

        :param driver:
        :return:
        """
        tab_xpath=self.order_tab(tab_name)
        return self.element_click(driver,By.XPATH,tab_xpath)
