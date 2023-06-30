class GoodsBase:
    def goods_title(self):
        """
        商品标题
        :return:
        """
        return  "//div[@class='el-textarea el-input--mini el-input--suffix']//textarea[@placeholder='请输入商品标题']"
    def goods_details(self):
        """
        商品详情
        :return:
        """
        return  "//div[@class='el-textarea el-input--mini el-input--suffix']//textarea[@placeholder='请输入商品详情']"
    def goods_num(self,plus=True):
        """
                商品详情
                ：param plus:如果为True,则为使用加号，为false则为直接输入数量
                :return:
                """
        if plus:
            return "//span[@class='el-input-number__increase']"
        else:
            return "//*[@id='app']//input[@placeholder='商品数量']"
    def goods_img(self):
        """
        商品图片
        :return:
        """
        return "//input[@type='file']"
    def goods_price(self):
        """
        商品单价
        :return:
        """
        return "//input[@placeholder='请输入商品单价']"
    def goods_status(self):
        """
        商品状态
        :return:
        """
        return "//input[@placeholder='请选择商品状态']"
    def goods_status_select(self,select_name):
        """
        选则商品状态
        :param select_name:上架或下架
        :return:
        """
        return "//span[text()='"+select_name+"']/parent::li"
    def add_goods_botton(self,select_name):
        """
        提交商品信息
        :param select_name: 提交或者重置
        :return:
        """
        return "//span[text()='"+select_name+"']/parent::button"










