from time import sleep

from base.GoodsBase import GoodsBase
from base.ObjectMap import ObjectMap
from selenium.webdriver.common.by import By

from common.tools import get_img_path


class GoodsPage(GoodsBase,ObjectMap):
    def input_goods_title(self,driver,input_value):
        """
        输入商品标题
        :param input_value:
        :return:
        """
        goods_title=self.goods_title()
        return self.element_fill_value(driver,By.XPATH,goods_title,input_value)
    def input_goods_details(self,driver,input_value):
        """
        输入商品详情
        :param driver:
        :param input_value:
        :return:
        """
        goods_detail_xpath=self.goods_details()
        return self.element_fill_value(driver,By.XPATH,goods_detail_xpath,input_value)
    def select_goods_num(self,driver,num):
        """
        选择商品数量
        :param driver:
        :param num:
        :return:
        """
        goods_num_xpath=self.goods_num(plus=True)
        for i in range(int(num)):
            self.element_click(driver,By.XPATH,goods_num_xpath)
            sleep(0.5)
    def upload_goods_img(self,driver,img_name):
        """
        上传商品图片
        :param driver:
        :param img_name:
        :return:
        """
        img_xpath=get_img_path(img_name)
        upload_xpath=self.goods_img()
        return self.upload(driver,By.XPATH,upload_xpath,img_xpath)
    def input_goods_price(self,driver,input_value):
        """
        输入商品单价
        :param driver:
        :param input_value:
        :return:
        """
        price_xpath=self.goods_price()
        return self.element_fill_value(driver,By.XPATH,price_xpath,input_value)
    def click_goods_state(self,driver,select_name):
        """
        选择商品状态
        :return:
        """
        state_xpath=self.goods_status()
        self.element_click(driver,By.XPATH,state_xpath)
        sleep(1)
        state_up_xpath=self.goods_status_select(select_name)
        return self.element_click(driver, By.XPATH,state_up_xpath)
    def  submit_goods(self,driver,select_name):
        """
        提交或重置商品信息
        :param driver:
        :param select_name:
        :return:
        """
        submit_xpath=self.add_goods_botton(select_name)
        return self.element_click(driver,By.XPATH,submit_xpath)
    def add_new_goods(self,driver,goods_title,goods_details,goods_num,goods_pic_list,goods_price,goods_status,goods_button):
        """
        新增二手商品
        :param driver:
        :param goods_title:
        :param goods_details:
        :param goods_num:
        :param goods_pic_list:
        :param goods_price:
        :param goods_status:
        :param goods_button:
        :return:
        """
        self.input_goods_title(driver,goods_title)
        self.input_goods_details(driver,goods_details)
        self.select_goods_num(driver,goods_num)
        for goods_pic in goods_pic_list:
            self.upload_goods_img(driver, goods_pic)
            sleep(5)
        self.input_goods_price(driver, goods_price)
        self.click_goods_state(driver,goods_status)
        self.submit_goods(driver, goods_button)
        return True












