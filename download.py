from selenium import webdriver

options = webdriver.ChromeOptions()
'''
下载路径
download.default_directory默认路径
profile.default_content_settings禁止弹窗参数
'''
prefs = {
    'download.default_directory': '/Users/edz/Documents/',
    'profile.default_content_settings.popups': 0
}
options.add_experimental_option('prefs', prefs)
# 修改Chrome设置
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.imooc.com/mobile/app')
driver.find_element_by_class_name('android').click()
