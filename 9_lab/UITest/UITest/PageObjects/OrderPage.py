from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObjects.BasePage import BasePage
from tests.conf import *
from selenium import webdriver
import time
import json

class OrderPage(BasePage):
    def __init__(self, driver=None):
        super().__init__(driver)   
        self._LOGIN_STRING = 'login'
        self._PASSWORD_STRING = 'password'
        self._NAME_STRING = 'name'        
        self._EMAIL_STRING = 'email'        
        self._ADDRESS_STRING = 'address'        

        self._PRODUCTS_NAME_XPATH = "//*[@id='cart']/div/div//a"
        self._FIRST_PRODUCT = '1234'
        self._BTN_DEFAULT_CLASS = 'btn-default'
        self._BTN_PRIMARY_CLASS = 'btn-primary'
        
        self._ERROR_MSG_XPATH = '/html/body/h1'
        self._ERROR_MSG = 'Произошла ошибка'
        self._ALERT_DANGER = 'alert-danger'
        self._test_data = None
        
    def close(self):
        self._driver.close()    
        
    def load_test_data(self, file_path, json_name):
        with open(file_path) as f:
            test_data = json.load(f)
            self._test_data = test_data[json_name]

    def enter_value_in_input(self, input_name, value):
        elem = self._driver.find_element(By.NAME, input_name)
        elem.send_keys(value)
        
    def find_elem_by_xpath(self, xpath):
        elem = self._driver.find_element(By.XPATH, xpath)
        return elem             

    def find_elems_by_xpath(self, xpath):
        elems = self._driver.find_elements(By.XPATH, xpath)
        return elems
    
    def click_on_button(self, button_class_name):
        elem = self._driver.find_element(By.CLASS_NAME, button_class_name)
        elem.click()

    def check_availaility(self, elem_class_name):
        try:
            elem = self._driver.find_element(By.CLASS_NAME, elem_class_name)
            return True
        except:
            return False        