from TestAppium.po.pages.ContactPage import ContactPage
from TestAppium.po.pages.LaunchPage import LaunchPage
from utils.get_driver import get_appium_driver
import allure
import pytest
from faker import Faker
from run import run

fake = Faker("zh-CN")


@pytest.fixture(scope="class")
def page():
    return LaunchPage(get_appium_driver())


class TestAddContact:
    @allure.title("新增联系人")
    def test1(self, page):
        with allure.step("点击联系人下边栏"):
            add_page = page.goto_contact()
        with allure.step("点击进入添加成员页面"):
            add_page.goto_add_contact()
        with allure.step("保存成员,校验toast"):
            add_page.add_contact(fake.name(), fake.phone_number())
            assert add_page.save_successful_message.text == "添加成功"
            add_page.screen()


if __name__ == '__main__':
    run(__file__)
