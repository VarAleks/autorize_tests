from pages import page_selectors
from pages.auth_page import AuthPage
from pages.base_page import BasePage


class RestorePage(AuthPage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = self.url + "/welcome"

    def should_be_restore_page(self):
        self.assert_exp_act(self.wait_contain_text(page_selectors.AuthPage.TITLE,
                                                   "Введите номер телефона, который был привязан к вашему Яндекс ID"),
                            "Страница восстановления пароля не открылась. Текст на странице не был обнаружен.")
