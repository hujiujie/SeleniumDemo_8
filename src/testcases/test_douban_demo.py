# coding=utf-8


from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test_douban_window():
    driver = webdriver.Chrome()
    driver.get("https://www.douban.com/")
    driver.implicitly_wait(10)
    # iframe 不同
    login_frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(login_frame)

    # 定义即将要找的内容
    forget_password_locater = (By.CLASS_NAME, "account-form-link")
    # 显示等待 一直等待【收不到验证码】文字加载完成---20表示最大等待20秒 如果在0.5秒内找到了，则就不等待了。
    WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(forget_password_locater))

    # 定位 收不到验证码文字
    driver.find_element_by_class_name("account-form-link").click()
    windows = driver.window_handles
    print(windows)
    driver.switch_to.window(windows[1])
    # 断言切换窗口成功
    assert driver.title == "帐号 使用帮助"
