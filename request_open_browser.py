import requests
import json


class request_webdriver:
    def __init__(self):
        self.driver = self.chrome_driver()

    def chrome_driver(self):
        url = 'http://127.0.0.1:4444/wd/hub/session/'
        data = json.dumps({
            'desiredCapabilities': {
                'browserName': 'chrome'
            }
        })
        res = requests.post(url, data).json()
        sessionid = res['sessionId']
        driver = url + sessionid
        return driver

    def get_url(self, url):
        base_url = self.driver + '/url'
        data = json.dumps({
            'url': url
        })
        requests.post(base_url, data)

    def find_ele_by_name(self, value):
        base_url = self.driver + '/element'
        data = json.dumps({
            'using': 'name',
            'value': value
        })
        res = requests.post(base_url, data).json()['value']['ELEMENT']
        print(res)


if __name__ == "__main__":
    resdriver = request_webdriver()
    resdriver.get_url('https://www.imooc.com/user/newlogin/form_url/')
    resdriver.find_ele_by_name('email')
