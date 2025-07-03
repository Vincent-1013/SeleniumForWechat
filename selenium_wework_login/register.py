from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Register:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def register(self):

        sleep(1)
        #<a class="login_registerBar_link" href="/wework_admin/register_wx?from=myhome">企业注册</a>
        #document.querySelector("#wework_admin\\.loginpage_wx2_\\$ > main > div.login_registerBar > a")
        self._driver.find_element(By.ID,"corp_name").send_keys("企业微信实战")
        self._driver.find_element(By.ID,"manager_name").send_keys("小红")
        self._driver.find_element(By.ID,"register_tel").send_keys("17897352017")
        sleep(2)
        self._driver.quit()
        return True


