from appium import webdriver
import time

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
步骤：
1.创建 TouchAction 对象 
2.通过对象调用想执行的手势 
3. 通过 perform() 执行动作
"""

"""
# 轻敲
# 1. 打开《设置》
# 2. 轻敲 “WLAN”

# 首先找到轻巧的元素
wlan_element = driver.find_element(By.XPATH, "//*[@text='无线网络']")
# # 1.创建 TouchAction 对象
# touch_action = TouchAction(driver)
#
# # 2.通过对象调用想执行的手势
# action_tap = touch_action.tap(wlan_element)
#
# # 3. 通过 perform() 执行动作
# action_tap.perform()
# 简化成一行代码,使用元素或者坐标轻敲
# TouchAction(driver).tap(wlan_element).perform()
# TouchAction(driver).tap(x=400, y=700).perform()
"""

"""
# 按下和抬起
# 使用坐标的形式按下 WLAN （650, 650），2 秒后，按下（650, 650）的位置，并抬起
TouchAction(driver).press(x=400, y=700)
time.sleep(2)
TouchAction(driver).press(x=400, y=700).release().perform()
time.sleep(2)
driver.quit()
"""

"""
等待的方法：wait()
# 使用坐标的形式点击 WLAN （200, 500），2 秒后，按下（500, 900）的位置，暂停 2 秒，并抬起
TouchAction(driver).tap(x=200, y=500).perform()
time.sleep(2)
TouchAction(driver).press(x=500, y=900).wait(2000).release().perform()
"""

"""
长按long_press(x=500, y=900, duration=2000)

# 使用坐标的形式点击 WLAN （650, 650），2 秒后，长按（650, 650）的位置持续 2 秒,再松开
TouchAction(driver).tap(x=200, y=500).perform()
time.sleep(2)
# TouchAction(driver).long_press(x=500, y=900).wait(2000).perform()
TouchAction(driver).long_press(x=500, y=900, duration=2000).release().perform()
"""
time.sleep(2)
driver.quit()

