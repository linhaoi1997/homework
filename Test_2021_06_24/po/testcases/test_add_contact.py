import allure

from utils.get_driver import get_driver
from Test_2021_06_24.po.pages.ContactPage import AddContactPage

from faker import Faker
from run import run

d = get_driver()
fake = Faker("zh-CN")


class TestAddContact:

    @allure.title("创建联系人并校验")
    def test1(self, page:AddContactPage):
        with allure.step("进入表单填写页面"):
            page.op_create_page()
        with allure.step("填写表单"):
            phone = page.add_person()
        with allure.step("校验页面存在刚才的值"):
            assert page.exist(phone)
            page.screen()


if __name__ == '__main__':
    run(__file__)
