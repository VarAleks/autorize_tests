import urllib
from flask import Flask
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

    def open(self):
        self._browser.get_driver()
        return super().open_url("https://" + self.url + "/add?origin=dzen&retpath=https://dzen.ru/")

    def fill_login_field(self, text):
        self.set_text(self.select.LOGIN_FIELD, text)

    def fill_phone_field(self, number):
        self.set_text(self.select.PHONE_FIELD, number)

    def send_char_to_phone_filed(self, char):
        self.send_text(self.select.PHONE_FIELD, char)

    def clear_phone_field(self):
        self.clear_input(self.select.PHONE_FIELD)

    def click_sign_in(self):
        self.click_element(self.select.SIGN_IN_BTN)

    def click_email_tab(self):
        self.click_element(self.select.LOGIN_TAB)

    def click_phone_tab(self):
        self.click_element(self.select.PHONE_TAB)

    def click_restore_link(self):
        self.click_element(self.select.RESTORE_LINK)

    def should_be_only_chars_in_phone_field(self, expected_chars, msg):
        self.assert_exp_act(self.wait_input_value(self.select.PHONE_FIELD, expected_chars, 2), msg)

    def should_be_empty_phone_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.PHONE_ALERT,
                                  "Паспорт не смог обработать запрос. Попробуйте позднее или обновите страницу.", 2),
            "Не сработала валидация на пустое поле номера телефона. Не вывелось предупредительное сообщение.")

    def should_be_invalid_phone_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.PHONE_ALERT, "Недопустимый формат номера", 2),
            "Не сработала валидация на пустое поле номера телефона. Не вывелось предупредительное сообщение.")

    def should_be_non_existing_account_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.LOGIN_ALERT, "Такого аккаунта нет", 2),
            "Не сработала валидация при попытке войти под несуществующим аккаунтом")

    def should_be_invalid_login_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.LOGIN_ALERT, "Такой логин не подойдет", 2),
            "Не сработала валидация на корректность введенного значения в поле логин. Не вывелось предупредительное сообщение.")

    def should_be_empty_login_alert(self):
        self.assert_exp_act(
            self.wait_text_appear(self.select.LOGIN_ALERT, "Логин не указан", 2),
            "Не сработала валидация на пустые данные в поле логин. Не вывелось предупредительное сообщение.")
