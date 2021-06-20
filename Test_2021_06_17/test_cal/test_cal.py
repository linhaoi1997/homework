import allure
import pytest
import yaml
from run import run
from utils import return_path, logger, record_jpg, record_text


def get_data(name):
    with open(return_path("data/test_2021_06_07/data.yaml")) as f:
        data = yaml.safe_load(f)[name]
    return data


@pytest.fixture(autouse=True)
def setup_and_teardown():
    logger.debug("开始计算")
    yield
    logger.debug("结束计算")


@allure.feature("测试计算器")
class TestAddDivision:

    @allure.story("测试加法")
    @allure.title("正向用例: ({a})+({b}) == {result}")
    @pytest.mark.parametrize(**get_data("add_success"))
    def test_add_success(self, a, b, result, calc):
        logger.debug(f"assert add ({a},{b}) success equal {result}")
        assert calc.add(a, b) == result

    @allure.story("测试加法")
    @allure.title("浮点数相加，有精度损失")
    def test_add_float(self, calc):
        logger.debug(f"assert  float add success")
        assert round(calc.add(0.1, 0.2), 2) == 0.3

    @allure.story("测试加法")
    @allure.title("反向用例: raise {error_type}")
    @pytest.mark.parametrize(**get_data("add_fail"))
    def test_add_fail(self, a, b, error_type, calc):
        logger.debug(f"assert ({a},{b}) add fail")
        with pytest.raises(eval(error_type)):
            calc.add(a, b)

    @allure.story("测试除法")
    @allure.title("正向用例: ({a})/({b}) == {result}")
    @pytest.mark.parametrize(**get_data("division_success"))
    def test_division_success(self, a, b, result, calc):
        logger.debug(f"assert ({a}/{b})  success equal {result}")
        assert calc.div(a, b) == result

    @allure.story("测试除法")
    @allure.title("反向用例: raise {error_type}")
    @pytest.mark.parametrize(**get_data("division_fail"))
    def test_division_success(self, a, b, error_type, calc):
        logger.debug(f"assert ({a}/{b})  fail")
        with pytest.raises(eval(error_type)):
            calc.div(a, b)


@allure.feature("测试allure")
class TestAllure:

    @allure.title("测试步骤和截图")
    def test(self):
        with allure.step("给文本"):
            record_text("存储文本", "文本具体内容")
        with allure.step("给截图"):
            record_jpg("存储截图", "test.jpg")


if __name__ == '__main__':
    run(__file__)
