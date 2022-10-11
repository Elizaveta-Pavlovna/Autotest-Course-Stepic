from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import time
import math

browser = webdriver.Chrome()

def solve_quiz_and_get_code():
    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")

try:
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")

    price = browser.find_element_by_class_name("price_color").text
    product_name = browser.find_element(By.XPATH,"//div[contains(@class,'product_main')]/h1").text
    browser.find_element_by_id("add_to_basket_form").click()
    solve_quiz_and_get_code()
    time.sleep(75)

    basket_sum = browser.find_element(By.XPATH,"//div[contains(@class,'alertinner')]/p/strong").text



finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

print(price, product_name, basket_sum)

