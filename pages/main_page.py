from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

# Этот класс является наследником класса BasePage, второй в своб очередь называется для MainPager класс-предок
class MainPage(BasePage):
    # Так как браузер у нас хранится как аргумент класса BasePage,
    # обращаться к нему нужно соответствующим образом с помощью self
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        time.sleep(2)
