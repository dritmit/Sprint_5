import random


def random_name():
    new_name = f'dmitrypuzanov7{random.randint(100,999)}@burger.com'
    return new_name

def random_password():
    chars = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    length = 8
    new_password = ''
    for i in range(length):
        new_password += random.choice(chars)

    return new_password


URL = 'https://stellarburgers.nomoreparties.site/'

NEW_NAME = random_name()
NEW_PASSWORD = random_password()

NAME = 'dmitry'
EMAIL = 'dmitrypuzanov7000@ya.ru'
PASSWORD = '1qaz2wsx'

WRONG_NAME = 'wrongname'
WRONG_EMAIL = 'wrongmail@ya.com'
WRONG_PASSWORD = '123'
