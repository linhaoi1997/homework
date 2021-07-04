from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy as By
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium.webdriver.support.wait import WebDriverWait


class Element(object):
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
        element.send_keys(value)

    def __get__(self, instance, owner) -> WebElement:
        return self._handle(instance)


class Elements(Element):
    def _handle(self, instance):
        driver = instance.driver
        return WebDriverWait(driver, self.wait_time).until(
            lambda d: driver.find_elements(*self.locator)
        )

    def __get__(self, instance, owner) -> list:
        return self._handle(instance)


class ScrollLocatedElement(Element):
    def __init__(self, *args, wait_time=20, try_number=10):
        super(ScrollLocatedElement, self).__init__(*args, wait_time=wait_time)
        self.num = try_number

    def _handle(self, instance):
        driver = instance.driver
        for i in range(self.num):
            try:
                return WebDriverWait(driver, 1).until(
                    lambda d: driver.find_element(*self.locator)
                )
            except TimeoutException:
                instance.scroll()
            if i == self.num - 1:
                raise NoSuchElementException
