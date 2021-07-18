import logging
import random
from typing import List

import allure
import requests

from TestRequest.Api.base_api import BaseApi


class AddContact(BaseApi):
    PATH = "user/create"

    def add_contact(self, user_id, name, department_ids: List[int], **kwargs):
        """
        除了上述参数还要任选mobile或者email传参
        :param user_id:
        :param name:
        :param department_ids:
        :param kwargs:
        :return: 创建结果
        """
        variables = {
            "userid": user_id,
            "name": name,
            "department": department_ids,
            "to_invite": False
        }
        variables.update(kwargs)
        return self.post(variables)


class DepartmentList(BaseApi):
    PATH = 'department/list'

    def department_list(self, id_=None):
        params = {}
        if id:
            params["id"] = id_
        return self.get(params=params)

    @property
    def random_department(self):
        return random.choice(self.department_list().json().get("department"))

    @property
    def random_department_id_list(self):
        return [self.random_department.get("id")]

class Contact(BaseApi):
    PATH = "user/get"

    def contact(self, user_id):
        return self.get({"userid": user_id})


class Contacts(BaseApi):
    PATH = "user/simplelist"

    def contacts(self, department_id):
        return self.get({"department_id": department_id})


class DeleteContact(BaseApi):
    PATH = "user/delete"

    def delete_contact(self, user_id):
        return self.get({"userid": user_id})


class UpdateContact(BaseApi):
    PATH = "user/update"

    def update_contact(self, user_id, **kwargs):
        variables = {"userid": user_id}
        variables.update(kwargs)
        return self.post(variables)


if __name__ == '__main__':
    from faker import Faker

    fake = Faker(["zh_CN"])
    print(DepartmentList().random_department)
    # print(AddContact().add_contact("api111", "ces", [1], mobile=fake.phone_number()).json())
    # print(Contacts().contacts(1).json())
