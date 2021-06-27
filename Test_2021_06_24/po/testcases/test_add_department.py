import allure

from utils.get_driver import get_driver
from Test_2021_06_24.po.pages.ContactPage import AddContactPage

from faker import Faker
from run import run

d = get_driver()
fake = Faker("zh-CN")


class TestAddContact:
    def setup_class(self):
        self.root_department_name = "test"
        self.department_name = fake.iana_id() + "部"

    @allure.title("创建部门成功")
    def test1(self, page: AddContactPage):
        with allure.step("创建部门"):
            add_department_page = page.op_add_department_page()
            department_name = self.department_name
            result = add_department_page.add_department(department_name, self.root_department_name)
        with allure.step("校验创建成功"):
            assert result == "新建部门成功"
            assert department_name in page.departments_names
            page.screen()

    @allure.title("创建部门失败")
    def test2(self, page: AddContactPage):
        with allure.step("创建部门"):
            add_department_page = page.op_add_department_page()
            department_name = self.department_name
            result = add_department_page.add_department(department_name, self.root_department_name)
        with allure.step("校验创建失败"):
            assert result == "该部门已存在"
            page.screen()


if __name__ == '__main__':
    run(__file__)
