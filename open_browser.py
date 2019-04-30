from selenium import webdriver
import sys
sys.path.append('/Users/edz/Documents/VS_Code/BaseImooc')
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from handle_json import handlejson
from readinit import read_ini
from pykeyboard import PyKeyboard
import time


class seleniumDriver:
    def __init__(self, browser):
        self.driver = self.openBroswer(browser)

    # 打开浏览器
    def openBroswer(self, browser):
        try:
            options = webdriver.ChromeOptions()
            if browser == 'chrome':
                # 设置默认路径并禁止弹窗
                prefs = {
                    'download.default_directory': '/Users/edz/Documents/',
                    'profile.default_content_settings.popups': 0
                }
                options.add_experimental_option('prefs', prefs)
                # 添加配置参数，下载文件至指定位置
                self.driver = webdriver.Chrome(options=options)
            elif browser == 'firefox':
                profile = webdriver.FirefoxProfile()
                profile.set_preference('broswer.download.dir',
                                       '/Users/edz/Documents/')
                # 使用自定义的下载路径
                profile.set_preference('broswer.download.folderList', 2)
                # 禁止弹窗
                profile.set_preference(
                    'broswer.helperApps.neverAsk.saveToDisk',
                    'application/zip')
                self.driver = webdriver.Firefox(firefox_options=profile)
            time.sleep(7)
            return self.driver
        except Exception:
            print('浏览器打开失败')
            return None

    # 访问网址
    def getUrl(self, url):
        if self.driver is not None:
            if 'http://' in url:
                self.driver.get(url)
                print('浏览器打开成功')
            else:
                print('输入的URL不正确')
        else:
            print('用例执行失败')

    # 检查页面是否正确
    def check_page(self, title_name=None):
        if title_name is not None:
            title = EC.title_contains(title_name)
            return title(self.driver)

    # 检查打开的页面是否正确
    def check_open(self, url, title_name=None):
        self.driver.get(url)
        print('浏览器是否正常打开:' + str(self.check_page(title_name)))
        return self.check_page(title_name)

    # 切换页面
    def switch_window(self, title_name=None):
        handles_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        time.sleep(15)
        for i in handles_list:
            if i != current_handle:
                time.sleep(3)
                self.driver.switch_to.window(i)
                title = EC.url_contains(title_name)
                if title(self.driver):
                    print('找到目标页')
                    break
        time.sleep(3)
        print('开始输入微博账号')
        self.driver.find_element_by_id('userId').send_keys('1234')
        print('微博账号输入完毕')
        time.sleep(3)

    # 关闭浏览器
    def close_broswer(self):
        self.driver.close()
        print('浏览器已经关闭')

    # 操作浏览器
    def handle_windows(self, *args):
        length = len(args)
        if length == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        # 设置窗口为指定大小
        elif length == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print('输入的参数有误！')

    def login(self):
        # 进入慕课网首页点击登录
        self.driver.get('https://www.imooc.com/user/newlogin')
        self.driver.find_element_by_name('email') \
            .send_keys('zhouting_java@126.com')
        self.driver.find_element_by_name('password') \
            .send_keys('zhouting414')
        self.driver.find_element_by_class_name('moco-btn').click()
        time.sleep(3)
        # 登录完成后进入个人设置页面点击微博绑定
        self.driver.get('https://www.imooc.com/user/setbindsns')
        self.driver.find_elements_by_class_name('inner-i-box')[1]. \
            find_element_by_class_name('moco-btn-normal').click()
        print('打开微博登录页')

    # 判断元素是否展示
    def element_isdisplayed(self, element):
        flag = element.is_displayed()
        if flag:
            return element
        else:
            print('元素展示失败！')
            return False

    '''
    获取元素element
    @parame info 获取哪个元素
    @return element  返回一个元素
    '''

    def get_element(self, info):
        element = None
        by, value = self.get_local_element(info)
        print("by和value的值分别为：",by+"  ",value)
        try:
            if by == 'id':
                element = self.driver.find_element_by_id(value)
            elif by == 'name':
                element = self.driver.find_element_by_name(value)
                print("获取到element的值为：", element)
            elif by == 'class':
                element = self.driver.find_element_by_class_name(value)
            elif by == 'css':
                element = self.driver.find_element_by_css_selector(value)
            elif by == 'xpath':
                element = self.driver.find_element_by_xpath(value)
        except Exception:
            print('定位方式：', by, '定位值:', value, '定位失败！')
        return self.element_isdisplayed(element)

    '''
    获取元素列表elements
    @parame info 获取哪个元素
    @return elements  返回元素列表
    '''

    def get_elements(self, info):
        elements = None
        elements_list = []
        by, value = self.get_local_element(info)
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif by == 'class':
            elements = self.driver.find_elements_by_class_name(value)
        elif by == 'css':
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == 'xpath':
            elements = self.driver.find_elements_by_xpath(value)
        # 判断列表中的元素是否全部展示可见
        for element in elements:
            if self.element_isdisplayed(element) is False:
                print('元素', element, '未展示')
                continue
            else:
                elements_list.append(element)
        return elements_list

    '''
    层级定位element
    查找父节点下的子节点

    @parame parent_info 父节点元素
    @parame nodevalue  子节点元素
    @return child_info  返回元素
    '''

    def get_level_element(self, parent_info, child_info):
        parent_element = self.get_element(parent_info)
        nodeby, nodevalue = self.get_local_element(child_info)
        if parent_element is False:
            return False
        if nodeby == 'id':
            element = parent_element.find_element_by_id(nodevalue)
        elif nodeby == 'name':
            element = parent_element.find_element_by_name(nodevalue)
        elif nodeby == 'class':
            element = parent_element.find_element_by_class_name(nodevalue)
        elif nodeby == 'css':
            element = parent_element.find_element_by_css_selector(nodevalue)
        elif nodeby == 'xpath':
            element = parent_element.find_element_by_xpath(nodevalue)
        elif nodeby == 'tag':
            element = parent_element.find_element_by_tag_name(nodevalue)
        return self.element_isdisplayed(element)

    '''
    列表索引定位element
    查找父节点下的子节点

    @parame by 获取方式
    @parame value  值
    @parame index 索引
    @return element  返回元素
    '''

    def get_list_element(self, info, index):
        elements = self.get_elements(info)
        print('elements元素')
        if index > len(elements):
            print('输入的索引有误！')
            return None
        return elements[index]

    '''
    在元素中输入值
    '''

    def set_value(self, info, key_value):
        element = self.get_element(info)
        if element is False:
            print('元素未展示，输入失败！')
        else:
            if element is not None:
                element.send_keys(key_value)
                print("元素输入完毕！")
            else:
                print('定位有误，输入失败！')

    '''
    点击元素
    '''

    def click_element(self, info):
        element = self.get_element(info)
        if element is False:
            print('元素未展示，点击失败！')
        else:
            if element is not None:
                element.click()
            else:
                print('定位有误，输入失败！')

    '''
    操作复选框
    @parame check 是否选中（boolean）
    '''

    def oprate_check_box(self, info, check=None):
        element = self.get_element(info)
        if element is not False:
            flag = element.is_selected()
            if flag:
                if check is False:
                    element.click()
                    print('点击取消复选框')
            else:
                if check:
                    element.click()
                    print('点击选中复选框')
        else:
            print('元素不可见，选中操作未生效')

    '''
    获取本地配置文件的数据
    @parame info 配置文件中的元素
    '''

    def get_local_element(self, info):
        data = read_ini.get_value(info)
        datas = data.split('>')
        print("拆分后的值：", datas)
        return datas

    '''
    选中下拉框的值
    '''

    def get_selected(self, info, value_index, index=None):
        if index is not None:
            select_element = self.get_list_element(info, index)
            print(select_element)
        else:
            select_element = self.get_element(info)
        return Select(select_element).select_by_index(value_index)

    '''
    非input类型上传文件
    @parame filename  上传文件路径
    '''

    def upload_file(self, filename):
        pk = PyKeyboard()
        # pk.tap_key(pk.shift_key)  切换中英文
        pk.type_string(filename)  # 输入文件路径
        time.sleep(2)
        pk.tap_key('return')

    '''
    下载文件
    '''

    def download_element(self, info):
        self.click_element(info)

    '''
    执行js
    '''

    def js_excute(self, info):
        by, value = self.get_local_element(info)
        if by == 'id':
            by_key = 'getElementsById'
            js = 'document.%s("%s").removeAttribute("readonly");' \
                % (by_key, value)
        elif by == 'class':
            by_key = 'getElementsByClassName'
            js = 'document.%s("%s")[0].removeAttribute("readonly");' % (by_key,
                                                                        value)
        self.driver.execute_script(js)

    def calender(self, info, value):
        element = self.get_element(info)
        try:
            element.get_attribute('readonly')
            self.js_excute(info)
        except Exception:
            print('不是只读属性的日历')
        element.clear()
        self.set_value(info, value)

    '''
    移动鼠标到某个元素上
    '''
    def moveto_element(self, info):
        element = self.get_element(info)
        ActionChains(driver).move_to_element(element).perform()

    '''
    强制刷新
    '''
    def force_refresh(self):
        ActionChains(self.driver).key_down(
            Keys.COMMAND).send_keys('r').send_keys(Keys.NULL).perform()

    '''
    切换iframe
    '''
    def switch_iframne(self, info=None):
        # 切入
        if info is None:
            self.driver.switch_to.default_content()
        # 切出
        else:
            element = self.get_element(info)
            self.driver.switch_to.frame(element)

    '''
    系统级弹窗
    @parame info 是否弹窗
    @parame value 是否需要输入值
    '''
    def switch_alert(self, info, value=None):
        window_alert = self.driver.switch_to.alert
        if info == 'accept':
            if value is not None:
                window_alert.send_keys('test')
            window_alert.accept()
        else:
            window_alert.dismiss()

    '''
    滚动页面查找元素（针对慕课网【手记】模块）
    '''
    def scroll_getelement(self, list_info, name):
        elements = self.get_elements(list_info)
        # 滑动至页面底部
        js = 'document.documentElement.scrollTop=100000;'
        flag = True
        while flag:
            for element in elements:
                title_name = element.find_element_by_tag_name('p').text
                print('titlename:', title_name)
                if title_name in name:
                    element.click()
                    flag = False
            self.driver.execute_script(js)
            time.sleep(3)
    '''
    滑动查找元素（通用）
    '''
    def scroll_element(self, info):
        js = 'document.documentElement.scrollTop=300;'
        flag = True
        while flag:
            try:
                self.get_element(info)
                flag = False
            except Exception:
                self.driver.execute_script(js)
                time.sleep(3)

    def load_cookie(self):
        cookie = self.driver.get_cookies()
        handlejson.writeJson(cookie)

    def set_cookie(self):
        cookie = handlejson.getData()
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.add_cookie(cookie)
        time.sleep(2)
    '''
    保存截图
    '''
    def save_screen(self):
        now_time = time.strftime('%Y%m%d.%H.%M.%S')
        self.driver.get_screenshot_as_file('%s.png' % now_time)
    def delete_cookie(self):
        self.driver.delete_all_cookies()

