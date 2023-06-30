import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class DriverConfig:

    #@pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(self,item, call):
        # 什么时候去识别用例的执行结果，后置处理
        outcome = yield
        rep = outcome.get_result()
        if rep.when == 'call' and rep.failed:
            img =self.driver.get_screenshot_as_png()
            allure.attach(img, '失败截图', allure.attachment_type.PNG)
            # 在这里实现失败的截图和添加allure附件
            # 截图方法需要driver对象


    def get_driver(self,browser):

        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            # 设置窗口大小，设置为1920*1080
            options.add_argument("window-size=1920,1080")
            # 去除"chrome正受到自动测试软件的控制"的提示
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            # 解决selenium无法访问https的问题
            options.add_argument("--ignore-certificate-errors")
            # 允许忽略localhost上的TLS/SSL错误
            options.add_argument("--allow-insecure-localhost")
            # 设置为无痕模式
            options.add_argument("--incognito")
            # 设置为无头模式
            # options.add_argument("--headless")
            # 解决卡顿
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

            driver = webdriver.Chrome(ChromeDriverManager(url="https://registry.npmmirror.com/-/binary/chromedriver",
                                                          latest_release_url="https://registry.npmmirror.com/-/binary/chromedriver/LATEST_RELEASE",
                                                          cache_valid_range=365).install(),
                                      options=options)
            # 删除所有cookies
            driver.delete_all_cookies()

        """
                   浏览器驱动
                   :return:
                   """

        if browser=='firfox':
            driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())



        return driver






