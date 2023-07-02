from time import sleep

import pytest

from config.driver_config import DriverConfig



class TestPytest:
    @pytest.fixture()
    def driver(self):
        get_driver=DriverConfig().get_driver("chrome")
        return get_driver
    @pytest.fixture(scope='class')
    def scope_class(self):
        print("我只运行一次")
    @pytest.mark.bing
    def test_open_bing(self,driver):
        # driver=DriverConfig().get_driver("chrome")
        driver.get("https://cn.bing.com")
        sleep(3)
        driver.quit()
    @pytest.mark.baidu
    def test_open_baidu(self,driver):
        # driver = DriverConfig().get_driver("chrome")
        driver.get("https://www.baidu.com")
        sleep(3)
        driver.quit()
