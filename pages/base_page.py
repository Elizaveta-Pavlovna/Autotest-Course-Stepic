from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math

class BasePage():
    #конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__
    # timeout=10 - неявное ожидание со значением по-умолчанию 10
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # open открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)

    # Здесь будем перехватывать исключение. В него будем передавать два аргумента:
    # как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Неделя 3.3.1
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")