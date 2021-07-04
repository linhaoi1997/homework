from appium.webdriver.common.mobileby import MobileBy

from TestAppium.po.appium_elements import Element
from TestAppium.po.pages.BasePage import BasePage


class ContactDetailSettingPage(BasePage):
    edit = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b5r"]')

    def goto_edit(self):
        from TestAppium.po.pages.ContactEditPage import ContactEditPage
        self.click(self.edit)
        self.logging("进入编辑页面")
        return ContactEditPage(self.driver)
