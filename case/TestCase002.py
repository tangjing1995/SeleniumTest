# -*- coding: UTF-8 -*-
import unittest
from webdriver.SeleniumDriver import SeleniumDriver
class TestCase002(object):
    pass


if __name__ == '__main__':
    driver = SeleniumDriver(SeleniumDriver.Chrome)
    driver.open_url_is_true("https://www.baidu.com/","百度一下")
    driver.click_element("phone")