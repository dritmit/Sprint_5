from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import StellarBurgersLocators
from conftest import driver


class TestRegistration:

    def test_registration(self, driver):
        driver.get(settings.URL + 'register')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(settings.NEW_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(settings.NEW_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASS_FIELD).send_keys(settings.NEW_PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        (WebDriverWait(driver, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.LOGIN_PAGE_TITLE,
                                                 'Вход')))

        title = driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_TITLE).text
        assert title == 'Вход'
        driver.quit()

    def test_registration_wrong_password(self, driver):
        driver.get(settings.URL + 'register')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_FIELD).send_keys(settings.WRONG_NAME)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_FIELD).send_keys(settings.WRONG_EMAIL)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASS_FIELD).send_keys(settings.WRONG_PASSWORD)
        driver.find_element(*StellarBurgersLocators.REGISTRATION_BUTTON).click()

        (WebDriverWait(driver, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.REGISTRATION_PASSWORD_ERROR,
                                                                  'Некорректный пароль')))

        password_error = driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_ERROR).text
        assert password_error == 'Некорректный пароль'
        driver.quit()
