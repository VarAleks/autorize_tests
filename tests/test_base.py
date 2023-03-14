import pytest

from browser import Browser


class TestBase:
    """
    Базовый класс для всех тестовых классов.
    Содержит методы, необходимые всем тестам.
    """

    @pytest.fixture
    def browser(self, request):
        """
        Создает браузер, автоматически закрываемый после теста.

        :return: фикстура, создающая браузер, автоматически закрываемый после теста
        """
        return self.create_browser(request)

    def create_browser(self, request, browser_config=None):
        """
        Создает браузер и закрывает его после теста.

        :param browser_config: конфигурация бразуре
        :return: браузер, автоматически закрываемый после теста
        """
        browser = Browser(browser_config)
        browser.open()

        def browser_close():
            browser.close()

        request.addfinalizer(browser_close)
        return browser
