import os

import pytest
import yaml
from functools import wraps
from run import run

from Test_2021_06_17.calculator.calculator import Calculator


def get_data(name):
    with open(os.path.dirname(__file__) + "/data.yaml", "r") as f:
        datas = yaml.safe_load(f)[name]
    return datas


def expect_fail(func):
    @wraps(func)
    def wrapper(instance, a, b, error_type):
        try:
            result = func(instance, a, b, error_type)
            raise AssertionError(f"不应该进行到这一步，预期发生{error_type}错误")
        except eval(error_type) as e:
            print(e)

    return wrapper


class TestAddDivision:
    def setup_class(self):
        self.cal = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    @pytest.mark.parametrize(**get_data("add_success"))
    def test_add_success(self, a, b, result):
        assert self.cal.add(a, b) == result

    @pytest.mark.parametrize(**get_data("add_fail"))
    @expect_fail
    def test_add_fail(self, a, b, error_type):
        self.cal.add(a, b)

    @pytest.mark.parametrize(**get_data("division_success"))
    def test_division_success(self, a, b, result):
        assert self.cal.div(a, b) == result

    @pytest.mark.parametrize(**get_data("division_fail"))
    @expect_fail
    def test_division_success(self, a, b, error_type):
        self.cal.div(a, b)


if __name__ == '__main__':
    run(__file__)
