from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = dict()
# 平台的名字，大小写不区分
desired_caps['platformName'] = 'Android'
# 平台的版本
desired_caps['platformVersion'] = '8.0'
# 设备的名字，安卓不是真正的设备的名字，ios需要严格的设备名称如 iPhone 7
desired_caps['deviceName'] = '192.168.0.108:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 要打开的应用程序
desired_caps['appPackage'] = 'com.android.settings'
# 要打开的界面
desired_caps['appActivity'] = '.ChooseLockPattern'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.find_element(By.ID, "android:id/button1").click()
TouchAction(driver).long_press(x=196, y=504, )\
    .move_to(x=300, y=504).wait(2000).move_to(x=404, y=505)\
    .move_to(x=300, y=609).move_to(x=194, y=711).move_to(x=300, y=711)\
    .move_to(x=406, y=711).release().perform()

time.sleep(10)
driver.quit()
