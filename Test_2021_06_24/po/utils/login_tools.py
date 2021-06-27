from utils.get_driver import get_driver
from selenium import webdriver
from utils.load_yaml import return_path
import yaml


def get_cookies():
    d = get_driver()
    cookies = d.get_cookies()
    with open(return_path("Test_2021_06_24/cookies.yaml"), "w") as f:
        yaml.safe_dump(cookies, f)


def get_login_driver():
    with open(return_path("Test_2021_06_24/cookies.yaml"), "r") as f:
        cookies = yaml.safe_load(f)
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    return driver


if __name__ == '__main__':
    get_cookies()
