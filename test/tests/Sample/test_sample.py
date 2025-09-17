import allure
import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@allure.title("Dry run of the framework 1")
@allure.description("Verify dry run working fine 1")
@allure.feature("TC0 - Sample Passing Test Run")
@pytest.mark.sample
def test_sample_1():
    print("Hello Sample")
    assert True==True


@allure.title("Dry run of the framework 2")
@allure.description("Verify dry run working fine 2")
@allure.feature("TC1 - Sample Failed Test Run")
@pytest.mark.sample
def test_sample_2():
    print("Hello Sample")
    assert True==False