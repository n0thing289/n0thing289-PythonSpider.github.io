from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#  荣耀电脑里不需要这句话
r = r"D:\edgedriver\msedgedriver.exe"
brower = webdriver.Edge()
url = "https://www.baidu.com/"
brower.get(url)
brower.find_element(By.ID, "kw").send_keys("蔡徐坤")
brower.find_element(By.ID, "su").click()
brower.save_screenshot("百度截图.png")

print(brower.page_source)
print(brower.get_cookie("cookie"))
print(brower.current_url)

js1 = "window.open('https://acgdh.org/1075.html')"
js2 = "window.open('https://acgdh.org/1060.html')"
js3 = "window.open('https://acgdh.org/3766.html')"

time.sleep(2)
brower.execute_script(js1)
time.sleep(2)

brower.execute_script(js2)
time.sleep(2)

brower.execute_script(js3)

# js3-js1
time.sleep(5)
brower.switch_to.window(brower.window_handles[0])#1 1
time.sleep(5)
brower.switch_to.window(brower.window_handles[1])#3 3
time.sleep(5)
brower.switch_to.window(brower.window_handles[2])#4 2
time.sleep(5)
brower.switch_to.window(brower.window_handles[3])#2 4

brower.quit()