# coding=utf-8
import logging
import os

import pytest
import allure
from src.initilization.browerdriver import BuildUpDriver
from src.pages.music.loginpage import LoginPageObject


@pytest.fixture(scope='session', autouse=True)
def login_douban():
    logging.info("Start init login douban")

    # 登录放在初始文件中，表示只运行一次
    login_page_object = LoginPageObject()
    login_page_object.login("18810054187","qwe789")

    yield
    logging.info("End all testcases")
    BuildUpDriver.driver.quit()

@pytest.fixture(scope='module',autouse=True)
def login_douban():
    #截图
    BuildUpDriver.driver.get_screenshot_as_png()
    yield
    #截图
    BuildUpDriver.driver.get_screenshot_as_png()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # we only look at actual failing test calls, not setup/teardown
    if (rep.when == "call" or rep.when == "setup") and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""

            f.write(rep.nodeid + extra + "\n")

        pic_info = BuildUpDriver.driver.get_screenshot_as_png()
        with allure.step('添加失败截图'):
            allure.attach('失败截图',pic_info,allure.attach_type.PNG)
