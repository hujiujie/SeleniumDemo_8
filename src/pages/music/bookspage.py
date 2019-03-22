# coding=utf-8
from selenium.webdriver.common.by import By

from .basepage import BasePageObject


class BooksPageObject(BasePageObject):

    _to_book= (By.PARTIAL_LINK_TEXT, "读书")
    _search_text = (By.NAME, 'search_text')
    #_search_text = (By.XPATH ,"//*[@placeholder='书名、作者、ISBN']")
    _search_btn = (By.CLASS_NAME, "inp-btn")
    #_book_name = (By.PARTIAL_LINK_TEXT, "利用Python进行数据分析")
    _book_name = (By.CLASS_NAME, 'title-text')
    _book_author = (By.XPATH, "//meta abstract[contains(.,'Wes McKinney')]")

    def __init__(self):
        BasePageObject.__init__(self)

    def toBook(self):
        self.extend_find_element(BooksPageObject._to_book).click()

    def _locate_search_book(self):
        return self.extend_find_element(BooksPageObject._search_text)

    def input_book_name(self,name):
        self._locate_search_book().send_keys(name)

    def _locate_search_btn(self):
        return self.extend_find_element(BooksPageObject._search_btn)

    def click_search_icon(self):
        self.click_element(self._locate_search_btn())

    '''
    def search_book(self,name):
        self.extend_find_element(BooksPageObject._search_text).send_keys(name)
        self.extend_find_element(BooksPageObject._search_btn).click()    
    '''
    def switch_windows(self):
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[-1])


    def search(self,name):
        self.switch_windows()
        self.toBook()
        self.switch_windows()
        self.input_book_name(name)
        self.click_search_icon()


    def search_result_list(self):
        elements = self.extend_find_element(BooksPageObject._book_name).text
        print(elements)
        #book_author = self.extend_find_element(BooksPageObject._book_author).text
        #print((book_author))
        return elements


