from selenium.common.exceptions import NoSuchElementException

from TestAppium.po.pages.app import App
from utils.get_driver import get_appium_driver
import allure
import pytest
from faker import Faker
from run import run

fake = Faker("zh-CN")


@pytest.fixture(scope="session")
def app():
    app = App(get_appium_driver())
    yield app
    app.quit()


@pytest.fixture()
def page(app):
    yield app.goto_main()
    app.restart()


class TestAddContact:
    @allure.title("新增联系人")
    def test1(self, page):
        with allure.step("进入手动添加联系人页面"):
            pass
            add_page = page.goto_contact().goto_add_contact().goto_manual_add_page()
        with allure.step("保存成员,校验toast"):
            add_page.add_contact(fake.name(), fake.phone_number())
            assert add_page.get_toast() == "添加成功"
            add_page.screen()


class TestDeleteContact:
    @allure.title("删除联系人")
    def test2(self, page):
        # 从数据库中获取还是从哪里搞
        name = "孙瑜"
        with allure.step("进入删除联系人页面"):
            page = page.goto_contact().go_to_user_detail(name)
        with allure.step("选择联系人，并进入删除页面删除联系人"):
            page = page.goto_setting().goto_edit().delete_current_user()
        with allure.step("验证联系人删除成功"):
            with pytest.raises(NoSuchElementException):
                page.find_user(name)
        page.screen()


if __name__ == '__main__':
    run(__file__)
