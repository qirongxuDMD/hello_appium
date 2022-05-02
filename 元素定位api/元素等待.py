from appium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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
driver.find_element(By.ID, "android:id/button1").click()

"""
# 隐式等待
# 所有元素的超时时间设置为20秒
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//*[@content-desc='转到上一层级']").click()

time.sleep(5)
driver.quit()
"""
# 显示等待
# 实例化，即wait为对象，调用WebDriverWait类里面的方法,30表示超时时间，10表示两次寻找元素的间隔
wait = WebDriverWait(driver, 20, 10)
# 调用until（）方法,获得元素特征，即返回按钮
back_button = wait.until(lambda x: x.find_element(By.XPATH, "//*[@content-desc='转到上一层级']"), "qqqTimeoutException")
# 点击返回按钮
back_button.click()


time.sleep(5)
driver.quit()
