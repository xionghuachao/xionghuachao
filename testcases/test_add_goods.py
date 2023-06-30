import pytest

from config.driver_config import DriverConfig
from page import LeftMenuPage
from page.Loginpage import LoginPage
from page.LeftMenuPage import LeftMenuPage
from page.GoodsPage import GoodsPage
from time import sleep
goods_info=[
    {
            "goods_title":"新增商品测试1",
            "goods_details":"新增测试商品详情1",
            "goods_num":1,
            "goods_pic_list":["2.jpg"],
            "goods_price":123,
            "goods_status":"上架",
            "goods_button":"提交"
           },{
            "goods_title":"新增商品测试2",
            "goods_details":"新增测试商品详情1",
            "goods_num":1,
            "goods_pic_list":["2.jpg"],
            "goods_price":123,
            "goods_status":"上架",
            "goods_button":"提交"
           }]



class TestAddGoods:
    @pytest.mark.parametrize("goods_info",goods_info)
    def test_add_goods_001(self,driver,goods_info):
        # driver=DriverConfig().get_driver("chrome")
        driver.maximize_window()

        sleep(3)
        LoginPage().login(driver)
        sleep(3)
        LeftMenuPage().click_level_one_menu(driver,"产品")
        sleep(1)
        LeftMenuPage().click_level_two_menu(driver,"新增二手商品")
        sleep(2)
        GoodsPage().add_new_goods(
            driver,
            goods_title=goods_info["goods_title"],
            goods_details=goods_info["goods_details"],
            goods_num=goods_info["goods_num"],
            goods_pic_list=goods_info["goods_pic_list"],
            goods_price=goods_info["goods_price"],
            goods_status=goods_info["goods_status"],
            goods_button=goods_info["goods_button"]

        )
        sleep(3)
        driver.quit()


