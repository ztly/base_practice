from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin')
time.sleep(3)
driver.find_element_by_name('email').send_keys('zhouting_java@126.com')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(3)
driver.get('https://www.imooc.com/wenda/save')
time.sleep(3)
# element = driver.find_element_by_id('ueditor_0')
# 切换到frame模块
driver.switch_to.frame('ueditor_0')
time.sleep(3)
# 查找frame下的p标签元素
p_element = driver.find_element_by_tag_name('p')
# 将鼠标移动到输入框元素并输入值
ActionChains(driver).move_to_element(p_element).click().send_keys(
    'this is test').perform()
time.sleep(3)
# 切换出默认element
driver.switch_to.default_content()
driver.close()
