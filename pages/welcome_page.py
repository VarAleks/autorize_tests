from pages import page_selectors
from pages.auth_page import AuthPage


class WelcomePage(AuthPage):
    """
    Страница ввода пароля при авторизации по логину или email.
    """

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = self.url + "/welcome"
        self.select = page_selectors.WelcomePage

    def fill_password_field(self, paswrd):
        self.set_text(self.select.INPUT_PASSWORD, paswrd)

    def should_be_password_page(self, login):
        """
        Проверка, что мы находимся на странице ввода пароля.
        :param login: логин или email, по которому мы авторизовались
        """
        self.assert_page_load(self.select.WELCOME_PAGE_ATTR, "Ввода пароля",
                              "попытки входа по корректному логину: '{0}'".format(login), 3)
