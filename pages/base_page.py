from selenium.common.exceptions import NoSuchElementException

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