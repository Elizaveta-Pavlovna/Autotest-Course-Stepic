from selenium.webdriver.common.by import By
# Когда мы выносим селекторы в отдельную сущность,
# мы уменьшаем время на поддержку тестов и сильно упрощаем себе жизнь в долгосрочной перспективе.

# каждый селектор — это пара: как искать и что искать.
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

# comment com+/
class LoginPageLocators ():
   LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
   REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")