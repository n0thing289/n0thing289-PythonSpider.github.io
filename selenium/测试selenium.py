import time

from selenium import webdriver

# 打开浏览器
brower = webdriver.Edge('D:\edgedriver\msedgedriver.exe')

# 访问百度（加载页面知识点）
brower.get('http://www.baidu.com/')
# 保存截图

time.sleep(2)
brower.save_screenshot('百度截图.png')  # 如果知道位置也可以截取指定区域

# 延时一会
time.sleep(2)

brower.close()

"""
因为要渲染界面，所以selenium比较慢
PhantomJS浏览器，但是被封杀了
"""