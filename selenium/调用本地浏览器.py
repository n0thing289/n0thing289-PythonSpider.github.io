from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time
option = webdriver.EdgeOptions()
option.add_argument('--user-data-dir='+r'C:\Users\28927\AppData\Local\Microsoft\Edge\User Data\Default') #加载前面获取的 个人资料路径
s = Service()
driver = webdriver.Edge(options=option, service=s)  #启动Chrome驱动，这里为Linux系统，Windows 和 Mac OS 根据实际路径填写
driver.get("https://movie.douban.com/top250")

time.sleep(100)