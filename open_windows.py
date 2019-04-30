from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

'''
进入慕课网首页点击登录
'''
driver.get('https://www.imooc.com/user/newlogin')
driver.find_element_by_name('email').send_keys('zhouting_java@126.com')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(3)

# 判断页面元素是否全部加载并显示
locator = (By.ID, 'username')
EC.visibility_of_all_elements_located(locator)

'''
登录完成后进入个人设置页面点击微博绑定
'''
driver.get('https://www.imooc.com/user/setbindsns')
driver.find_elements_by_class_name('inner-i-box')[1] \
    .find_element_by_class_name('moco-btn-normal').click()
'''
切换页面
'''

# 获取句柄列表
handles_list = driver.window_handles
# 获取当前句柄
current_handle = driver.current_window_handle
time.sleep(15)
for i in handles_list:
    if i != current_handle:
        time.sleep(3)
        driver.switch_to.window(i)
        title = EC.url_contains('网站连接')
        if title(driver):
            break
time.sleep(2)
driver.find_element_by_id('userId').send_keys('1234')
time.sleep(2)
driver.close()
