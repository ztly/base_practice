from selenium import webdriver
import time
driver = webdriver.Chrome()
# 打开带有日历控件的界面
driver.get('http://baidu.com')
time.sleep(5)
# 移除日历控件的只读属性
js = 'document.getElementById("calander").removeAttribute("readonly");'
# 执行js
driver.execute_script(js)
element = driver.find_element_by_id('calander')
# 清空日历控件的默认值
element.clear()
# 重新设置日历的时间
element.send_keys('2018-8-8')
