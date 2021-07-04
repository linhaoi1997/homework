from TestAppium.po.pages.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from TestAppium.po.appium_elements import Elements, ScrollLocatedElement
from TestAppium.po.pages.ContactDetailProfilePage import ContactDetailProfilePage
from TestAppium.po.pages.MemberInviteMenuPage import MemberInviteMenuPage


class ContactPage(BasePage):
    # add_contact_button = Element(MobileBy.ANDROID_UIAUTOMATOR,
    #                              'new UiScrollable(new UiSelector().scrollable(true).\
    #                              instance(0)).scrollIntoView(new UiSelector().\
    #                              text("添加成员").instance(0));')
    add_contact_button = ScrollLocatedElement(MobileBy.XPATH, "//*[contains(@text,'添加成员')]")
    contacts = Elements(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/hiz']/android.widget.TextView")

    def goto_add_contact(self):
        """点击按钮进入添加成员界面"""
        self.add_contact_button.click()
        return MemberInviteMenuPage(self.driver)

    def find_user(self, name):
        self.logging(f"寻找人员{name}")
        return self.scroll_and_find(MobileBy.XPATH, f"//*[contains(@text,'{name}')]")

    def go_to_user_detail(self, name):
        self.click(self.find_user(name))
        self.logging(f"进入 {name} 用户详情页面")
        return ContactDetailProfilePage(self.driver)


if __name__ == '__main__':
    from utils.get_driver import appium_debug_driver

    p = ContactPage(appium_debug_driver())
    print(len(p.contacts))
