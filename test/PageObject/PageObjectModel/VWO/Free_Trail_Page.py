import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from test.utils.Common_Utils import webdriver_wait
from test.utils import Common_Utils

class Free_trail:
    def __init__(self,driver):
        self.driver=driver

    free_trail_button=(By.XPATH,"//a[normalize-space()='Start a free trial']")
    email_button = (By.XPATH, "//input[@id='page-v1-step1-email']")
    check_box=(By.XPATH,"//input[@id='page-free-trial-step1-cu-gdpr-consent-checkbox']")
    click_create_trail_button = (By.XPATH, "//button[normalize-space()='Create a Free Trial Account']")
    error_message=(By.XPATH,"//div[normalize-space()='The email address you entered is incorrect.']")


    def get_free_trail(self):
        return self.driver.find_element(*Free_trail.free_trail_button)

    def get_email_button(self):
        return self.driver.find_element(*Free_trail.email_button)

    def get_agree_button(self):
        return self.driver.find_element(*Free_trail.check_box)

    def get_create_trail_button(self):
        return self.driver.find_element(*Free_trail.click_create_trail_button)

    def get_error_message(self):
        webdriver_wait(driver=self.driver, element_tuple=self.error_message, timeout=5)
        return self.driver.find_element(*Free_trail.error_message)

    def enter_free_trail_invalid(self,invalid_email):
        try:
            self.get_free_trail().click()
            self.get_email_button().send_keys(invalid_email)
            time.sleep(2)
            self.get_agree_button().click()
            time.sleep(2)
            self.get_create_trail_button().click()
        except Exception as e:
            print(e)

    def get_error_trail_message(self):
        return self.get_error_message().text
