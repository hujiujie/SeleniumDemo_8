# coding=utf-8

from selenium import webdriver

# 初始化driver
class BuildUpDriver:
    driver = ''

    @staticmethod
    def build_up_driver():
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-infobars')
        BuildUpDriver.driver= webdriver.Chrome(options=chrome_options)
        BuildUpDriver.driver.implicitly_wait(20)
        BuildUpDriver.driver.get("https://www.douban.com/")
        BuildUpDriver.driver.maximize_window()