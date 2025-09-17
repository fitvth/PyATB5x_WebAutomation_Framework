import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
import os
from test.utils.Utils import*


@allure.title("VWO login")
@allure.description("TC11- Negative test case for invalid credential")
@allure.feature("VWO with invalid credentials")
@pytest.mark.negativelogin
def test_vwo_login_negative():
    load_dotenv()
    match os.getenv("BROWSER"):
        case "chrome":
            chrome_options = Options()
            chrome_options.add_argument("--incognito")
            driver = webdriver.Chrome(options=chrome_options)


        case "firefox":
            driver = webdriver.Firefox()


    # Step1: Find mail and type mail ID
    driver.get(os.getenv("URL"))
    time.sleep(3)
    email_web_element =driver.find_element(By.ID, "login-username")
    email_web_element.send_keys(os.getenv("INVALID_USERNAME"))
    time.sleep(2)
    password_web_element = driver.find_element(By.ID, "login-password")
    password_web_element.send_keys(os.getenv("INVALID_PASSWORD"))
    time.sleep(2)
    take_screenshot(driver=driver,name="Login screenshot")

    # find submit button
    submit_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_web_element.click()
    time.sleep(3)

    # error message
    error_message = driver.find_element(By.CLASS_NAME, "notification-box-description")
    print(error_message.text)
    assert error_message.text == os.getenv("error_message_expected")
    time.sleep(5)
    take_screenshot(driver=driver,name= "Error screenshot")
    driver.quit()
