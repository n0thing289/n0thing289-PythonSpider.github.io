from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 打开浏览器
brower = webdriver.Edge()

# 打开百度
brower.get('http://www.baidu.com/')


# 定位并且尝试发送一条信息
# brower.find_element_by_id("kw").send_keys("蔡徐坤")
brower.find_element(By.ID, "kw").send_keys("蔡徐坤")

time.sleep(2)

# 点击歹毒一下
brower.find_element(By.ID, "su").click()

# time.sleep(2)

# 严格来说时关闭这一个页面
# brower.close()
