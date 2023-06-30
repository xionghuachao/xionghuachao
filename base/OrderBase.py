class OrderBase:

    def order_tab(self,tab_name):
        """
        订单tab按钮
        :param tab_name: 全部，待付款，代发货，运输中，待确认，待评价
        :return:

        """
        return "//div[@role='tab' and text()='"+tab_name+"']"

