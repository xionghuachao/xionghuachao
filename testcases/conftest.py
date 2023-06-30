import pytest

from config.driver_config import DriverConfig
from common.report_add_img import add_img_2_report
@pytest.fixture
def driver():
    global get_driver
    get_driver=DriverConfig().get_driver("chrome")
    yield get_driver
    get_driver.quit()
@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    #获取钩子方法的调用结果
    out=yield
    #从钩子方法的调用结果获取测试报告
    report=out.get_result()
    report.description=str(item.function.__doc__)
    if report.when=="call":
        if report.failed:
            #失败了截图
            add_img_2_report(get_driver,"失败截图",need_sleep=False)



