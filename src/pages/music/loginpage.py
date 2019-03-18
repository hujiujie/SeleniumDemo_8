# coding=utf-8
from .basepage import BasePageObject
from selenium.webdriver.common.by import By


class LoginPageObject(BasePageObject):
    _login_frame = (By.TAG_NAME, 'iframe')
    _account_login_tab = (By.CLASS_NAME, 'account-tab-account')
    _username_field = (By.ID, 'username')
    _password_field = (By.ID, 'password')
    _login_button = (By.LINK_TEXT, '登录豆瓣')
    _my_douban = (By.LINK_TEXT, "我的豆瓣")

    def __init__(self):
        BasePageObject.__init__(self)

    def _locate_login_frame(self):
        return self.extend_find_element(LoginPageObject._login_frame)

    def switch_to_login_frame(self):
        self.switch_frame_by_element(self._locate_login_frame())

    def _locate_login_tab(self):
        return self.extend_find_element(LoginPageObject._account_login_tab)

    def click_login_tab(self):
        self.click_element(self._locate_login_tab())

    def _locate_username_field(self):
        return self.extend_find_element(LoginPageObject._username_field)

    def input_user_name(self, user_name):
        self.set_value(self._locate_username_field(), user_name)

    def _locate_password_field(self):
        return self.extend_find_element(LoginPageObject._password_field)

    def input_password(self, password):
        self.set_value(self._locate_password_field(), password)

    def _locate_login_button(self):
        return self.extend_find_element(LoginPageObject._login_button)

    def click_login_button(self):
        element = self._locate_login_button()
        self.click_element(self._locate_login_button())

    def _locate_my_douban(self):
        return self.extend_find_element(LoginPageObject._my_douban)

    def get_my_douban_text(self):
        return self.get_element_text(self._locate_my_douban())

    def login(self, username, password):
        self.switch_to_login_frame()
        self.click_login_tab()
        self.input_user_name(username)
        self.input_password(password)
        self.click_login_button()
