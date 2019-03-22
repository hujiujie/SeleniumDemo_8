# coding=utf-8
import pytest

from src.initilization.browerdriver import BuildUpDriver

if __name__ == "__main__":
    BuildUpDriver.build_up_driver()
    pytest.main(['-s', 'testcases/login/test_login.py'])