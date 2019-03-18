# coding=utf-8

from selenium import webdriver

# 初始化driver
def build_up_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-infobars')
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)
    driver.get("https://www.douban.com/")
    return driver