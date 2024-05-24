from PageObjects.MainPage import MainPage
import unittest
import json
from parameterized import parameterized
from conf import *
import time

class AddProductInCartTest(unittest.TestCase):  
    def setUp(self) -> None:        
        self._MainPage = MainPage()
        
        
    def tearDown(self) -> None:
        self._MainPage.close()
        
    def test_add_one_product(self):
        self._MainPage.click_on_hyperlink(self._MainPage._FIRST_PRODUCT)
        self._MainPage.click_on_hyperlink(self._MainPage._BTN_ADD_TO_CART)
        
        time.sleep(1)
        
        elements = self._MainPage.find_elems_by_xpath(self._MainPage._PRODUCTS_NAME_XPATH)
        texts = [elem.text for elem in elements]
        self.assertTrue(texts[1], self._MainPage._FIRST_PRODUCT.lower())
        
    def test_add_two_product(self):
        self._MainPage.click_on_hyperlink(self._MainPage._FIRST_PRODUCT)
        self._MainPage.click_on_hyperlink(self._MainPage._BTN_ADD_TO_CART)
        
        time.sleep(1)
        
        self._MainPage.click_on_button(self._MainPage._BTN_CLOSE_CLASS)
        self._MainPage.go_back()
        
        self._MainPage.click_on_hyperlink(self._MainPage._SECOND_PRODUCT)
        self._MainPage.click_on_hyperlink(self._MainPage._BTN_ADD_TO_CART)
        
        time.sleep(1)

        elements = self._MainPage.find_elems_by_xpath(self._MainPage._PRODUCTS_NAME_XPATH)
        texts = [elem.text for elem in elements]
        
        self.assertTrue(texts[1], self._MainPage._FIRST_PRODUCT.lower())
        self.assertTrue(texts[3], self._MainPage._SECOND_PRODUCT.lower())