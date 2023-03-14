from pages import page_selectors
from pages.base_page import BasePage


class AuthPage(BasePage):
    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        super().__init__(browser)
        self.url = self.url + "/auth"
        self.select = page_selectors.AuthPage

    def fill_login_field(self, text):
        self.set_text(self.select.LOGIN_FIELD, text)

    def click_sign_in(self):
        self.click_element(self.select.SIGN_IN_BTN)