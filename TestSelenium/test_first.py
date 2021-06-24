import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def test_wait(self):
        self.driver.find_element(By.ID)

        def wait(d):
            d.find_element_by_id("kw")

        WebDriverWait(self.driver, 20).until(wait)
