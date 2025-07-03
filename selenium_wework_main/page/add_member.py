from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AddMember:
    def __init__(self, driver:WebDriver):
        self._driver = driver

    def add_member(self):
        self._driver.find_element(By.ID,'username').send_keys("Wei005")
        self._driver.find_element(By.ID,'memberAdd_english_name').send_keys("Vincent")
        self._driver.find_element(By.ID,'memberAdd_acctid').send_keys("0007")
        self._driver.find_element(By.NAME,'gender').click()
        self._driver.find_element(By.ID,'memberAdd_phone').send_keys("10789735979")
        self._driver.find_element(By.ID,'memberAdd_telephone').send_keys("10789739312")
        self._driver.find_element(By.ID,'memberEdit_address').send_keys("太湖大道")
        self._driver.find_element(By.ID,'memberAdd_mail').send_keys("107897352312@qq.com")
        self._driver.find_element(By.ID,'memberAdd_title').send_keys("测试工程师")
        self._driver.find_element(By.NAME,'identity_stat').click()
        self._driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()
        sleep(3)
        # self._driver.quit()
        return True


    def get_member(self):
        #需要使用elements，要加s，获取多个值
        #此操作是获取所有姓名

        elements =  self._driver.find_elements(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')


        #method1  分开写
        # list = []
        # for element in elements:
        #     list.append(element.get_attribute('title'))
        #  return list


        #method2 合在一起写
        return [element.get_attribute('title') for element in elements]


