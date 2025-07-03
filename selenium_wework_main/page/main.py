from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember


class Main:
        def __init__(self):

            options = Options()
            # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=options)
            self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
            # self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
            # self._driver.maximize_window()
            self._driver.implicitly_wait(3)

        def goto_add_member(self):
            #click add member
            sleep(2)
            self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap').click()
            # self._driver.find_element(By.CSS_SELECTOR, '.index_service_cnt js_service_list:nth-child(1)').click()

            return AddMember(self._driver)
