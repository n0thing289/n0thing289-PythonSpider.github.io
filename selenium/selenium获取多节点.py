from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
# 驱动浏览器
brower = webdriver.Edge()
option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)
# 打开一个网页
url = 'https://movie.douban.com/top250'
brower.get(url)

#
xpath = "//ol[@class='grid_view']/li"
# 获取多个节点，因为返回的是一个列表
ret_list = brower.find_elements(By.XPATH,xpath)

print(ret_list[1].text)

