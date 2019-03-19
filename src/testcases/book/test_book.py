# coding=utf-8

from src.pages.music.bookspage import BooksPageObject
import pytest

class TestBook:
    def test_search(self):
        self.book_page_object = BooksPageObject()
        self.book_page_object.search("利用Python进行数据分析")
        assert "利用Python进行数据分析" == self.book_page_object.search_result_list()
