from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('')
driver.find_element_by_id('alert').click()
time.sleep(2)
# 弹框类型
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_id('confirm').click()
time.sleep(2)
# 确认or取消类型
driver.switch_to.alert.accept()  # 点击确认
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element_by_id('confirm').click()
time.sleep(2)
driver.switch_to.alert.dismiss()  # 点击取消
time.sleep(2)
driver.refresh()
driver.find_element_by_id('input').click()
# 弹框中输入内容确认or取消
driver.switch_to.alert.send_keys('xx')
time.sleep(2)
driver.close()
