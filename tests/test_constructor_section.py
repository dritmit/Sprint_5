from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
from conftest import driver_login
from conftest import driver


class TestConstructorSections:

    def test_go_to_fillings_in_constructor(self, driver_login):
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_SECTION_FILLINGS)))
        driver_login.find_element(*StellarBurgersLocators.CONSTRUCTOR_SECTION_FILLINGS).click()

        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.FILLINGS_HEADER)))

        header = driver_login.find_element(*StellarBurgersLocators.FILLINGS_HEADER).text
        assert header == 'Начинки'

    def test_go_to_sauces_in_constructor(self, driver_login):
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_SECTION_SAUCES)))
        driver_login.find_element(*StellarBurgersLocators.CONSTRUCTOR_SECTION_SAUCES).click()

        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAUCES_HEADER)))

        header = driver_login.find_element(*StellarBurgersLocators.SAUCES_HEADER).text
        assert header == 'Соусы'

    def test_go_to_buns_in_constructor(self, driver_login):
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.CONSTRUCTOR_SECTION_BUNS)))
        driver_login.find_element(*StellarBurgersLocators.CONSTRUCTOR_SECTION_SAUCES).click()
        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.SAUCES_HEADER)))
        driver_login.find_element(*StellarBurgersLocators.CONSTRUCTOR_SECTION_BUNS).click()

        (WebDriverWait(driver_login, 10)
         .until(expected_conditions.visibility_of_element_located(StellarBurgersLocators.BUNS_HEADER)))

        header = driver_login.find_element(*StellarBurgersLocators.BUNS_HEADER).text
        assert header == 'Булки'
