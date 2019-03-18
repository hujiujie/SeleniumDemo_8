# coding=utf-8
from selenium.webdriver.common.by import By

from .basepage import BasePageObject


class BooksPageObject(BasePageObject):

    _to_book= (By.PARTIAL_LINK_TEXT, "豆瓣读书")
    #_search_text = (By.NAME, "search_text")
    _search_text = (By.XPATH ,"//*[@placeholder='书名、作者、ISBN']")
    _search_btn = (By.CLASS_NAME, "inp-btn")
    _book_name = (By.PARTIAL_LINK_TEXT, "利用Python进行数据分析")
    _book_author = (By.XPATH, "//div[contains(.,'Wes McKinney')]")

    def __init__(self):
        BasePageObject.__init__(self)

    def toBook(self):
        self.extend_find_element(BooksPageObject._to_book).click()
        return self

    def search_book(self,name):
        self.extend_find_element(self._search_text).send_keys(name)
        self.extend_find_element(self._search_btn).click()
        return self

    def search_result_list(self):
        self.extend_find_element(BooksPageObject._book_name)
        pass
