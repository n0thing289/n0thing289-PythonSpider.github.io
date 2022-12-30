from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
option = webdriver.ChromeOptions()
option.add_argument(r'--user-data-dir=C:\Users\28927\AppData\Local\Google\Chrome\User Data\Default') #加载前面获取的 个人资料路径
s = Service("D:\chromedriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=option, service=s)  #启动Chrome驱动，这里为Linux系统，Windows 和 Mac OS 根据实际路径填写

time.sleep(100)