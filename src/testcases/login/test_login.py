# coding=utf-8

import pytest

from src.pages.music.loginpage import LoginPageObject


@pytest.mark.parametrize('username, password',
                         [('18810054187', 'qwe789'),
                          ('18810099999', 'qwe789'),
                          ]
                         )
def test_douban(username, password):
    login_page_object = LoginPageObject()
    login_page_object.login(username, password)

    text = login_page_object.get_my_douban_text()
    assert text == "我的豆瓣"
