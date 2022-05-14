"""
@Time ： 2022/5/8 12:51
@Auth ： heyeping
@File ：baidu_page.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium.webdriver.common.by import By
from base.base import Base


class BaiduPage(Base):
    elem_input_wd = (By.NAME, "wd")  # 百度首页输入框
    elem_click_su = (By.ID, "su")  # 百度一下按钮

    def input_wd(self, driver, words):
        self.base_input(driver, self.elem_input_wd, words)

    def click_su(self, driver):
        self.base_click(driver, self.elem_click_su)

    # 判读link_text中是否包含关键词本文
    def exist_word(self, driver, word):
        self.base_link_text_is_exist(driver, word)

