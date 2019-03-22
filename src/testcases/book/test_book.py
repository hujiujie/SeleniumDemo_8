# coding=utf-8

from src.pages.music.bookspage import BooksPageObject
import pytest

class TestBook:

    @pytest.mark.parametrize("book_name",["利用Python进行数据分析","红楼梦","韩寒","钢铁是怎样练成的"])
    def test_search(self,book_name):
        self.book_page_object = BooksPageObject()
        self.book_page_object.search(book_name)
        assert book_name in self.book_page_object.search_result_list()
