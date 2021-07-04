import logging

import allure
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    def screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), "截个图", allure.attachment_type.PNG)

    def scroll(self):
        size = self.driver.get_window_size()
        width = size["width"]
        height = size["height"]

        start_x = width / 2
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.3

        duration = 2000
        self.driver.swipe(start_x, start_y, end_x, end_y, duration)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def scroll_and_find(self, by, value, num=5):
        driver = self.driver
        self.driver.implicitly_wait(1)
        for i in range(num):
            try:
                ele = WebDriverWait(driver, 1).until(
                    lambda d: driver.find_element(by, value)
                )
                self.driver.implicitly_wait(5)
                return ele
            except TimeoutException:
                self.scroll()
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException

    @staticmethod
    def click(ele):
        WebDriverWait(ele, 10).until(lambda x: x.is_enabled() is True)
        ele.click()

    @staticmethod
    def logging(message):
        logging.info(message)
        allure.attach(message, "log", allure.attachment_type.TEXT)

