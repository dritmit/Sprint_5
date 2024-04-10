import pytest
from selenium import webdriver
from locators import StellarBurgersLocators
import settings


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)

    return chrome_driver


@pytest.fixture(scope='function')
def driver_login():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)
    chrome_driver.find_element(*StellarBurgersLocators.MAIN_PAGE_LOGIN_BUTTON).click()
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()

    return chrome_driver
