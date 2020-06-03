from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random
import getlinks

logins = ['capcha_remake1', 'capcha_remake2', 'capcha_remake3']
f = open("proxy.txt", 'r')
proxies = f.read().split('\n')
f.close()
qst = {'8+8=': '16', 'Самая большая страна мира по площади?': 'Россия', 'Имя первого космонавта?': 'Юра',
       'Как называется наша планета?': 'Земля', '2+2=': '4', 'Что светит в небе?': 'Солнце'}
mes = 'Пионер! Поменяй капчу!!!'

again = []
firefox_capabilities = webdriver.DesiredCapabilities.FIREFOX
firefox_capabilities['marionette'] = True
proxy = random.choice(proxies)
print(proxy)
firefox_capabilities['proxy'] = {
    "proxyType": "MANUAL",
    "httpProxy": proxy,
    "ftpProxy": proxy,
    "sslProxy": proxy
}


def change_prox():
    proxy = random.choice(proxies)
    print(proxy)
    firefox_capabilities['proxy'] = {
        "proxyType": "MANUAL",
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy
    }


for i in testxts.find_threads('https://freetp.org/forum/categories-10'):
    try:
        driver = webdriver.Firefox(capabilities=firefox_capabilities)
        driver.get(i)
        change_prox()
        driver.get(i)
        log = random.choice(logins)
        driver.find_element_by_xpath("//input[@name=\"login_name\"]").send_keys(log)
        driver.find_element_by_xpath("//input[@name=\"login_password\"]").send_keys(log)
        driver.find_element_by_xpath("//input[@onclick=\"submit();\"]").click()
        driver.find_element_by_xpath("//textarea[@id=\"text_msg\"]").send_keys('Пионер, измени капчу!!!!')
        f = driver.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/dl/dt").text[8:]
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/dl/dd/input').send_keys(
            qst[f])
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/button').click()
        time.sleep(10)
        driver.close()
    except BaseException:
        again.append(i)

while again != []:
    j = random.choice(again)
    try:
        driver = webdriver.Firefox(capabilities=firefox_capabilities)
        driver.get(j)
        change_prox()
        driver.get(j)
        log = random.choice(logins)
        driver.find_element_by_xpath("//input[@name=\"login_name\"]").send_keys(log)
        driver.find_element_by_xpath("//input[@name=\"login_password\"]").send_keys(log)
        driver.find_element_by_xpath("//input[@onclick=\"submit();\"]").click()
        driver.find_element_by_xpath("//textarea[@id=\"text_msg\"]").send_keys('Пионер, измени капчу!!!!')
        f = driver.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/dl/dt").text[8:]
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/dl/dd/input').send_keys(
            qst[f])
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div[3]/div[1]/div[1]/div/div/div[1]/div/form/ol/li/div[3]/button').click()
        time.sleep(10)
        again.pop(again.index(j))
        driver.close()
    except BaseException:
        again.append(i)
