from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

from selenium_wework_login.index import Index


class TestRegister():

    def setup_method(self,driver:WebDriver):
        self.index = Index()




    def test_register(self):
        self.index.goto_login().goto_register().register()
        # self.index.switch_to.window(self.index.window_handles[-1])




        # self.index.goto_register().register()


        sleep(3)

