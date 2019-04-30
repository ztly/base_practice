from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin')
time.sleep(2)
driver.save_screenshot('test.png')