# coding=utf-8

import pytest

from src.initilization.browerdriver import BuildUpDriver


@pytest.fixture(scope='session', autouse=True)
def login_douban():
    print("starting")
    yield
    BuildUpDriver.driver.quit()
