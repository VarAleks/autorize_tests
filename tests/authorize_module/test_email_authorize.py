from tests.authorize_module.test_authorize_base import TestAuthorizeBase
from tests.test_base import TestBase


class TestEmailAuthorize(TestAuthorizeBase):

    def test_existing_email_authorize(self, auth_page, welcome_page, dzen_page):
        login = "zxcvbnm-5.asdfghjklqwertyuiop"
        auth_page.click_email_tab()
        auth_page.fill_login_field(login + "@yandex.ru")
        auth_page.click_sign_in()
        welcome_page.fill_password_field("eoun998922")
        auth_page.click_sign_in()
        dzen_page.click_profile()
        dzen_page.should_be_profile_authorize(login)

    def test_non_existing_email_authorize(self, auth_page):
        email = "zxcvbnm-5-asdfghjklqwtyuiop@yandex.ru"
        auth_page.click_email_tab()
        auth_page.fill_login_field(email)
        auth_page.click_sign_in()
        auth_page.should_be_non_existing_account_alert()
