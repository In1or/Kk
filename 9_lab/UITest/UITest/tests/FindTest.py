from PageObjects.MainPage import MainPage
import unittest
import json
from parameterized import parameterized
from conf import *

class FindTest(unittest.TestCase):
    def setUp(self) -> None:        
        self._MainPage = MainPage()
        
    def tearDown(self) -> None:
        self._MainPage.close()
        
    @parameterized.expand([
        ['Men'],
        ['Women'],
        ['Kids']
    ])
    
    def test_find_by_categories(self, category):
        self._MainPage.click_on_hyperlink(category)
        self.assertTrue(self._MainPage.check_availaility(self._MainPage._PRODUCT_CLASS), msg=f'Error with categor {category}')
        elem = self._MainPage.find_elem_by_xpath(self._MainPage._CATEGORY_NAME_XPATH)
        self.assertEqual(elem.text, category, msg=f'Error with name category - {category}')
        
    def test_find_by_input_with_non_empty_value(self):
        self._MainPage.enter_value_in_input_with_enter(self._MainPage._TEST_PRODUCT_NAME, self._MainPage._TEST_PRODUCT_VALUE)
        self.assertTrue(self._MainPage.check_availaility(self._MainPage._PRODUCT_CLASS), msg=f'Error with find by input with non empty value')
        
    def test_find_by_input_with_empty_value(self):
        self._MainPage.enter_value_in_input_with_enter(self._MainPage._TEST_PRODUCT_NAME, '')
        self.assertFalse(self._MainPage.check_availaility(self._MainPage._PRODUCT_CLASS), msg=f'Error with find by input with empty value')