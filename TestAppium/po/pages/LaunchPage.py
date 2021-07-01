from TestAppium.po.pages.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from utils.elements import AppiumElement


class LaunchPage(BasePage):
    contact = AppiumElement('//*[@text="通讯录"]')

    def goto_contact(self):
        from TestAppium.po.pages.ContactPage import ContactPage
        self.contact.click()
        return ContactPage(self.driver)
