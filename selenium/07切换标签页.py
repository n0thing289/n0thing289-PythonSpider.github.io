from selenium import webdriver
from selenium.webdriver.common.by import By
import time

brower = webdriver.Edge()
brower.get("https://www.baidu.com/")

js = "window.open('https://www.jd.com')"
brower.execute_script(js)

brower.switch_to.window(brower.window_handles[0])
time.sleep(5)
brower.switch_to.window(brower.window_handles[1])

time.sleep(100)