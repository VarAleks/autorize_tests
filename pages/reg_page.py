from pages import page_selectors
from pages.auth_page import AuthPage


class RegPage(AuthPage):
    """
    Страница ввода кода из СМС.
    """

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = self.url + "/reg"
        self.select = page_selectors.RegPage

    def should_be_sms_password_page(self, phone):
        """
        Проверка, что мы находимся на странице ввода СМС кода.
        :param phone: номер телефона, который был введен на предыдущей странице при входе по номеру телефона
        """
        self.assert_page_load(self.select.REG_PAGE_ATTR, "Ввода одноразового пароля СМС",
                              "попытки входа по корректному номеру телефона: '{0}'".format(phone), 3)
