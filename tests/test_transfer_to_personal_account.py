from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver_login


class TestTransfers:

    def test_open_account_profile_from_main(self, driver_login):

        driver_login.find_element(*StellarBurgersLocators.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions
                .text_to_be_present_in_element(StellarBurgersLocators
                                               .PROFILE_PAGE_DESCRIPTION,
                                               'В этом разделе вы можете изменить свои персональные данные')))

        description = driver_login.find_element(*StellarBurgersLocators.PROFILE_PAGE_DESCRIPTION).text

        assert description == 'В этом разделе вы можете изменить свои персональные данные'
        driver_login.quit()

    def test_click_constructor_from_account_profile(self,driver_login):
        driver_login.find_element(*StellarBurgersLocators.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions
                .text_to_be_present_in_element(StellarBurgersLocators
                                               .PROFILE_PAGE_DESCRIPTION,
                                               'В этом разделе вы можете изменить свои персональные данные')))
        driver_login.find_element(*StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                              'Оформить заказ')))
        order_button = driver_login.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'
        driver_login.quit()



    def test_click_logo_from_account_profile(self, driver_login):
        driver_login.find_element(*StellarBurgersLocators.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions
                .text_to_be_present_in_element(StellarBurgersLocators
                                               .PROFILE_PAGE_DESCRIPTION,
                                               'В этом разделе вы можете изменить свои персональные данные')))
        driver_login.find_element(*StellarBurgersLocators.LOGO).click()
        (WebDriverWait(driver_login, 10)
            .until(
            expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON,
                                                              'Оформить заказ')))
        order_button = driver_login.find_element(*StellarBurgersLocators.ACCOUNT_PAGE_PLACE_ORDER_BUTTON).text

        assert order_button == 'Оформить заказ'
        driver_login.quit()
