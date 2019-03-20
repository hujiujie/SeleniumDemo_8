# coding=utf-8


# 公共方法 在这里写
from src.initilization import browerdriver


class BasePageObject:

    def __init__(self):
        self.driver = browerdriver.BuildUpDriver.driver

    def extend_find_element(self,locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].style.background "
                                   "= 'rgb(138,43,226 )';",
                                   element)
        return element

    def switch_frame_by_element(self,element):
        self.driver.switch_to.frame(element)

    def get_element_text(self,element):
        return element.text

    def get_table_content(self,tabel_name):
        pass

    def set_value(self,element,value):
        element.clear()
        element.click()
        element.send_keys(value)

    def click_element(self,element):
        element.click()