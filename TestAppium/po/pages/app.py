from appium.webdriver.webdriver import WebDriver

from TestAppium.po.pages.LaunchPage import LaunchPage


class App:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def start(self):
        if self.driver.current_activity != "com.tencent.wework.launch.WwMainActivity":
            self.driver.launch_app()

    def restart(self):
        self.driver.launch_app()

    def quit(self):
        self.driver.quit()

    def goto_main(self):
        # 进入主页 入口
        return LaunchPage(self.driver)
