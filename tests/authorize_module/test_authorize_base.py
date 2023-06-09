import pytest as pytest

from pages.auth_page import AuthPage
from pages.dzen_page import DzenPage
from pages.reg_page import RegPage
from pages.restore_page import RestorePage

from pages.welcome_page import WelcomePage
from tests.test_base import TestBase


class TestAuthorizeBase(TestBase):
    """
    Базовый класс для тестов на авторизацию.
    """

    @pytest.fixture
    def auth_page(self, browser):
        return AuthPage(browser).open()

    @pytest.fixture
    def welcome_page(self, browser):
        return WelcomePage(browser)

    @pytest.fixture
    def reg_page(self, browser):
        return RegPage(browser)

    @pytest.fixture
    def dzen_page(self, browser):
        return DzenPage(browser)

    @pytest.fixture
    def restore_page(self, browser):
        return RestorePage(browser)
