from PageObjects.LoginPage import LoginPage
import unittest
import json
import time
from parameterized import parameterized
from conf import *

class AuthTest(unittest.TestCase):
    def setUp(self) -> None:
            
        self._LoginPage = LoginPage()


    def tearDown(self) -> None:
        self._LoginPage.close()
        
    @parameterized.expand([
        ['valid',  'alert-success'],
        ['invalid', 'alert-danger']
    ])
    
    def test_auth(self, name, msg):
        self._LoginPage.load_test_data(AUTH_TEST_FILE_PATH, name)
        item = self._LoginPage._test_data
        
        self._LoginPage.enter_value_in_input(self._LoginPage._LOGIN_STRING, item[self._LoginPage._LOGIN_STRING])
        self._LoginPage.enter_value_in_input(self._LoginPage._PASSWORD_STRING, item[self._LoginPage._PASSWORD_STRING])
        
        self.assertTrue(self._LoginPage.check_availaility('has-success'), msg='Error with success icon')
        
        self._LoginPage.click_on_button(self._LoginPage._BTN_CLASS)
        
        self.assertTrue(self._LoginPage.check_availaility(msg), msg=f'Error with {msg}')
        
    def test_auth_with_empty_data(self):
        self._LoginPage.load_test_data(AUTH_TEST_FILE_PATH, 'empty')
        item = self._LoginPage._test_data
        
        self._LoginPage.enter_value_in_input(self._LoginPage._LOGIN_STRING, item[self._LoginPage._LOGIN_STRING])
        self._LoginPage.enter_value_in_input(self._LoginPage._PASSWORD_STRING, item[self._LoginPage._PASSWORD_STRING])
        
        time.sleep(1)

        self.assertTrue(self._LoginPage.check_availaility('has-error'), msg='Error with error icon')
        
        self._LoginPage.click_on_button(self._LoginPage._BTN_CLASS)
        
        self.assertFalse(self._LoginPage.check_availaility('alert-success'), msg='Error with alert-seccess')
        self.assertFalse(self._LoginPage.check_availaility('alert-danger'), msg='Error with alert-danger')