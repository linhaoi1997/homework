import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from TestAppium.po.appium_elements import ScrollLocatedElement
from TestAppium.po.pages.BasePage import BasePage


class ContactDetailProfilePage(BasePage):
    detail = ScrollLocatedElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/hcm"]')

    def goto_setting(self):
        from TestAppium.po.pages.ContactDetailSettingPage import ContactDetailSettingPage
        time.sleep(1)
        self.click(self.detail)
        self.logging("进入个人设置页面")
        return ContactDetailSettingPage(self.driver)


