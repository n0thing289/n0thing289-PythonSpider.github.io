from selenium import webdriver
from selenium.webdriver.common.by import By
import time

brower = webdriver.Edge()

brower.get("https://www.baidu.com/")

js = "window.open('https://www.jd.com')"
brower.execute_script(js)
time.sleep(1000)