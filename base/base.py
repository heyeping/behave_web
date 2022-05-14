"""
@Time ： 2022/5/8 12:44
@Auth ： heyeping
@File ：base.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class Base:

    def base_find_elem(self, driver, loc, timeout=10, poll=0.5):
        """
        使用显式等待 查找元素
        :param loc: 定位器
        :param timeout:
        :param poll:
        :return:
        """
        return WebDriverWait(driver,
                             timeout=timeout,
                             poll_frequency=poll).until(
            lambda x: x.find_element(*loc))  # *locator的意思是传入参数时候自行以元祖形式解析,控制台打印这段代码意思是没有找到相关元素

    # 访问URL
    def get_url(self, driver, url):
        # self.driver.maximize_window()
        driver.get(url)

    # 释放资源
    def quit(self, driver):
        time.sleep(3)
        driver.quit()

    # 点击元素方法
    def base_click(self, driver, loc):
        self.base_find_elem(driver, loc).click()

    # 输入元素方法
    def base_input(self, driver, loc, value):
        elem = self.base_find_elem(driver,loc)
        elem.clear()
        elem.send_keys(str(value))

    # 元素键盘操作,keys是复制或粘贴，此处应填写'c'or'v'
    def base_keys(self, driver, loc, keys):
        elem = self.base_find_elem(driver,loc)
        elem.clear()
        elem.send_keys(Keys.COMMAND, str(keys))

    # 获取某处文本信息，使用命令复制并返回内容的方法
    def base_get_text(self, driver, loc):
        text = self.base_find_elem(driver, loc).text
        os.system("echo '%s' | pbcopy" % text)
        return text

    # 截图方法
    def base_get_image(self, driver):
        driver.get_screenshot_as_file('../image/{}.png'.format(time.strftime('%Y_%m_%d %H_%M_%S')))

    # 判断元素是否存在
    def base_elem_is_exist(self, driver, loc):
        try:
            self.base_find_elem(driver, loc, timeout=2)
            return True
        except:
            return False

    # 判断文本是否包含value
    def base_link_text_is_exist(self, driver, value):
        try:
            driver.find_element_by_link_text(value)
            return True
        except:
            return False