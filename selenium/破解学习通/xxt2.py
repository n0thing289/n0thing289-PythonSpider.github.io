from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Edge()

def sign_in(browser):
    sign_in_url = 'https://i.chaoxing.com/'
    browser.get(sign_in_url)
    id_xpath = '//div[@class="lg-item icon-tel margin-btm24"]/input'
    password_xpath = '//div[@class="lg-item item-pwd icon-pwd"]/input'
    ID = 18928370646
    PASSWORD = '1598sd246w789'
    time.sleep(2)
    browser.find_element(By.XPATH, id_xpath).send_keys(ID)
    browser.find_element(By.XPATH, password_xpath).send_keys(PASSWORD)

    browser.find_element(By.ID, 'loginBtn').click()


def search_video(browser):
    time.sleep(10)
    # 习新
    video_xpath = '/html/body/div/div/div/div[2]/div[1]/div[2]/div[2]/ul/li[5]/div[1]/a'
    browser.find_element(By.XPATH, video_xpath).click()
if __name__ == "__main__":
    sign_in(browser=browser)
    search_video(browser=browser)
time.sleep(10000)