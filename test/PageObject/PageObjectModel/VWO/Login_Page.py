# Login Page Class
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from test.utils.Common_Utils import webdriver_wait

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    # Page Locators
    # =============================================================================

    username = (By.ID, "login-username")
    password = (By.ID, "login-password")
    sign_in_button=(By.XPATH,"//button[@id='js-login-btn']")
    error_message = (By.ID, "js-notification-box-msg")

    # Page Action
    # =============================================================================

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_sign_in_button(self):
        return self.driver.find_element(*LoginPage.sign_in_button)

    def get_error_message(self):
        webdriver_wait(driver=self.driver,element_tuple=self.error_message,timeout=5)
        return self.driver.find_element(*LoginPage.error_message)

    def login_to_vwo(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_sign_in_button().click()
        except Exception as e:
            print(e)

    def error_message_text(self):
        return self.get_error_message().text



