from time import sleep

from config.driver_config import DriverConfig
from page.AccountPage import AccountPage
from page.LeftMenuPage import LeftMenuPage
from page.Loginpage import LoginPage


class TestPersonalInfo:
    def test_upload_personal(self,driver):
        # driver=DriverConfig().get_driver("chrome")
        LoginPage().login(driver)
        LeftMenuPage().click_level_one_menu(driver,"账户设置")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"个人资料")
        sleep(2)
        AccountPage().upload_avatar(driver,"2.jpg")
        sleep(3)
        AccountPage().click_save(driver)
        driver.quit()
