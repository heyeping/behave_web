"""
@Time ： 2022/5/8 12:52
@Auth ： heyeping
@File ：baidu_search_steps.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import time
from behave import *

@given("关键字:{words}")
def step_impl(context, words):  # context是上下文对象，有参数的话，加上对应参数
    context.words = words  # 将参数绑定上下文对象，以便其他步骤使用


@when("打开百度页面:{url}")
def step_impl(context, url):
    context.BaiduPage.get_url(context.drivers.driver1, url)
    time.sleep(1)


@when("输入关键字")
def step_impl(context):
    context.BaiduPage.input_wd(context.drivers.driver1, context.words)
    time.sleep(0.5)


@when("点击百度一下按钮")
def step_impl(context):
    context.BaiduPage.click_su(context.drivers.driver1)
    time.sleep(0.5)


@then("页面中应包含关键字:{keyword}")
def step_impl(context, keyword):
    context.BaiduPage.exist_word(context.drivers.driver1, keyword)
    time.sleep(2)




@when("{key} 打开百度页面:{url}")
def step_impl(context, key, url):
    driver = context.drivers.driver1 if key == '浏览器1' else context.drivers.driver2
    context.BaiduPage.get_url(driver, url)
    time.sleep(1)


@when("{key} 输入关键字 {value}")
def step_impl(context, key,value):
    driver = context.drivers.driver1 if key == '浏览器1' else context.drivers.driver2
    context.BaiduPage.input_wd(driver, value)
    time.sleep(0.5)


@when("{key} 点击百度一下按钮")
def step_impl(context, key):
    driver = context.drivers.driver1 if key == '浏览器1' else context.drivers.driver2
    context.BaiduPage.click_su(driver)
    time.sleep(0.5)

@then("{key} 页面中应包含关键字:{keyword}")
def step_impl(context, key, keyword):
    driver = context.drivers.driver1 if key == '浏览器1' else context.drivers.driver2
    context.BaiduPage.exist_word(driver, keyword)
    time.sleep(2)

@then("页面中应包含关键词{keyword}")
def step_impl(context, keyword):
    context.BaiduPage.exist_word(keyword)
    time.sleep(2)