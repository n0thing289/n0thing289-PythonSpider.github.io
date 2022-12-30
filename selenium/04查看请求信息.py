from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#1.打开浏览器
broswer = webdriver.Edge()
#2.打开页面
broswer.get(url="https://www.baidu.com/")
print(broswer.page_source)
mycookie = None
# print("\n\n\n" + broswer.get_cookie())
print(broswer.current_url)