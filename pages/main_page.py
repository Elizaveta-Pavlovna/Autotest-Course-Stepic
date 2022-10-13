from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
import time

# Этот класс является наследником класса BasePage, второй в своб очередь называется для MainPager класс-предок
class MainPage(BasePage):
    # Так как браузер у нас хранится как аргумент класса BasePage,
    # обращаться к нему нужно соответствующим образом с помощью self
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    # метод __init__ вызывается при создании объекта. Конструктор выше с ключевым словом super на самом деле только
    # вызывает конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор MainPage.

