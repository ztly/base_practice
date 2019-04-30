from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://imooc.com')
title_name = driver.title
if '慕课网' in title_name:
    print('网页打开正确')
else:
    print('网页打开失败')
title = driver.title
title_a = EC.title_is('慕课网')
print(title_a(driver))
title_b = EC.title_contains('慕课网')
print(title_b(driver))
driver.close()

'''
print(EC.title_is('慕课网'))
print(EC.title_contains('慕课网'))
'''
