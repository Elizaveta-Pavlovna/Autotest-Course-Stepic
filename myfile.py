from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import math

browser = webdriver.Chrome()


try:
    browser.get("http://selenium1py.pythonanywhere.com/")

    content = browser.find_element(By.XPATH, "//span[contains(@class, 'btn-group')]/a")
    content.click()
    text_empty = browser.find_element(By.XPATH,"//div[@id='content_inner']/p").text

    #basket_sum = browser.find_element(By.XPATH,"//div[contains(@class,'alertinner')]/p/strong").text

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

print(text_empty == 'Ваша корзина пуста Продолжить покупки')

