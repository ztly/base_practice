from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.imooc.com/article/ai')
time.sleep(2)
js = 'document.documentElement.scrollTop=100000;'
t = True
while t:
    element_list = driver.find_elements_by_class_name('article-lwrap')
    for element in element_list:
        text = element.find_element_by_tag_name('p').text
        print(text)
        if text == 'python深拷贝与浅拷贝':
            element.click()
            t = False
            time.sleep(3)
    driver.execute_script(js)
