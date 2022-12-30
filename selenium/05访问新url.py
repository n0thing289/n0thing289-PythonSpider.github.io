from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#1.打开浏览器
brower = webdriver.Edge()
#2.打开页面
brower.get(url="https://www.baidu.com/")
#3.定位页面
time.sleep(2)
brower.find_element(By.ID, "kw").send_keys("古巨基 必杀技")
#4.点击页面
brower.find_element(By.ID, "su").click()
time.sleep(1)

#5. 打开新页面
brower.get("https://www.jd.com")
time.sleep(1000)