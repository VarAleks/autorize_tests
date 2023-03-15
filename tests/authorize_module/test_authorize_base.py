import pytest as pytest

from pages.auth_page import AuthPage
from pages.reg_page import RegPage

from pages.welcome_page import WelcomePage
from tests.test_base import TestBase


class TestAuthorizeBase(TestBase):

    @pytest.fixture
    def auth_page(self, browser):
        return AuthPage(browser).open()

    @pytest.fixture
    def welcome_page(self, browser):
        return WelcomePage(browser)

    @pytest.fixture
    def reg_page(self, browser):
        return RegPage(browser)
