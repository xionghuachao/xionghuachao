from selenium.webdriver.common.by import By

from base.LeftMenuBase import LeftMenuBase
from base.ObjectMap import ObjectMap


class LeftMenuPage(LeftMenuBase,ObjectMap):
    def click_level_one_menu(self,driver,menu_name):
        """
        点击一级菜单
            """
        menu_xpath=self.level_one_menu(menu_name)
        return self.element_click(driver,By.XPATH,menu_xpath)
    def click_level_two_menu(self,driver,menu_name):
        menu_xpath=self.level_two_menu(menu_name)
        return self.element_click(driver,By.XPATH,menu_xpath)
    



