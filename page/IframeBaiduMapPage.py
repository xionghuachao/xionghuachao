from selenium.webdriver.common.by import By

from base.IframBaiduMapBase import IframeBaiduMapBase
from base.ObjectMap import ObjectMap


class IframeBaiduMapPage(ObjectMap,IframeBaiduMapBase):
    def click_search(self,driver):
        """
        定位搜索
        :return:
        """
        search_xpath=self.search_button()
        return self.element_click(driver,By.XPATH,search_xpath)
    def switch_baidu_map(self,driver):
        """
        切换到百度地区iframe
        :param driver:
        :return:
        """
        iframe_xpath=self.baidu_map_iframe()
        return self.switch_iframe(driver,By.XPATH,iframe_xpath)
    def iframe_out(self,driver):
        """
        从百度退出iframe
        :param driver:
        :return:
        """
        return self.switch_from_iframe_to_content(driver)
