# coding=utf-8
from time import sleep

from src.pages.music.basepage import BasePageObject
from src.pages.music.bookspage import BooksPageObject
import pytest

def test_search():
    book = BooksPageObject().toBook()
    sleep(10)
    book.search_book("利用Python进行数据分析")
    print("222222222")
    # assert "利用Python进行数据分析" in self.book.search_result_list()
