from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from .BasePage import BasePage
from ..elements import Elements, Element


class AddDepartmentLocator:
    add_department_link = (By.CSS_SELECTOR, ".js_create_party")
    department_name = (By.NAME, "name")
    parent = (By.CSS_SELECTOR, ".js_parent_party_name")
    parent_options = (By.XPATH, "//div[label='所属部门']//li/a")
    submit = (By.XPATH, "//a[@d_ck='submit']")
    tip = (By.ID, "js_tips")


class AddDepartmentPage(BasePage):
    add_department_link = Element(*AddDepartmentLocator.add_department_link)
    department_name = Element(*AddDepartmentLocator.department_name)
    parent = Element(*AddDepartmentLocator.parent)
    parent_options = Elements(*AddDepartmentLocator.parent_options)
    submit = Element(*AddDepartmentLocator.submit)
    tip = Element(*AddDepartmentLocator.tip)

    def add_department(self, name, parent):
        self.add_department_link.click()
        self.department_name = name
        self.parent.click()
        for option in self.parent_options:
            if option.text == parent:
                option.click()
            self.submit.click()
            return self.tip_message
        else:
            return False

    @property
    def tip_message(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(self.tip))
        return self.tip.text
