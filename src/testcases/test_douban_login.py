# coding=utf-8
#1. 用账号密码的方式登录豆瓣
#2. 检查登录是否成功
#3. pytest自动测试框架
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin():
    def test_login(self):
        # 打开浏览器时去掉弹窗提示的您的浏览器正在受第三方监控
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-infobars')
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.douban.com/")

        # 定位登录iframe
        login_frame = self.driver.find_element_by_tag_name("iframe")
        #高亮显示某区域，通常在调试的时候用
        self.driver.execute_script("arguments[0].style.background = 'rgb(138,43,226 )';", login_frame)

        self.driver.switch_to.frame(login_frame)
        #print(self.driver.page_source)
        self.driver.find_element_by_class_name("account-tab-account").click()
        self.driver.find_element_by_id("username").send_keys("18810054187")
        self.driver.find_element_by_name("password").send_keys("qwe789")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "登录豆瓣").click()
        # 断言登录成功
        #element= self.driver.find_element(By.XPATH, "//*[@placeholder='搜索你感兴趣的内容和人']")
        #assert len(element) > 0
        elements = self.driver.find_elements_by_link_text("我的豆瓣")
        assert len(elements) > 0
        page = self.driver.page_source
        assert '说句话' in page

