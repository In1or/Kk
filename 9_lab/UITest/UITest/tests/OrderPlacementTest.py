from PageObjects.OrderPage import OrderPage
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
import unittest
from parameterized import parameterized
import time
import json
from conf import *

class MakingOrderTest(unittest.TestCase):
    def setUp(self) -> None: 
        self._OrderPage = OrderPage()
    
    def tearDown(self) -> None:
        self._OrderPage.close()

    def test_with_auth(self):
        self._LoginPage = LoginPage(self._OrderPage._driver)
        self._LoginPage.load_test_data(AUTH_TEST_FILE_PATH, 'valid')
        item = self._LoginPage._test_data
        
        self._LoginPage.enter_value_in_input(self._LoginPage._LOGIN_STRING, item[self._LoginPage._LOGIN_STRING])
        self._LoginPage.enter_value_in_input(self._LoginPage._PASSWORD_STRING, item[self._LoginPage._PASSWORD_STRING])
        
        self._LoginPage.click_on_button(self._LoginPage._BTN_CLASS)
        
        self._MainPage = MainPage(self._LoginPage._driver)
        
        self._MainPage.find_elem_by_xpath(self._MainPage._LOGO_XPATH).click()
        self.add_to_cart()
        time.sleep(1)
        
        elements = self._MainPage.find_elems_by_xpath(self._MainPage._PRODUCTS_NAME_XPATH)
        texts = [elem.text for elem in elements]
        
        self.assertEqual(texts[1], self._MainPage._FIRST_PRODUCT.lower(), msg='Error with name product')   
        self._MainPage.click_on_button(self._MainPage._BTN_PRIMARY_CLASS)

        self._OrderPage = OrderPage(self._MainPage._driver)
     
        self._OrderPage.click_on_button(self._OrderPage._BTN_DEFAULT_CLASS)
        time.sleep(1)
        time.sleep(1)
        err_msg = self._OrderPage.find_elem_by_xpath(self._OrderPage._ERROR_MSG_XPATH).text
        self.assertEqual(err_msg, self._OrderPage._ERROR_MSG, msg='Error with redirect to error page')    

    def test_without_auth(self):        
        self._MainPage = MainPage(self._OrderPage._driver)
        self.add_to_cart()
        time.sleep(1)
        
        elements = self._MainPage.find_elems_by_xpath(self._MainPage._PRODUCTS_NAME_XPATH)
        texts = [elem.text for elem in elements]
        
        self.assertEqual(texts[1], self._MainPage._FIRST_PRODUCT.lower(), msg='Error with name product')   
        self._MainPage.click_on_button(self._MainPage._BTN_PRIMARY_CLASS)

        self._OrderPage = OrderPage(self._MainPage._driver)
      
        self._OrderPage.load_test_data(MAKING_ORDER_TEST_PATH, 'valid')
        _test_data = self._OrderPage._test_data
        self.fill_inputs_for_make_order(_test_data)
        
        self._OrderPage.click_on_button(self._OrderPage._BTN_DEFAULT_CLASS)
        time.sleep(1)
        err_msg = self._OrderPage.find_elem_by_xpath(self._OrderPage._ERROR_MSG_XPATH).text
        self.assertEqual(err_msg, self._OrderPage._ERROR_MSG, msg='Error with redirect to error page')
        
    @parameterized.expand([
        ['with_busy_email'],
        ['with_busy_login']
    ])
    def test_without_auth_with_busy_parameters(self, name):
        self._MainPage = MainPage(self._OrderPage._driver)
        self.add_to_cart()
        time.sleep(1)
        self._MainPage.click_on_button(self._MainPage._BTN_PRIMARY_CLASS)
        
        self._OrderPage = OrderPage(self._MainPage._driver)
        time.sleep(1)
        self._OrderPage.load_test_data(MAKING_ORDER_TEST_PATH, name)
        
        time.sleep(1)
        self.fill_inputs_for_make_order(self._OrderPage._test_data)
        time.sleep(1)
        self._OrderPage.click_on_button(self._OrderPage._BTN_DEFAULT_CLASS)
        
        time.sleep(1)
        self.assertTrue(self._OrderPage.check_availaility(self._OrderPage._ALERT_DANGER), msg=f'Error with alert msg for {name}')
        time.sleep(1)

    def add_to_cart(self):
        self._MainPage.click_on_hyperlink(self._MainPage._FIRST_PRODUCT)
        self._MainPage.click_on_hyperlink(self._MainPage._BTN_ADD_TO_CART)
        time.sleep(2)

    def fill_inputs_for_make_order(self, json_data):
        self._OrderPage.enter_value_in_input(self._OrderPage._LOGIN_STRING, json_data[self._OrderPage._LOGIN_STRING])
        self._OrderPage.enter_value_in_input(self._OrderPage._PASSWORD_STRING, json_data[self._OrderPage._PASSWORD_STRING])
        self._OrderPage.enter_value_in_input(self._OrderPage._NAME_STRING, json_data[self._OrderPage._NAME_STRING])
        self._OrderPage.enter_value_in_input(self._OrderPage._EMAIL_STRING, json_data[self._OrderPage._EMAIL_STRING])
        self._OrderPage.enter_value_in_input(self._OrderPage._ADDRESS_STRING, json_data[self._OrderPage._ADDRESS_STRING])
