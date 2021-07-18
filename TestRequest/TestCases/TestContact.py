import time
import threading

from TestRequest.Api.contact_api import *
import pytest

from faker import Faker

fake = Faker(["zh_CN"])


def fake_name(name):
    return "_".join([name, threading.currentThread().name, str(int(time.time()))])


@pytest.fixture()
def new_contact():
    user_id = fake_name("userid")
    name = fake_name("name")
    department_ids = DepartmentList().random_department_id_list
    mobile = fake.phone_number()
    r = AddContact().add_contact(user_id, name, department_ids, mobile=mobile)
    if r.json().get("errcode") == 0:
        return user_id, name, department_ids


class TestContact:

    @pytest.mark.parametrize("params", [{"mobile": fake.phone_number()}, {"email": fake.email()}],
                             ids=["测试手机创建", "测试email创建"])
    def test1(self, params):
        user_id = fake_name("userid")
        name = fake_name("name")
        department_ids = DepartmentList().random_department_id_list
        r = AddContact().add_contact(user_id, name, department_ids, **params).json()
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "created"

    @allure.title("更新联系人")
    def test2(self, new_contact):
        user_id, name, department_ids = new_contact
        r = UpdateContact().update_contact(user_id, name=fake_name("更新后的名字")).json()
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "updated"

    @allure.title("查询联系人")
    def test3(self, new_contact):
        user_id, name, department_ids = new_contact
        r = Contact().contact(user_id).json()
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "ok"
        assert r.get("userid") == user_id

    @allure.title("删除联系人")
    def test4(self, new_contact):
        user_id, name, department_ids = new_contact
        r = DeleteContact().delete_contact(user_id).json()
        assert r.get("errcode") == 0
        assert r.get("errmsg") == "deleted"


if __name__ == '__main__':
    from run import run

    run(__file__)
