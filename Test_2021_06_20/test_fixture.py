import pytest


@pytest.fixture(scope="module")
def login():
    print("登录")
    yield
    print("退出登录")


def test1():
    print("ceshi1")


def test2(login):
    print("ceshi2")


def test3():
    print("ceshi3")
