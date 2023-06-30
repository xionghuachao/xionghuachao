from selenium.webdriver.common.by import By

from common.yaml_config import GetConf
from config.driver_config import DriverConfig


class BasePage:

    element=None
    def __init__(self,driver):

        self.driver=driver


    def get_element(self, key):

        i = 0;

        flag = True


        while (flag):
            try:

                self.element=self.driver.find_element(self.login_input())

                flag = False

            except Exception as e:
                i = i + 1
                if i == 10:
                    flag = False
        return  self.element

    def login_input(self, key):
        dict_c = GetConf().load_file("D:\\web\\config\\element.yaml")
        data=dict_c[key]
        for i in data:
            if i == 'id':
                return By.ID,data[i]

            elif i == 'name':
                return By.NAME
            elif i == 'classname':
                return self.driver.find_element_by_class_name(data[i])
            elif i == 'tagname':
                return self.driver.find_element_by_tag_name(data[i])
            elif i == 'xpath':
                return By.XPATH,data[i]
            elif i == 'linktext':
                return self.driver.find_element_by_link_text(data[i])

            else:
                raise Exception("没有找到元素,定位方式"+i,"定位表达式"+data[i])



if  __name__=="__main__":
   print(1)



