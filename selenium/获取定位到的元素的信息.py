from selenium import webdriver
from selenium.webdriver.common.by import By
# 驱动浏览器
brower = webdriver.Edge()

# 指定url 打开url
url = 'https://douban.com'
brower.get(url)

# 定位h1标签
ret = brower.find_elements(By.TAG_NAME, 'h1')
print(ret[0].text)

#通过a标签定位，可以部分或者全部的超链接的内容来找（找这个a标签，根据你a标签的内容来定位你a标签）
ret2 = brower.find_elements(By.LINK_TEXT, '扫码下载豆瓣 APP')
print(ret2)

#处理cookie
cookie_list = brower.get_cookies()
cookie_dict = {x["name" : x["value"] for x in cookie_list}