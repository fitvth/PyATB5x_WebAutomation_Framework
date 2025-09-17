import allure
import pytest
import time
from selenium import webdriver
from dotenv import load_dotenv
import os
from test.PageObject.PageObjectModel.VWO import Free_Trail_Page
from test.constants import constants
from test.constants.constants import Constants
from test.PageObject.PageObjectModel.VWO.Free_Trail_Page import Free_trail
from test.utils import Common_Utils
from test.utils import*
from test.utils.Utils import take_screenshot


@pytest.fixture()
def setup():
    load_dotenv()
    driver=webdriver.Chrome()
    driver.get(Constants.dashboard_url())
    return driver

@allure.title("VWO Free_trail")
@allure.description("TC0- VWO Free trail Negative test case")
@allure.feature("Feature| TC0-VWO Free trail Negative test case")
def test_free_trail1(setup):
    driver=setup
    Trail=Free_trail(driver=driver)
    Trail.enter_free_trail_invalid(invalid_email=os.getenv("INVALID_USERNAME1"))
    error_trail_message=Trail.get_error_trail_message()
    take_screenshot(driver=driver, name="Free_trail_Error_snap")
    print(f" Actaul Message is: {error_trail_message}")
    print(f" Expected Message is: {os.getenv("free_error_message_expected")}")
    assert error_trail_message==os.getenv("free_error_message_expected")