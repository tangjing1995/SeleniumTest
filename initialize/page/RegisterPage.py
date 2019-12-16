# -*- coding: UTF-8 -*-
# from webdriver.SeleniumDriver import SeleniumDriver
class RegisterPage(object):

    def __init__(self,driver):
        self.driver = driver
        # self.driver = SeleniumDriver(SeleniumDriver.Chrome)

    #点击首页登录按钮
    def click_home_login(self):
        return self.driver.click_element("phone")

    #输入手机号码/或者邮箱输入
    def send_phone(self,vaule):
        return self.driver.send_value("phone",vaule)

    #输入密码
    def send_password(self,value):
        return self.driver.send_value("password",value)

    #登录按钮
    def click_login_submit(self):
        return self.driver.click_element("login_submit")

    #错误的手机号码/或者邮箱输入框提示
    def get_error_phone_text(self):
        return self.driver.get_element_text("phone_error")

    #错误的密码提示
    def get_element_password(self):
        return self.driver.get_element_text("password_error")