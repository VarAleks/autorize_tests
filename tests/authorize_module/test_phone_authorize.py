import pytest

from tests.authorize_module.test_authorize_base import TestAuthorizeBase


def valid_phone_data():
    return ["+79312562325",
            "+393509809407",
            "+212628612646"]


class TestClass(TestAuthorizeBase):
    @pytest.mark.parametrize('data', valid_phone_data())
    def test_valid_phone_authorize(self, auth_page, reg_page, data):
        auth_page.click_phone_tab()
        reg_page.fill_phone_filed(data)
        auth_page.click_sign_in()
        reg_page.should_be_sms_password_page(data)
