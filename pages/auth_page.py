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

    def click_email_tab(self):
        self.click_element(self.select.LOGIN_TAB)

    def click_phone_tab(self):
        self.click_element(self.select.PHONE_TAB)

    def should_be_invalid_login_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.LOGIN_ALERT, "Такой логин не подойдет", 2),
            "Не сработала валидация на корректность введенного значения в поле логин. Не вывелось предупредительное сообщение.")

    def should_be_empty_login_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.LOGIN_ALERT, "Логин не указан", 2),
            "Не сработала валидация на пустые данные в поле логин. Не вывелось предупредительное сообщение.")
