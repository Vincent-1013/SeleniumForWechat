import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestBase:

    def setup_method(self):
        # method1    --remote-debugging-port
        # /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir=/tmp/chrome-profile
        options = Options()
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        # self.driver.find_element(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        #option+command+L 格式优化
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': ''},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1782874408, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'sameSite': 'None', 'secure': True, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': '1688854804698408'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': '1688854804698408'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': '1970325317997244'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False,
        #      'value': 'vF87aJ-1lub-glDfkYuHL7HCS8HHgoRLABPlKcOz-57548vZMo5OQaQiQ-VLLoqpDefTjRUTtfi52tbWYVJOyA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False,
        #      'value': 'GRMiS_poyQgaDVJ7tMnhupTDaR8mwBM9nCALJijbm7qZs2wvINeBl2y2DbhGv0hmUYYGBbqBw5tgohlBonRQGysIN7tUaAoyLX7sH2NOtgfbQXmlKZpYXGuNKWeQr76HcACo2q5Bd9raCIT25xt75sBzpi-xsIN-FOSrJ0t_Rn7Vl4EgHU6W5KJNVdVmg8-gJcieJNseAIgTQk5-V8Qn5lb-MWH_coC3S6XXqpceZoYXAp4NOoTgw9NRwSSHco_CZhYjig9pfylgRzrcVSNJVOvxgFkt0faD_xhGCBj0Lkk'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': 'true'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1753931456, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'sameSite': 'Lax', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'sameSite': 'Lax',
        #      'secure': False, 'value': '0628708'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1753930408.2356, 'httpOnly': False, 'name': 'ww_lang', 'path': '/',
        #      'sameSite': 'None', 'secure': True, 'value': 'cn,zh'}]

        #一定要提前访问才能获取到cookies
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

        db = shelve.open("cookies")
        # db['cookies'] = self.driver.get_cookies()

        cookies = db["cookies"]

        # 浏览器处于哪个页面就获取那个页面的cookies
        # print(self.driver.get_cookies())
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        sleep(3)
        db.close()
