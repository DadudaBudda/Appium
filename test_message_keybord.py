from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
import time

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Pixel 3a API 28",
    "appPackage": "com.google.android.apps.messaging",
    "appActivity": ".ui.ConversationListActivity",
    "unicodeKeyboard": False,
    "resetKeyboard": False,
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                          desired_capabilities=desired_capabilities)
driver.implicitly_wait(5)
a = driver.find_element(By.ID, "com.google.android.apps.messaging:id/start_new_conversation_button")
a.click()
number = driver.find_element(By.ID, "com.google.android.apps.messaging:id/recipient_text_view")
number.click()
time.sleep(2)
driver.swipe(start_x=59, start_y=1603, end_x=59, end_y=1403, duration=2300)
driver.swipe(start_x=59, start_y=1603, end_x=59, end_y=1403, duration=2300)
driver.swipe(start_x=59, start_y=1603, end_x=59, end_y=1403, duration=2300)
driver.press_keycode(66)
time.sleep(2)
new = driver.find_element(By.ID, "com.google.android.apps.messaging:id/compose_message_text")
new.click()
time.sleep(2)
driver.tap([(223, 2026)], 2000)
lang = driver.find_element(By.ID, "android:id/text1")
lang.click()
time.sleep(2)
addlang = driver.find_element(By.ID, "com.google.android.inputmethod.latin:id/add_language_button")
addlang.click()
time.sleep(2)
searchlang = driver.find_element(By.ID, "android:id/search_button")
searchlang.click()
time.sleep(2)
driver.tap([(376, 1603), (700, 1600), (220, 1733)])
time.sleep(2)
driver.tap([(150, 1030)])
time.sleep(2)
done_addlang = driver.find_element(By.ID,
                                   "com.google.android.inputmethod.latin:id/language_specific_setting_done_button")
done_addlang.click()
driver.press_keycode(4)
time.sleep(2)
driver.tap([(330, 2016)])
time.sleep(2)
driver.tap([(355, 1875), (600, 2010), (63, 1876)])
time.sleep(2)
driver.tap([(540, 1600),(640, 1736), (246, 1733), (150, 1736), (446, 1876), (600, 2010)])
for i in range(2):
    driver.swipe(start_x=156, start_y=1603, end_x=156, end_y=1423, duration=2300)
    driver.swipe(start_x=933, start_y=1603, end_x=933, end_y=1423, duration=2300)
driver.tap([(600, 2010), (633, 1593),(640, 1736), (833, 1733), (640, 1736), (446, 1876),(83,2006)])
time.sleep(2)
for i in range(3):
    driver.tap([(753, 1873)])
# driver.tap([(220, 1600)])
# new.send_keys("Happy New Year!!!")
# driver.implicitly_wait(5)
