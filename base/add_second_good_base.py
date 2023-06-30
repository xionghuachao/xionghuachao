from page.basepage import BasePage


class Add_goods(BasePage):
    #获取一级菜单-产品页面元素
    def get_product_element(self):
        return self.get_element("one_menu")
    #获取新增二手商品页面元素
    def get_goods_element(self):
        return self.get_element("one_menu")

