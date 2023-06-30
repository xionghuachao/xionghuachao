#显示等待
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from testcases.conftest import driver
#两种方式until和until not，元素等待成功则返回该元素对象
element=WebDriverWait(driver,10,0.5).until(
    lambda el: driver.find_element('xpath','//*[@id="z1"]/h3'),message="显示等待查找失败"
)
#alert弹窗浏览器本身的弹窗
#切换到弹窗
driver=webdriver.Chrome()
alert=driver.switch_to.alert
alert.acept()
alert.dismiss()
#需要输入文本信息
alert.send_keys("需要输入的文本信息")
text=alert.text
