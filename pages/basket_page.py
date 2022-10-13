from pages.base_page import BasePage
from .locators import BasketPageLocators
import time

class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_CONTENT), \
            "Basket is empty"
        assert self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET).text == 'Ваша корзина пуста Продолжить покупки'