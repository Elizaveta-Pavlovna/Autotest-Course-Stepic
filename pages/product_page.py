from pages.base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        link.click()
        time.sleep(1)
        self.solve_quiz_and_get_code()
        time.sleep(1)
        product_name2 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME2).text
        basket_sum = self.browser.find_element(*ProductPageLocators.BASKET_SUM).text
        assert product_price == basket_sum, "prices are not equal"
        assert product_name == product_name2, "products are not equal"