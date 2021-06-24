import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from utils.get_driver import get_driver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
import pytest
import yaml
from faker import Faker
from run import run

fake = Faker("zh-CN")


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
        WebDriverWait(driver, self.wait_time).until(
            lambda d: driver.find_element(*self.locator)
        )
        return driver.find_element(*self.locator)

    def __set__(self, instance, value):
        element = self._handle(instance)
        Clear(element)
        element.send_keys(value)

    def __get__(self, instance, owner) -> WebElement:
        return self._handle(instance)


def get_cookies():
    d = get_driver()
    cookies = d.get_cookies()
    with open("./cookies.yaml", "w") as f:
        yaml.safe_dump(cookies, f)


def get_login_driver():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    with open("./cookies.yaml", "r") as f:
        cookies = yaml.safe_load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
    return driver


class AddContactLoactor:
    add_button = (By.XPATH, "//div[@class='js_has_member']//a[text()='添加成员']")
    name_input = (By.ID, "username")
    en_name_input = (By.ID, "memberAdd_english_name")
    accid = (By.ID, "memberAdd_acctid")
    man = (By.XPATH, "//input[@value='1']")
    woman = (By.XPATH, "//input[@value='2']")
    mobile = (By.NAME, "mobile")
    save = (By.XPATH, "//a[text()='保存']")


class AddContactPage:
    add_button = BaseElement(*AddContactLoactor.add_button)
    name_input = BaseElement(*AddContactLoactor.name_input)
    en_name_input = BaseElement(*AddContactLoactor.en_name_input)
    accid = BaseElement(*AddContactLoactor.accid)
    man = BaseElement(*AddContactLoactor.man)
    woman = BaseElement(*AddContactLoactor.woman)
    mobile = BaseElement(*AddContactLoactor.mobile)
    save = BaseElement(*AddContactLoactor.save)

    def __init__(self, driver):
        self.driver = driver

    def op_create_page(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(AddContactLoactor.add_button)
        )
        for i in range(10):
            self.add_button.click()
            time.sleep(1)
            if not self.add_button.is_displayed():
                break

    def exist(self, name):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, f"//td[@title='{name}']"))
            )
            return True
        except TimeoutException as e:
            return False

    def screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), "截个图", allure.attachment_type.PNG)


@pytest.fixture()
def page():
    d = get_login_driver()
    yield AddContactPage(d)
    d.quit()


class TestAddContact:

    @allure.title("创建联系人并发现")
    def test1(self, page):
        with allure.step("进入表单填写页面"):
            page.op_create_page()
        with allure.step("填写表单"):
            name = fake.name()
            page.name_input = name
            page.en_name_input = fake.name()
            page.accid = fake.iana_id()
            page.mobile = fake.phone_number()
            page.save.click()
        with allure.step("校验页面存在刚才的值"):
            page.exist(name)
            page.screen()


if __name__ == '__main__':
    run(__file__)
