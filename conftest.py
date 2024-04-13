import pytest
from selenium import webdriver
from locators import StellarBurgersLocators
import settings


@pytest.fixture(scope='function')
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.get(settings.URL)

    yield chrome_driver

    chrome_driver.quit()


@pytest.fixture(scope='function')
def driver_login(driver):
    chrome_driver = driver
    chrome_driver.find_element(*StellarBurgersLocators.MAIN_PAGE_LOGIN_BUTTON).click()
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
    chrome_driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()

    yield chrome_driver
