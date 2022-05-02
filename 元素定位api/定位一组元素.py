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
driver.find_element(By.ID, "android:id/button1").click()
"""

# 通过id形式获取所有id为“com.android.settings:id/title”的内容并打印
titles = driver.find_elements(By.ID, "com.android.settings:id/title")
# 打印出titles是什么内容
print(titles)
# 打印出列表第二个数据的内容
print(titles[1].text)
# 打印出列表的长度
print(len(titles))


for title in titles:
    print(title.text)
titles[1].click()

"""

# 通过class-name形式获取所有class为“android.widget.TextView”的内容并打印
# text_viewers = driver.find_elements(By.CLASS_NAME, "android.widget.TextView")
# for text_viewer in text_viewers:
#     print(text_viewer.text)
# print(text_viewers)

# 通过xpath形式获取所有class为“设”的内容并打印
# 打印出文本内容为‘设’的
# driver.find_elements(By.XPATH, "//*[@text='设']")
elements = driver.find_elements(By.XPATH, "//*[contains(@text,'设')]")
print(len(elements))
for ele in elements:
    print(ele.text)
