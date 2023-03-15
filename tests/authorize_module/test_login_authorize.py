from tests.authorize_module.test_authorize_base import TestAuthorizeBase


class TestLoginAuthorize(TestAuthorizeBase):
    """
    Авторизация ЯНДЕКСА по логину.
    """

    def test_existing_login_authorize(self, auth_page, welcome_page, dzen_page):
        """
        авторизация по существующему логину
        """
        login = "zxcvbnm-5.asdfghjklqwertyuiop"
        auth_page.click_email_tab()
        auth_page.fill_login_field(login)
        auth_page.click_sign_in()
        welcome_page.fill_password_field("eoun998922")
        auth_page.click_sign_in()
        dzen_page.click_profile()
        dzen_page.should_be_profile_authorize(login)

    def test_non_existing_login_authorize(self, auth_page):
        """
        авторизация по несуществующему логину
        """
        login = "zxcvbnm-5-asdfghjklqwtyuiop"
        auth_page.click_email_tab()
        auth_page.fill_login_field(login)
        auth_page.click_sign_in()
        auth_page.should_be_non_existing_account_alert()
