class BasePage():
    #конструктор — метод, который вызывается, когда мы создаем объект.
    # Конструктор объявляется ключевым словом __init__
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # open открывает нужную страницу в браузере, используя метод get()
    def open(self):
        self.browser.get(self.url)