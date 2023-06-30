from config.driver_config import DriverConfig
from page.ExteralPage import ExteralPage


class test_cookies:
    def test_login(self,driver):

        driver.get("https://www.imooc.com/")
        ExteralPage().get_more_cookies(driver)
