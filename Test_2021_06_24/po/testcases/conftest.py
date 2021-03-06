import allure
import pytest
from Test_2021_06_24.po.utils.login_tools import get_login_driver
from Test_2021_06_24.po.pages.MainPage import MainPage
from utils.get_driver import get_driver


@pytest.fixture(scope="session")
def page():
    d = get_login_driver()
    # 调试用
    # d = get_driver()
    yield MainPage(d).click_contact()
    d.quit()
