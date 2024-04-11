from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver_login
from conftest import driver


class TestTransfers:

    def test_open_account_profile_from_main(self, driver_login):

        driver_login.find_element(*StellarBurgersLocators.MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions
                .text_to_be_present_in_element(StellarBurgersLocators
                                               .PROFILE_PAGE_DESCRIPTION,
                                               'В этом разделе вы можете изменить свои персональные данные')))
        driver_login.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.text_to_be_present_in_element(StellarBurgersLocators.LOGIN_PAGE_TITLE,
                                                                  'Вход')))

        title = driver_login.find_element(*StellarBurgersLocators.LOGIN_PAGE_TITLE).text
        assert title == 'Вход'
