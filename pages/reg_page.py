from pages import page_selectors
from pages.auth_page import AuthPage
from pages.base_page import BasePage


class RegPage(AuthPage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = self.url + "/reg"
        self.select = page_selectors.RegPage

    def should_be_sms_password_page(self, phone):
        self.assert_page_load(self.select.REG_PAGE_ATTR, "Ввода одноразового пароля СМС",
                              "попытки входа по корректному номеру телефона: '{0}'".format(phone), 3)
