from selenium.webdriver.common.by import By


class StellarBurgersLocators:

    REGISTRATION_NAME_FIELD = (
        By.XPATH, "//label[text()='Имя']/parent::div/input"
    )  #  поле "Имя" на странице регистрации

    REGISTRATION_EMAIL_FIELD = (
        By.XPATH, "//label[text()='Email']/parent::div/input"
    )  # поле Email на странице регистрации

    REGISTRATION_PASS_FIELD = (
        By.XPATH, "//label[text()='Пароль']/parent::div/input"
    )  # поле Пароль на странице регистрации

    REGISTRATION_BUTTON = (
        By.XPATH, ".//button[text() = 'Зарегистрироваться']"
    )  # кнопка Зарегистрироваться на странице регистрации

    LOGIN_PAGE_TITLE = (
        By.XPATH, '//h2[text()="Вход"]'
    )  # заголовок "Вход" на странице авторизации

    REGISTRATION_PASSWORD_ERROR = (
        By.XPATH, ".//p[@class='input__error text_type_main-default']"
    )  # сообщение об ошибке Некорректный пароль при регистрации

    MAIN_PAGE_LOGIN_BUTTON = (
        By.XPATH, './/button[text()="Войти в аккаунт"]'
    )  # кнопка "Войти" в аккаунт на главной странице

    MAIN_PAGE_PERSONAL_ACCOUNT_BUTTON = (
        By.XPATH, './/p[text()="Личный Кабинет"]'
    )  # кнопка "Личный кабинет" в аккаунт на главной странице

    LOGIN_PAGE_LOGIN_FIELD = (
        By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @ name="name"]'
    )  # поле для ввода логина на странице авторизации

    LOGIN_PAGE_PASSWORD_FIELD = (
        By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @ name="Пароль"]'
    )  # поле для ввода пароля на странице авторизации

    LOGIN_PAGE_LOGIN_BUTTON = (
        By.XPATH, './/h2[text()="Вход"]/parent::div//button[text()="Войти"]'
    )  # кнопка Войти на странице авторизации

    ACCOUNT_PAGE_PLACE_ORDER_BUTTON = (
        By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'
    )  # кнопка оформить заказ в личном кабинете

    REGISTRATION_PAGE_LOGIN_LINK = (
        By.XPATH, './/p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'
    )  # ссылка Войти на странице регистрации

    FORGOT_PASS_PAGE_LOGIN_LINK = (
        By.XPATH, './/p[text()="Вспомнили пароль?"]/a[text()="Войти"]'
    ) #  ссылка Войти на странице восстановления пароля

    PROFILE_LOGIN_FIELD = (
        By.XPATH, ".//input[@value='dmitrypuzanov7000@ya.ru']"
    )  # поле Логин в профиле пользователя

    PROFILE_PAGE_DESCRIPTION = (
        By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']"
    )

    CONSTRUCTOR_BUTTON = (
        By.XPATH, './/p[contains(@class, "AppHeader") and text()="Конструктор"]'
    )  # кнопка Конструктор

    LOGO = (
        By.XPATH, './/div[contains(@class, "AppHeader_header__logo")]//a[@href="/"]'
    )  # Логотип

    LOGOUT_BUTTON = (
        By.XPATH, './/button[contains(@class, "Account") and text()="Выход"]'
    )  # кнопка Выход

    CONSTRUCTOR_SECTION_BUNS = (
        By.XPATH, './/section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Булки"]/parent::div'
    )  # раздел Конструктора Булки

    CONSTRUCTOR_SECTION_SAUCES = (
        By.XPATH, './/section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Соусы"]/parent::div'
    )  # раздел Конструктора Соусы

    CONSTRUCTOR_SECTION_FILLINGS = (
        By.XPATH, './/section[contains(@class, "BurgerIngredients_ingredients")]//span[text()="Начинки"]/parent::div'
    )  # раздел Конструктора Начинки

    FILLINGS_HEADER = (
        By.XPATH, './/h2[text()="Начинки"]'
    )  # заголовок Начинки

    SAUCES_HEADER = (
        By.XPATH, './/h2[text()="Соусы"]'
    )  # заголовок Соусы

    BUNS_HEADER = (
        By.XPATH, './/h2[text()="Булки"]'
    )  # заголовок Булки


