from appium import webdriver
import time
from appium.webdriver.connectiontype import ConnectionType

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

desired_caps = dict()
# 平台的名字，大小写不区分
desired_caps['platformName'] = 'Android'
# 平台的版本
desired_caps['platformVersion'] = '6.0.1'
# 设备的名字，安卓不是真正的设备的名字，ios需要严格的设备名称如 iPhone 7
desired_caps['deviceName'] = '192.168.0.108:5555'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 要打开的应用程序
desired_caps['appPackage'] = 'com.android.settings'
# 要打开的界面
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element(By.ID, "android:id/button1").click()

"""
# 获取当前屏幕的分辨率
print(driver.get_window_size())
print(driver.get_window_size()["width"])
# driver.get_screenshot_as_file("C:/Users/dmd/Desktop/a.png")
driver.get_screenshot_as_file("a.png")
"""

"""

# 获取当前手机的网络
# 获取当前手机的网络
# print(driver.network_connection)
# # 设置当前手机的网络
driver.set_network_connection(2)
if driver.network_connection == ConnectionType.DATA_ONLY:
    print(1)
else:
    print(0)
"""

"""
# 发送键到设备
# 点击三次音量加，再点击返回，再点击两次音量减。
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(24)
driver.press_keycode(4)
time.sleep(2)
driver.press_keycode(25)
driver.press_keycode(25)
"""
# 打开通知栏
driver.open_notifications()

# 关闭通知栏
driver.press_keycode(4)
time.sleep(5)
driver.quit()
