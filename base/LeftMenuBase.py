class LeftMenuBase:

    def level_one_menu(self, menu_name):
        """
        一级菜单栏
        :param menu_name: 菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/ancestor::li"

    def level_two_menu(self, menu_name):
        """
        二级菜单栏
        :param menu_name: 菜单栏名称
        :return:
        """
        return "//aside[@class='el-aside']//span[text()='" + menu_name + "']/parent::li"
    def click_wailian(self):
         """
         点击外部链接
         :return:
         """
         return "//span[text()='外链']//parent::li"



if __name__ == '__main__':
    # print(LeftMenuBase().level_one_menu("产品"))
    print(LeftMenuBase().level_two_menu("我的商品列表"))