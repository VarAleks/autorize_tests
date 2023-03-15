import pytest

from tests.authorize_module.test_authorize_base import TestAuthorizeBase


def valid_phone_data():
    return ["+79312562325",
            "+393509809407",
            "+212628612646",
            "89090035386"]


class TestPhoneValidationField(TestAuthorizeBase):
    """
    Валидация поля номер телефона
    """
    @pytest.mark.parametrize('data', valid_phone_data())
    def test_phone_field_valid_data(self, auth_page, reg_page, data):
        """
        заполнение поля номер телефона допустимыми данными
        """
        auth_page.click_phone_tab()
        auth_page.fill_phone_field(data)
        auth_page.click_sign_in()
        reg_page.should_be_sms_password_page(data)

    def test_phone_field_invalid_data(self, auth_page):
        """
        заполнение поля номер телефона недопустимыми данными
        """
        auth_page.click_phone_tab()
        input_str = """rпZЙ!#$%^:&*()+-*\/'"{}[]`~|№;?_=<>,"""
        for char in input_str:
            auth_page.send_char_to_phone_filed(char)
            auth_page.should_be_only_chars_in_phone_field("+7",
                                                          "Ожидалось что после ввода символа '{0}' в поле номера, поле будет содержать только {1}".format(
                                                              char, "+7"))

    def test_phone_field_with_space(self, auth_page):
        """
        заполнение поля номер телефона двумя пустыми пробелами
        """
        auth_page.click_phone_tab()
        auth_page.clear_phone_field()
        auth_page.send_char_to_phone_filed(" ")
        auth_page.send_char_to_phone_filed(" ")
        auth_page.should_be_only_chars_in_phone_field("+",
                                                      "Ожидалось что после ввода пробела в поле номера, поле будет содержать только +")

    def test_empty_phone_field(self, auth_page):
        """
        проверка валидации пустого поля номер телефона
        """
        auth_page.click_phone_tab()
        auth_page.clear_phone_field()
        auth_page.click_sign_in()
        auth_page.should_be_invalid_phone_alert()

    def test_short_value_in_phone_field(self, auth_page):
        """
        ввод номера телефона неполной длины
        """
        auth_page.click_phone_tab()
        auth_page.fill_phone_field("+7909003555")
        auth_page.click_sign_in()
        auth_page.should_be_invalid_phone_alert()

    def test_overflow_phone_field(self, auth_page):
        """
        ввод номера телефона избыточной длины
        """
        input_number = "+7909003555555556"
        auth_page.click_phone_tab()
        auth_page.fill_phone_field(input_number)
        auth_page.click_sign_in()
        auth_page.should_be_only_chars_in_phone_field("+7 (909) 003-55-555555",
                                                      "После ввода номера {0} избыточной длины не сработала валидация поля номера телефона".format(
                                                          input_number))
