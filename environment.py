"""
@Time ： 2022/4/17 16:53
@Auth ： heyeping
@File ：environment.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from selenium import webdriver
import time
import os
import shutil

from base.driver_init import driverInit
from page.baidu_page import BaiduPage


def before_scenario(context, feature):
    context.drivers = driverInit(index=2)

    context.BaiduPage = BaiduPage()


def after_scenario(context, feature):
    context.drivers.quits()

