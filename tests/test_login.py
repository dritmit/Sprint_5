from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import StellarBurgersLocators
from conftest import driver


class TestLogin:

    def test_login_login_button_on_main_page(self, driver):

        driver.find_element(*StellarBurgersLocators.MAIN_PAGE_LOGIN_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()
        (WebDriverWait(driver, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                                  'Оформить заказ')))
        order_button = driver.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'

    def test_login_personal_account_button_on_main_page(self, driver):

        driver.find_element(*StellarBurgersLocators.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()
        (WebDriverWait(driver, 10)
         .until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                              'Оформить заказ')))
        order_button = driver.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'

    def test_login_link_login_on_register_page(self, driver):

        driver.get(settings.URL + 'register')
        driver.find_element(*StellarBurgersLocators.REGISTRATION_PAGE_LOGIN_LINK).click()
        (WebDriverWait(driver, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.LOGIN_PAGE_TITLE,
                                                                  'Вход')))
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()
        (WebDriverWait(driver, 10)
            .until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                              'Оформить заказ')))

        order_button = driver.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'

    def test_login_link_login_on_forgot_pass_page(self, driver):
        driver.get(settings.URL + 'forgot-password')
        driver.find_element(*StellarBurgersLocators.FORGOT_PASS_PAGE_LOGIN_LINK).click()
        (WebDriverWait(driver, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.LOGIN_PAGE_TITLE,
                                                                  'Вход')))
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_FIELD).send_keys(settings.EMAIL)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_PASSWORD_FIELD).send_keys(settings.PASSWORD)
        driver.find_element(*StellarBurgersLocators.LOGIN_PAGE_LOGIN_BUTTON).click()
        (WebDriverWait(driver, 10)
            .until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                              'Оформить заказ')))

        order_button = driver.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'
