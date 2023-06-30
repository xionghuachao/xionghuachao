from selenium.webdriver.common.by import By

from common.yaml_config import GetConf
from config.driver_config import DriverConfig


class Page:
    def login_input(self):
        data=GetConf().load_file("D:\web\config\environment.yaml")
        print(data['url'])

    # def test1(self):
    #     self.driver = DriverConfig().get_driver("chrome")
    #     self.driver.get("http://www.tcpjwtester.top/login?url=%2F")
    #     return self.driver.find_element_by_xpath("//input[@placeholder='用户名']")

if  __name__=="__main__":
    Page().login_input()












