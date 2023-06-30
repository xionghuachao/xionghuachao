from time import sleep

import pytest


from page.LeftMenuPage import LeftMenuPage
from page.Loginpage import LoginPage
from page.OrderPage import OrderPage

# tab_lsit=["全部","待付款","待发货","运输中","待确认","待评价"]
tab_lsit=["全部","待付款"]
class  Test_Order_tab:
    @pytest.mark.parametrize("tab",tab_lsit)
    def test_order_tab(self,driver,tab):
        """
        点击已买到宝贝的tab页
        :return:
        """
        # driver=DriverConfig().get_driver("chrome")
        LoginPage().login(driver)
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"我的订单")
        sleep(2)
        LeftMenuPage().click_level_two_menu(driver,"已买到的宝贝")
        OrderPage().click_tab(driver, tab)
        sleep(2)






        driver.quit()
if __name__=="__main__":
    pytest.main()
