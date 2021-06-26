from utils.get_driver import get_driver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import TouchActions, ActionChains
from selenium.webdriver.common.keys import Keys

d = get_driver()

# TouchActions(d).scroll(0, 1000).perform()
# TouchActions(d).flick(0, 1000)
# search_box = d.find_element_by_id("kw")
# search_box.click()
# print(search_box.get_attribute("value"))
# ActionChains(d).click(search_box).key_down(Keys.COMMAND).send_keys("A").key_up(Keys.CONTROL).pause(1).send_keys(
#     Keys.SPACE).perform()
# ActionChains(d).click(search_box).send_keys(Keys.DELETE)
# ActionChains(d).click(search_box).key_down(Keys.BACKSPACE).pause(10).perform()
# ActionChains(d).send_keys(Keys.BACK_SPACE).perform()

# search_box.send_keys(Keys.CONTROL)
# search_box.send_keys("a")
# search_box.send_keys(Keys.BACKSPACE)
eles=d.find_elements_by_xpath("//tr/td[2]")
print([i.text for i in eles])