from selenium.webdriver.common.by import By
from ..elements import BaseElement

from .BasePage import BasePage


class MainLocator:
    contact = (By.ID, "menu_contacts")


class MainPage(BasePage):
    contact = BaseElement(*MainLocator.contact)

    def click_contact(self):
        from .ContactPage import AddContactPage
        self.contact.click()
        return AddContactPage(self.driver)
