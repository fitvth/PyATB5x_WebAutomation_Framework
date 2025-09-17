from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from test.utils.Common_Utils import webdriver_wait

class Dashboard:
    def __init__(self,driver):
        self.driver=driver

    user_log=(By.XPATH,"//span[@class='Fw(semi-bold) ng-binding']")

    def get_dashboard(self):
        return self.driver.find_element(*Dashboard.user_log)

    def user_logged_text(self):
        webdriver_wait(driver=self.driver,element_tuple=self.user_log,timeout=5)
        return self.get_dashboard().text
