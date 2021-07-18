from selenium import webdriver as s_webdriver
from appium import webdriver


# from uiautomator2.init import Initer
# import adbutils
# import logging
#
# serial = None
# device = adbutils.adb.device(serial)
# init = Initer(device, loglevel=logging.DEBUG)
# init.install()


def get_appium_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = 'emulator-5554'
    # desired_caps["automationName"] = "UiAutomator1"
    desired_caps["noReset"] = "true"
    # desired_caps["dontStopAppOnReset"] = "true"
    desired_caps['appPackage'] = 'com.tencent.wework'
    desired_caps['appActivity'] = 'com.tencent.wework.launch.LaunchSplashActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def appium_debug_driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '7.1.2'
    desired_caps['deviceName'] = 'emulator-5554'
    # desired_caps["automationName"] = "UiAutomator1"
    desired_caps["noReset"] = "true"
    desired_caps["dontStopAppOnReset"] = "true"
    desired_caps["skipDeviceInitialization"] = "true"
    desired_caps['appPackage'] = 'com.xueqiu.android'
    desired_caps['appActivity'] = '.community.my.MyStatusActivity'
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    return driver


def get_driver(port=8889):
    options = s_webdriver.ChromeOptions()
    options.add_experimental_option("w3c", False)
    options.add_experimental_option("debuggerAddress", "127.0.0.1:%s" % port)
    c = s_webdriver.Chrome(port=19888, options=options)
    return c
