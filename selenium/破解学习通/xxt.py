from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import json

def browser_initial():

    brower = webdriver.Edge()
    goal_url = 'https://i.chaoxing.com/base?t=1672385865021'
    brower.get('https://i.chaoxing.com/')
    return goal_url, brower


def get_cookie(log_url, brower):
    brower.get(log_url)
    time.sleep(30)
    dictCookies = brower.get_cookies()
    jsonCookies = json.dumps(dictCookies)

    with open('xxt_cookies.txt', 'w') as f:
        f.write(jsonCookies)

    print('cookies保存成功')

def log_xxt(goal_url, browser):
    with open('xxt_cookies.txt', 'r', encoding='UTF-8') as f:
        listCookies = json.loads(f.read())


    for cookie in listCookies:
        # print("\n===" + str(cookie) + "===")
        if not cookie.get('expiry'):
            cookie_dict = {
                'domain': cookie.get('domain'),
                'httpOnly': cookie.get('httpOnly'),
                'name': cookie.get('name'),
                'path': '/',
                'secure': cookie.get('secure'),
                'value': cookie.get('value'),
                # 'HostOnly': False,
            }
            # print(cookie_dict)
            browser.add_cookie(cookie_dict)
        else:
            from main import insert_kv
            # print(insert_kv(cookie))
            browser.add_cookie(insert_kv(cookie))


    browser.get(goal_url)


if __name__ == "__main__":
    tur = browser_initial()
    # get_cookie(tur[0], tur[1])
    log_xxt(tur[0], tur[1])
    time.sleep(100)

