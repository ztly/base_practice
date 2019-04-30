from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.imooc.com/')
element = driver.find_element_by_class_name('menuContent') \
    .find_elements_by_class_name('item')[1]
# 鼠标滑动操作
ActionChains(driver).move_to_element(element).perform()
driver.find_elements_by_class_name('tag-box')[1] \
    .find_element_by_link_text('前端工具').click()
