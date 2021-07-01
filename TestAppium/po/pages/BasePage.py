import allure
from appium.webdriver.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), "截个图", allure.attachment_type.PNG)