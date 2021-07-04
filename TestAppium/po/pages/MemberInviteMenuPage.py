from appium.webdriver.common.mobileby import MobileBy

from TestAppium.po.appium_elements import Element
from TestAppium.po.pages.BasePage import BasePage
from TestAppium.po.pages.ContactAddFastModePage import ContactAddFastModePage


class MemberInviteMenuPage(BasePage):
    manual_add_button = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cha"]')

    def goto_manual_add_page(self):
        self.manual_add_button.click()
        return ContactAddFastModePage(self.driver)
