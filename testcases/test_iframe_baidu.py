from time import sleep

from base.IframBaiduMapBase import IframeBaiduMapBase
from config.driver_config import DriverConfig
from page.IframeBaiduMapPage import IframeBaiduMapPage
from page.LeftMenuPage import LeftMenuPage
from page.Loginpage import LoginPage


class TestIframeBadduMap:
    def test_iframe_baidu_map(self,driver):
        # driver=DriverConfig().get_driver("chrome")
        LoginPage().login(driver)
        sleep(1)
        LeftMenuPage().click_level_one_menu(driver, "iframe测试")
        sleep(5)
        IframeBaiduMapPage().switch_baidu_map(driver)
        IframeBaiduMapPage().click_search(driver)
        IframeBaiduMapPage().iframe_out(driver)
        LeftMenuPage().click_level_one_menu(driver, "首页")
        sleep(3)
        driver.quit()