if __name__ == "__main__":
    driver = seleniumDriver('chrome')
    driver.getUrl('http://order.imooc.com/myorder')
    time.sleep(3)
    '''driver.set_value('username', 'zhouting_java@126.com')
    time.sleep(2)
    driver.set_value('password', 'zhouting414')
    driver.click_element('loginbutton')
    time.sleep(3)'''
    # driver.load_cookie()  # 获取登录状态的cookie
    driver.delete_cookie()  # 删除本地cookie
    print("删除cookie")
    time.sleep(2)
    driver.force_refresh()  # 删除本地cookie后刷新
    time.sleep(2)
    driver.set_cookie()  # 设置cookie
    print("设置cookie")
    time.sleep(2)
    driver.getUrl('http://order.imooc.com/myorder')
    


    driver.scroll_getelement('titlelist', 'python深拷贝与浅拷贝')
    # driver.scroll_getelement('titlelist', 'python深拷贝与浅拷贝')
    #driver.save_screen()
    #time.sleep(2)
    '''driver.getUrl('http://www.imooc.com/user/newlogin')
    time.sleep(2)
    driver.set_value('username', 'zhouting_java@126.com')
    time.sleep(2)
    driver.set_value('password', 'zhouting414')
    driver.click_element('loginbutton')
    time.sleep(3)
    driver.getUrl('http://www.imooc.com/user/setprofile')
    time.sleep(7)
    driver.get_selected('job', 1, 0)
    driver.force_refresh()
    time.sleep(5)
    driver.close_broswer()'''
    # driver = seleniumDriver('chrome')
    # driver.getUrl('http://www.imooc.com/user/newlogin')
    # driver.oprate_check_box('id', 'auto-signin', False)
    # driver.check_open('http://www.imooc.com', '慕课网')
    # driver.login()
    # driver.switch_window('网站连接')
    #driver.close_broswer()
