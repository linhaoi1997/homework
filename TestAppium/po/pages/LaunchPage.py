from TestAppium.po.pages.BasePage import BasePage
from TestAppium.po.appium_elements import Element


class LaunchPage(BasePage):
    contact = Element("//*[contains(@text,'通讯录')]")

    def goto_contact(self):
        from TestAppium.po.pages.ContactPage import ContactPage
        self.logging("进入联系人页面")
        self.contact.click()
        return ContactPage(self.driver)
