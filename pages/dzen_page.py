from pages import page_selectors
from pages.auth_page import AuthPage
from pages.base_page import BasePage


class DzenPage(BasePage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = "dzen.ru"
        self.select = page_selectors.DzenPage

    def click_profile(self):
        self.click_element(self.select.PROFILE_ELEMENT)

    def should_be_profile_authorize(self, profile_login):
        self.assert_exp_act(self.wait_contain_text(self.select.PROFILE_TEXT_CONTENT, profile_login),
                            "Не был найден авторизованный профиль пользователя после попытки авторизации")
