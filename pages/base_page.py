from selenium.webdriver import Keys

from services.assert_exception import AssertException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from services.wait_service import WaitService


class BasePage:
    """
    Базовый класс всех страниц, содержащий общие методы для всех страниц. Не имеет url.
    """
    ELEM_TIMEOUT = 30

    def __init__(self, browser):
        """
        :param browser: браузер, в котором будет работать страница
        """
        self._browser = browser
        if browser is not None:
            self.url = browser.browser_config.get_browser_base_url()

    def open(self):
        """
        Открывает страницу по собственному url.
        """
        return self.open_url(self.url)

    def open_url(self, url):
        """
        Открывает заданный url на странице.

        :param url: открываемый url
        """
        if "http" not in url:
            url = "http://" + url
        self._browser.get_driver().get(url)
        return self

    def find_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Ищет элемент в течение заданного интервала.

        :param selector: селектор
        :param timeout: интервал, в течение которого элемент будет переискиваться, если не был сразу найден
        :return: найденный элемент, или исключение с причиной, почему элемент не найден
        """
        locator = self.get_locator(selector)
        return WaitService(timeout=timeout, ignored_except=WebDriverException).until(
            lambda driver: driver.find_element(*locator), "Ошибка при поиске элемента.",
            self._browser.get_driver())

    def click_element(self, selector, timeout=ELEM_TIMEOUT):
        """
        Кликает на элемент.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут предприниматься попытки кликнуть на элемент
        """

        def click_element(driver):
            web_elem = driver.find_element(*self.get_locator(selector))
            if web_elem.get_attribute("disabled") is None:
                web_elem.click()
                return True
            else:
                raise WebDriverException("Element {0} is disabled".format(selector))

        self.elem_act_until(click_element, timeout)

    def elem_act_until(self, elem_func, timeout=ELEM_TIMEOUT):
        """
        Вызывает функцию elem_func в течение интервала, игнорируя все исключения.
        Если функция не вернула значение, выбрасывает исключение.

        :param timeout: таймаут, в течение которого будет вызываться elem_func
        :param elem_func: функция без аргументов, которая будет вызываться
        """
        return WaitService(timeout=timeout, ignored_except=Exception). \
            until(elem_func, "Ошибка при взаимодействии с элементом.", self._browser.get_driver())

    def set_text(self, selector, text, timeout=ELEM_TIMEOUT):
        """
        Устанавливает текст в элемент.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут придприниматься попытки установить текст в элемент
        :param text: устанавливаемый текст
        """

        def set_text(driver):
            web_element = driver.find_element(*self.get_locator(selector))
            web_element.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
            web_element.send_keys(text)
            return True

        self.elem_act_until(set_text, timeout)

    def send_text(self, selector, text, timeout=ELEM_TIMEOUT):
        """
        Отправляет текст в элемент, не очищая его.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут придприниматься попытки установить текст в элемент
        :param text: устанавливаемый текст
        """

        def send_text(driver):
            web_element = driver.find_element(*self.get_locator(selector))
            web_element.send_keys(text)
            return True

        self.elem_act_until(send_text, timeout)

    def clear_input(self, selector, timeout=ELEM_TIMEOUT):
        """
        Очищает поле input.

        :param selector: селектор
        :param timeout: интервал, в течение которого будут придприниматься попытки установить текст в элемент
        """

        def clear_input(driver):
            web_element = driver.find_element(*self.get_locator(selector))
            web_element.send_keys(Keys.CONTROL + "a" + Keys.DELETE)
            return True

        self.elem_act_until(clear_input, timeout)

    def is_presence(self, selector, timeout=ELEM_TIMEOUT):
        """
        Проверяет в течение интервала, если ли элемент на странице.
        Если за интервал элемент не появился на странице, выбрасывает Exception.

        :param selector: селектор
        :param timeout: таймаут, в течение которого будет проверяться присутствие элемента, пока он не появится
        """

        def is_presence(driver):
            driver.find_element(*self.get_locator(selector))
            return True

        try:
            return self.elem_act_until(is_presence, timeout)
        except Exception as ex:
            raise Exception(
                "Проверка присутствия элемента {1} на странице провалилась. {0} ".format(ex.args[0], selector))

    def get_element_text(self, selector, timeout=ELEM_TIMEOUT):
        """
        :param selector: селектор
        :param timeout: таймаут, в течение которого будет ожидаться появление элемента на странице
        :return текст, внутри элемента (inner text)
        """
        return self.find_element(selector, timeout).text

    def get_attribute(self, selector, attr, timeout=ELEM_TIMEOUT):
        """
        Возвращает значение атрибута.

        :param selector: селектор
        :param attr: атрибут, значение которого надо возвратить
        :param timeout: таймаут, в течение которого будет ожидаться появление элемента на странице
        """
        return self.find_element(selector, timeout).get_attribute(attr)

    def wait_text_appear(self, selector, expected, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока текстовое содержимое элемента не будет равно ожидаемому тексту.

        :param selector: селектор
        :param expected: ожидаемый текст
        :param timeout: максимальное время ожидания
        """

        def wait_text_appear(driver):
            actual = self.get_element_text(selector, 0).replace('\n', '').strip()
            act_normalize = actual.replace(' ', '')
            if exp_normalize == act_normalize:
                return AssertException(expected, expected)
            else:
                raise AssertException(expected, actual)

        try:
            expected = expected.replace('\n', '').strip()
            exp_normalize = expected.replace(' ', '')
            return self.elem_act_until(wait_text_appear, timeout)
        except Exception as ex:
            if isinstance(ex.args[1], AssertException):
                return ex.args[1]
            else:
                return AssertException(expected, ex)

    def wait_contain_text(self, selector, expected, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока текстовое содержимое элемента не будет содержать ожидаемый текст.

        :param selector: селектор
        :param expected: ожидаемый текст
        :param timeout: максимальное время ожидания
        """

        def wait_contain_text(driver):
            actual = self.get_element_text(selector, 0).replace('\n', '').strip()
            act_normalize = actual.replace(' ', '')
            if exp_normalize in act_normalize:
                return AssertException(expected, expected)
            else:
                raise AssertException(expected, actual)

        try:
            expected = expected.replace('\n', '').strip()
            exp_normalize = expected.replace(' ', '')
            return self.elem_act_until(wait_contain_text, timeout)
        except Exception as ex:
            if isinstance(ex.args[1], AssertException):
                return ex.args[1]
            else:
                return AssertException(expected, ex)

    def wait_input_value(self, selector, expected_value, timeout=ELEM_TIMEOUT):
        """
        Ожидание, пока значение атрибута value не будет равно expected_value.

        :param selector: селектор
        :param expected_value: ожидаемое значение атрибута
        :param timeout: максимальное время ожидания
        """

        def wait_input_value(driver):
            actual_value = self.get_attribute(selector, 'value', 0)
            if expected_value == actual_value:
                return AssertException(expected_value, expected_value)
            else:
                raise AssertException(expected_value, actual_value)

        try:
            return self.elem_act_until(wait_input_value, timeout)
        except Exception as ex:
            if isinstance(ex.args[1], AssertException):
                return ex.args[1]
            else:
                return AssertException(expected_value, ex)

    def assert_page_load(self, selector, page_name, after_actions, timeout=ELEM_TIMEOUT):
        """
        Ожидание и проверка, что страница загрузилась.
        """
        pass
        self.assert_presence(selector, \
                             "Страница '{0}' не открыта после {1}".format(page_name, after_actions), timeout)

    def assert_presence(self, selector, msg="", timeout=ELEM_TIMEOUT):
        """
        Ожидание и проверка присутсвия элемента на странице в течение таймаута.

        :param selector: селектор
        :param msg: сообщение, в случае отсутствия элемента на странице
        :param timeout: максимальное время ожидания
        :return: raise AssertionError если элемент не был найден за интервал timeout
        """
        try:
            self.is_presence(selector, timeout)
        except Exception as ex:
            raise AssertionError("{0}\n{1}".format(msg, ex.args[0]))

    def assert_exp_act(self, assert_exception, msg=""):
        """
        Проверка результата ожидания на странице.

        :param assert_exception: объект классса AssertException, возвращаемый методами not_url_page.wait...
        :param msg: сообщение, выдаваемое в случае несовпадения ожидаемого значения и фактического
        """
        assert assert_exception.expected == assert_exception.actual, msg + assert_exception.assert_msg

    def get_browser(self):
        return self._browser

    def get_url(self):
        return self._browser.get_driver().current_url

    def get_locator(self, selector):
        """
        :param selector: селектор
        :return: tuple - (как искать, селектор), созданный из поданного в качестве параметра селектора
        """
        if selector[0] == "/":
            return By.XPATH, selector
        else:
            return By.CSS_SELECTOR, selector
