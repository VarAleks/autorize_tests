import pytest

from tests.authorize_module.test_authorize_base import TestAuthorizeBase
from tests.test_base import TestBase


def valid_email_data():
    return ["zxcvbnm-5-asdfghjklqwertyuiop@yandex.ru",
            "zxcvbnm-5-asdfghjklqwertyuiop@яндекс.рф"]


def invalid_email_data():
    return ["zxcvbnm-5-asdfghjklqwertyuiopyandex.ru",
            "zxcvbnm-5-asdfghjklqwertyuiop@yandexru",
            "zxcvbnm-5-asdfghjklqwertyuiop@яндексрф",
            "zxcvbnm-5-asdfghjklqwertyuiop@yandex",
            "zxcvbnm-5-asdfghjklqwertyuiop@.ru",
            "zxcvbnm-5-asdfghjklqwertyuiop@"]


class TestEmailValidationField(TestAuthorizeBase):
    @pytest.mark.parametrize('data', valid_email_data())
    def test_email_field_valid_data(self, auth_page, welcome_page, data):
        auth_page.click_email_tab()
        auth_page.fill_login_field(data)
        auth_page.click_sign_in()
        welcome_page.should_be_password_page(data)

    @pytest.mark.parametrize('data', invalid_email_data())
    def test_email_field_invalid_data(self, auth_page, data):
        auth_page.click_email_tab()
        auth_page.fill_login_field(data)
        auth_page.click_sign_in()
        auth_page.should_be_invalid_login_alert()
