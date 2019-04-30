from selenium import webdriver
from selenium.webdriver.support.select import Select
import time


driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin')
driver.find_element_by_name('email').send_keys('zhouting_java@126.com')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(3)
driver.get('https://www.imooc.com/user/setprofile')
time.sleep(5)
# 定位下拉框元素
selement_element = driver.find_elements_by_class_name('moco-form-control')[7]
# select 下拉框操作
Select(selement_element).select_by_index('2')
time.sleep(2)
driver.close()
