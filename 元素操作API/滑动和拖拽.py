from appium import webdriver
import time

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
swipe（）方法滑动
driver.swipe(200, 1500, 200, 500, 5000)
"""

# screen_size = driver.get_window_size()
# width = screen_size["width"]
# height = screen_size["height"]
# x1 = width * 0.8
# y1 = height * 0.2
# x2 = width * 0.5
# y2 = height * 0.7
# driver.swipe(x1, y1, x2, y2, 800)


"""
参数是元素
scroll(origin_el, destination_el)方法有惯性
和driver.drag_and_drop(origin_el, destination_el)方法没有惯性
实现滚动
"""
origin_el = driver.find_element(By.XPATH, "//*[@text='声音和振动']")
destination_el = driver.find_element(By.XPATH, "//*[@text='蓝牙']")
# driver.scroll(origin_el, destination_el)
driver.drag_and_drop(origin_el, destination_el)


time.sleep(10)
driver.quit()
