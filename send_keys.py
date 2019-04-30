from selenium import webdriver
import time
from pykeyboard import PyKeyboard

'''driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin')
driver.find_element_by_name('email').send_keys('zhouting_java@126.com')
driver.find_element_by_name('password').send_keys('zhouting414')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(3)
driver.get('https://www.imooc.com/user/setprofile')
time.sleep(5)
# 上传图片
element = driver.find_element_by_id("upload")
element.send_keys('/Users/edz/Downloads/Picture.jpg')
time.sleep(6)'''

driver = webdriver.Chrome()
driver.get('chrome://settings/importData')
time.sleep(10)
pykey = PyKeyboard()
pykey.press_key(pykey.return_key)
pykey.tap_key('return')
time.sleep(3)
driver.close()
