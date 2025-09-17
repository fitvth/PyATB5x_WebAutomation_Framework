from turtledemo.clock import setup

import allure
import pytest
import time
from selenium import webdriver
from dotenv import load_dotenv
import os

from test.PageObject.PageObjectModel.VWO.Dashboard_Page import Dashboard
from test.PageObject.PageObjectModel.VWO.Login_Page import LoginPage
# Assertion and use the page object class
# User Interaction + assertion
# close webdriver

from test.constants.constants import Constants
from test.utils.Utils import *
from test.PageObject.PageObjectModel import VWO

@pytest.fixture()
def setup():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get(Constants.vwo_url())
    return driver

@allure.title("VWO Login test")
@allure.description("TC0- VWO Negative test case")
@allure.feature("Feature| TC0- VWO Negative test case")
def test_vwo_negative(setup):
    driver=setup
    login_page=LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("INVALID_USERNAME"),pwd=os.getenv("INVALID_PASSWORD"))
    error_message=login_page.error_message_text()
    take_screenshot(driver=driver,name="error_snap")
    print(f"Error is: {error_message}")
    assert error_message==os.getenv("error_message_expected")

@allure.title("VWO Login test")
@allure.description("TC1- VWO Positive test case")
@allure.feature("Feature| TC1- VWO Positive test case")
def test_vwo_positive(setup):
    driver = setup
    login_page=LoginPage(driver=driver)
    login_page.login_to_vwo(usr=os.getenv("CORRECT_USERNAME"),pwd=os.getenv("CORRECT_PASSWORD"))
    dashboard_page=Dashboard(driver=driver)
    take_screenshot(driver=driver, name="success_snap")
    assert os.getenv("USERNAME_LOGGED_IN")in dashboard_page.user_logged_text()

