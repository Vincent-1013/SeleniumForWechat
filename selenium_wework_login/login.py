from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
# from selenium.webdriver.commen.By import By

from selenium_wework_login.register import Register


class Login:
    #driver:WebDriver 后面的:WebDriver不是必须写的（标签），但是写了之后相当于告诉selenium这个driver是WebDriver的driver
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def scanf(self):
        pass

    def goto_register(self):
        sleep(2)
        self._driver.find_element(By.CSS_SELECTOR,'.login_registerBar_link').click()
        return Register(self._driver)
