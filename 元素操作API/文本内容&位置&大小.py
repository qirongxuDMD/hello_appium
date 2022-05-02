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
# desired_caps['unicodekeyboard'] = True
# desired_caps['resetkeyboard'] = True
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True

# 要打开的应用程序
desired_caps['appPackage'] = 'com.android.settings'
# 要打开的界面
desired_caps['appActivity'] = '.Settings'
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element(By.ID, "android:id/button1").click()
"""
# 获取文本内容，获取所有 resource-id 为 ”com.android.settings:id/title“ 的元素，并打印其文字内容
# elements = driver.find_elements(By.ID, "com.android.settings:id/title")
# for i in elements:
#     print(i.text)
"""

"""
# 获取元素的位置和大小
# 1. 打开《设置》
# 2. 获取 ”放大镜“ 的位置和大小
search_button = driver.find_element(By.ID, "com.android.settings:id/search")
# 打印出的位置和大小是字典的形式，跟json数据格式很像，取的时候用中括号加引号的形式[""],取出x和y两个k值
print(search_button.location)
print(search_button.location["x"])
print(search_button.location["y"])

print(search_button.size)
print(search_button.size["height"])
print(search_button.size["width"])

time.sleep(2)
driver.quit()

"""

# 1. 打开《设置》
# 2. 获取所有 resource-id 为 ”com.android.settings:id/title“ 的元素
elements = driver.find_elements(By.ID, "com.android.settings:id/title")

# 3. 使用 get_attribute 获取这些元素的 enabled、text、content-desc、resource-id、class 的属性值
for i in elements:
    print(i.get_attribute("enabled"))
    print(i.get_attribute("text"))

    # print(i.get_attribute("content-desc"))
    print(i.get_attribute("name"))

    # print(i.get_attribute("resource-id"))
    print(i.get_attribute("resourceId"))

    # print(i.get_attribute("class"))
    print(i.get_attribute("className"))

time.sleep(2)
driver.quit()
