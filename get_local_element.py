from read_init import ReadIni
from open_browser import seleniumDriver
import sys
import time
sys.path.append('/Users/edz/Documents/VS_Code/imooc')

readIni = ReadIni()
driver = seleniumDriver('chrome')
data = readIni.get_value('username')
data_info = data.split('>')
by = data_info[0]
value = data_info[1]
driver.getUrl('http://www.imooc.com/user/newlogin')
time.sleep(2)
driver.set_value(by, value, 'zhouting_java@126.com')
time.sleep(2)
driver.close_broswer()
