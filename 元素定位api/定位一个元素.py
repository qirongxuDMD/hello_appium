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
# 要打开的应用程序
desired_caps['appPackage'] = 'com.android.settings'
# 要打开的界面
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

from appium.webdriver.connectiontype import ConnectionType

# def set_no_connection(driver):
#     """
#     设置成-无网络
#     :param driver:
#     :return:
#     """
#     driver.set_network_connection(ConnectionType.NO_CONNECTION)
#     return driver

# def set_wifi(driver):
#     """
#     设置成-开启wifi
#     :param driver:
#     :return:
#     """
#     driver.set_network_connection(ConnectionType.WIFI_ONLY)
#     return driver
# driver.find_element_by_id("android:id/button1").click()
# 通过id定位元素特征，点击
driver.find_element(By.ID, "android:id/button1").click()
driver.find_element(By.ID, "com.android.settings:id/search").click()
# 通过class定位元素特征，输入
# driver.find_element_by_class_name()废弃了，用下面的方法
driver.find_element(By.CLASS_NAME, "com.meizu.common.widget.SearchEditText").send_keys("hello")
# 通过xpath定位元素特征，点击
driver.find_element(By.XPATH, "//*[@content-desc='转到上一层级']").click()

# driver.find_element("class", "android.widget.TextView").send_keys("hello")

time.sleep(8)
driver.quit()

