import pytest
from Test_2021_06_17.calculator.calculator import Calculator


def pytest_collection_modifyitems(session, config, items) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope="class")
def calc():
    return Calculator()
