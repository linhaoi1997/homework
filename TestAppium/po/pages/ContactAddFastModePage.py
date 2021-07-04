from appium.webdriver.common.mobileby import MobileBy

from TestAppium.po.appium_elements import Element
from TestAppium.po.pages.BasePage import BasePage


class ContactAddFastModePage(BasePage):
    name = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/b09"]')
    phone = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/f7y"]')
    is_send_invite = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ew3"]')
    save_button = Element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/ad2"]')
    toast_message = Element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_contact(self, name, phone):
        self.name = name
        self.phone = phone
        self.is_send_invite.click()
        self.save_button.click()

    def get_toast(self):
        return self.toast_message.text
