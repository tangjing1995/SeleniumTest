# -*- coding: UTF-8 -*-
from selenium import webdriver
from utlis.read_res.Read_ini import read_ini
from utlis.read_res.Read_json import read_json
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver.WebDriverWait import WebDriverWait
# from pykeyboard import PyKeyboard
from PIL import Image
from utlis.file.FileUtil import file_utils
import time

class ElementUtlis(object):


    def __init__(self,browser,File_Download_Path,configuration_file_download):
        self.driver = self.__open_browser(browser,File_Download_Path,configuration_file_download)
        # self.pkb = PyKeyboard()

    '''
   
    打开浏览器
    chrome:
        #download.default_directory：设置下载路径
        #profile.default_content_settings.popups：设置为 0 禁止弹出窗口
    firefox:
        browser.download.dir：指定下载路径
        browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
        browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
        browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问

    '''

    def __open_browser(self,browser,File_Download_Path,configuration_file_download):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if configuration_file_download:
                prefs = {"profile.default_content_settings.popups": 0, "download.default_directory": File_Download_Path}
                options.add_experimental_option("prefs",prefs)
            driver = webdriver.Chrome(executable_path=file_utils.location_file("config/drive/chromedriver.exe"),options=options)
        elif browser== "firefox":
            options = webdriver.FirefoxOptions()
            if configuration_file_download:
                options.set_preference("browser.download.dir",File_Download_Path)
                options.set_preference("browser.download.folderList", "2")
                options.set_preference("browser.download.manager.showWhenStarting", False)
                options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
            driver = webdriver.Firefox(executable_path=file_utils.location_file("config/drive/geckodriver.exe"),options=options)
        elif browser== "ie":
            driver = webdriver.Ie(executable_path=file_utils.location_file("config/drive/IEDriverServer.exe"))
        else:
            driver = webdriver.edge()
        print("当前打开的浏览器是:"+browser)
        return driver

    '''
        判断元素是否存在页面
    '''
    def __element_isdisplayed(self,element):
        flag = element.is_displayed()
        if flag == True:
            return element
        else:
            return False

    def __get_url(self, url):
        if self.driver != None:
            if 'http' in url:
                self.driver.get(url)
            elif 'C' or 'D' or 'E' in url:
                self.driver.get(url)
            else:
                print("你的URL有问题")
        else:
            print("case失败")

    def __upload_file(self,file_name):
        self.pkb.type_string(file_name)
        time.sleep(2)
        self.pkb.tap_key(self.pkb.return_key)

    def __js_execute_calendar(self,info):
        by,value=info
        if by == "id":
            by_key = "getElementById"
            js = 'document.%s("%s").removeAttribute("readonly");' %(by_key,value)
        else:
            by_key = "getElementClassName"
            js = 'document.%s("%s")[1].removeAttribute("readonly");' %(by_key,value)
        self.driver.execute_script(js)

    def open_url_is_true(self,url,title_name):
        self.__get_url(url)
        return self.assert_title(title_name)

    def get_element(self,info):
        by,value=self.get_local_element(info)
        if by=="id":
            return self.driver.find_element_by_id(value)
        elif by=="name":
            return self.driver.find_element_by_name(value)
        elif by=="class":
            return self.driver.find_element_by_class_name(value)
        elif by == "css":
            return self.driver.find_element_by_css_selector(value)
        else:
            return self.driver.find_element_by_xpath(value)

    def wait_element(self, info, timeout=12):
        return WebDriverWait(self.driver, timeout).until(self.get_element, info)

    def get_elements(self,info):
        by, value = self.get_local_element(info)
        if by=="id":
            elements = self.driver.find_elements_by_id(value)
        elif by=="name":
            elements = self.driver.find_elements_by_name(value)
        elif by=="class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
        return elements

    def wait_elements(self, info, timeout=12):
        element_list = []
        elements = WebDriverWait(self.driver, timeout).until(self.get_element, info)
        for element in elements:
                element_list.append(element)
        return element_list


    def get_leve_element(self, info_level, info_node):
        node_by, node_value = self.get_local_element(info_node)
        element = self.get_element(info_level)
        if element == False:
            return False
        if node_by == "id":
            node_element = element.find_element_by_id(node_value)
        elif node_by == "name":
            node_element = element.find_element_by_name(node_value)
        elif node_by == "class":
            node_element = element.find_element_by_class_name(node_value)
        elif node_by == "css":
            node_element = element.find_element_by_css_selector(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return self.__element_isdisplayed(node_element)

    #此函数有点多余
    '''
    下标获取info元素element
     @parame by 子节点定位方式
     @parame value 子节点定位位置
     @parame node_by 父节点定位方式
     @parame node_value 父节点定位位置
     @return node_element 查找成功返回一个元素   否则返回Flase
    '''
    def get_list_element(self, info, index):
        elements = self.wait_elements(info)
        if index > len(elements):
            print("你输入的index有误")
            return None
        else:
            return elements[index]

    def handle_windows(self,*args):
        value = len(args)
        if value == 1:
            if args[0] == "max":
                self.driver.maximize_window()
            elif args[0] == "min":
                self.driver.minimize_window()
            elif args[0] == "back":
                self.driver.back()
            elif args[0] == "go":
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value ==2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print("你传递的参数有问题")

    def switch_to_handle(self,title_name):
        hander_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in hander_list:
            if i!=current_handle:
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

    def send_value(self,info,key):
        element = self.wait_element(info)
        element.send_keys(key)



    def click_element(self,info):
        self.wait_element(info).click()


    '''
        点击check元素
    '''
    def check_box_is_selected(self,info,check=False):
        element = self.wait_element(info)
        flag = element.is_selected()
        if check != flag:
            self.wait_element(info).click()


    '''
        判断元素list是否存在页面
    '''
    def elements_isdisplayed(self,elements):
        element_list = []
        if elements:
            for element in  elements:
                if self.__element_isdisplayed(element)==False:
                    print("element元素不存在页面:"+element)
                    continue
                else:
                    element_list.append(element)
        return element_list




    '''
    通过index的值来设置 Select下拉框
    '''
    def set_selected_Index(self,info,value_index,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)


    '''
    通过value的值来设置 Select下拉框
    '''
    def set_selected_Value(self,info,value,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_value(value)

    '''
    通过visible_text的值来设置 Select下拉框
    '''
    def set_selected_visible_text(self,info,visible_text,index=None):
        selected_element= None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.wait_element(info)
        Select(selected_element).select_by_visible_text(visible_text)


    '''
    上传文件
    file_name:文件路径
    info:非input类型上传文件/上传按钮元素信息
    send_info:input类型上传文件/input元素信息
    '''
    def upload_file_function(self,file_name,info=None,send_info=None):
        if send_info:
            self.send_value(send_info,file_name)
        else:
            self.click_element(info)
            time.sleep(2)
            self.__upload_file(file_name)
    '''
    下载文件
    info:文件下载按钮的元素信息
    '''
    def download_file_function(self,info):
        self.click_element(info)

    '''
    设置日历的值
    info:日历元素元素信息
    value:需要修改的值
    '''
    def set_calendar_value(self,info,value):
        element = self.wait_element(info)
        try:
            element.get_attribute("readonly")
            self.__js_execute_calendar(info)
        except:
            print("日历中没有readonly属性，可读可写")
        element.clear()
        self.send_value(info,value)


    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''
    def moveto_element_mouse(self,info):
        element = self.wait_element(info)
        ActionChains(self.driver).move_to_element(element).perform()

    '''
    F5强制刷新
    '''
    def F5(self):
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()



    '''
    切换iframe
    '''
    def switch_iframe(self,info):
        if info!=None:
            iframe_element = self.wait_element(info)
            self.driver.switch_to_frame(iframe_element)
        else:
            self.driver.switch_to_default_content()
    '''
    点击系统弹框
    
    '''
    def switch_alert(self,info,value=None):
        if info=="accept":
            if value:
                self.driver.switch_to_alert().send_keys(value)
            self.driver.switch_to_alert().accept()
        else:
            self.driver.switch_to_alert().dismiss()

    '''
    滚动查找一个元素
    '''
    def scroll_element(self,info):
        js = 'document.documentElement.scrollTop=1000;'
        try:
            self.wait_element(info)
        except:
            self.driver.execute_script(js)
            pass




    '''
    得到当前网页的cookie数据
    '''
    def get_cookie(self):
        return self.driver.get_cookies()

    '''
      设置网页cookie
    '''
    def set_cookie(self):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.add_cookie(read_json.get_data())




    def get_element_text(self,info):
        return self.wait_element(info).text

    def get_element_value_text(self,info):
        return self.wait_element(info).get_attribute("value")

    def get_element_tag_text(self,info,tag):
       if self.get_element(info) !=False :
            return self.wait_element(info).get_attribute(tag)









    '''
       截取element图片
    '''
    def get_element_screen(self,info,image_name=None):
        img_path = self.save_screen(image_name)
        location = self.wait_element(info).location
        size = self.wait_element(info).size
        left = location["x"]
        top = location["y"]
        right  = left+size["width"]
        bottom  = top+size["height"]
        img = Image.open(img_path)
        img = img.crop((left, top, right, bottom))
        img.save(img_path)
        return img_path

    '''
        断言当前网页title是否正确
    '''
    def assert_title(self,title_name):
        print("当前title:"+title_name)
        return title_name in self.driver.title


    '''
       整个页面截图
    '''
    def save_screen(self,img_name=None):
        if not img_name:
            img_name = time.strftime('%Y_%m_%d_%H_%M_%S')
        path = file_utils.location_file("config/image/"+img_name+".png")
        self.driver.save_screenshot(path)
        return path

    '''
       关闭浏览器
    '''
    def close(self):
        self.driver.close()
        self.driver.quit()


    def get_local_element(self, info):
        value = read_ini.get_content("element", info)
        return self.parsing_content(value)

    def get_local_url(self, value):
        return read_ini.get_content("url", value)



    def parsing_content(self, text_content):
        if text_content:
            return text_content.split("<")
        else:
            return False


