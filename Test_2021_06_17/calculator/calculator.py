import allure


class Calculator:
    @allure.step("调用相加")
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    @allure.step("调用相除")
    def div(self, a, b):
        return a / b
