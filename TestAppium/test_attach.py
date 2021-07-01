from appium import webdriver
from appium.webdriver.common.mobileby import By
from uiautomator2.init import Initer
import adbutils
import logging

serial = None
device = adbutils.adb.device(serial)
init = Initer(device, loglevel=logging.DEBUG)
init.install()

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1.2'
desired_caps['deviceName'] = 'emulator-5554'
# desired_caps["automationName"] = "UiAutomator1"
desired_caps["noReset"] = "true"
desired_caps["dontStopAppOnReset"] = "true"
# desired_caps['appPackage'] = 'com.taobao.taobao'
# desired_caps['appActivity'] = 'com.taobao.search.searchdoor.SearchDoorActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

from   selenium.webdriver.support.expected_conditions import element_to_be_clickable