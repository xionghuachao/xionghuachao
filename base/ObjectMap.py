import time
from selenium.common.exceptions import ElementNotVisibleException, WebDriverException,NoSuchElementException,StaleElementReferenceException


from selenium.webdriver.common.keys import Keys

from config.driver_config import DriverConfig


class ObjectMap:

    #获取基础地址

    def get_element(self, driver, locate_type, locator_expression, timeout=10, must_be_visible=False):
        """
        单个元素获取
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :param must_be_visible: 元素是否可见，True是必须可见，False默认值
        :return:
        """
        # 开始时间
        start_ms = time.time() * 1000
        # 结束时间
        stop_ms = start_ms + (timeout * 1000)
        print(stop_ms - start_ms)
        for x in range(int(timeout * 10)):
            # 查找元素
            try:
                element = driver.find_element(by=locate_type, value=locator_expression)
                # 如果元素不是必须可见的，就直接返回元素
                if not must_be_visible:
                    return element
                # 如果元素必须是可见的，则需要判断元素是否可见
                else:
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
            except Exception:
                now_ms = time.time() * 1000
                if now_ms >= stop_ms:
                    break

                pass
            time.sleep(0.1)
        raise ElementNotVisibleException("元素定位失败，定位方式：" + locate_type + "定位值：" + locator_expression)


    def wait_for_ready_state_complete(self, driver, timeout=30):

        start_ms = time.time() * 1000
        stop_ms = start_ms + (timeout * 1000)
        for x in range(int(timeout * 10)):
            try:
                # 获取页面状态
                ready_state = driver.execute_script("return document.readyState")
            except  WebDriverException:
                # 如果有driver的错误，执行js失败，就直接跳过
                time.sleep(0.03)
                return True
            # 如果页面元素全部加载完成，返回True
            if ready_state == "complete":
                time.sleep(0.01)
                return True
            else:
                now_ms = time.time() * 1000
                # 如果超时就break
                if now_ms >= stop_ms:
                    break
                    time.sleep(0.1)
        raise Exception("打开网页时,页面元素在%s秒后仍然没有加载完" % timeout)

    def element_disappear(self,driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素消失
        :param self: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression: 定位表达式
        :param timeout: 超时时间
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        now_ms = time.time() * 1000
                        if now_ms >= stop_ms:
                            break
                        time.sleep(0.1)

                except Exception:
                    return True
            raise Exception("元素没有消失，定位方式" + locate_type + "\n定位表达式" + locator_expression)
        else:
            pass

    def element_appear(self, driver, locate_type, locator_expression, timeout=30):
        """
        等待页面元素出现
        :param self:
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param timeout:
        :return:
        """
        if locate_type:
            # 开始时间
            start_ms = time.time() * 1000
            # 设置结束时间
            stop_ms = start_ms + (timeout * 1000)
            for x in range(int(timeout * 10)):
                try:
                    element = driver.find_element(by=locate_type, value=locator_expression)
                    if element.is_displayed():
                        return element
                    else:
                        raise Exception()
                except Exception:
                    now_ms = time.time() * 1000
                    if now_ms >= stop_ms:
                        break
                    time.sleep(0.1)
                    pass


            raise ElementNotVisibleException("元素没有出现，定位方式" + locate_type + "\n定位表达式" + locator_expression)
        else:
            pass




    def element_to_url(self,driver,url,locate_type_disappear=None,
                       locator_expression_disappear=None,
                       locate_type_appear=None,
                       locator_expression_appear=None):
        """
        挑战地址
        :param self:
        param url:跳转的地址
        :param driver: 浏览器驱动
        :param locate_type_disappear: 等待页面元素消失的定位方式
        :param locator_expression_disappear: 等待页面元素消失的定位表达式
        :param locate_type_appear: 等待页面元素出现的定位方式
        :param locator_expression_appear: 等待页面元素出现的定位表达式
        :return:
        """
        try:
            driver.get(url)
            #等待页面元素都加载完成
            self.wait_for_ready_state_complete(driver)
            #跳转地址后等待元素消失
            self.element_disappear(driver,
                                   locate_type_disappear,
                                   locator_expression_disappear)
            #跳转地址后等待元素出现
            self.element_appear(driver,locate_type_appear,locator_expression_appear)
        except Exception as e:
            print("跳转地址出现异常，异常原因：%s"%e)
            return False
        return True
    def element_is_diaplay(self,driver,locate_type,locator_expression):
        """

        :param self:
        :param driver:
        :param locate_type:
        :param locator_expression:
        :return:
        """
        try:
            driver.find_element(by=locate_type,value=locator_expression)
            return True
        except NoSuchElementException:
         #发生了NoSuchElementException异常，说明页面中未找到该元素，返回False
                return False
    def element_fill_value(self,driver,locate_type,locator_expression,fill_value,timeout=30):
        """

        :param self:
        :param driver: 浏览器驱动
        :param locate_type:定位方式
        :param locator_expression: 定位表达式
        :param fill_value:
        :param timeout:
        :return:
        """
        #元素必须先出现
        element=self.element_appear(
            driver,
        locate_type=locate_type,
        locator_expression=locator_expression,
        timeout=timeout)
        try:
            #清除原有值
            element.clear()
            #页面元素没有刷新出来就对元素进行捕获
        except StaleElementReferenceException  as e:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element=self.element_appear(
                driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout
            )
            try:
                element.clear()
            except:
                pass
        except Exception:
            pass
        #填入值转成字符串
        if type(fill_value) is int or type(fill_value) is float:
            fill_value=str(fill_value)
        try:
                #填入的值不是以\n结尾
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                #123\n
                fill_value=fill_value[:-1]
                element.send_keys(Keys.RETURN)
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element=self.element_appear( driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout)
            element.clear()
            if not fill_value.endswith("\n"):
                element.send_keys(fill_value)
                self.wait_for_ready_state_complete(driver=driver)
            else:
                #123\n
                fill_value=fill_value[:-1]
                element.send_keys(Keys.RETURN)
                self.wait_for_ready_state_complete(driver=driver)
        except Exception:
            raise Exception("元素填值失败")
        return True
    def element_click(self,driver,locate_type,locator_expression,
                      locate_type_disappear=None,
                      locator_expression_disappear=None,
                      locate_type_appear=None,
                      locator_expression_appear=None,
                      timeout=30

                      ):
        """
        元素点击
        :param self:
        :param driver: 浏览器驱动
        :param locate_type: 定位方式类型
        :param locator_expression:
        :param locate_type_disappear: 等待元素消失
        :param locator_expression_disappear:
        :param locate_type_appear: 等待元素出现的定位表达式
        :param locator_expression_appear:
        :return:
        """
        #元素可见
        element=self.element_appear(
            driver=driver,
            locate_type=locate_type,
            locator_expression=locator_expression,
            timeout=timeout
        )
        try:
            #点击元素
             element.click()
        except StaleElementReferenceException:
            self.wait_for_ready_state_complete(driver=driver)
            time.sleep(0.06)
            element=self.element_appear(
                driver=driver,
                locate_type=locate_type,
                locator_expression=locator_expression,
                timeout=timeout

            )
            element.click()
        except Exception as e:
             print("页面元素出现异常，元素不可点击",e)
             return False
        try:
            #点击后元素
            self.element_appear(
                driver,
                locate_type_appear,
                locator_expression_appear
            )
            self.element_disappear(
                driver,
                locate_type_disappear,
                locator_expression_disappear
            )
        except Exception as e:
            print("等待元素出现消失或出现失败",e)
            return False
        return True
    def upload(self,driver,locate_type,locator_expression,fill_path):
        """
        文件上传
        :param driver:
        :param locate_type:
        :param locator_expression:
        :param fill_path:
        :return:
        """
        element=self.get_element(driver,locate_type,locator_expression)
        return element.send_keys(fill_path)
    def switch_window_handle(self,driver):

        """
        句柄切换窗口到最新窗口
        :return: 
        """
        window_handles=driver.window_handles
        current_handle=driver.current_window_handle
        for  handle in window_handles:
            if handle!=current_handle:
                driver.switch_to.window(handle)
            else:
                continue
    def switch_iframe(self,driver,locate_iframe_type,locate_iframe_expression):
        """
        切换到iframe
        :param driver: 浏览器驱动
        :param locate_iframe_type:
        :param locate_iframe_expression:
        :return:
        """
        iframe_element=self.get_element(driver,locate_iframe_type,locate_iframe_expression)
        driver.switch_to_frame(iframe_element)
    def switch_from_iframe_to_content(self,driver):

        """
        从iframe切回主文档
        :param driver:
        :return:
        """
        driver.switch_to_default_content()
    def get_cookie(self, driver):

        cookies=driver.get_cookies()

        for cookie in cookies:
            if cookie['name']=='apsid':
                print("已经在登录状态")
            else:
                driver.delete_all_cookies()
                cookie = {"name":"apsid","value":"Y1NTE3MmUwMmE5OTM5NTE2MjRkZGQ2Yjk1Yjc4ZDUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOTQ1OTA1MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4MTgwNTgzNDI4NTZAMTYzLmNvbQAAAAAAAAAAAAAAADVlM2RmZDVlNWY4YTc5MDllYmZhY2VhZWMyOGQ5YjdhB%2ByWZFe7lWI%3DYj", "domain":".imooc.com", "path":"/"}
                driver.add_cookie(cookie)
                driver.refresh()
    def get_text(self,driver,locate_type,locate_expression):
        element=self.get_element(driver,locate_type,locate_expression)
        return  element.text













if __name__ == '__main__':
    ObjectMap().element_get()
