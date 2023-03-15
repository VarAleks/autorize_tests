from tests.authorize_module.test_authorize_base import TestAuthorizeBase


class TestPasswordRestore(TestAuthorizeBase):
    def test_open_password_restore_page(self, auth_page, restore_page):
        auth_page.click_email_tab()
        auth_page.click_restore_link()
        restore_page.should_be_restore_page()





