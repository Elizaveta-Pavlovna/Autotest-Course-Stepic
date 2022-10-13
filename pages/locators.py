from selenium.webdriver.common.by import By
# Когда мы выносим селекторы в отдельную сущность,
# мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.

# каждый селектор — это пара: как искать и что искать.
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# comment com+/
class LoginPageLocators():
   LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
   REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form")
    PRODUCT_PRICE = (By.CLASS_NAME, "price_color")
    BASKET_SUM = (By.XPATH, "//div[contains(@class,'alertinner')]/p/strong")
    PRODUCT_NAME = (By.XPATH,"//div[contains(@class,'product_main')]/h1")
    PRODUCT_NAME2 = (By.XPATH,"//div[contains(@class,'alertinner')]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
