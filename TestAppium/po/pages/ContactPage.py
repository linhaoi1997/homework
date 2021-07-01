from TestAppium.po.pages.BasePage import BasePage
from appium.webdriver.common.mobileby import MobileBy
from utils.elements import AppiumElement


class ContactPage(BasePage):
    add_contact_button = AppiumElement(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).\
                                 instance(0)).scrollIntoView(new UiSelector().\
                                 text("添加成员").instance(0));')
    manual_add_button = AppiumElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/cha"]')
    name = AppiumElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b09"]')
    phone = AppiumElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/f7y"]')
    save_button = AppiumElement(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ad2"]')
    save_successful_message = AppiumElement(MobileBy.XPATH, '//*[contains(@text, "添加成功")]')

    def goto_add_contact(self):
        """点击按钮进入添加成员界面"""
        self.add_contact_button.click()
        self.manual_add_button.click()

    def add_contact(self, name, phone):
        self.name = name
        self.phone = phone
        self.save_button.click()
