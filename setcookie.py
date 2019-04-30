from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://order.imooc.com/myorder')
driver.delete_all_cookies()
print("删除cookie")
time.sleep(5)
print()
cookie = {
    'domain':
    '.imooc.com',
    'expiry': 1555492195,
    'httpOnly': False,
    'name': 'apsid',
    'path': '/',
    'secure': False,
    'value': 'RmZGI4ODFkNTlhYzJhZTE3MmMwMzUyZWJjYWNhMDMAAAAAAAAAA \
             AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA \
             AAAAAAAAAAAAAAAAAAAAAAAANzM2NTMzMQAAAAAAAAAAAAAAAAA \
             AAAAAAAAAAAAAAAB6aG91dGluZ19qYXZhQDEyNi5jb20AAAAAAA \
             AAAAAAADZhOTAxNTQyOTNhMjk0NTBhMjlkZDg0OTczZjVmNTBhY \
             2CPXGNgj1w%3DOW'
}
driver.add_cookie(cookie)
print("已添加cookie")
time.sleep(2)
driver.get('https://order.imooc.com/myorder')
time.sleep(3)
driver.close()
