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

# 1. 打开《设置》
# 2. 点击 ”放大镜“
search_button = driver.find_element(By.ID, "com.android.settings:id/search")
search_button.click()
# 3. 输入 ”hello“
search_text = driver.find_element(By.ID, "com.android.settings:id/mc_search_edit")
time.sleep(2)
search_text.send_keys("hello")
# 4. 暂停 2 秒
time.sleep(2)
# 5. 清空所有文本内容
search_text.clear()
# 6. 暂停 5 秒
time.sleep(5)
# 7. 输入 ”你好“
# 注意：输入中文没有效果，需要将Unicode参数设置为ture
print("------------开始打印你好")
search_text.send_keys("你好")
time.sleep(2)
print("------------打印完成")

time.sleep(2)
driver.quit()
