from appium.webdriver.common.touch_action import TouchAction
from utils.get_driver import appium_debug_driver

d = appium_debug_driver()
d.switch_to.context(context_name="ces")
print(len(d.find_elements_by_xpath("//*")))
import requests

r=requests.get()