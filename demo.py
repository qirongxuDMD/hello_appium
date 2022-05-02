from appium import webdriver
import time

desired_caps = dict()
# 平台的名字，大小写不区分
desired_caps['platformName'] = 'Android'
# 平台的版本
desired_caps['platformVersion'] = '8.0'
# 设备的名字，安卓不是真正的设备的名字，ios需要严格的设备名称如 iPhone 7
desired_caps['deviceName'] = '192.168.56.101:5555'
# 要打开的应用程序
desired_caps['appPackage'] = 'com.amaze.filemanager'
# 要打开的界面
desired_caps['appActivity'] = '.activities.MainActivity'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
driver.quit()
