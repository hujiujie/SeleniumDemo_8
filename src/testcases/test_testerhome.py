# coding=utf-8
from time import sleep
from unittest import TestCase

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestTesterHome(TestCase):
    def test_index(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        print(self.driver.page_source)
        self.driver.maximize_window()  #最大化窗口
        #源码< input class ="form-control" name="q" type="text" value="" placeholder="搜索本站内容" >
        #self.driver.find_element(By.XPATH, "//*[@placeholder='搜索本站内容']")    #可以使用xpath定位，或者下面的都行
        self.driver.find_element(By.NAME, "q").send_keys("热门",Keys.ENTER)
        sleep(10)

    def test_window(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(15)
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()
        # PARTIAL_LINK_TEXT --对应源码中，href后面可以点击跳转的链接
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "测试工程师生存指南").click()
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "https://jinshuju.net/f/iBwLDt").click()
        # 查看当前打开了几个窗口
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        # 切换到指定窗口
        self.driver.switch_to.window(windows[1])
        print(self.driver.page_source)

    def test_headless(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.headless = True
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.implicitly_wait(15)
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()

    def test_remote_webdriver(self):
        # 低版本java jdk不能运行已下方法，推荐升级到jdk 10
        self.driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub",
                                       desired_capabilities=DesiredCapabilities.CHROME)

        self.driver.implicitly_wait(15)
        self.driver.get("https://testerhome.com/")
        self.driver.maximize_window()







