# -*- coding: UTF-8 -*-
from initialize.page.RegisterPage import RegisterPage
class LoginHandle(object):


    def __init__(self,driver):
        self.driver = driver
        self.register_page = RegisterPage(self.driver)


    #点击首页登录按钮
    def click_home_login(self):
        return self.register_page.click_home_login()

    #输入手机号码/或者邮箱输入
    def send_phone(self,value):
        print ("你输入的手机号码/邮箱是:"+value)
        return self.register_page.send_phone(value)

    #输入密码
    def send_password(self,value):
        print ("你输入的密码是:" + value)
        return self.register_page.send_password(value)

    #登录按钮
    def click_login_submit(self):
        return self.register_page.click_login_submit()



    def get_error_text(self,info):
    #错误的手机号码/或者邮箱输入框提示
        try:
            if info=="usr_phone_error":
                return self.register_page.get_error_phone_text()
            elif info=="usr_password_error":
                return self.register_page.get_element_password()
            else:
                print ("你输入的信息有误")
        except:
            return None




