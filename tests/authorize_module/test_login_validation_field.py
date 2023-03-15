import pytest

from pages.welcome_page import WelcomePage
from tests.authorize_module.test_authorize_base import TestAuthorizeBase


def valid_login_data():
    return ["zxcvbnmasdfghjklqwertyuiop",
            "zxcvbnm-asdfghjklqwertyuiop",
            "zxcvbnmasdfghjklqwertyuiop1",
            "zxcvbnm.asdfghjklqwertyuiop",
            "1234567890",
            "zxcvbnm-5-asdfghjklqwertyuiop"]


def invalid_login_data():
    return ["абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
            """!#$%^:&*()+-*\/'"{}[]`~|№;?_=<>,""",
            "1varaxin.aleks",
            ".varaxin.aleks",
            "varaxin.aleks.",
            "-varaxin.aleks",
            "varaxin.aleks-"]


class TestLoginValidationField(TestAuthorizeBase):

    @pytest.mark.parametrize('data', valid_login_data())
    def test_login_field_valid_data(self, auth_page, welcome_page, data):
        auth_page.click_email_tab()
        auth_page.fill_login_field(data)
        auth_page.click_sign_in()
        welcome_page.should_be_password_page(data)

    @pytest.mark.parametrize('data', invalid_login_data())
    def test_login_field_invalid_data(self, auth_page, data):
        auth_page.click_email_tab()
        auth_page.fill_login_field(data)
        auth_page.click_sign_in()
        auth_page.should_be_invalid_login_alert()

    def test_login_field_with_space_symbol(self, auth_page):
        auth_page.click_email_tab()
        auth_page.fill_login_field(" ")
        auth_page.click_sign_in()
        auth_page.should_be_empty_login_alert()

    def test_login_field_empty_data(self, auth_page):
        auth_page.click_email_tab()
        auth_page.click_sign_in()
        auth_page.should_be_empty_login_alert()
