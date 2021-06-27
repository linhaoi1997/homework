import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from .BasePage import BasePage
from ..elements import Element, Elements
from faker import Faker

fake = Faker("zh-CN")


class AddContactLoactor:
    add_button = (By.XPATH, "//div[@class='js_has_member']//a[text()='添加成员']")
    name_input = (By.ID, "username")
    en_name_input = (By.ID, "memberAdd_english_name")
    accid = (By.ID, "memberAdd_acctid")
    man = (By.XPATH, "//input[@value='1']")
    woman = (By.XPATH, "//input[@value='2']")
    mobile = (By.NAME, "mobile")
    save = (By.XPATH, "//a[text()='保存']")
    add_department_button = (By.CSS_SELECTOR, ".member_colLeft_top_addBtn")
    departments = (By.XPATH, "//div[@class='member_colLeft_bottom']//li/a")


class AddContactPage(BasePage):
    add_button = Element(*AddContactLoactor.add_button)
    name_input = Element(*AddContactLoactor.name_input)
    en_name_input = Element(*AddContactLoactor.en_name_input)
    accid = Element(*AddContactLoactor.accid)
    man = Element(*AddContactLoactor.man)
    woman = Element(*AddContactLoactor.woman)
    mobile = Element(*AddContactLoactor.mobile)
    save = Element(*AddContactLoactor.save)
    add_department_button = Element(*AddContactLoactor.add_department_button)
    departments = Elements(*AddContactLoactor.departments)

    def op_create_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AddContactLoactor.add_button)
        )
        for i in range(10):
            self.add_button.click()
            time.sleep(1)
            if not self.add_button.is_displayed():
                break

    def add_person(self, **kwargs):
        phone = fake.phone_number() if not kwargs.get("phone") else kwargs.get("phone")
        self.name_input = fake.name()
        self.en_name_input = fake.name()
        self.accid = fake.iana_id()
        self.mobile = phone
        self.save.click()
        for key, value in kwargs.items():
            ele = getattr(self, key)
            ele = value
            # setattr(self, key, value)
        return phone

    def exist(self, name):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, f"//td[@title='{name}']"))
            )
            return True
        except TimeoutException as e:
            return False

    def op_add_department_page(self):
        from .DepartmentPage import AddDepartmentPage
        self.add_department_button.click()
        return AddDepartmentPage(self.driver)

    @property
    def departments_names(self):
        return [i.text for i in self.departments]
