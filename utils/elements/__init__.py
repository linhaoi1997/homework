from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


def Clear(element):
    element.clear()
    element.send_keys(Keys.ARROW_DOWN)
    while element.get_attribute("value"):
        element.send_keys(Keys.BACKSPACE)


class BaseElement(object):
    def __init__(self, *args, wait_time=20):
        self.wait_time = wait_time
        if len(args) == 1:
            args = [By.XPATH, args[0]]
        self.locator = args

    def _handle(self, instance):
        driver = instance.driver
        return WebDriverWait(driver, self.wait_time).until(
            lambda d: driver.find_element(*self.locator)
        )

    def __set__(self, instance, value):
        element = self._handle(instance)
        Clear(element)
        element.send_keys(value)

    def __get__(self, instance, owner) -> WebElement:
        return self._handle(instance)


class Element(BaseElement): pass


class Elements(BaseElement):
    def _handle(self, instance):
        driver = instance.driver
        return WebDriverWait(driver, self.wait_time).until(
            lambda d: driver.find_elements(*self.locator)
        )

    def __get__(self, instance, owner) -> list:
        return self._handle(instance)


class AppiumElement(BaseElement):

    def __set__(self, instance, value):
        element = self._handle(instance)
        element.send_keys(value)
