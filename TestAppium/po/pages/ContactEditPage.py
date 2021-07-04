from appium.webdriver.common.mobileby import MobileBy
from TestAppium.po.appium_elements import Element, ScrollLocatedElement
from TestAppium.po.pages.BasePage import BasePage


class ContactEditPage(BasePage):
    delete = ScrollLocatedElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/e65"]')
    confirm = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/bg8"]')

    def delete_current_user(self):
        from TestAppium.po.pages.ContactPage import ContactPage
        delete = self.delete
        self.click(self.delete)
        self.click(self.confirm)
        self.logging("删除当前用户")
        return ContactPage(self.driver)
