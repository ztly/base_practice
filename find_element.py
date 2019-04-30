from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://imooc.com')
# element = driver.find_element_by_name('email')
# element.send_keys('zhouting_java@126.com')
# driver.find_element_by_class_name('')
# driver.find_element_by_partial_link_text('初识HTML').click()
# driver.find_element_by_link_text('初识HTML+CSS').click()

time.sleep(2)
driver.find_element_by_id('js-signin-btn').click()  # 点击登录
time.sleep(2)


def oprate_check_box(element, check=None):
    flag = element.is_selected()
    if flag:
        if check:
            return
        else:
            element.click()
    else:
        if check:
            element.click()
        else:
            return


element = driver.find_element_by_id('auto-signin')
oprate_check_box(element, False)

'''
driver.find_element_by_name('email').send_keys('zhouting_java@126.com')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_css_selector('.rlf-group>.moco-btn').click()
# driver.find_element_by_class_name('moco-btn-lg').click()
time.sleep(2)
driver.find_element_by_xpath("//div[@class='showhide-search'] \
    /preceding-sibling::div[1]/input[1]").send_keys("测试")
driver.get('https://www.imooc.com/user/setprofile')
time.sleep(5)
node_element = driver.find_element_by_id('profile')
node_element.find_element_by_name('nickname').send_keys('zhouting')
time.sleep(3)
driver.close()
'''
