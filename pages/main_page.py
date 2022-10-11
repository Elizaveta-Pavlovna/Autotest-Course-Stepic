from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
import time

# Этот класс является наследником класса BasePage, второй в своб очередь называется для MainPager класс-предок
class MainPage(BasePage):
    # Так как браузер у нас хранится как аргумент класса BasePage,
    # обращаться к нему нужно соответствующим образом с помощью self
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        time.sleep(1)
        # alert = self.browser.switch_to.alert
        # alert.accept()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

