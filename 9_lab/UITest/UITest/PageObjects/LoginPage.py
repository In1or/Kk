from selenium.webdriver.common.by import By
from PageObjects.BasePage import BasePage
from tests.conf import *
import json
from selenium import webdriver
import time

class LoginPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)
        self._BTN_CLASS = 'btn'

        self._LOGIN_STRING = 'login'
        self._PASSWORD_STRING = 'password'
        self._ACCOUNT = 'Account'
        self._ENTER = 'Вход'
        
        self.click_on_hyperlink(self._ACCOUNT)
        self.click_on_hyperlink(self._ENTER)
        self._test_data = None

    def load_test_data(self, file_path, json_name):
        with open(file_path) as f:
            test_data = json.load(f)
            self._test_data = test_data[json_name]
        
    def enter_value_in_input(self, input_name, value):
        elem = self._driver.find_element(By.NAME, input_name)
        elem.send_keys(value)

    def open_page(self, url):
        self._driver.get(url)
        
    def click_on_button(self, button_class_name):
        elem = self._driver.find_element(By.CLASS_NAME, button_class_name)
        elem.click()
        
    def click_on_hyperlink(self, hyperlink_text):
        elem = self._driver.find_element(By.LINK_TEXT, hyperlink_text)
        elem.click()
        time.sleep(1)
        
    def check_availaility(self, elem_class_name):
        try:
            elem = self._driver.find_element(By.CLASS_NAME, elem_class_name)
            return True
        except:
            return False
        
    def close(self):
        self._driver.close()      