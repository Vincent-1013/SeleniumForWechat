from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_login.login import Login
from selenium_wework_login.register import Register


class Index:

    def __init__(self):
        self._driver = webdriver.Chrome()
        self._driver.get("https://work.weixin.qq.com/")

    def goto_login(self):
        #打开页面后点击登录企业微信，然后跳转到登录页面
        self._driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        sleep(2)
        return Login(self._driver)




    def goto_register(self):
        #打开企业微信页面后，点击立即注册按钮，跳转到注册页面
        self._driver.find_element(By.CSS_SELECTOR,'.index_head_info_pCDownloadBtn').click()
        sleep(2)
        return Register(self._driver)

