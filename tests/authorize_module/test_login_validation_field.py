import pytest

from pages.welcome_page import WelcomePage
from tests.authorize_module.test_authorize_base import TestAuthorizeBase


def valid_login_data():
    return ["zxcvbnmasdfghjklqwertyuiop",
            "zxcvbnm-asdfghjklqwertyuiop",
            "zxcvbnmasdfghjklqwertyuiop1",
            "zxcvbnm.asdfghjklqwertyuiop",
            "1234567890",
            "zxcvbnm-5-asdfghjklqwertyuiop"
            ]


class TestLoginValidationField(TestAuthorizeBase):

    @pytest.mark.parametrize('data', valid_login_data())
    def test_login_field_valid_data(self, browser, auth_page, data):
        auth_page.fill_login_field(data)
        auth_page.click_sign_in()
        WelcomePage(browser).should_be_password_page(data)

    # def test_login_field_invalid_data(self):
    #     pass
