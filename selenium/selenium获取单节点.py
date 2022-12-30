import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 获取浏览器1驱动对象
brower = webdriver.Edge()
# 打开指定url
url = 'https://news.baidu.com/'
brower.get(url)  # 打开任何一个网页都要完成渲染，线程才会继续往下走
time.sleep(1)
ret = brower.find_element(By.ID,'ww')
print(ret)

time.sleep(10)
brower.quit()
