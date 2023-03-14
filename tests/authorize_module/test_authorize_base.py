import pytest as pytest

from pages.auth_page import AuthPage
from tests.test_base import TestBase


class TestAuthorizeBase(TestBase):

    @pytest.fixture
    def auth_page(self, browser):
        return AuthPage(browser).open()
